"""
🛠️ 12/08/2023
Utility functions for HTTP methods that use a `page` parameter.
"""

import functools


def iter_pages(func, one_at_a_time: bool = True, page_start: int = 1, yield_index: bool = False, **kw):
  """
  A function that returns an iterator for http methods that use a `page` paramater.
  The iterator will keep returning items until an empty list will be returned, or an error will be raised
  :param func: the http function to recieve data from
  :param one_at_a_time: if True, will return one item each time instead of the whole page
  :param page_start: page index to start at. defaults to 1 (first page)
  :param yield_index: whether to yield a tuple of (page_index, result) instead of just the result, if True along with RETURN_ITEMS, will yield (item_index, result)
  :param kw: arguments to pass to the http function, this simply uses functools.partial() so you can do that yourself if you want...

  Example:
  ```py
  '''Iterate over all thanks in a user's profile'''
  import stips
  from stips.pagetools import iter_pages

  api = stips.StipsClient()
  user = api.get_user(244844)

  for thank in iter_pages(user.get_thanks):
    print(thank.text)
    input("Press enter to print the next thank...")
  ```
  """

  call = functools.partial(func, **kw)

  page = page_start
  resp = []

  items_idx = 0

  while (page == page_start) or len(resp) > 0:
    resp = call(page=page)

    # print(f'PAGE: {page} | RESP: {len(resp)}')

    if len(resp) == 0:
      break

    if one_at_a_time:
      for item in resp:
        items_idx += 1
        yield (items_idx, item) if yield_index else item
    else:
      yield (page, resp) if yield_index else resp

    page += 1
