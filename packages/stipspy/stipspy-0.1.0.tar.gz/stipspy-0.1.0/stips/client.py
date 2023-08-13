"""
🛠️ 12/08/2023
The main client class, provides access to all of stips's API endpoints.
"""

import json
import io
import os
import random
import string

import magic
import requests

from stips import errors, http_man as http, enums, utils
from stips.helpers import ABCHelpers
from stips.models import *


def _parse_cookies_string(cookies_string: str) -> dict:
  """
  Users may pass cookies from the document.cookie result, which is raw.
  This function parses the raw cookies string into a dictionary

  :param cookies_string: the raw cookies string
  :returns: a dictionary of the cookies
  """
  try:
    return dict(map(
      lambda cookie: cookie.strip().split('=', 1),
      cookies_string.strip().strip("'\"").split(';')))
  except ValueError:
    raise errors.InvalidCredentials("Failed to parse cookies string (try copying document.cookie)")


class StipsClient:
  """
  A client class provides access to stips's API endpoints.
  Both non-user and user methods are available.

  To use user methods you must pass either a pair of email & password, or auth cookies:
    - StipsClient(email='my.email@gmail.com', password='mypassword')
    - StipsClient(cookies='Login%5FUser=hashedpassword=...')

  :param email: email for authentication, must go with the password param
  :param password: password for authentication, must go with the email param
  :param cookies: cookies for authentication, can be either a dictionary or the raw string (document.cookie)
  :param safe_filter: whether to use the safe filter option when fetching content
  """

  def __init__(self, email: str = None, password: str = None, cookies: typing.Union[str, dict] = None,
               safe_filter: bool = False):
    self.email = email
    self.password = password
    self.cookies = cookies
    self.safe_filter = safe_filter

    if self.cookies:
      if isinstance(self.cookies, str):
        self.cookies: dict = _parse_cookies_string(self.cookies)

    elif self.email and self.password:
      # get cookies from email & password
      params = dict(
        name='user.login',
        api_params=json.dumps(dict(email=self.email, password=self.password, auth_token=""))
      )

      js, resp = http._get(params=params, maybe_json=True)

      if not js:
        raise errors.HttpUnknown("Failed to login using email & password, perhaps try using cookies instead")

      if not js.get('data', {}).get('logged', False):
        raise errors.InvalidCredentials("Email or password (or both) are incorrect.")

      self.cookies = resp.cookies.get_dict()

    self.http = http.HTTPClient(cookies=self.cookies)

    self.me: typing.Optional[AppUser] = None

    if self.cookies:
      try:
        self.me: typing.Optional[AppUser] = self.get_app_user()
      except KeyError:
        raise errors.InvalidCredentials(
          "Failed to authenticate using provided credentials, please ensure that they are correct, or initialize the API without an account.")

    self.channels_cache = {}

  def _get_remote_config(self, cache_channels=True, **kw) -> RemoteConfig:
    """
    An endpoint that returns the list of channels (מוסיקה, טכנולוגיה, ...).

    :param cache_channels: Whether to cache the channels in the client object
    :returns: RemoteConfig object
    """
    dt: RemoteConfig = self.http.get(params={'namespace': 'item', 'unit': 'RemoteConfig'}, action='smartdata.get', **kw)

    if cache_channels:
      for channel in dt.channels:
        self.channels_cache[channel.id] = channel

    return dt

  @staticmethod
  def _parse_delete(id, title, points, message, ban, warn_only=False, remove_from_channel=False):
    """
    Simple helper function to generate a delete request body, it is used by the delete_*() methods.

    Note: If you warn only + (remove points / ban) at the same time then the message will just be deleted.
    """
    dt = dict(
      params={'id': id},
      data={"deleteMsg": dict(
        title=title,
        points=points,
        msg=message,
        ban=ban,
        removeFromChannelOnly=remove_from_channel,
        warningOnly=warn_only
      )},
      omnirest="DELETE",
      get_success=True
    )

    if ban is None:
      del dt['data']['deleteMsg']['ban']

    return dt

  @ABCHelpers.moderator_endpoint
  def delete_question(self, id: int, title: str = '', points: typing.Optional[int] = None, message: str = '',
                      ban: bool = False,
                      **kw) -> bool:
    """Delete a question

    :param id: The question id to delete
    :param title: Title reason
    :param points: Points to remove
    :param message: Message reason
    :param ban: Whether to ban the user for 24 hours
    :returns Whether successfully deleted the question
    """
    return self.http.get(
      **self._parse_delete(id=id, title=title, points=points, message=message, ban=ban, warn_only=False),
      omniobj='ask', **kw)

  @ABCHelpers.moderator_endpoint
  def delete_answer(self, id: int, title: str = '', points: typing.Optional[int] = None, message: str = '',
                    ban: bool = False,
                    **kw) -> bool:
    """Delete an answers

    :param id: The answer id to delete
    :param title: Title reason
    :param points: Points to remove
    :param message: Message reason
    :param ban: Whether to ban the user for 24 hours
    :returns Whether successfully deleted the answer
    """
    return self.http.get(
      **self._parse_delete(id=id, title=title, points=points, message=message, ban=ban, warn_only=False),
      omniobj='ans', **kw)

  @ABCHelpers.moderator_endpoint
  def warn_answer(self, id: int, title: str = '', message: str = '', **kw) -> bool:
    """Warns an answers author

    :param id: The id of the answer to warn its author
    :param title: Title reason
    :param message: Message reason
    :returns Whether successfully warned the answers author
    """
    return self.http.get(
      **self._parse_delete(id=id, title=title, points=None, message=message, ban=None, warn_only=True),
      omniobj='ans', **kw)

  @ABCHelpers.moderator_endpoint
  def warn_question(self, id: int, title: str = '', message: str = '', **kw) -> bool:
    """Warns a questions author

    :param id: The id of the question to warn its author
    :param title: Title reason
    :param message: Message reason
    :returns Whether successfully warned the questions author
    """
    return self.http.get(
      **self._parse_delete(id=id, title=title, points=points, message=message, ban=ban, warn_only=True),
      omniobj="ask", **kw)

  @ABCHelpers.moderator_endpoint
  def remove_question_from_channel(self, id: int, channel_id: int = None, channel_name: str = None, **kw) -> bool:
    """Warns a questions author

    :param id: The id of the question to remove from the channel
    :param channel_id: id of the channel that the question is attached to, channel name can be passed instead
    :param channel_name: name of the channel that the question is attached to, channel id can be passed instead
    :returns Whether successfully removed the question from the channel
    """
    CHANNEL_REMOVE_MESSAGE = "השאלה הוסרה מהערוץ {} מכיוון שהיא לא שייכת לערוץ זה. \nהשאלה לא נמחקה והיא ממשיכה להופיע ברשימת השאלות הכללית."
    remove_msg = CHANNEL_REMOVE_MESSAGE.format(f'שהיא שוייכה אליו')

    if channel_name:
      remove_msg = CHANNEL_REMOVE_MESSAGE.format(f'"{channel_name}"')
    else:
      if not self.channels_cache.get(channel_id):
        self._get_remote_config(cache_channels=True)

      if self.channels_cache.get(channel_id):
        remove_msg = CHANNEL_REMOVE_MESSAGE.format(f'"{self.channels_cache[channel_id].name}"')

    return self.http.get(
      **self._parse_delete(id=id, title="", points=None, message=remove_msg, ban=None, warn_only=True,
                           remove_from_channel=True),
      omniobj="ask", **kw)

  @ABCHelpers.moderator_endpoint
  def delete_penfriend(self, id: int, title: str = '', points: typing.Optional[int] = None, message: str = '',
                       ban: bool = False, fake_delete: bool = False,
                       **kw) -> bool:
    """Delete a penfriends item

    :param id: The penfriend item id to delete
    :param title: Title reason
    :param points: Points to remove
    :param message: Message reason
    :param ban: Whether to ban the user for 24 hours
    :param fake_delete: If this is true, the item will not be deleted but a notification will be sent to the author
    :returns Whether successfully deleted the penfriends item
    """
    return self.http.get(
      **self._parse_delete(id=id, title=title, points=points, message=message, ban=ban, warn_only=fake_delete),
      omniobj='penfriendsitem', **kw)

  @ABCHelpers.moderator_endpoint
  def delete_thank(self, id: int, title: str = '', points: typing.Optional[int] = None, message: str = '',
                   ban: bool = False, fake_delete=False,
                   **kw) -> bool:
    """Delete a wall item

    :param id: The wall item id to delete
    :param title: Title reason
    :param points: Points to remove
    :param message: Message reason
    :param ban: Whether to ban the user for 24 hours
    :param fake_delete: If this is true, the item will not be deleted but a notification will be sent to the author
    :returns Whether successfully deleted the wall item
    """
    return self.http.get(
      **self._parse_delete(id=id, title=title, points=points, message=message, ban=ban, warn_only=fake_delete),
      omniobj='thanksmsg', **kw)

  @ABCHelpers.moderator_endpoint
  def get_reports(self, page: int = 1, **kw) -> typing.List[ReportItem]:
    """Get reports list

    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'method': 'report_item.open', 'page': page}, action='objectlist', conn=self, **kw)

  @ABCHelpers.moderator_endpoint
  def decline_reports(self, id: int, **kw) -> bool:
    """Decline/Remove **all** reports of an item from the reports list

    :param id: The item id to decline reports for
    """
    return self.http.get(params={'id': id}, action='reports.remove', get_success=True, **kw)

  def get_home_questions(self, **kw) -> typing.List[Question]:
    """Get home page questions"""

    return self.http.get(params={}, action='homepage.content', conn=self, **kw)

  def get_profile(self, user_id: int, **kw) -> Profile:
    """Get public profile details for a user (age, answers, badges, flowers, active_since, questions, status)

    :param user_id: The User ID to check the details for
    """
    return self.http.get(params={'userid': user_id}, action='profile.page_data', conn=self, **kw)

  def get_user(self, id: int, **kw) -> User:
    """Get more public profile details for a user (gender, photo, nickname, points, online, perm_blocked)

    :param user_id: The User ID to check the details for
    """
    return self.http.get(params={'id': id}, action='omniobj', omniobj='user', omnirest='GET', conn=self, **kw)

  def get_answers(self, question_id: int, page: int = 1, **kw) -> typing.List[Answer]:
    """Get answers for a question

    :param question_id: The Question ID to receive answers from
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'askid': question_id, 'method': 'ans.for_item', 'page': page}, action='objectlist',
                         conn=self, **kw)

  @ABCHelpers.require_cookies
  def get_notifications_count(self, **kw) -> NotificationsCount:
    """Get notifications"""

    return self.http.get(params={}, action='messages.count', **kw)

  @ABCHelpers.require_cookies
  def get_notifications_list(self, page: int = 1, **kw) -> typing.List[NotificationItem]:
    """Get notifications list

    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'page': page}, action='notifications.list', **kw)

  def get_question(self, id: int, **kw) -> Question:
    """Get info about a question

    :param id: The Question ID to receive data from
    """
    return self.http.get(params={'id': id}, action='omniobj', omniobj='ask', omnirest='GET', conn=self, **kw)

  @ABCHelpers.safe_filter
  def get_new_questions(self, page: int = 1, **kw) -> typing.List[Question]:
    """Get new questions

    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'method': 'ask.new', 'page': page}, action='objectlist', conn=self, **kw)

  @ABCHelpers.safe_filter
  def get_category_new_questions(self, channel: typing.Union[enums.ChannelType, str], page: int = 1, **kw) -> \
      typing.List[Question]:
    """Get new questions in a certain category

    :param channel: The category to get questions from
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'method': 'ask.new', 'channel': enums.get_enum(channel), 'page': page},
                         action='objectlist', conn=self, **kw)

  @ABCHelpers.safe_filter
  def get_hot_questions(self, section: typing.Union[enums.TimeType, str] = enums.TimeType.now, page: int = 1, **kw) -> \
      typing.List[Question]:
    """Get hot questions

    :param section: Filter hot questions type (now, today, week)
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'method': 'ask.hot', 'filter_section_name': enums.get_enum(section), 'page': page},
                         action='objectlist', conn=self, **kw)

  @ABCHelpers.safe_filter
  def get_category_hot_questions(self, channel: typing.Union[enums.ChannelType, str],
                                 section: typing.Union[enums.TimeType, str] = enums.TimeType.week, page: int = 1,
                                 **kw) -> typing.List[Question]:
    """Get hot questions in a certain category

    :param channel: The category to get questions from
    :param section: Filter hot questions type (week, month)
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(
      params={'method': 'ask.hot', 'channel': channel, 'filter_section_name': enums.get_enum(section), 'page': page},
      action='objectlist', conn=self, **kw)

  @ABCHelpers.require_cookies
  @ABCHelpers.safe_filter
  def get_user_questions(self, section: typing.Union[enums.MyQuestionType, str] = enums.MyQuestionType.asked,
                         page: int = 1, **kw) -> typing.List[Question]:
    """Get questions by you (either "asked", "answered" or "pinned")

    :param section: Filter questions type ("asked", "answered", "pinned")
    :param page: Items page to get (Gets first page by default)
    """
    if isinstance(section, str) and section == 'answered': section = 'ansed'  # typo ?

    return self.http.get(
      params={'method': 'ask.user_activity', 'filter_section_name': enums.get_enum(section), 'for_current_user': True,
              'page': page}, action='objectlist', conn=self, **kw)

  def get_user_thanks(self, user_id: int, page: int = 1, **kw) -> typing.List[Thank]:
    """Get wall messages

    :param user_id: The User ID to get wall messages from
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'objType': 'thanksmsg', 'userid': user_id, 'page': page}, action='objectlist',
                         conn=self, **kw)

  def get_profile_activity(self, user_id: int,
                           action: typing.Union[enums.ActivityType, str] = enums.ActivityType.answers, **kw) -> \
      typing.List[ChartData]:
    """Get User activity

    :param user_id: The User ID to get activity from
    :param action: The activity action to get (ans, ask, flowers)
    """
    return self.http.get(params={'userid': user_id, 'action': enums.get_enum(action)}, action='profile.actions_chart',
                         **kw)

  def get_user_flowers(self, user_id: int, page: int = 1, **kw) -> typing.List[Answer]:
    """Get User's answers that were flowered

    :param user_id: The User ID to get flowered answers from
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'method': 'ans.flower_for_user', 'userid': user_id, 'page': page}, action='objectlist',
                         conn=self, **kw)

  @ABCHelpers.require_cookies
  def edit_wall(self, text: str, user_id: int = None, **kw) -> bool:
    """Edit wall content (bio)

    :param text_status: The wall content (bio content)
    :param user_id: The User ID to edit the wall content (I assume admins can edit people's wall)
    """
    return self.http.post(params={'userid': user_id or self.me.id, 'text_status': text},
                          omniobj='user_profile_page',
                          omnirest='POST', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def send_thank(self, user_id: int, text: str, **kw) -> int:
    """Send wall message

    :param user_id: The User ID to send the wall message to
    :param text: The Message to send
    """
    return self.http.post(params={'touserid': user_id, 'msg': text}, omniobj='thanksmsg', omnirest='PUT', get_id=True,
                          **kw)

  @ABCHelpers.require_cookies
  def send_message(self, user_id: int, text: str, **kw) -> int:
    """Send a Private Message to a User

    :param user_id: The User ID to send the Message to
    :param text: The Message to send to the User
    """
    return self.http.get(params={'touserid': user_id, 'msg': text}, action='messages.send', get_id=True, **kw)

  @ABCHelpers.require_cookies
  def get_messages(self, user_id: int, message_id: int = 0, first_load: bool = False, history: bool = False, **kw) -> \
      typing.Union[
        bool, typing.List[MessageItem]]:
    """Get Private Messages from a User

    :param user_id: The User ID to get the Private Messages from
    :param message_id: The Message ID to receive the Messages Since (ie: msgid=15 all messages_id >= 15 will be returned). If set to 0 first_load
    :param first_load: Whether to load most recent (22?) messages, can be used with message_id=0
    :param history: Whether fetching historical messages
    :returns: A list of messages OR False if the user is blocked
    """
    return self.http.get(params={'userid': user_id, 'msgid': message_id, 'first_load': first_load, 'history': history},
                         action='messages.from_user',
                         **kw)

  @ABCHelpers.require_cookies
  def get_messages_list(self, page: int = 1, **kw) -> typing.List[MessagesListItem]:
    """Get most recent Users that the User has Texted With

    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'page': page}, action='messages.list', conn=self, **kw)

  @ABCHelpers.require_cookies
  def get_contacts(self, page: int = 1, get_all: bool = True, **kw) -> typing.List[User]:
    """Get Users that the User has Texted With

    :param page: Items page to get (Gets first page by default)
    :param get_all: Whether to recieve all users at once, will ignore the page argument if set to True
    """
    return self.http.get(params={'method': 'contacts.most_active', 'no_pagination': get_all, 'page': page},
                         action='objectlist', conn=self, **kw)

  @ABCHelpers.require_cookies
  def update_details(self, name: str = None, birth_date: typing.Union[datetime.datetime, str] = None,
                     gender: typing.Union[enums.Gender, str] = None, user_id: int = None, **kw) -> bool:
    """Update Details for a User

    :param name: The User's Nickname
    :param birth_date: The User's Birth Date (DD/MM/YYYY eg. 17/05/2000)
    :param gender: The User's Gender (male, female)
    :param user_id: The User ID to update the details for (I assume admins can edit people's details)
    """
    return self.http.get(params={'userid': user_id, 'nickname': name,
                                 'birth_date': birth_date.strftime('%d/%m/%Y') if isinstance(birth_date,
                                                                                             datetime.datetime) else birth_date,
                                 'gender': enums.get_enum(gender)}, action='user.update.details', get_success=True,
                         **kw)

  @ABCHelpers.require_cookies
  def pin(self, id: int, **kw) -> bool:
    """Add a pin to a question

    :param id: The Question ID to pin
    """
    return self.http.get(params={'id': id, 'minus': False}, action='item.add_pin', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def unpin(self, id: int, **kw) -> bool:
    """Remove a pin from a question

    :param id: The Question ID to unpin
    """
    return self.http.get(params={'id': id, 'minus': True}, action='item.add_pin', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def upvote(self, id: int, **kw) -> bool:
    """Upvote an answer

    :param id: The Answer ID to upvote
    """
    return self.http.get(params={'objType': 'ans', 'vote': 1, 'id': id}, action='item.vote', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def downvote(self, id: int, **kw) -> bool:
    """Downvote an answer

    :param id: The Answer ID to downvote
    """
    return self.http.get(params={'objType': 'ans', 'vote': -1, 'id': id}, action='item.vote', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def reset_vote(self, id: int, **kw) -> bool:
    """Resets votes for an answer

    :param id: The Answer ID to reset the votes for
    """
    return self.http.get(params={'objType': 'ans', 'vote': 0, 'id': id}, action='item.vote', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def answer(self, question_id: int, text: str, name: str = None, link_url: str = None, link_name: str = None,
             anonymous: bool = False, **kw) -> int:
    """Add an answer to a Question

    :param question_id: The Question ID to add the answer to
    :param text: The answer content
    :param name: The Username to send the answer as, works with anonymous=True
    :param link_url: The URL of the Link
    :param link_name: The URL Title of the Link
    :param anonymous: Whether or not to send the answer anonymously
    """
    return self.http.post(
      params={'askid': question_id, 'a': text, 'name': name, 'link1': link_url, 'link1name': link_name,
              'annoflg': anonymous},
      omniobj='ans', omnirest='PUT', get_id=True, **kw)

  @ABCHelpers.require_cookies
  def report_question(self, id: int, reason: str, **kw) -> bool:
    """Report bad content

    :param id: The ID of the Question reporting
    :param reason: The reason for reporting
    """
    return self.http.get(params={'itemid': id, 'reason': reason, 'itemtype': 'ask', 'reason_id': 0},
                         action='reports.send', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def report_answer(self, id: int, reason: str, **kw) -> bool:
    """Report bad content

    :param id: The ID of the Answer reporting
    :param reason: The reason for reporting
    """
    return self.http.get(params={'itemid': id, 'reason': reason, 'itemtype': 'ans', 'reason_id': 0},
                         action='reports.send', get_success=True, **kw)

  def get_tags(self, title: str, **kw) -> typing.List[str]:
    """Get automatically generated tags by title

    :param title: The Title to generate the tags from
    """
    return self.http.get(params={'title': title}, action='item.autotags', **kw)

  @ABCHelpers.require_cookies
  def get_questions_limit(self, **kw) -> QuestionsLimit:
    """Get how many questions you have asked and if you can ask more (Stips limit: 10 Per Day)"""

    return self.http.get(params={'namespace': 'ask', 'unit': 'DailyAskCount'}, action='smartdata.get', **kw)

  def get_images_gallery(self, tags: list, **kw) -> typing.List[GalleryImage]:
    """Get images loaded/generated/filtered by tags

    :param tags: The tags to load the images from
    """
    return self.http.get(params={'tags': tags}, action='photos.tag_gallery', **kw)

  @ABCHelpers.require_cookies
  def ask(self, title: str, content: str = '', name: str = '', photo: str = None, link: str = '', tags: list = [],
          anonymous: bool = False, **kw) -> int:
    """Ask a Question

    :param title: The question to ask
    :param content: The additional content for the question
    :param name: The Username to ask the Question as
    :param photo: The unsplash photo
    :param link: The link in the question
    :param tags: The question's tags
    :param anonymous: Whether or not to post the question Anonymously
    """
    return self.http.post(params={'q': title, 'text_content': content, 'name': name,
                                  'photo': utils.unsplash(photo), 'q_link': qlink_link,
                                  'tagslist': tags, 'anonflg': anonymous, 'ask_type': 11}, omniobj='ask',
                          omnirest='PUT', get_id=True, **kw)

  def get_penfriends(self, page: int = 1, **kw) -> typing.List[PenfriendsItem]:
    """Get Penfriends Messages

    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(params={'method': 'penfriendsitem.new', 'page': page}, action='objectlist', conn=self, **kw)

  @ABCHelpers.require_cookies
  def send_penfriends(self, text: str, **kw) -> int:
    """Send a Penfriends Message

    :param text: The Message to send
    """
    return self.http.post(params={'msg': text}, omniobj='penfriendsitem', omnirest='PUT', get_id=True, **kw)

  @ABCHelpers.require_cookies
  def can_send_penfriends(self, **kw) -> PenfriendsLimit:
    """Check if you can send any Penfriends Message (Due to Time Limit).

    If allowed, then minutes_left will be a negative number (~minutes since last pen)
    """
    return self.http.get(params={'namespace': 'penfriends', 'unit': 'PostAllowed'}, action='smartdata.get', **kw)

  @ABCHelpers.require_cookies
  def get_app_user(self, **kw) -> AppUser:
    """Get Private Details of a User"""

    return self.http.get(params={}, action='user.get_app_user', **kw)

  def flower(self, id: int, **kw) -> bool:
    """Send a Flower to an Answer

    :param id: The Message ID to send the Flower to
    """
    return self.http.get(params={'id': id}, action='item.send_flower', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def enable_question_notifications(self, id: int, **kw) -> bool:
    """Enable receiving Question Notifications

    :param id: The Question ID to Enable the Notifications in
    """
    return self.http.get(params={'id': id, 'add': True, 'objType': 'ask'}, action='item.notifications_register',
                         get_success=True, **kw)

  @ABCHelpers.require_cookies
  def disable_question_notifications(self, id: int, **kw) -> bool:
    """Disable receiving Question Notifications

    :param id: The Question ID to Disable the Notifications in
    """
    return self.http.get(params={'id': id, 'add': False, 'objType': 'ask'}, action='item.notifications_register',
                         get_success=True, **kw)

  @ABCHelpers.require_cookies
  def has_questions_notifications(self, id: int, **kw) -> bool:
    """Check if you have Question Notifications Enabled or not

    :param id: The Question ID to Check the Notifications in
    """
    return self.http.get(params={'id': id, 'namespace': 'ask', 'unit': 'AskAdditionalData'}, action='smartdata.get',
                         get_success=True, **kw)
    # NOTE:              ^ asks for get_success but actually gets data.results.notificationsRegistered

  @ABCHelpers.require_cookies
  def set_question_anonymous(self, id: int, **kw) -> bool:
    """Turn a Question into Anonymous

    :param id: The Question ID to set anonymous
    """
    return self.http.get(params={'id': id, 'objType': 'ask'}, action='item.set_anonymous', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def set_answer_anonymous(self, id: int, **kw) -> bool:
    """Turn an Answer into Anonymous

    :param id: The Answer ID to set anonymous
    """
    return self.http.get(params={'id': id, 'objType': 'ans'}, action='item.set_anonymous', get_sucess=True, **kw)

  @ABCHelpers.require_cookies
  def enable_safe_mode(self, user_id: int = None, **kw) -> bool:
    """Enable Safe Mode

    :param user_id: The User ID to Enable Safe Mode for (I assume admins can change people's safe mode setting)
    """
    return self.http.get(params={'userid': user_id or self.me.id, 'settings_name': 'safeFilter', 'value': True},
                         action='user.update.settings', get_sucess=True, **kw)

  @ABCHelpers.require_cookies
  def disable_safe_mode(self, user_id: int = None, **kw) -> bool:
    """Disable Safe Mode

    :param user_id: The User ID to Disable Safe Mode for (I assume admins can change people's safe mode setting)
    """
    return self.http.get(params={'userid': user_id or self.me.id, 'settings_name': 'safeFilter', 'value': False},
                         action='user.update.settings', get_sucess=True, **kw)

  @ABCHelpers.require_cookies
  def edit_question(self, id: int, title: str = None, content: str = None, tags: list = None, photo: str = None,
                    **kw) -> bool:
    """Modify a Question

    :param id: The Question to Modify
    :param title: The question title
    :param content: The additional content for the question
    :param tags: The question's tags
    :param photo: The unsplash photo
    """
    return self.http.post(
      params={'id': id, 'q': title, 'text_content': content, 'tagslist': tags, 'photo': utils.unsplash(photo)},
      omniobj='ask', omnirest='POST', get_success=True, **kw)

  def get_question_history(self, id: int, page: int = 1, **kw) -> typing.List[RevisionQuestion]:
    """Get a Question's History

    :param id: The ID of the Question to get the History from
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(
      params={'itemid': id, 'method': 'omniobj_revision.for_item', 'itemObjType': 'ask', 'page': page},
      action='objectlist', conn=self, **kw)

  def get_answer_history(self, id: int, page: int = 1, **kw) -> typing.List[
    RevisionAnswer]:
    """Get a Answer's History

    :param id: The ID of the Answer to get the History from
    :param page: Items page to get (Gets first page by default)
    """
    return self.http.get(
      params={'itemid': id, 'method': 'omniobj_revision.for_item', 'itemObjType': 'ans', 'page': page},
      action='objectlist', conn=self, **kw)

  def get_answer(self, id: int, **kw) -> Answer:
    """Get an answer

    :param id: The ID of the Answer
    """
    return self.http.get(params={'id': id}, action='omniobj', omniobj='ans', omnirest='GET', conn=self, **kw)

  def get_thank(self, id: int, **kw) -> Thank:
    """Get a wall thank message

    :param id: The ID of the thank
    """
    return self.http.get(params={'id': id}, action='omniobj', omniobj='thanksmsg', omnirest='GET', conn=self, **kw)

  def get_penfriend(self, id: int, **kw) -> PenfriendsItem:
    """Get a penfriends item

    :param id: The ID of the penfriends item
    """
    return self.http.get(params={'id': id}, action='omniobj', omniobj='penfriendsitem', omnirest='GET', conn=self, **kw)

  @ABCHelpers.require_cookies
  def upload_profile_image(self, image: typing.Union[str, io.BytesIO, bytes], **kw) -> bool:
    """Upload and validate an image

    :param image: Image to upload, can be either an Image URL, io.BytesIO object, bytes, or a Filename

    04/01/2021: Implemented!
    """
    image_formats = ("image/png", "image/jpeg", "image/jpg", "image/gif")
    filename, filedata, mimetype = None, None, None

    def from_buffer(buffer):
      _dt = buffer.read()
      return _dt, getattr(buffer, 'name', None), magic.from_buffer(_dt, mime=True)

    if isinstance(image, str):
      if os.path.exists(image):
        with open(image, "rb") as fp:
          filedata, filename, mimetype = from_buffer(fp)
      else:
        try:
          resp = requests.get(image)
          filedata = resp.content
          filename = os.path.basename(image)
          mimetype = resp.headers['Content-Type']
        except requests.exceptions.MissingSchema as exc:
          raise errors.InvalidImage(
            "image param is a string, but is not a valid image URL or a Path to an image file") from exc
    elif isinstance(image, io.BytesIO):
      filedata, filename, mimetype = from_buffer(image)
    elif isinstance(image, bytes):
      filedata = image
      mimetype = magic.from_buffer(image, mime=True)
    else:
      raise errors.InvalidImage("image param must be an Image URL, io.BytesIO object, bytes, or a Filename")

    # if mimetype not in image_formats:
    #   raise errors.InvalidImage("Invalid image format, allowed formats are image/png, image/jpeg and image/gif")

    if not filename:
      filename = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(5)) + "." + \
                 mimetype.split('/')[1]

    return self.http.post(
      url='https://stips.co.il/scripts/upload/photo.asp?photo_type=profile_photo',
      files={
        'file': (filename, filedata, mimetype, {})
      },
      get_success=True,
      **kw
    )

    # NOTE: This method also works (perhaps could be used if we dont have mimetype)

    # import urllib3
    # http = urllib3.PoolManager()
    # resp = http.request(
    #   method="POST",
    #   url='https://stips.co.il/scripts/upload/photo.asp?photo_type=profile_photo',
    #   fields={
    #     'file': (filename, filedata)
    #   },
    #   headers={
    #     "Cookie": "; ".join([f"{k}={v}" for k, v in self.cookies.items()])
    #   }
    # )
    # print(resp.status, resp._body)

  @ABCHelpers.require_cookies
  def resize_profile_image(self, x0: int = 0, x1: int = 0, y0: int = 0, y1: int = 0, user_id: int = None, **kw) -> bool:
    """Resize a profile image

    :param x0: Used to modify the image size in the first X coordinate
    :param x1: Used to modify the image size in the second X coordinate
    :param y0: Used to modify the image size in the first Y coordinate
    :param y1: Used to modify the image size in the second Y coordinate
    :param user_id: The User ID to resize the profile image (I assume admins can resize people's profile image)
    """
    return self.http.get(params={'userid': user_id or self.me.id, 'x0': x0, 'x1': x1, 'y0': y0, 'y1': y1},
                         action='profile.set_thumbnail', get_success=True, **kw)

  @ABCHelpers.require_cookies
  def remove_profile_image(self, user_id: int = None, **kw) -> bool:
    """Remove current profile image

    :param user_id: The User ID to remove the profile image for
    """
    return self.http.post(params={'userid': user_id or self.me.id}, action='profile.remove_photo',
                          get_success=True, **kw)

  @ABCHelpers.require_cookies
  def edit_answer(self, id: int, text: str, name: str, link_url: str = None, link_name: str = None, **kw) -> bool:
    """Edit an answer

    :param id: The Answer ID to edit
    :param text: The answer content
    :param link1: The URL of the Link
    :param link1name: The URL Title of the Link
    """
    return self.http.post(params={'id': id, 'a': text, 'name': name, 'link1': link_url, 'link1name': link_name},
                          omniobj='ans', omnirest='POST', get_success=True, **kw)

  def search_profiles(self, keyword: str, fuzz=True, get_ratio=False, **kw) -> typing.List[PartialUser]:
    """Search profiles (includes Full Usernames and IDs) by Username Keyword

    :param keyword: The Keyword to search with
    :param fuzz: Whether to sort the results with a better search
    :param get_ratio: Whether to return the ratio for keyword and user name
    """
    resp = self.http.get(params={'q': keyword, 'namespace': 'users', 'unit': 'Search'}, action='smartdata.get',
                         conn=self, **kw)

    if resp and fuzz:
      return utils.users_sort(keyword=keyword, results=resp, get_ratio=get_ratio)
    return resp

  def search_profile(self, keyword: str, fuzz=True, get_ratio=False, **kw) -> typing.Optional[PartialUser]:
    """Shortcut for the first item in search_profiles(keyword=keyword)
    :param keyword: The Keyword to search with
    :param fuzz: Try to find the closest match instead of getting the first result from search_profiles
    :param get_ratio: Whether to return the ratio for keyword and user name
    """
    resp = self.http.get(params={'q': keyword, 'namespace': 'users', 'unit': 'Search'}, action='smartdata.get',
                         conn=self, **kw)
    if resp and fuzz:
      return utils.users_sort(keyword=keyword, results=resp, get_ratio=get_ratio)[0]
    elif resp and not fuzz:
      return resp[0]
    return None

  def search_topic(self, keyword: str, **kw) -> typing.List[str]:
    """Search for Questions Tags by Tag Keyword

    :param keyword: The Keyword to search with
    """
    return self.http.get(params={'q': keyword}, action='item.tag_suggest', **kw)

  def get_channels(self, use_cache: bool = True, **kw) -> typing.List[ChannelConfig]:
    """Get a list of the channels that are shown in the right navbar

    :param use_cache: Whether to use the cache for better performance but a chance for misleading data
    """
    if use_cache and self.channels_cache:
      return list(self.channels_cache.values())

    return self._get_remote_config(cache_channels=True, **kw).channels
