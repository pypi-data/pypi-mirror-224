"""
🛠️ 12/08/2023
All the models are created by methods from the formatter.py file.
These models represent the data that is returned from the API,
and some of them (like the User class) allow chaining methods.

Exmaple:
```py
from stips import StipsClient

bot = StipsClient(email='...', password='...')

user = bot.get_user(id=123456)
profile = user.get_profile()  # chaining
```
"""

from __future__ import annotations  # https://stackoverflow.com/questions/39740632

import dataclasses
import datetime
import typing

from dataclasses_json import dataclass_json

from stips.enums import Rank, Gender, Badge, ReportType, NotificationType, PhotoType, ItemEditor, ActivityType
from stips.errors import AnonymousPartialUser

# https://stackoverflow.com/questions/39740632/python-type-hinting-without-cyclic-imports
if typing.TYPE_CHECKING:
  from stips import StipsClient


def check_user_id(func):
  """A decorator that forces the user in the model to not be anonymous,
    since you cannot run methods on anonymous users.
  """

  def inner(self, *args, **kw):
    if not self.id:
      raise AnonymousPartialUser("Cannot run method on an anonymous user")

    return func(self, *args, **kw)

  return inner


class UserIdMethods:
  """Methods that use self.id as the user id"""
  _state: StipsClient

  @check_user_id
  def get_profile(self, **kw) -> Profile:
    return self._state.get_profile(user_id=self.id, **kw)

  @check_user_id
  def get_user(self, **kw) -> Profile:
    return self._state.get_user(id=self.id, **kw)

  @check_user_id
  def get_thanks(self, page: int = 1, **kw) -> typing.List[Thank]:
    return self._state.get_user_thanks(user_id=self.id, page=page, **kw)

  @check_user_id
  def get_activity(self, action: typing.Union[ActivityType, str] = ActivityType.answers, **kw) -> typing.List[
    ChartData]:
    return self._state.get_profile_activity(user_id=self.id, action=action, **kw)

  @check_user_id
  def get_flowers(self, page: int = 1, **kw) -> typing.List[Answer]:
    return self._state.get_user_flowers(user_id=self.id, page=page, **kw)

  @check_user_id
  def edit_wall(self, text: str, **kw) -> bool:
    return self._state.edit_wall(text=text, user_id=self.id, **kw)

  @check_user_id
  def send_thank(self, text: str, **kw) -> int:
    return self._state.send_thank(user_id=self.id, text=text, **kw)

  @check_user_id
  def send_message(self, text: str, **kw) -> int:
    return self._state.send_message(user_id=self.id, text=text, **kw)

  @check_user_id
  def get_messages(self, message_id: int = 0, first_load: bool = False, history: bool = False, **kw) -> typing.Union[
    bool, typing.List[MessageItem]]:
    return self._state.get_messages(user_id=self.id, message_id=message_id, first_load=first_load, history=history,
                                    **kw)

  @check_user_id
  def update_details(self, name: str = None, birth_date: typing.Union[datetime.datetime, str] = None,
                     gender: typing.Union[enums.Gender, str] = None, **kw) -> bool:
    return self._state.update_details(name=name, birth_date=birth_date, gender=gender, user_id=self.id, **kw)

  @check_user_id
  def enable_safe_mode(self, **kw) -> bool:
    return self._state.enable_safe_mode(user_id=self.id, **kw)

  @check_user_id
  def disable_safe_mode(self, **kw) -> bool:
    return self._state.disable_safe_mode(user_id=self.id, **kw)

  @check_user_id
  def resize_profile_image(self, x0: int = 0, x1: int = 0, y0: int = 0, y1: int = 0, **kw) -> bool:
    return self._state.resize_profile_image(user_id=self.id, x0=x0, x1=x1, y0=y0, y1=y1, **kw)

  @check_user_id
  def remove_profile_image(self, **kw) -> bool:
    return self._state.remove_profile_image(user_id=self.id, **kw)


# ✅
@dataclass_json()
@dataclasses.dataclass()
class DeletedItem:
  """Represents a deleted item

  :param time: The time the item was deleted
  :param hebrew_time: The time the item was deleted in hebrew
  :param reason: The reason the item was deleted
  :param deletor: The user who deleted the item (or the role)
  :param points: The amount of points the user lost
  """
  time: datetime.datetime
  hebrew_time: str
  reason: str
  deletor: str
  points: int


# ✅
@dataclass_json()
@dataclasses.dataclass()
class PartialUser(UserIdMethods):
  """Represents a partial user

  :param _state: The state of the client to use for methods
  :param anonymous: Whether the user is anonymous
  :param id: The user's id
  :param name: The user's name
  :param online: Whether the user is online
  :param photo: The user's photo
  :param is_question_owner: Whether the user is the owner of the question
  :param gender: The user's gender
  """
  _state: StipsClient

  anonymous: bool
  id: typing.Optional[int]
  name: typing.Optional[str]
  online: typing.Optional[bool]
  photo: typing.Optional[str]

  is_question_owner: typing.Optional[bool]  # Answer.author
  gender: typing.Optional[Gender]  # ContactUserItem

  # for ratio search_profile(s)
  ratio: typing.Optional[float] = None


@dataclass_json()
@dataclasses.dataclass()
class UserPhoto:
  """
  Represents a user photo

  :param id: The user_id who the photo belongs to
  :param photostamp: The upload photostamp of the photo
  :param url: The url of the photo
  """
  user_id: int
  photostamp: int
  url: str

  def __repr__(self) -> str:
    return self.url if self.url else super().__repr__()

  def __str__(self) -> str:
    return self.url if self.url else super().__repr__()


# ✅
@dataclass_json()
@dataclasses.dataclass(repr=False)
class Photo:
  """
  Represents a photo

  :param type: The type of the photo
  :param url: The url of the photo
  :param url_small: The url of the small photo (unsplash only)
  :param creator_name: The name of the creator of the photo (unsplash credits)
  :param creator_username: The username of the creator of the photo (unsplash credits)
  """
  type: PhotoType
  url: str
  url_small: typing.Optional[str]
  creator_name: typing.Optional[str]
  creator_username: typing.Optional[str]

  def __repr__(self) -> str:
    return self.url

  def __str__(self) -> str:
    return self.url


# ✅
@dataclass_json()
@dataclasses.dataclass(repr=False)
class Link:
  """
  Represents a link in a question or an answer

  :param url: The url of the link
  :param name: The name of the link (that is displayed)
  """
  url: str
  name: typing.Optional[str] = None

  def __repr__(self) -> str:
    return self.url

  def __str__(self) -> str:
    return self.url


# ✅
@dataclass_json()
@dataclasses.dataclass()
class Permissions:
  """
  Represents the permissions of a user

  :param ban: Whether the user can ban the author
  :param delete: Whether the user can delete the item
  :param delete_without_notification: Whether the user can delete without notification
  :param edit: Whether the user can edit the item
  :param owner: Whether the user is the owner of the item
  :param report: Whether the user can report the item
  :param admin_messages: Whether the user can view admin messages (if there are)
  """
  ban: bool
  delete: bool
  delete_without_notification: bool
  edit: bool
  owner: bool
  report: bool
  admin_messages: bool


# ✅
@dataclass_json()
@dataclasses.dataclass()
class Ban:
  """
  Represents a ban

  :param reason: The reason of the ban
  :param ends_at: The time the ban ends at (unless permanent)
  """
  reason: str
  ends_at: typing.Optional[datetime.datetime]


# ✅
@dataclass_json()
@dataclasses.dataclass()
class Status:
  """
  Represents a wall status

  :param name: Who wrote the status (quote writer)
  :param text: The text of the status
  :param last_modified: The time the status was last modified
  """
  name: str
  text: str
  last_modified: typing.Optional[datetime.datetime]
  view: str = None

  def __post_init__(self):
    self.view = f'{self.text}\n~{self.name}~'


# ✅
@dataclass_json()
@dataclasses.dataclass()
class PartialQuestion:
  """
  Represents a partial question

  :param id: The id of the question
  :param title: The title of the question
  """
  id: int
  title: str


#############
# ✅ dataclasses: DeletedItem, Link, PartialUser
@dataclass_json()
@dataclasses.dataclass()
class Answer:
  """
  Represents an answer

  :param _state: The state of the client to use for methods
  :param id: The id of the answer
  :param question_id: The id of the question the answer belongs to
  :param question_url: The url of the question the answer belongs to
  :param question_title: The title of the question the answer belongs to
  :param text: The text of the answer
  :param anonymous: Whether the answer is anonymous
  :param deleted: Whether the answer is deleted, and information in case it is
  :param link: The link in the answer (if there is)
  :param author: The author of the answer (partial)
  :param flowered: Whether the answer is flowered
  :param time: The time the answer was posted
  :param hebrew_time: The hebrew time the answer was posted
  :param has_revisions: Whether the answer has revisions (was edited)
  :param votes: The amount of votes the answer has that is displayed (upvotes - downvotes)
  :param upvotes: The amount of upvotes the answer has
  :param downvotes: The amount of downvotes the answer has
  :param me_vote: The vote of the client (if there is)
  :param permissions: The permissions of the client on the answer
  """
  _state: StipsClient

  id: int
  question_id: int
  question_url: str
  question_title: typing.Optional[str]
  text: str
  anonymous: bool
  deleted: typing.Union[bool, DeletedItem]
  link: typing.Optional[Link]
  author: PartialUser
  flowered: bool
  time: datetime.datetime
  hebrew_time: str
  has_revisions: bool
  votes: int
  upvotes: int
  downvotes: int
  me_vote: int  # -1: downvote, 0: no vote, 1: upvote
  permissions: Permissions

  def delete(self, title: str = '', points: typing.Optional[int] = None, message: str = '', ban: bool = False,
             **kw) -> bool:
    return self._state.delete_answer(id=self.id, title=title, points=points, message=message, ban=ban, **kw)

  def warn(self, title: str = '', message: str = '', **kw) -> bool:
    return self._state.warn_answer(id=self.id, title=title, message=message, **kw)

  def upvote(self, **kw) -> bool:
    return self._state.upvote(id=self.id, **kw)

  def downvote(self, **kw) -> bool:
    return self._state.downvote(id=self.id, **kw)

  def reset_vote(self, **kw) -> bool:
    return self._state.reset_vote(id=self.id, **kw)

  def report(self, reason: str, **kw) -> bool:
    return self._state.report_answer(id=self.id, reason=reason, **kw)

  def flower(self, **kw) -> bool:
    return self._state.flower(id=self.id, **kw)

  def set_anonymous(self, **kw) -> bool:
    return self._state.set_answer_anonymous(id=self.id, **kw)

  def history(self, page: int = 1, **kw) -> typing.List[RevisionAnswer]:
    return self._state.get_answer_history(id=self.id, page=page, **kw)

  def edit(self, text: str, name: str, link_url: str = None, link_name: str = None, **kw) -> bool:
    return self._state.edit_answer(id=self.id, text=text, name=name, link_url=link_url, link_name=link_name, **kw)


########
# ✅ dataclasses: DeletedItem, PartialUser, Photo, Link, Permissions
@dataclass_json()
@dataclasses.dataclass()
class Question:
  """
  Represents a question

  :param _state: The state of the client to use for methods
  :param id: The id of the question
  :param url: The url of the question
  :param anonymous: Whether the question is anonymous
  :param answer_count: The amount of answers the question has
  :param pin_count: The amount of pins the question has
  :param deleted: Whether the question is deleted, and information in case it is
  :param title: The title of the question
  :param link: The link in the question (if there is)
  :param has_revisions: Whether the question has revisions (was edited)
  :param safe_filter: Whether the question triggers the safe filter
  :param tags: The tags of the question
  :param content: The content of the question
  :param time: The time the question was posted
  :param hebrew_time: The hebrew time the question was posted
  :param author: The author of the question (partial)
  :param me_pinned: Whether the client pinned the question
  :param photo: The photo of the question
  :param permissions: The permissions of the client on the question
  """

  _state: StipsClient

  id: int
  url: str
  anonymous: bool
  answer_count: int
  pin_count: int
  deleted: typing.Union[bool, DeletedItem]
  title: str
  link: typing.Optional[Link]
  has_revisions: bool
  safe_filter: bool
  tags: typing.List[str]
  content: str
  time: datetime.datetime
  hebrew_time: str
  author: PartialUser
  me_pinned: bool
  photo: Photo
  permissions: Permissions

  def answers(self, page: int = 1, **kw) -> typing.List[Answer]:
    return self._state.get_answers(self.id, page)

  def answer(self, text: str, name: str = None, link_url: str = None, link_name: str = None, anonymous: bool = False,
             **kw) -> int:
    return self._state.answer(question_id=self.id, text=text, name=name, link_url=link_url, link_name=link_name,
                              anonymous=anonymous, **kw)

  def report(self, reason: str, **kw) -> bool:
    return self._state.report_question(id=self.id, reason=reason, **kw)

  def history(self, page: int = 1, **kw) -> typing.List[RevisionQuestion]:
    return self._state.get_question_history(id=self.id, page=page, **kw)

  def delete(self, title: str = '', points: typing.Optional[int] = None, message: str = '', ban: bool = False,
             **kw) -> bool:
    return self._state.delete_question(id=self.id, title=title, points=points, message=message, ban=ban, **kw)

  def warn(self, title: str = '', message: str = '', **kw) -> bool:
    return self._state.warn_question(id=self.id, title=title, message=message, **kw)

  def pin(self, **kw) -> bool:
    return self._state.pin(id=self.id, **kw)

  def unpin(self, **kw) -> bool:
    return self._state.unpin(id=self.id, **kw)

  def enable_notifications(self, **kw) -> bool:
    return self._state.enable_question_notifications(id=self.id, **kw)

  def disable_notifications(self, **kw) -> bool:
    return self._state.disable_question_notifications(id=self.id, **kw)

  def has_notifications(self, **kw) -> bool:
    return self._state.has_questions_notifications(id=self.id, **kw)

  def set_anonymous(self, **kw) -> bool:
    return self._state.set_question_anonymous(id=self.id, **kw)

  def edit(self, title: str = None, content: str = None, tags: list = None, photo: str = None, **kw) -> bool:
    return self._state.edit_question(id=self.id, title=title, content=content, tags=tags, photo=photo, **kw)

  def remove_from_channel(self, channel_id: int = None, channel_name: str = None, **kw) -> bool:
    return self._state.remove_question_from_channel(id=self.id, channel_id=channel_id, channel_name=channel_name, **kw)


# ✅ dataclasses: Ban
@dataclass_json()
@dataclasses.dataclass()
class AppUser:
  """
  Represents the client details

  :param id: The id of the client
  :param ban: Whether the client is banned, and information in case it is
  :param birth_date: The birth date of the client
  :param rank: The rank of the client
  :param permissions: The permissions of the client
  :param phone_validated: Whether the client validated their phone
  :param points: The points of the client
  :param safe_filter: Whether the client has the safe filter on
  :param email: The email of the client
  :param flowers: The amount of flowers the client has
  :param gender: The gender of the client
  """
  id: int
  ban: typing.Union[bool, Ban]
  birth_date: datetime.datetime
  rank: typing.Optional[Rank]
  permissions: dict  # needs more investigation
  phone_validated: bool
  points: int
  safe_filter: bool
  email: str
  flowers: int
  gender: Gender


# ✅ dataclasses: Permissions
@dataclass_json()
@dataclasses.dataclass()
class User(UserIdMethods):
  """
  Represents a user

  :param _state: The state of the client to use for methods
  :param id: The id of the user
  :param url: The url to the user's profile
  :param photo: The photo of the user
  :param photo_updated_stamp: The time that the user's photo was updated
  :param points: The points of the user
  :param online: Whether the user is online
  :param name: The name of the user
  :param permissions: The permissions that the client has on the user
  """
  _state: StipsClient

  id: int
  url: str
  gender: Gender
  photo: typing.Optional[UserPhoto]
  photo_updated_stamp: typing.Optional[datetime.datetime]
  points: int
  online: bool
  name: str

  permissions: Permissions


# ✅ dataclasses: Status
@dataclass_json()
@dataclasses.dataclass()
class Profile(UserIdMethods):
  """
  Represents a user's profile

  :param _state: The state of the client to use for methods
  :param id: The id of the user
  :param url: The url to the user's profile
  :param age: The age of the user
  :param birth_year: The birth year of the user
  :param questions: The amount of questions the user asked
  :param answers: The amount of answers the user answered
  :param flowers: The amount of flowers the user has
  :param badges: The badges the user has
  :param created_at: The time the user created their account
  :param status: The status of the user
  """
  _state: StipsClient

  id: typing.Optional[int]
  url: str
  age: int
  birth_year: int
  questions: int
  answers: int
  flowers: int
  badges: typing.List[Badge]
  created_at: datetime.datetime
  status: Status

  # special attrs
  hide_age: typing.Optional[bool] = None
  hide_stats: typing.Optional[bool] = None


# ✅ dataclasses: PartialUser, Permissions
@dataclass_json()
@dataclasses.dataclass()
class Thank:
  """
  Represents a thank (מקיר התודות)

  :param _state: The state of the client to use for methods
  :param id: The id of the thank
  :param author: The author of the thank
  :param to_id: The id of the user that the thank is for
  :param text: The text of the thank
  :param time: The time the thank was sent
  :param hebrew_time: The hebrew time the thank was sent
  :param permissions: The permissions that the client has on the thank
  """
  _state: StipsClient

  id: int
  author: PartialUser
  to_id: int
  text: str
  time: datetime.datetime
  hebrew_time: str

  permissions: Permissions

  def delete(self, title: str = '', points: typing.Optional[int] = None, message: str = '', ban: bool = False,
             fake_delete: bool = False, **kw) -> bool:
    return self._state.delete_thank(id=self.id, title=title, points=points, message=message, ban=ban,
                                    fake_delete=fake_delete, **kw)


# ✅ dataclasses: Question, Answer, PartialUser, Permissions
@dataclass_json()
@dataclasses.dataclass()
class ReportItem:
  """
  Represents a report item (question/answer)

  :param _state: The state of the client to use for methods
  :param id: The id of the report item
  :param type: The type of the report item
  :param question: The question of the report item
  :param answer: The answer of the report item
  :param partial_question: The partial question of the report item
  :param reason: The reason for the report
  :param author: The author of the report
  :param time: The time the report was sent
  :param hebrew_time: The hebrew time the report was sent
  :param permissions: The permissions that the client has on the report
  :param item: The item that was reported
  """
  _state: StipsClient

  id: int
  type: ReportType
  question: typing.Optional[Question]
  answer: typing.Optional[Answer]
  partial_question: typing.Optional[PartialQuestion]
  reason: str
  author: PartialUser
  time: datetime.datetime
  hebrew_time: str

  permissions: Permissions
  item: typing.Union[Question, Answer] = None  # gets set in __post_init__

  def __post_init__(self):
    self.item = {
      ReportType.question: self.question,
      ReportType.answer: self.answer
    }.get(self.type)

  def delete(self, title: str = '', points: typing.Optional[int] = None, message: str = '', ban: bool = False,
             **kw) -> bool:
    delete_method = {
      ReportType.question: self._state.delete_question,
      ReportType.answer: self._state.delete_answer
    }.get(self.type)
    #                                   ^
    # if you're looking for type hints its either one above
    return delete_method(id=self.item.id, title=title, points=points, message=message, ban=ban, **kw)

  def decline(self, **kw) -> bool:
    return self._state.decline_reports(id=self.item.id, **kw)


# ✅ dataclasses: PartialUser
@dataclass_json()
@dataclasses.dataclass()
class PenfriendsItem:
  """
  Represents a penfriends item (מחברים לעט)

  :param _state: The state of the client to use for methods
  :param id: The id of the penfriends item
  :param time: The time the penfriends item was sent
  :param hebrew_time: The hebrew time the penfriends item was sent
  :param author: The author of the penfriends item
  :param text: The text of the penfriends item
  """
  _state: StipsClient

  id: int
  time: datetime.datetime
  hebrew_time: str
  author: PartialUser
  text: str

  def delete(self, title: str = '', points: typing.Optional[int] = None, message: str = '', ban: bool = False,
             fake_delete: bool = False, **kw) -> bool:
    return self._state.delete_penfriend(id=self.id, title=title, points=points, message=message, ban=ban,
                                        fake_delete=fake_delete, **kw)


# ✅ dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class NotificationItem:
  """
  Represents a notification item (התראה)

  :param id: The id of the notification item
  :param type: The type of the notification item
  :param viewed: Whether the notification item was viewed
  :param time: The time the notification item was sent
  :param click_url: The url that the notification item will redirect to when clicked
  :param link_item_id: The id of the item that the notification item links to
  :param real_item_id: if link_item_id is an answer, then the real_item_id is the id of its question
  :param text: The text of the notification item
  :param message: The message of the notification item
  :param points: The points that were taken from the user in the notification (למשל מחיקה)
  """
  id: int
  type: NotificationType
  viewed: bool
  time: datetime.datetime
  click_url: typing.Optional[str]
  link_item_id: int
  real_item_id: int
  text: str
  message: str
  points: int


# ✅ dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class MessagesListItem:
  """
  Represents a DM

  :param id: The id last message
  :param from_user: The user that sent the last message
  :param time: The time the last message was sent
  :param hebrew_time: The hebrew time the last message was sent
  :param view_time: The time the last message was viewed
  :param new_messages_count: The amount of new messages
  :param last_message: The last message sent (its content)
  :param url: The url to the DM
  :param is_me_last_message: Whether the last message was sent by the client
  :param me_id: The id of the client
  """
  id: int
  is_me_last_message: bool
  from_user: PartialUser
  me_id: int
  time: datetime.datetime
  hebrew_time: str
  view_time: typing.Optional[datetime.datetime]
  new_messages_count: int
  last_message: str
  url: str = None

  def __post_init__(self):
    self.url = f'https://stips.co.il/messages/{self.from_user.id}'


# dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class MessageItem:
  """
  Represents a message in a DM

  :param id: The id of the message
  :param from_id: The id of the user that sent the message
  :param to_id: The id of the user that received the message
  :param time: The time the message was sent
  :param hebrew_time: The hebrew time the message was sent
  :param view_time: The time the message was viewed
  :param text: The text of the message
  """
  id: int
  from_id: int
  to_id: int
  time: datetime.datetime
  hebrew_time: str
  view_time: typing.Optional[datetime.datetime]
  text: str


# dataclasses: User
@dataclass_json()
@dataclasses.dataclass()
class ContactUserItem(User):
  """
  Represents a user in the contact list

  :param blocked: Whether the user is blocked
  :param permissions: The permissions that the client has on the user

  ... rest of the params are the same as User
  """
  blocked: bool
  permissions = Permissions


# ✅ dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class NotificationsCount:
  """
  Represents the notifications in the bell and the chats icons

  :param messages: The amount of unread messages that the client has
  :param notifications: The amount of unread notifications that the client has
  """
  messages: int
  notifications: int


# ✅ dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class ChartData:
  """
  Represents a data item as part of a chart (user answers, questions, flowers)

  :param time: Data item time
  :param count: Data item value
  """

  time: datetime.datetime
  count: int


# ✅ dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class QuestionsLimit:
  """
  Represents the questions limit of the client

  :param allowed: Whether the client is allowed to ask any more questions
  :param current: The amount of questions the client asked today
  :param max: The max amount of questions the client can ask today (likely 10)
  """
  allowed: bool
  current: int
  max: int


# ✅ dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class GalleryImage:
  """
  Represents an image from stips' database (gallery)

  :param id: The id of the image
  :param url: The url of the image
  """
  id: int
  url: str

  def __repr__(self) -> str:
    return self.url

  def __str__(self) -> str:
    return self.url


# dataclasses:
@dataclass_json()
@dataclasses.dataclass()
class PenfriendsLimit:
  """
  Represents the penfriends limit of the client

  :param allowed: Whether the client is allowed to post a penfriends item
  :param minutes_left: The amount of minutes left until the client can post a penfriends item
  :param allowed_every: The amount of minutes the client has to wait between posting penfriends items
  """
  allowed: bool
  minutes_left: int
  allowed_every: int

  def __bool__(self):
    return self.allowed


# ✅ dataclasses: Link, PartialUser, Permissions
@dataclass_json()
@dataclasses.dataclass()
class RevisionQuestion:
  """
  Represents a question revision (edit)

  :param editor: The editor of the question (moderator or the author)
  :param id: The id of the revision
  :param question_id: The id of the question
  :param title: The title of the question
  :param content: The content of the question
  :param tags: The tags of the question
  :param photo: The photo of the question
  :param link: The link in the question
  :param channel_id: The id of the channel the question was in
  :param time: The time the revisioned question was made
  :param hebrew_time: The hebrew time the revisioned question was made
  :param author: The author of the revisioned question (partial)
  :param permissions: The permissions that the client has on the revisioned question
  """
  editor: ItemEditor
  id: int
  question_id: int
  title: str
  content: str
  tags: typing.List[str]
  photo: Photo
  link: typing.Optional[Link]
  channel_id: int
  time: datetime.datetime
  hebrew_time: str
  author: PartialUser

  permissions: Permissions


@dataclass_json()
@dataclasses.dataclass()
class RevisionAnswer:
  """
  Represents an answer revision (edit)

  :param editor: The editor of the answer (moderator or the author)
  :param id: The id of the revision
  :param answer_id: The id of the answer
  :param text: The text of the answer
  :param link: The link in the answer
  :param time: The time the revisioned answer was made
  :param hebrew_time: The hebrew time the revisioned answer was made
  :param author: The author of the revisioned answer (partial)
  :param permissions: The permissions that the client has on the revisioned answer
  """
  editor: ItemEditor
  id: int
  answer_id: int
  text: str
  link: typing.Optional[Link]
  time: datetime.datetime
  hebrew_time: str
  author: PartialUser

  permissions: Permissions


@dataclass_json()
@dataclasses.dataclass()
class ChannelConfig:
  """
  Represents a channel's config from the remote config

  :param id: The id of the channel
  :param name: The name of the channel (מוסיקה, טכנולוגיה, ...)
  :param background_color_css: The background color of the channel in css format
  :param background_url: The background url of the channel
  :param icon_name: The icon name of the channel
  :param no_channel_remove_notification: Whether the user that asked a question in this
                                          channel, and it got removed should get a notification
  :param slogan: The slogan of the channel (not sure what it could be yet)
  """
  id: int
  name: str
  background_color_css: str
  background_url: str
  icon_name: str
  no_channel_remove_notification: bool
  slogan: typing.Optional[typing.Any]  # not sure what it could be yet


@dataclass_json()
@dataclasses.dataclass()
class RemoteConfig:
  """
  Represents the remote config (currently I know only about channels)

  :param channels: The channels (listed on the top right sidebar)
  """
  channels: typing.List[ChannelConfig]
