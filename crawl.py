''' 
bilibili 视频基本信息: https://socialsisteryi.github.io/bilibili-API-collect/docs/video/info.html
bilibili 历史弹幕: https://socialsisteryi.github.io/bilibili-API-collect/docs/danmaku/history.html
'''

from fake_useragent import UserAgent
from datetime import datetime, date, time as _time, timedelta
import time
from utils import logger
from google.protobuf import message, json_format
import dm_pb2 as danmaku
import json
import pandas as pd
import numpy as np
import requests

# 弹幕字段
field = {
    'id': np.int64,  # 弹幕 dmid。唯一，可用于操作参数
    'progress': np.int32,  # 视频内弹幕出现时间。毫秒
    'mode': np.int32,  # 弹幕类型。1 2 3：普通弹幕 4：底部弹幕 5：顶部弹幕 6：逆向弹幕 7：高级弹幕 8：代码弹幕 9：BAS 弹幕（仅限于特殊弹幕专包）
    'fontsize': np.int32,  # 弹幕字号。18：小 25：标准 36：大
    'color': np.uint32,  # 弹幕颜色。十进制 RGB888 值
    'midHash': str,  # 发送者 mid 的 HASH。用于屏蔽用户和查看用户发送的所有弹幕，也可反查用户 id
    'content': str,  # 弹幕内容。utf-8 编码
    'ctime': np.int64,  # 弹幕发送时间。时间戳
    'idStr': str,  # 弹幕 dmid。字串形式。唯一，可用于操作参数
    'attr': np.int32,  # 弹幕属性位。bit0：保护 bit1：直播 bit2：高赞
}


def get_video_information(aid: str = None, bvid: str = None, cookie: str = None) -> dict:
    '''
    从给定的 aid 或 bvid 中获取视频信息
    ---
    
    :param aid: 视频的 aid，可选。若 aid 为空，则必须提供 bvid 参数
    :param bvid: 视频的 bvid，可选。若 bvid 为空，则必须提供 aid 参数
    :param cookie: 必要的 cookie
    :return: 视频信息，以 json 格式返回
    '''
    url = 'https://api.bilibili.com/x/web-interface/view'  # 获取视频详细信息（web 端）
    if cookie is None:
        raise ValueError('请输入有效的 Cookie')
    headers = {
        'User-Agent': UserAgent().random,
        'Cookie': cookie,
    }
    if aid is not None:
        headers.update({'aid': aid})
    elif bvid is not None:
        headers.update({'bvid': bvid})
    else:
        raise ValueError('请输入视频的 aid/bvid')
    response = requests.get(url=url, headers=headers)
    context = response.json()
    return context


def get_history_danmaku_index(cid: str = None, cookie: str = None, month: str = None) -> dict:
    '''
    从给定的 cid 与 month 中获取历史弹幕日期
    ---
    
    :param cid: 必要的弹幕 cid
    :param month: 必要的查询目标年月，YYYY-MM
    :param cookie: 必要的 cookie
    :return: 历史弹幕日期，以 json 格式返回
    '''
    url = 'https://api.bilibili.com/x/v2/dm/history/index'  # 查询历史弹幕日期 url
    if cid is None:
        raise ValueError('请输入弹幕的 cid')
    if cookie is None:
        raise ValueError('请输入有效的 Cookie')
    if month is None:
        raise ValueError('请输入有效的 month')
    headers = {
        'User-Agent': UserAgent().random,
        'Cookie': cookie,
    }
    params = {
        'type': 1,
        'oid': cid,
        'month': month,  # 查询目标年月，YYYY-MM
    }
    response = requests.get(url=url, headers=headers, params=params)
    context = response.json()
    return context


def get_history_danmaku(aid: str = None, bvid: str = None, page: int = 1, cookies: list[str] = None, start: str = None, end: str = None, delay: float = 1.0) -> dict:
    '''
    从给定的 aid/bvid 与时间段中获取历史弹幕
    ---
    :param aid: 视频的 aid，可选。若 aid 为空，则必须提供 bvid 参数
    :param bvid: 视频的 bvid，可选。若 bvid 为空，则必须提供 aid 参数
    :param page: 视频分 p，可选。默认为 1
    :param cookies: 必要的 cookie 列表，若提供多个 cookie，将在当前账号被监测到的时候自动替换为下一个账号
    :param start: 指定时间段开始，YYYY-MM-DD 格式，可选。默认为 None，表示从视频发布时间开始
    :param end: 指定时间段结束，YYYY-MM-DD 格式，可选。默认为 None，表示至当前时间结束
    :param delay: 每次请求的延迟时间，建议大于 1s，可选。默认为 1
    :return: 历史弹幕，每天最多返回 500 条弹幕数据，以 json 格式返回
    '''
    url = 'https://api.bilibili.com/x/v2/dm/web/history/seg.so'  # 获取历史弹幕 protobuf 接口，最小单位为天，每天最多返回 500 条弹幕数据
    if cookies is None:
        raise ValueError('请输入有效的 Cookie')
    cookies = iter(cookies)
    cookie = next(cookies)
    headers = {
        'User-Agent': UserAgent().random,
        'Cookie': cookie,
    }
    params = {
        'type': 1,
    }
    if aid is not None or bvid is not None:
        context = get_video_information(aid=aid, bvid=bvid, cookie=cookie)  # 获取视频信息
        # 解析获取到的数据
        data = context['data']
        aid = data['aid']  # 稿件 avid
        argue_info = data['aid']  # 争议/警告信息
        bvid = data['bvid']  # 稿件 bvid
        cid = data['cid']  # 视频 1P cid
        copyright = data['copyright']  # 视频类型。1：原创 2：转载
        ctime = data['ctime']  # 用户投稿时间。秒级时间戳
        desc = data['desc']  # 视频简介
        desc_v2 = data['desc_v2']  # 新版视频简介
        dimension = data['dimension']  # 视频 1P 分辨率
        disable_show_up_info = data['disable_show_up_info']  # TODO
        duration = data['duration']  # 稿件总时长（所有分 P）。单位为秒
        dynamic = data['dynamic']  # 视频同步发布的动态的文字内容
        enable_vt = data['enable_vt']  # TODO
        honor_reply = data['honor_reply']  # TODO
        is_chargeable_season = data['is_chargeable_season']  # TODO
        is_season_display = data['is_season_display']  # TODO
        is_story = data['is_story']  # TODO
        is_story_play = data['is_story_play']  # TODO
        is_upower_exclusive = data['is_upower_exclusive']  # TODO
        is_upower_play = data['is_upower_play']  # TODO
        is_upower_preview = data['is_upower_preview']  # TODO
        is_view_self = data['is_view_self']  # TODO
        like_icon = data['like_icon']  # TODO
        need_jump_bv = data['need_jump_bv']  # TODO
        no_cache = data['no_cache']  # TODO
        owner = data['owner']  # 视频 UP 主信息
        pages = data['pages']  # 视频分 P 列表
        pic = data['pic']  # 稿件封面图片 url
        premiere = data['premiere']  # TODO
        pubdate = data['pubdate']  # 稿件发布时间。秒级时间戳
        rights = data['rights']  # 视频属性标志
        stat = data['stat']  # 视频状态数
        state = data['state']  # 视频状态
        subtitle = data['subtitle']  # 视频 CC 字幕信息
        teenage_mode = data['teenage_mode']  # TODO
        tid = data['tid']  # 分区 tid
        tid_v2 = data['tid_v2']  # 新版分区 tid
        title = data['title']  # 稿件标题
        tname = data['tname']  # 子分区名称
        tname_v2 = data['tname_v2']  # 新版子分区名称
        user_garb = data['user_garb']  # 用户装扮信息
        videos = data['videos']  # 稿件分 P 总数。默认为1
        vt_display = data['vt_display']  # TODO
        if page == 1:
            params.update({'oid': cid})
        else:
            cid = data['pages'][page - 1]['cid']
            params.update({'oid': cid})
    else:
        raise ValueError('请输入视频的 aid/bvid')
    # 若视频弹幕数为 0，则返回空 dict
    if stat['danmaku'] == 0:
        logger.info(f'{title}：弹幕数为 0')
        return {}
    # 开始时间
    start_dt: date = datetime.fromtimestamp(int(pubdate)).date() if start is None else datetime.strptime(start, '%Y-%m-%d').date()
    # 结束时间
    end_dt: date = datetime.now().date() if end is None else datetime.strptime(end, '%Y-%m-%d').date()
    if start_dt > end_dt:
        raise ValueError('请输入有效的 start 和 end：start 不能超过 end')
    # 跳过没有弹幕记录的时间直至记录的开始，以确定弹幕记录时间的左边界
    # 同时也是以防用户输入错误的 start 参数导致获取速度变慢（跳过的最小时间单位步长为月）
    start_Ym = start_dt.strftime(format='%Y-%m')
    start_index = get_history_danmaku_index(cid=cid, cookie=cookie, month=start_Ym)
    while start_index['data'] is None:  # 直到获取有记录的月份
        logger.info(f'{title}：{start_Ym} 无弹幕记录，将跳过该月')
        time.sleep(delay)  # 反爬
        start_dt += pd.DateOffset(months=1)  # 跳转到下一个月
        start_dt = pd.offsets.MonthBegin().rollback(
            start_dt)  # 仅偏移到下一个月的月初而不是下一个月的当前日期，保证 start_dt 始终小于等于 end_dt，以防在相对月份加减后，导致 start_dt.year == end_dt.year, start_dt.month == end_dt.month, start_dt.day > end_dt.day
        start_Ym = start_dt.strftime(format='%Y-%m')
        start_index = get_history_danmaku_index(cid=cid, cookie=cookie, month=start_Ym)
    # 跳过没有弹幕记录的时间直至记录的结束，以确定弹幕记录时间的右边界
    # 同时也是以防用户输入错误的 end 参数导致获取速度变慢（跳过的最小时间单位步长为月）
    end_Ym = end_dt.strftime(format='%Y-%m')
    end_index = get_history_danmaku_index(cid=cid, cookie=cookie, month=end_Ym)
    while end_index['data'] is None:  # 直到获取有记录的月份
        logger.info(f'{title}：{end_Ym} 无弹幕记录，将跳过该月')
        time.sleep(delay)  # 反爬
        end_dt += pd.DateOffset(months=-1)  # 跳转到上一个月
        end_dt = pd.offsets.MonthEnd().rollforward(
            end_dt)  # 仅偏移到上一个月的月末而不是上一个月的当前日期，保证 start_dt 始终小于等于 end_dt，以防在相对月份加减后，导致 start_dt.year == end_dt.year, start_dt.month == end_dt.month, start_dt.day > end_dt.day
        end_Ym = end_dt.strftime(format='%Y-%m')
        end_index = get_history_danmaku_index(cid=cid, cookie=cookie, month=end_Ym)
    # 获取含有的弹幕记录的时间
    record_data = []
    for m in pd.date_range(start=start_Ym, end=end_Ym, freq='MS'):
        time.sleep(delay)  # 反爬
        Ym = m.strftime(format='%Y-%m')
        index = get_history_danmaku_index(cid=cid, cookie=cookie, month=Ym)
        # 忽略 start_dt 至 end_dt 中间没有弹幕的月份
        index_data = index['data']
        if index_data is not None:
            logger.info(f'{title}：{Ym} 含有弹幕记录日期为：{index_data}')
            record_data.extend(index_data)
        else:
            logger.info(f'{title}：{Ym} 无弹幕记录，将跳过该月')
    # 将所有弹幕汇总为一个 json 对象，方便处理
    res_json = []
    # 初始化 protobuf 中定义的数据结构
    danmaku_seg = danmaku.DmSegMobileReply()
    # 遍历每个时间段
    for d in pd.date_range(start=start_dt, end=end_dt, freq='D'):
        # 跳过不在弹幕记录的时间
        now_date = str(d.date())
        if now_date not in record_data:
            continue
        params.update({
            'date': str(now_date),  # 弹幕日期，YYYY-MM-DD
        })
        # 直到获取到正确的数据后退出
        while True:
            time.sleep(delay)  # 反爬
            response = requests.get(url=url, headers=headers, params=params)
            try:  # 当前账号被监测到导致返回数据解析失败
                # 解析文本 proto 字符串
                danmaku_seg.ParseFromString(response.content)
            except message.DecodeError as e:  # google.protobuf.message.DecodeError: Error parsing message with type 'bilibili.community.service.dm.v1.DmSegMobileReply'
                logger.warning(e)
                try:
                    # 替换为下一个账号
                    cookie = next(cookies)
                    headers.update({'Cookie': cookie})
                except StopIteration as e:  # 剩余可用 cookie 为 0
                    raise Exception('所有账号被平台监测，请在次日延长 delay 参数后重新运行')
                continue  # retry again
            break
        logger.info(f'{title}：{now_date} 获取到的弹幕条数：{len(danmaku_seg.elems)}')
        # 遍历每条弹幕
        for e in danmaku_seg.elems:
            res_json.append(json_format.MessageToJson(e, ensure_ascii=False))
    # 将 json 对象转存为 Python 对象
    dm = json.loads('[' + ','.join(res_json) + ']')
    return dm
