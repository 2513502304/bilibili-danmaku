'''
配置文件
'''

# 茜特拉莉（bushi，原神怎么你了）
# 视频的 aid 列表，可选。若 aids 为空，则必须提供 bvids 参数。若设置了 file 参数，则忽略
aids = [
    '113736958350047',
]
# 视频的 bvid 列表，可选。若 bvids 为空，则必须提供 aids 参数。若设置了 file 参数，则忽略
bvids = [
    'BV1ft6hYxE75',
]
# 视频弹幕的 cid，ignore
cids = [
    '27598718983',
]

# 任务名称，用于设置记录信息的文件名
task = '延迟退休'

# 若视频的 aid/bvid 列表来源自文件中的某一字段，则指定 file 参数中的各个键值对，以批量设置 aids/bvids/save_name 参数
from_file = True  # 视频的 aid/bvid 列表是否来源自文件中的某一字段，仅为 True 时读取文件字段，为 False 时则使用 aids/bvids 参数
file = {
    'file_path': './' + 'bilibili_search_keywords=延迟退休_start=2024-09-13_end=2025-01-01_contents.csv',  # 文件路径
    'field': 'video_id',  # aid/bvid 在文件中的字段名
    'type': 'aid',  # 用于指定 aid 还是 bvid
    'prefix': '',  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的前缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
    'suffix': '-danmaku',  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的后缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
}

# 替换为你自己的 cookie，若提供多个 cookie，将在当前账号被监测到的时候自动替换为下一个账号
cookies = [
    'buvid3=E4B0FF67-ED6D-3C9A-FAD7-C1E2D593C2B060088infoc; b_nut=1719544260; _uuid=5B778C10C-9594-12F8-361F-102CC6AAB4DAC61385infoc; enable_web_push=DISABLE; buvid4=16089B19-FFE6-58C5-CF1E-9E337FB79FC161029-024062803-z6Uxn9V9Crd0fXW3HIgGdw%3D%3D; rpdid=0zbfAI6DyH|2RQZtZ6J|1RD|3w1SqFRV; header_theme_version=CLOSE; LIVE_BUVID=AUTO4217286542998787; PVID=2; fingerprint=0885da303e16d96e4d000078be62ed7c; buvid_fp_plain=undefined; buvid_fp=0885da303e16d96e4d000078be62ed7c; CURRENT_QUALITY=80; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1736585546; is-2022-channel=1; _tea_utm_cache_586864={%22creative_id%22:181369634}; bp_t_offset_86137069=1022955905899036672; home_feed_column=5; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; b_lsid=C3B22F2F_19484E9F3F2; bsource=search_bing; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzc2NTU5MTMsImlhdCI6MTczNzM5NjY1MywicGx0IjotMX0.WmBDGa2LmwoNdu6hxrYoF2OeQqN3zN1vci4eMJjlcEg; bili_ticket_expires=1737655853; bp_t_offset_71951017=1024609880624857088; SESSDATA=807969f8%2C1752952618%2C0ae52%2A11CjAyUNzrx2aDnhrGKmj9GykUFOPN54BHt7URVf2M1RXkc2DusvF_ouiRiqPEoFpDVg4SVldWTzUxaFZBQWpEeDlBblJwOGc5VzRrZW1NZDZ6X1RJeXlGcXAtSjdjcVJJaTBfejdLYVU0NVF5STBFWWsyNVc1NzZVRWtnbUgzNmE3NGFINGFmWllnIIEC; bili_jct=ceef3dbe0a38330886d0634e08576c7f; DedeUserID=71951017; DedeUserID__ckMd5=a97d5c02401bdcd2; CURRENT_FNVAL=2000; sid=pmobk9b2; browser_resolution=1536-310',
    'buvid3=E4B0FF67-ED6D-3C9A-FAD7-C1E2D593C2B060088infoc; b_nut=1719544260; _uuid=5B778C10C-9594-12F8-361F-102CC6AAB4DAC61385infoc; enable_web_push=DISABLE; buvid4=16089B19-FFE6-58C5-CF1E-9E337FB79FC161029-024062803-z6Uxn9V9Crd0fXW3HIgGdw%3D%3D; rpdid=0zbfAI6DyH|2RQZtZ6J|1RD|3w1SqFRV; header_theme_version=CLOSE; LIVE_BUVID=AUTO4217286542998787; PVID=2; fingerprint=0885da303e16d96e4d000078be62ed7c; buvid_fp_plain=undefined; buvid_fp=0885da303e16d96e4d000078be62ed7c; CURRENT_QUALITY=80; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1736585546; is-2022-channel=1; _tea_utm_cache_586864={%22creative_id%22:181369634}; bp_t_offset_86137069=1022955905899036672; home_feed_column=5; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; b_lsid=C3B22F2F_19484E9F3F2; bsource=search_bing; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzc2NTU5MTMsImlhdCI6MTczNzM5NjY1MywicGx0IjotMX0.WmBDGa2LmwoNdu6hxrYoF2OeQqN3zN1vci4eMJjlcEg; bili_ticket_expires=1737655853; bp_t_offset_71951017=1024609880624857088; SESSDATA=ad749c3f%2C1752951032%2C15692%2A11CjCDlbcQUsvvhHR6mZhcpOzJvZeQWiej17RMNefQeRJkx-9rIUTVNnOJZWG2f6epV7kSVi1hTTVZWFFZQXBxdjYyaHBNWGVHbFF4TzZhN0JKNFk5YUFubE9BOElFZnJTRVVCTHZQRTQ5VDJTNFFMQkRsUF9fWUFjNXFJLXhMUFpEdjdRQXVtS3NBIIEC; bili_jct=d651d4e544aa2c0df409f3b4a051e8c3; DedeUserID=86137069; DedeUserID__ckMd5=9c9e29b3c177de79; CURRENT_FNVAL=4048; sid=6a1fbv0x; browser_resolution=1536-310',
]

# 视频分 p
page = 1

# 指定时间段开始，YYYY-MM-DD 格式，为 None，表示从视频发布时间开始
start = None

# 指定时间段结束，YYYY-MM-DD 格式，为 None，表示至当前时间结束
end = '2025-01-01'

# 每次请求的延迟时间，建议大于 1s
delay = 1

# 转存的文件格式，默认为 csv，支持 csv，xlsx，json
file_format = 'csv'

# 转存的文件名称列表，必须与 aids/bvids 中提供的视频个数一致
save_name = [
    '茜特拉莉弹幕',
]

# 转存的文件夹，默认为当前目录下的 Data 文件夹中
save_dir = './Data'

try:
    from storage import get_aid_form_file, get_bvid_form_file
    from utils import logger
    import os

    # 视频的 aid/bvid 列表是否来源自文件中的某一字段，仅为 True 时读取文件字段，为 False 时则使用 aids/bvids 参数
    if from_file:
        fp = file.get('file_path', '')  # 文件路径
        f = file.get('field', '')  # aid/bvid 在文件中的字段名
        tp = file.get('type', '')  # 用于指定 aid 还是 bvid
        pre = file.get('prefix', '')  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的前缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
        suf = file.get('suffix', '')  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的后缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
        # 文件是否存在
        if os.path.exists(fp):
            # 类型是否匹配
            match tp:
                case 'aid':
                    aids = get_aid_form_file(file_path=fp, field=f)  # 字段是否正确
                    save_name = [pre + aid + suf for aid in aids]
                case 'bvid':
                    bvids = get_bvid_form_file(file_path=fp, field=f)  # 字段是否正确
                    save_name = [pre + bvid + suf for bvid in bvids]
                case _:
                    raise ValueError('错误的 type 参数')
        else:
            raise FileNotFoundError('错误的 file_path 参数')
    else:
        pass
except Exception as e:  # !catch any exception form pandas module
    logger.warning(e)
