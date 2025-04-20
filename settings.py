'''
配置文件
'''

# 茜特拉莉（bushi，原神怎么你了）
# 视频的 aid 列表，可选。若 aids 为空，则必须提供 bvids 参数。若设置了 file 参数，则忽略
aids: list[str] = [
    '113736958350047',
]
# 视频的 bvid 列表，可选。若 bvids 为空，则必须提供 aids 参数。若设置了 file 参数，则忽略
bvids: list[str] = [
    'BV1ft6hYxE75',
]
# 视频弹幕的 cid，ignore 该参数
cids: list[str] = [
    '27598718983',
]

# 任务名称，用于设置记录信息的文件名
task: str = '延迟退休'

# 若视频的 aid/bvid 列表来源自文件中的某一字段，则指定 file 参数中的各个键值对，以批量设置 aids/bvids/save_name 参数
from_file: bool = True  # 视频的 aid/bvid 列表是否来源自文件中的某一字段，仅为 True 时读取文件字段，为 False 时则使用 aids/bvids 参数
file: dict = {
    'file_path': './' + 'bilibili_search_keywords=延迟退休_start=2024-09-13_end=2025-01-01_contents.csv',  # 文件路径
    'field': 'video_id',  # aid/bvid 在文件中的字段名
    'type': 'aid',  # 用于指定 aid 还是 bvid
    'prefix': '',  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的前缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
    'suffix': '-danmaku',  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的后缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
}

# 替换为你自己的 cookie，若提供多个 cookie，将在当前账号被监测到的时候自动替换为下一个账号
cookies: list[str] = [ 
    'buvid3=E4B0FF67-ED6D-3C9A-FAD7-C1E2D593C2B060088infoc; b_nut=1719544260; _uuid=5B778C10C-9594-12F8-361F-102CC6AAB4DAC61385infoc; enable_web_push=DISABLE; buvid4=16089B19-FFE6-58C5-CF1E-9E337FB79FC161029-024062803-z6Uxn9V9Crd0fXW3HIgGdw%3D%3D; rpdid=0zbfAI6DyH|2RQZtZ6J|1RD|3w1SqFRV; header_theme_version=CLOSE; LIVE_BUVID=AUTO4217286542998787; PVID=2; fingerprint=0885da303e16d96e4d000078be62ed7c; buvid_fp_plain=undefined; buvid_fp=0885da303e16d96e4d000078be62ed7c; CURRENT_QUALITY=80; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1736585546; is-2022-channel=1; _tea_utm_cache_586864={%22creative_id%22:181369634}; bp_t_offset_86137069=1022955905899036672; home_feed_column=5; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; bsource=search_bing; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Mzc2NTU5MTMsImlhdCI6MTczNzM5NjY1MywicGx0IjotMX0.WmBDGa2LmwoNdu6hxrYoF2OeQqN3zN1vci4eMJjlcEg; bili_ticket_expires=1737655853; bp_t_offset_71951017=1024938961019076608; b_lsid=1016D3110D_1948DC188AE; browser_resolution=1536-742; SESSDATA=04c6c984%2C1753102396%2C4ae7b%2A11CjDdLefxjn-jSKfok8u4oKlGYbOzFI512A3PsbHBvttVB7KxDdz7bsn7GuUe9rdVA08SVmRSaXowbWROMHhwOU9EU2p0emJ1ZVkwbG5qRm95LWpaMHZsXy1pY2dfNG44OF9hUHBCMTNYVkN1VTJWZlNPNjdGNzJSQ0N6SHA1Rm53N2tQN1NWTUxRIIEC; bili_jct=e0035e48f24e1b44cbc76cd2b44943bb; DedeUserID=86137069; DedeUserID__ckMd5=9c9e29b3c177de79; sid=4lumbk4r; CURRENT_FNVAL=4048',
]

# 视频分 p
page: int = 1

# 指定时间段开始，YYYY-MM-DD 格式，为 None，表示从视频发布时间开始
start: str | None = None

# 指定时间段结束，YYYY-MM-DD 格式，为 None，表示至当前时间结束
end: str | None  = '2025-01-01'

# 每次请求的延迟时间，建议大于 1s
delay: float = 1

# 转存的文件格式，默认为 csv，支持 csv，xlsx，json
file_format: str = 'csv'

# 转存的文件名称列表，必须与 aids/bvids 中提供的视频个数一致
save_name: list[str] = [
    '茜特拉莉弹幕',
]

# 转存的文件夹，默认为当前目录下的 Data 文件夹中
save_dir: str = './Data'

# 是否添加 bilibili 弹幕用户信息字段，默认为 False。开启该功能可能会导致处理时间过长，因为涉及到通过 midHash 反查用户信息以及网络请求
user_info: bool = False

try:
    from storage import get_aid_form_file, get_bvid_form_file, add_user_information_field, PRETREATMENT
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
    
    if user_info:
        PRETREATMENT.append(add_user_information_field)  # 添加 bilibili 弹幕用户信息字段
        
except Exception as e:  #!catch any exception form pandas module
    logger.warning(e)



