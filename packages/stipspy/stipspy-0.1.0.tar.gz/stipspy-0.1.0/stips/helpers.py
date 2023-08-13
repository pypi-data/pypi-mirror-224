"""
🛠️ 12/08/2023
Helpers decorators for the HTTP functions.
"""

from functools import wraps
from stips import errors


class ABCHelpers:
  def safe_filter(func):
    """
    The safe_filter decorator passes the safe_filter parameter to the function based on the configuration in StipsClient.
    """

    @wraps(func)
    def inner(self, *args, **kwgs):
      safe = kwgs.get('safe_filter')
      if safe is None:
        kwgs['safe_filter'] = self.safe_filter
      return func(self, *args, **kwgs)

    return inner

  def require_cookies(func):
    """
    The require_cookies decorator notes that the function is a user method and required either cookies or email&password to be passed
    to the class.
    """

    @wraps(func)
    def inner(self, *args, **kwgs):
      if not self.cookies:
        raise errors.NoAccount(
          f"Function '{func.__name__}' requires connecting an account when initializing a StipsClient")
      return func(self, *args, cookies_required=True, **kwgs)

    return inner

  def moderator_endpoint(func):
    """
    The moderator_endpoint decorator notes that the function is a moderator method and requires the user to be a moderator (or above)
    """

    @wraps(func)
    def inner(self, *args, **kwgs):
      if not self.cookies:
        raise errors.NoAccount(f"Function '{func.__name__}' requires cookies to perform")

      rank = self.me.rank
      if not rank or rank.value <= 0:
        raise errors.NotAModerator(f"Function '{func.__name__}' requires moderator permissions to perform")

      return func(self, *args, cookies_required=True, **kwgs)

    return inner
