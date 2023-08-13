"""
🛠️ 12/08/2023
Contains custom library errors
"""


class StipsException(Exception):
  """Base of Stips Exceptions"""


class NoAccount(StipsException):
  """Cookies not provided"""


class MissingCredentials(StipsException):
  """Neither email & password or cookies were provided"""


class InvalidCredentials(StipsException):
  """Invalid email / password"""


class NotAModerator(StipsException):
  """"Not a moderator"""


class HttpUnknown(StipsException):
  """Stips fucks up"""


class AnonymousPartialUser(StipsException):
  """PartialUser is anonymous so no user id"""


class InvalidImage(StipsException):
  """Invalid image provided"""
