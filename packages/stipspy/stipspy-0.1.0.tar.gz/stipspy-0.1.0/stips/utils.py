"""
🛠️ 12/08/2023
Utility functions for the library.
"""

import contextlib
import difflib
import json
import re
import typing
from datetime import datetime

import dateparser

from stips import models, enums


def unsplash(photo: str = None) -> str:
  """Represent an Unsplash photo as a string."""
  return (f'unsplash:{photo}' if not photo.isdigit() else photo) if photo else None


def users_sort(keyword: str, results: typing.Iterable[models.PartialUser], get_ratio: bool = False) -> typing.List[
  models.PartialUser]:
  """Sort a list of users by their similarity to a keyword."""
  if len(results) == 1:
    return results

  keyword = keyword.lower()

  exact_match = [user for user in results if user.name.lower() == keyword]

  if exact_match:
    return exact_match

  # keyword: You Only Live Once (
  # results: ["You Only Live Once (YOLO)", "You Only Live Once #"]
  # with this search, the first item will be matched better,
  # without it, difflib will pick the second item

  matches = sorted(
    [{"ratio": difflib.SequenceMatcher(None, keyword, user.name).ratio(), "user": user} for user in results],
    key=lambda match: match['ratio'] + (5 if match['user'].name.lower().startswith(keyword) else 0),
    reverse=True
  )

  # print("\n".join([f'{m["user"].name} ({m["ratio"]})' for m in matches]))

  new_matches = []
  for match in matches:
    if get_ratio:
      match['user'].ratio = match['ratio']
    new_matches.append(match['user'])
  return new_matches


def translate_badges(badges):
  """Translate a list of badges to a list of Badge enums."""
  return [*map(lambda bg: enums.Badge(bg['name']), badges)]


def translate_rank(rank):
  """Translate a rank to a Rank enum."""
  idx = ['no', 'regular', 'senior', 'admin'].index(rank)
  if idx == 0:
    return None
  return enums.Rank(idx)


def translate_ban(ban):
  """Translate a ban data to a clearer format"""
  return False if not ban['banned'] else {
    "ends_at": None if ban['endlessBan'] else datetime.strptime(ban['endDateText'], '%Y/%m/%d'),
    "message": ban['msg']
  }


def translate_status(data):
  """
  Translate a raw user's wall status to an object
  """
  if 'profile_quote' in data:
    return dict(
      **data['profile_quote'],
      last_modified=None
    )

  status_data = data['user_profile_page']['data']
  matches = re.findall(r'~[^~]+~$', status_data['text_status'])
  name = None
  text = status_data['text_status']
  if len(matches) != 0:
    name = matches[0][1:-1]
    text = text[:-len(matches[0])]

  return dict(
    name=name,
    text=text,
    last_modified=datetime.strptime(status_data['text_status_modified'], '%Y/%m/%d %H:%M:%S')
  )


def hebrew_date(text) -> datetime:
  """Translates an hebrew date representation to a date object."""
  return dateparser.parse(text.replace('-', ''), languages=['he'])


def deleted(archived, meta):
  """Return whether an item is deleted, and incase it is, provide information."""
  return False if not archived else meta_cls.adminMsgs(meta['adminMsgs']) if 'adminMsgs' in meta else True


def to_time(time_str: str) -> datetime:
  """Translates a time string to a datetime object."""
  with contextlib.suppress(ValueError):
    return datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')

  return datetime.strptime(time_str, '%d/%m/%Y %H:%M:%S')


def get_photo(user_id, photostamp):
  """Get a user's photo by their id and the photo's photostamp."""
  return f'https://stipscdn-stips.netdna-ssl.com/photos/user_profile/a/{user_id}/{photostamp}.jpg'


def parse_cookies(cookies_string):
  """Parse a cookies string to a dictionary."""
  with contextlib.suppress(json.JSONDecodeError):
    return json.loads(cookies_string)

  cookies_string = cookies_string.strip('; "')
  blacklist = ['_ga', '_gid', '_gat', 'trc_cookie_storage', '__gads']
  converted = {sp[0].strip(): sp[1].strip() for sp in [cc.strip(';').split('=', 1) for cc in cookies_string.split(';')]}
  return {k: v for k, v in converted.items() if k not in blacklist}
