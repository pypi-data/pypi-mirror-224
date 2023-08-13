"""
🛠️ 12/08/2023
Takes care of all the base HTTP requests and responses
"""

import contextlib
import json
import random
from functools import wraps

import requests
from bs4 import BeautifulSoup

from stips import errors, formatter


class RequestError(Exception):
  pass


base = 'https://stips.co.il/api'


def create_headers():
  return {
    'authority': 'stips.co.il',
    'cache-control': 'no-cache',
    'Connection': 'keep-alive',
    'pragma': 'no-cache',
    'accept-language': 'en,he;q=0.9,en-US;q=0.8,he-IL;q=0.7,la;q=0.6,ru;q=0.5',
    'Accept': 'application/json, text/plain, */*',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/%d.%d (KHTML, like Gecko) Chrome/%d.%d.%d.%d Safari/%d.%d' % (
      random.randint(0, 500), random.randint(0, 500),
      random.randint(0, 500), random.randint(0, 500), random.randint(0, 500), random.randint(0, 500),
      random.randint(0, 500), random.randint(0, 500)
    ),
    'Referer': 'https://stips.co.il/'
  }


def _get(params: dict = None, maybe_json: bool = False):
  resp = requests.get(
    url=base,
    params=params,
    headers=create_headers()
  )

  resp.raise_for_status()

  if maybe_json:
    with contextlib.suppress(json.JSONDecodeError):
      return resp.json(), resp
    return None, resp

  return resp


def build_url(base: str, endpoint: str):
  return f'{base.lstrip("/")}/{endpoint.strip("/")}'


class HTTPClient:
  """
  An HTTP client for the stips.co.il API
  """

  def __init__(self, cookies=None):
    self.base = base
    self.cookies = cookies
    self.just_none = False
    self.raise_exc = True

  def use_cookies(func):
    @wraps(func)
    def inner(self, *args, **kwgs):
      cookies_required = kwgs.get('cookies_required', False)

      cookies = kwgs.get('cookies', None)

      # pass cookies anyways
      if not cookies_required and self.cookies:
        kwgs['cookies'] = self.cookies
        return func(self, *args, **kwgs)

      if not cookies_required:
        return func(self, *args, **kwgs)

      if not cookies and not self.cookies:
        raise errors.NoAccount
      if self.cookies and not cookies:
        kwgs['cookies'] = self.cookies
      return func(self, *args, **kwgs)

    return inner

  def _build_url(self, endpoint, base=None):
    if (base or self.base or "").endswith(endpoint):
      endpoint = ""

    return build_url(base or self.base, endpoint)

  def try_to_frmt(self, js):
    if isinstance(js, dict):
      if js.get('data', js).get('omniOmniObj'):
        src = js['data']['omniOmniObj']
        return src
    elif isinstance(js, list):
      return_arr = []
      for val in js:
        src = val
        if val.get('data', val).get('omniOmniObj'):
          src = val['data']['omniOmniObj']

        return_arr.append(src)
      return return_arr

  def parse_success(self, js):
    if js.get('success', None):
      return js.get('success')

    dt = js.get('data', None)
    ok = js['status'] == 'ok'

    # print(dt)

    if dt:
      if dt.get('voted') is not None:
        return dt['voted']
      if dt.get('flowerSent') is not None:
        return dt['flowerSent']
      if dt.get('results', {}).get('notificationsRegistered') is not None:
        return dt['results']['notificationsRegistered']
      if dt.get('success') is not None:
        return dt['success']

    return ok

  def return_manager(self, js, name=None, conn=None):
    js = js['data']

    if isinstance(js, dict):
      js = js.get('omniOmniObj', js)

    if name:
      deep = name.split('.')
      seek = formatter
      for it in deep:
        seek = getattr(seek, it, None)
      if seek:
        if conn is not None:
          return seek(js, conn)
        return seek(js)

    resp = self.try_to_frmt(js)

    if isinstance(resp, dict):
      return formatter.AccessibleDict(**{**resp.get('data', {}), **resp.get('extra', {}), **resp.get('meta', {})})
    elif isinstance(resp, list):
      return [formatter.AccessibleDict(**{
        **src.get('data', {}),
        **src.get('extra', {}),
        **src.get('meta', {})
      }) for src in resp]

  def parse_response(self, resp, name=None, only_json=False, raw=False, only_id=False, only_success=False, conn=None):
    if raw:
      return resp

    # from now on whatever we return will use the .json() method, so lets parse and check for errors now
    try:
      js = resp.json()
    except json.JSONDecodeError:
      soup = BeautifulSoup(resp.text, features='lxml')
      try:
        error_text = soup.select_one('html > body > p font').text
      except AttributeError:
        raise RequestError(f'Failed to parse response: {resp.text}')

      if self.just_none:
        return None
      elif self.raise_exc:
        raise RequestError(error_text)
      else:
        return {"error": error_text}

    if only_json:
      return js

    if only_success:
      return self.parse_success(js)

    if only_id:
      return js.get('data', {}).get('newid', None)

    return self.return_manager(js, name, conn=conn)

  def _parse_get_args(self, omniobj, name, omnirest, params, data):
    if omniobj:
      # https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={"objType":"ask","data":{"id":"3129782"}}
      data_f = {'name': name, "rest_action": omnirest,
                'omniobj': json.dumps({"data": params, "objType": omniobj}, ensure_ascii=False),
                'api_params': json.dumps(data, ensure_ascii=False) or '{}'}
      name += f'.{omniobj}'
    else:
      data_f = {'name': name, 'api_params': json.dumps(params, ensure_ascii=False) or '{}'}
      if name == 'objectlist' and ('method' in params or 'objType' in params):
        method_or_objtype = params.get('method', params.get('objType'))

        if 'itemObjType' in params:
          name = f'{params["itemObjType"]}.{method_or_objtype.split(".")[0]}'
        else:
          name = f'{method_or_objtype.split(".")[0]}.many'
      elif name == 'smartdata.get' and 'namespace' in params and 'unit' in params:
        name = f'{params["namespace"]}.{params["unit"]}'

    if json.loads(data_f['api_params']) is None or data_f['api_params'] == '{}':
      del data_f['api_params']

    return name, data_f

  @use_cookies
  def get(self, endpoint='/api', params=None, cookies=None, data=None, only_json=False, cookies_required=True,
          raw=False, conn=None, *args,
          **kw):
    """
    Makes a GET request
    :param endpoint: API endpoint, likely `/api`
    :param params: used as a filler for `omniobj.data` container if `omniobj`, otherwise as a filler for `api_params` container
    :param cookies: cookies for the request, if not provided will try to recieve them from the global client
    :param data: to fill the `api_params` container inside the `omniobj`
    :param only_json: whether to only return the raw json response
    :param cookies_required: whether the request requires cookies to return correct data
    :param raw: whether to only return the response object
    """
    omniobj = kw.pop('omniobj', None)
    name = kw.pop('action', 'omniobj')
    omnirest = kw.pop('omnirest', None)

    name, data_f = self._parse_get_args(omniobj, name, omnirest, params=params, data=data)

    if 'safe_filter' in kw:
      data_f['safe_filter'] = kw.pop('safe_filter')

    only_success = kw.pop('get_success', False)
    only_id = kw.pop('get_id', False)

    url = self._build_url(endpoint)

    # print("GET", url, data_f)
    resp = requests.get(url, params=data_f, cookies=cookies, headers=create_headers(), *args, **kw)
    return self.parse_response(resp, name=name, only_json=only_json, raw=raw, only_id=only_id,
                               only_success=only_success, conn=conn)

  @use_cookies
  def post(self, data=None, endpoint='/api', params=None, cookies=None, only_json=False, cookies_required=True,
           raw=False, parse_as_get=False, *args,
           **kw):
    """
    Makes a POST request
    :param data: used to fill the `api_params` container
    :param endpoint: API endpoint, likely `/api`
    :param params: used as the `data` for custom URL requests, and as a filler for `omniobj.data` container
    :param cookies: cookies for the request, if not provided will try to recieve them from the global client
    :param only_json: whether to only return the raw json response
    :param cookies_required: whether the request requires cookies to return correct data
    :param raw: whether to only return the response object
    """

    omniobj = kw.pop('omniobj', None)
    name = kw.pop('action', 'omniobj')
    omnirest = kw.pop('omnirest', None)
    only_success = kw.pop('get_success', False)
    only_id = kw.pop('get_id', False)

    if kw.get('url'):
      # print(kw)
      resp = requests.post(kw.pop('url'), cookies=cookies, data=params, headers=create_headers(), **kw)
    else:
      # params
      if omniobj:
        # https://stips.co.il/api?name=omniobj&rest_action=GET&omniobj={"objType":"ask","data":{"id":"3129782"}}
        data_p = {'name': name, "rest_action": omnirest,
                  'omniobj': json.dumps({"data": params, "objType": omniobj}, ensure_ascii=False)}
        name += f'.{omniobj}'
      else:
        data_p = {'name': name, 'api_params': data or {}}

      # print("POST", url, data_p)
      # print(data_p)
      url = self._build_url(endpoint)
      resp = requests.post(url, cookies=cookies, data=data_p, headers=create_headers(), *args, **kw)

    return self.parse_response(resp, name=name, only_json=only_json, raw=raw, only_id=only_id,
                               only_success=only_success)

  use_cookies = staticmethod(use_cookies)
