"""
🛠️ 12/08/2023
This module contains all the enums such as Rank, Gender, etc...
"""

import enum
import aenum


def get_enum(var):
  if isinstance(var, enum.Enum):
    return var.value
  return var


class ExtendedEnum(enum.Enum):
  pass


class Rank(ExtendedEnum):
  """The rank of the user (if any)"""
  moderator = 1
  senior_moderator = 2
  admin = 3


class Badge(ExtendedEnum):
  """The badge of the user"""
  senior_advisor = 'senior_advisor'
  moderator = 'moderator'
  senior_moderator = 'senior_moderator'
  old_expert = 'old_expert'
  custom = 'custom'


class Gender(aenum.MultiValueEnum):
  """The gender of the user"""
  male = 0, 1
  female = 2


class PhotoType(ExtendedEnum):
  """The type of the photo
  builtin: The photo is stored in some database in the stips' server
  unsplash: The photo is taken from https://unsplash.com
  """
  builtin = 1
  unsplash = 2


class Role(ExtendedEnum):
  """Notes who deleted an item, a moderator or the system"""
  moderators = 1
  system = 2


class ReportType(ExtendedEnum):
  """The type of the report"""
  question = 1
  answer = 2


class NotificationType(ExtendedEnum):
  """The type of the notification"""
  question_deleted = 1  # delete_ask
  answer_deleted = 2  # delete_ans
  thank_deleted = 3  # delete_thanks_wall_msg
  penfriends_deleted = 4  # delete_pen_friends_item
  report_accepted = 5  # user_report_thanks
  wall_message = 6  # new_thanks_wall_msg
  new_answer = 7  # new_ask_ans_registered
  new_flower = 8  # new_flower


class ItemEditor(ExtendedEnum):
  """Notes who edited an item, a moderator or the owner of the item"""
  owner = 1  # owner
  moderator = 2  # moderator


class ChannelType(ExtendedEnum):
  """The type of the channel"""
  music = 'מוסיקה'
  pets = 'בעלי חיים'
  studies = 'לימודים'
  internet = 'אינטרנט וטכנולוגיה'
  tv = 'סדרות וסרטים'
  philosophy = 'פילוסופיה'


class TimeType(ExtendedEnum):
  """Fetch questions by TimeType (now, today, week, month)"""
  now = 'now'
  today = 'today'
  week = 'week'
  month = 'month'


class MyQuestionType(ExtendedEnum):
  """Fetch questions that you asked / answered / pinned"""
  asked = 'asked'
  answered = 'ansed'  # typo ?
  ansed = 'ansed'
  pinned = 'pinned'


class ActivityType(ExtendedEnum):
  """Get the user's activity based on their answers / questions / flowers"""
  answers = 'ans'
  questions = 'ask'
  flowers = 'flowers'
