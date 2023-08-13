"""
🛠️ 12/08/2023
Provides typehints and dot.notation for the API responses
"""

from stips.utils import *


class AccessibleDict():
  """An accessible dict can be accessed with dot.notation"""

  def __init__(self, do_recurv=True, **itms):
    if do_recurv:
      self.obj = {}
      for k, v in itms.items():
        if isinstance(v, dict):
          self.obj[k] = AccessibleDict(**v)
        else:
          self.obj[k] = v
    else:
      self.obj = itms

  def __getattr__(self, item):
    return self.obj[item]

  def __getitem__(self, item):
    self.obj[item]

  def __setitem__(self, key, value):
    self.obj[key] = value

  def get(self, *args, **kw):
    return self.obj.get(*args, **kw)

  def __add__(self, other):
    if not isinstance(other, AccessibleDict):
      raise NotImplementedError

    # first (self) object gets to keep their value if duplicates

    v1 = vars(self)
    v2 = vars(other)

    new = v2.copy()

    for k, v in v1.items():
      new[k] = v

    return AccessibleDict(**new)

  def pop(self, itm):
    return self.obj.pop(itm)

  @property
  def __dict__(self):
    return self.obj

  def to_dict(self):
    """Recoursively make all AccessibleDict classes dictionaries"""
    new = {}
    for k, v in vars(self).items():
      if isinstance(v, AccessibleDict):
        new[k] = v.to_dict()
      else:
        new[k] = v
    return new

  def __repr__(self):
    all_nice = []
    for k, v in self.obj.items():
      if v is None:
        nice = 'null'
      elif isinstance(v, (float, int, str, list, dict)):
        disp = str(v).replace('\n', '\\n')
        nice = disp[:150] + ['', '...'][int(len(disp) > 150)]
      else:
        nice = f'{type(v).__name__ if not isinstance(v, AccessibleDict) else ""}<{v}>'

      all_nice.append(f'{k}={nice}')

    return f'AccessibleDict({", ".join(all_nice)})'

  def addAttr(self, attr_name, attr_value, boolean):
    if boolean:
      self.obj[attr_name] = attr_value
    return self


class meta_cls:
  @staticmethod
  def permissions(perms):
    return models.Permissions(
      ban=perms.get('ban'),
      delete=perms.get('delete'),
      delete_without_notification=perms.get('deleteWithoutMsg'),
      edit=perms.get('edit'),
      owner=perms.get('itemOwner'),
      report=perms.get('report'),
      admin_messages=perms.get('showAdminMsgs'),
    )

  @staticmethod
  def adminMsgs(msgs):
    frmt_msgs = []

    for msg in msgs:
      frmt_msgs.append(models.DeletedItem(
        # "action" seems to always be 'hide' so unnecessary
        time=hebrew_date(msg['hebrew_time']),
        hebrew_time=msg['hebrew_time'],
        reason=msg['msg'],
        deletor=enums.Role(1 if msg['nickname'] == 'נאמני סטיפס' else 2),
        points=msg['points'],
      ))

    return frmt_msgs[0] if len(frmt_msgs) == 1 else frmt_msgs


class user:
  @staticmethod
  def get_app_user(appUser, **kw):
    appUser = appUser.get('appUser', appUser)

    return models.AppUser(
      id=appUser['id'],
      ban=models.Ban(**translate_ban(appUser['ban'])) if translate_ban(appUser['ban']) else None,
      birth_date=to_time(appUser['isoBirthDate']),
      rank=translate_rank(appUser['moderator']),
      permissions=meta_cls.permissions(appUser['permissions']),
      phone_validated=not appUser['phoneNotValidated'],
      points=appUser['points'],
      safe_filter=appUser['safeFilter'],
      email=appUser['email'],
      flowers=appUser['flowersCount'],
      gender=enums.Gender(['male', 'female'].index(appUser['gender']) + 1),
    )


class omniobj:
  @staticmethod
  def user(omni, conn=None):
    if not omni:
      return None

    data = omni['data']
    extra = omni['extra']
    meta = omni['meta']

    return models.User(
      _state=conn,

      id=data['id'],
      url=f'https://stips.co.il/profile/{data["id"]}',
      gender=enums.Gender(data['gender']),
      photo=models.UserPhoto(user_id=data['id'], photostamp=None, url=None) if not data[
        'has_photo'] else models.UserPhoto(user_id=data['id'], photostamp=extra['photostamp'],
                                           url=get_photo(data['id'], extra['photostamp'])),
      name=data['nickname'],
      photo_updated_stamp=None if len(data['photo_updated_stamp']) == 0 else data['photo_updated_stamp'],
      points=data['points'],
      online=extra['item_profile']['online'],
      permissions=meta_cls.permissions(meta['permissions'])
    )

  @staticmethod
  def partial_user(part, conn=None):
    return models.PartialUser(
      _state=conn,

      id=part['userid'] if 'userid' in part else None,
      anonymous=part['anonflg'],
      name=part['nickname'],
      online=part['online'] if 'online' in part else None,
      photo=(None if len(part['photostamp']) == 0 else get_photo(part['userid'], part[
        'photostamp'])) if 'photostamp' in part and 'userid' in part else None,
      is_question_owner=part.get('parentItemCreatorResponse', None) or False,
      gender=part.get('gender', None)
    )

  @staticmethod
  def ask(q, conn=None):
    return ask.question(q, conn=conn)

  @staticmethod
  def ans(a, conn=None):
    return ans.answer(a, conn=conn)

  @staticmethod
  def thanksmsg(tm, conn=None):
    return thanksmsg.thank(tm, conn=conn)

  @staticmethod
  def penfriendsitem(pf, conn=None):
    return penfriendsitem.penfriend(pf, conn=conn)


class profile:
  @staticmethod
  def page_data(data, conn=None):
    if not data:
      return None

    data = data.get('data', data)
    user_id = data['user_profile_page']['data'].get('userid') if 'user_profile_page' in data else None

    return models.Profile(
      _state=conn,

      id=user_id,
      url=f'https://stips.co.il/profile/{user_id}' if user_id else None,
      age=data['age'],
      birth_year=datetime.utcnow().year - data['age'],
      questions=data['questions'],
      answers=data['answers'],
      flowers=data['flowers'],
      badges=translate_badges(data['badges']),
      created_at=hebrew_date(data['hebrew_active_since']),
      status=models.Status(**translate_status(data)),
      hide_age=data.get('hideAge', False),
      hide_stats=data.get('hideStats', False)
    )

  @staticmethod
  def actions_chart(chart):
    frmt_chart = []

    for dt in chart:
      frmt_chart.append(models.ChartData(
        time=to_time(dt['time']),
        count=dt['actionsCount']
      ))

    return frmt_chart


class ask:
  @staticmethod
  def question(q, conn=None):
    data = q['data']
    extra = q['extra']
    meta = q['meta']

    return models.Question(
      _state=conn,

      id=data['id'],
      url=f'https://stips.co.il/ask/{data["id"]}',
      anonymous=data['anonflg'],
      answer_count=data['answer_count'],
      pin_count=data['pin_count'],
      deleted=deleted(data['archive'], meta),
      title=data['q'],
      link=None if len(data['q_link']) == 0 else models.Link(url=data['q_link']),
      has_revisions=data['revision_flg'],
      safe_filter=data['safefilter'],
      tags=data['tagslist'],
      content=None if len(data['text_content']) == 0 else data['text_content'],
      time=to_time(data['time']),
      hebrew_time=extra['hebrew_time'],
      author=omniobj.partial_user(extra['item_profile'], conn=conn) if 'item_profile' in extra else None,
      me_pinned=False if data['user_pinned'] == -1 else True,
      photo=models.Photo(
        url=f"https://stipscdn-stips.netdna-ssl.com/photos/w400/{int(data['photo'])}.jpg" if data[
          'photo'].isdigit() else f"https://unsplash.com/photos/{data['photo'].strip('unsplash:')}/download",
        url_small=extra['content_image']['url_medium'] if 'content_image' in extra else None,
        type=enums.PhotoType(2 if data['photo'].startswith('unsplash:') else 1),
        creator_name=extra['content_image']['creator_name'] if 'content_image' in extra else None,
        creator_username=extra['content_image']['creator_username'] if 'content_image' in extra else None,
      ),
      permissions=meta_cls.permissions(meta['permissions'])
    )

  @staticmethod
  def new(questions, conn=None):
    return [ask.question(quest, conn=conn) for quest in questions]

  @staticmethod
  def many(questions, conn=None):
    return [ask.question(quest, conn=conn) for quest in questions]

  @staticmethod
  def hot(questions, conn=None):
    return [ask.question(quest, conn=conn) for quest in questions]

  @staticmethod
  def DailyAskCount(dt):
    results = dt['results']
    return models.QuestionsLimit(
      allowed=results['allowed'],
      current=results['count'],
      max=results['maxPerDay']
    )

  @staticmethod
  def omniobj_revision(revisions, conn=None):
    frmt_revs = []

    for rev in revisions:  # TODO: if question was deleted and get revisioned (get type/editor)
      data = rev['data']
      extra = rev['extra']
      meta = rev['meta']

      js = json.loads(data['jsonstring'])
      frmt_revs.append(models.RevisionQuestion(
        editor=enums.ItemEditor(['owner', 'moderator'].index(data['editor'] + 1)),
        id=data['id'],
        question_id=data['itemid'],
        title=js['q'],
        content=js['text_content'],
        tags=js['tagslist'],
        photo=models.Photo(
          url=f"https://stipscdn-stips.netdna-ssl.com/photos/w400/{int(js['photo'])}.jpg" if js[
            'photo'].isdigit() else f"https://unsplash.com/photos/{js['photo'].strip('unsplash:')}/download",
          url_small=extra['content_image']['url_medium'] if 'content_image' in extra else None,
          type=enums.Photo(2 if js['photo'].startswith('unsplash:') else 1),
          creator_name=extra['content_image']['creator_name'] if 'content_image' in extra else None,
          creator_username=extra['content_image']['creator_username'] if 'content_image' in extra else None,
        ),
        link=js['q_link'] if len(js['q_link']) > 0 else None,
        channel_id=js['channel_id'],
        time=to_time(data['time']),
        hebrew_time=extra['hebrew_time'],
        author=omniobj.partial_user(extra['item_profile'], conn=conn),
        permissions=meta_cls.permissions(meta['permissions'])
      ))

    return frmt_revs


class ans:
  @staticmethod
  def answer(a, conn=None):
    if a == {}: return None

    data = a['data']
    extra = a['extra']
    meta = a['meta']

    return models.Answer(
      _state=conn,

      id=data['id'],
      question_id=data['askid'],
      question_url=f'https://stips.co.il/ask/{data["askid"]}',
      question_title=extra.get('parent_item_title', None),
      text=data['a'],
      anonymous=data['anonflg'],
      deleted=deleted(data['archive'], meta),
      link=models.Link(name=data['link1name'] or None, url=data['link1']) if len(data['link1']) > 0 else None,
      author=omniobj.partial_user(
        {**extra['item_profile'], 'parentItemCreatorResponse': extra.get('parentItemCreatorResponse', None)},
        conn=conn),
      flowered=extra['flowered'],
      hebrew_time=extra['hebrew_time'],
      has_revisions=data['revision_flg'],
      time=to_time(data['time']),
      votes=data['votes_score'],
      upvotes=(data['votes_count'] + data['votes_score']) // 2,
      downvotes=(data['votes_count'] - data['votes_score']) // 2,
      me_vote=extra['userVote'],  # if logged in account voted (-1=downvotes, 0=not voted, 1=upvoted)
      permissions=meta_cls.permissions(meta['permissions']),
    )

  @staticmethod
  def for_item(answers, conn=None):
    return [ans.answer(answer, conn=conn) for answer in answers]

  @staticmethod
  def many(answers, conn=None):
    return [ans.answer(answer, conn=conn) for answer in answers]

  @staticmethod
  def flower_for_user(answers):
    return [ans.answer(answer, conn=conn) for answer in answers]

  @staticmethod
  def omniobj_revision(revisions, conn=None):
    frmt_revs = []

    for rev in revisions:  # TODO: if answer was deleted and got revisioned (get type/editor)
      data = rev['data']
      extra = rev['extra']
      meta = rev['meta']

      js = json.loads(data['jsonstring'])
      frmt_revs.append(models.RevisionAnswer(
        editor=enums.ItemEditor(['owner', 'moderator'].index(data['editor'] + 1)),
        id=data['id'],
        answer_id=data['itemid'],
        text=js['a'],
        link=models.Link(name=js['link1name'] or None, url=js['link1']) if len(js['link1']) > 0 else None,
        time=to_time(data['time']),
        hebrew_time=extra['hebrew_time'],
        author=omniobj.partial_user(extra['item_profile'], conn=conn),
        permissions=meta_cls.permissions(meta['permissions'])
      ))

    return frmt_revs


class penfriendsitem:
  @staticmethod
  def penfriend(pf_item, conn=None):
    data = pf_item['data']
    extra = pf_item['extra']
    meta = pf_item['meta']

    return models.PenfriendsItem(
      _state=conn,

      id=data['id'],
      time=to_time(data['time']),
      hebrew_time=extra['hebrew_time'],
      author=omniobj.partial_user(extra['item_profile'], conn=conn),
      text=data['msg']
    )

  @staticmethod
  def many(pf_items, conn=None):
    return [penfriendsitem.penfriend(pf, conn=conn) for pf in pf_items]

  @staticmethod
  def new(pf_items, conn=None):
    return [penfriendsitem.penfriend(pf, conn=conn) for pf in pf_items]

  @staticmethod
  def PostAllowed(dt):
    rs = dt['results']
    return models.PenfriendsLimit(
      allowed=rs['allowed'],
      minutes_left=rs['nextTimeInMinutes'],
      allowed_every=rs['postInterval']
    )


class homepage:
  @staticmethod
  def content(homepage, conn=None):
    return [ask.question(q, conn=conn) for q in homepage['pinnedItems']]


class messages:
  @staticmethod
  def count(dt):
    return models.NotificationsCount(
      messages=dt['messagesCount'],
      notifications=dt['notificationsCount']
    )

  @staticmethod
  def from_user(dt):
    if dt.get('userBlocked'):
      return False

    frmt_messages = []

    for msg in dt['messages']:
      frmt_messages.append(models.MessageItem(
        id=msg['id'],
        from_id=msg['fromuserid'],
        to_id=msg['touserid'],
        time=to_time(msg['time']),
        hebrew_time=msg['hebrew_time'],
        view_time=to_time(msg['viewtime']) if len(msg['viewtime']) > 0 else None,
        text=msg['msg']
      ))

    return frmt_messages

  @staticmethod
  def list(messages, conn=None):
    frmt_msgs = []

    for msg in messages['messages']:
      frmt_msgs.append(models.MessagesListItem(
        id=msg['id'],
        is_me_last_message=msg['currentUserMsg'],
        from_user=omniobj.partial_user(msg['itemProfile'], conn=conn),
        me_id=msg['fromuserid'] if msg['currentUserMsg'] else msg['touserid'],
        time=to_time(msg['time']),
        hebrew_time=msg['hebrew_time'],
        view_time=to_time(msg['viewtime']) if msg['viewtime'] and len(msg['viewtime']) > 0 else None,
        new_messages_count=msg['newCount'],
        last_message=msg['msg']
      ))

    return frmt_msgs


class notifications:
  @staticmethod
  def list(notifs):
    frmt_notifs = []

    map_types = ['delete_ask', 'delete_ans', 'delete_thanks_wall_msg', 'delete_pen_friends_item', 'user_report_thanks',
                 'new_thanks_wall_msg', 'new_ask_ans_registered', 'new_flower']

    # TODO: check if all types urls work
    for nf in notifs:
      if nf['type'] in ['delete_ask', 'delete_ans', 'user_report_thanks']: nf['linkPageName'] = 'ask'

      frmt_notifs.append(models.NotificationItem(
        id=nf['id'],
        type=enums.NotificationType(map_types.index(nf['type']) + 1),
        viewed=nf['viewed'],
        time=to_time(nf['time']),
        click_url=f'https://stips.co.il/{nf["linkPageName"]}/{nf["linkItemId"] or nf["realItemId"]}' \
          if nf['linkPageName'] and (nf['linkItemId'] or nf['realItemId']) else None,
        link_item_id=nf['linkItemId'],
        real_item_id=nf['realItemId'],
        text=nf['contentHtml'],  # can prob remove <strong> && </strong>
        message=nf['msgText'],
        points=nf['pointsRemoved']
      ))

    return frmt_notifs


class thanksmsg:
  @staticmethod
  def thank(thx, conn=None):
    data = thx['data']
    extra = thx['extra']
    meta = thx['meta']

    return models.Thank(
      _state=conn,

      id=data['id'],
      author=omniobj.partial_user(extra['item_profile'], conn=conn),
      to_id=data['touserid'],
      text=data['msg'],
      time=to_time(data['time']),
      hebrew_time=extra['hebrew_time'],
      permissions=meta_cls.permissions(meta['permissions'])
    )

  @staticmethod
  def many(todots, conn=None):
    return [thanksmsg.thank(toda, conn=conn) for toda in todots]


class contacts:
  @staticmethod
  def most_active(users, conn=None):
    return [omniobj.user(us, conn=conn) for us in users]


class item:
  @staticmethod
  def autotags(dt):
    return dt['tags']

  @staticmethod
  def tag_suggest(dt):
    return dt['tags']

  @staticmethod
  def RemoteConfig(dt):
    # at this time i only know it returns channels
    channels = []

    for channel in dt['results']['itemChannels']['channels']:
      channels.append(models.ChannelConfig(
        background_color_css=channel['backgroundColorCss'],
        background_url=channel['backgroundUrl'],
        icon_name=channel['icon'],
        id=channel['id'],
        name=channel['name'],
        no_channel_remove_notification=channel['noChannelRemoveNotification'],
        slogan=channel['slogan']
      ))

    return models.RemoteConfig(channels=channels)


class photos:
  @staticmethod
  def tag_gallery(dt):
    frmt_imgs = []

    for img in dt['photos']:
      frmt_imgs.append(models.GalleryImage(
        id=img['photo_id'],
        url=f"https://stipscdn-stips.netdna-ssl.com/photos/w400/{img['photo_id']}.jpg",
      ))

    return frmt_imgs


class users:
  @staticmethod
  def Search(dt, conn=None):
    profiles = dt['results']['profiles']
    return [omniobj.partial_user(prf, conn=conn) for prf in profiles]


class report_item:
  @staticmethod
  def report(rep, conn=None):
    data = rep['data']
    extra = rep['extra']
    meta = rep['meta']

    return models.ReportItem(
      _state=conn,

      id=data['id'],
      type=enums.ReportType(1 if data['itemtype'] == 'ask' else 2),
      reason=data['reason'],
      question=ask.question(extra['item'], conn=conn) if data['itemtype'] == 'ask' else None,
      answer=ans.answer(extra['item'], conn=conn) if data['itemtype'] == 'ans' else None,
      time=to_time(data['time']),
      hebrew_time=extra['hebrew_time'],
      author=omniobj.partial_user(extra['item_profile'], conn=conn),
      partial_question=models.PartialQuestion(id=extra['item_ask_id'], title=extra['item_ask_title']) if data[
                                                                                                           'itemtype'] == 'ans' else None,
      permissions=meta_cls.permissions(meta['permissions'])
    )

  @staticmethod
  def many(reports, conn=None):
    return [report_item.report(rep, conn=conn) for rep in reports]
