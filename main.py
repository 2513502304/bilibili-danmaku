'''
Author: 未来可欺 2513502304@qq.com
Date: 2025-01-14 02:27:22
LastEditors: 未来可欺 2513502304@qq.com
LastEditTime: 2025-01-18 01:48:31
Description: 支持任意历史时间筛选的 bilibili 弹幕爬虫
'''

import settings
from utils import logger
from crawl import get_history_danmaku
from storage import dump_history_danmaku
import time


def main():
    try:  # 尝试获取记录信息
        with open(f'{settings.save_dir}/.seen', mode='r', encoding='utf-8') as f:
            seen: list[str] = f.read().split('\n')[:-1:]  # ignore the last empty string: ''
    except FileNotFoundError as e:  # 初始化记录信息
        seen: list[str] = []
    # aid 不为空
    if settings.aids:
        for aid, name in zip(settings.aids, settings.save_name):
            # 当前 aid 在记录中，跳过爬取
            if aid in seen:
                logger.info(f'{aid} 已在当前记录中，将跳过该记录')
                continue
            time.sleep(settings.delay)  # 反爬
            # 从给定的 aid/bvid 与时间段中获取历史弹幕
            danmaku = get_history_danmaku(aid=aid, page=settings.page, cookies=settings.cookies, start=settings.start, end=settings.end, delay=settings.delay)
            # 转存为指定格式
            dump_history_danmaku(danmaku, save_name=name, save_dir=settings.save_dir, file_format=settings.file_format)
            # 记录当前信息
            seen.append(aid)
            with open(f'{settings.save_dir}/.seen', mode='a', encoding='utf-8') as f:
                f.write(aid + '\n')
    # bvid 不为空
    elif settings.bvids:
        for bvid, name in zip(settings.bvids, settings.save_name):
            # 当前 bvid 在记录中，跳过爬取
            if bvid in seen:
                logger.info(f'{bvid} 已在当前记录中，将跳过该记录')
                continue
            time.sleep(settings.delay)  # 反爬
            # 从给定的 aid/bvid 与时间段中获取历史弹幕
            danmaku = get_history_danmaku(bvid=bvid, page=settings.page, cookies=settings.cookies, start=settings.start, end=settings.end, delay=settings.delay)
            # 从给定的 aid/bvid 与时间段中获取历史弹幕
            # 转存为指定格式
            dump_history_danmaku(danmaku, save_name=name, save_dir=settings.save_dir, file_format=settings.file_format)
            # 记录当前信息
            seen.append(bvid)
            with open(f'{settings.save_dir}/seen', mode='a', encoding='utf-8') as f:
                f.write(bvid + '\n')
    else:
        raise ValueError('请配置 settings 中视频的 aids/bvids 参数')


if __name__ == "__main__":
    main()
