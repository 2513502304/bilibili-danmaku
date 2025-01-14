'''
Author: 未来可欺 2513502304@qq.com
Date: 2025-01-14 02:27:22
LastEditors: 未来可欺 2513502304@qq.com
LastEditTime: 2025-01-14 20:34:23
Description: 支持任意历史时间筛选的 bilibili 弹幕爬虫
'''

from crawl import get_history_danmaku
import pandas as pd

# 茜特拉莉（bushi，原神怎么你了）
aid = '113736958350047'  # 视频的 aid，可选。若 aid 为空，则必须提供 bvid 参数
bvid = 'BV1ft6hYxE75'  # 视频的 bvid，可选。若 bvid 为空，则必须提供 aid 参数
cid = '27598718983'  # ignore

# 替换为你自己的 cookie
cookie = ''

if __name__ == "__main__":
    # 从给定的 aid/bvid 与时间段中获取历史弹幕
    dm = get_history_danmaku(bvid=bvid, cookie=cookie)

    df = pd.DataFrame(dm)
    # 将 ctime 时间戳转换为 datetime64[ns]
    t = pd.to_datetime(df['ctime'].astype(int), unit='s')
    # 取年月日赋值给 date 字段
    df['date'] = t.dt.date
    # 取时分秒赋值给 time 字段
    df['time'] = t.dt.time

    # 转存
    save_path = './茜特拉莉弹幕.csv'
    df.to_csv(save_path)
