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
from_file: bool = False  # 视频的 aid/bvid 列表是否来源自文件中的某一字段，仅为 True 时读取文件字段，为 False 时则使用 aids/bvids 参数
file: dict = {
    'file_path': './Data/' + 'bilibili_search_keywords=延迟退休_start=2024-09-13_end=2025-01-01_contents.csv',  # 文件路径
    'field': 'video_id',  # aid/bvid 在文件中的字段名
    'type': 'aid',  # 用于指定 aid 还是 bvid
    'prefix': '',  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的前缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
    'suffix': '-danmaku',  # 基于文件中 aid/bvid 字段的各个值，批量为保存的文件名添加的后缀，文件名组成将为 prefix + aid/bvid + suffix + '.' + file_format
}

# 替换为你自己的 cookie，若提供多个 cookie，将在当前账号被监测到的时候自动替换为下一个账号
cookies: list[str] = [ 
    "buvid3=12E6B44B-299C-8283-A6DA-895FBA5D2C8190084infoc; b_nut=1749045090; _uuid=3D77E2DC-BFF3-1A103-3154-C345C610271C891845infoc; enable_web_push=DISABLE; enable_feed_channel=ENABLE; buvid4=586306EA-CB13-A936-3BA1-9344DBD048E691930-025060421-wN7xdrpDVP17x4SI8qKsEg%3D%3D; DedeUserID=86137069; DedeUserID__ckMd5=9c9e29b3c177de79; rpdid=|(u||uJJklYY0J'u~RmuullRm; CURRENT_QUALITY=80; SESSDATA=fb837ee3%2C1764766189%2C69950%2A62CjAKT5RPpWkFp6IE7cWaPZMetPomR8l13btPdDHn8MSL5RdaznySWtMVPLjWzVgJ44wSVmprdXBjZlpSVVBLWTZwQkduREN1b01rSmtPNUY3UjlnejZzTTlWYWZqTXdDNTRacWdyUDBZWThtU0JlRDdoeFF4YWRJU1RMd1FDbF9WeDE2MUptTFB3IIEC; bili_jct=9bf34e15f90be316dac4b5bf2e1cfe08; fingerprint=053daf026bdf318192bfc7b9f908986f; buvid_fp_plain=undefined; buvid_fp=053daf026bdf318192bfc7b9f908986f; header_theme_version=OPEN; theme-tip-show=SHOWED; theme-avatar-tip-show=SHOWED; theme-switch-show=SHOWED; hit-dyn-v2=1; PVID=3; bp_t_offset_86137069=1092045020405432320; bmg_af_switch=1; bmg_src_def_domain=i0.hdslb.com; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTM2OTk4MTYsImlhdCI6MTc1MzQ0MDU1NiwicGx0IjotMX0.pqVcBfIGlexKaDHCg5ubpyWNSq0cuKAVryhJT2otlbM; bili_ticket_expires=1753699756; sid=6ghbycmx; home_feed_column=5; CURRENT_FNVAL=4048; b_lsid=383C28410_19849DF44AA; browser_resolution=1536-303",
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



