'''
配置文件
'''

# 茜特拉莉（bushi，原神怎么你了）
# 视频的 aid 列表，可选。若 aids 为空，则必须提供 bvids 参数
aids = [
    '113736958350047',
]
# 视频的 bvid 列表，可选。若 bvids 为空，则必须提供 aids 参数
bvids = [
    'BV1ft6hYxE75',
]
# 视频弹幕的 cid，ignore
cids = [
    '27598718983',
]

# 替换为你自己的 cookie，若提供多个 cookie，将在当前账号被监测到的时候自动替换为下一个账号
cookies = [
    'buvid3=E7A60D04-A623-D874-3258-419DD662DBD778682infoc; b_nut=1706261678; _uuid=9ACE110A10-C4C8-C773-10B105-109BB2838110DC79825infoc; buvid_fp=65b84bf6b66a9ebdc7eb814ad192ce25; buvid4=412792E4-4F69-EA2C-E164-E2E7F63516A280717-024012609-LO6Ew%2BZRNVcR3BHdc%2FoGnyTTMv2KNC6pxT9yH2%2B%2FOG8vDQeaEQSY68zMTktyqHO8; header_theme_version=CLOSE; enable_web_push=DISABLE; home_feed_column=5; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcyNTU0NTgsImlhdCI6MTczNjk5NjE5OCwicGx0IjotMX0.PmchbUQVkcTymTYCvEjadLalc62SILV1UZnjV4Cm-t0; bili_ticket_expires=1737255398; rpdid=0zbfAI6DyG|mOqVMo6K|3Ce|3w1Tyglj; SESSDATA=1b9a2efa%2C1752556128%2C4e80a%2A12CjDQEzGl4ZZuyFOK1fT2aQwZbfzbczltMLrmTtYL8TTTIk1Ou6JHSRwRAE0DYhZ8P7gSVi1lQkthOU54dkZNRWI0c2dPeVNXOHZKd3VielBTNHQxWkd6UDg2U0RzRjhiSER6Ym1XTGhIX1dKUFJlcDRxWFJENnJsZlR0Z180azFnemVlT2hOM1FRIIEC; bili_jct=7e2a7f36f541b13731eca813d1f0ed0b; DedeUserID=86137069; DedeUserID__ckMd5=9c9e29b3c177de79; CURRENT_FNVAL=4048; b_lsid=885FF175_1947525F9DF; bsource=search_bing; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; browser_resolution=1492-358',
    'buvid3=E4B0FF67-ED6D-3C9A-FAD7-C1E2D593C2B060088infoc; b_nut=1719544260; _uuid=5B778C10C-9594-12F8-361F-102CC6AAB4DAC61385infoc; enable_web_push=DISABLE; buvid4=16089B19-FFE6-58C5-CF1E-9E337FB79FC161029-024062803-z6Uxn9V9Crd0fXW3HIgGdw%3D%3D; rpdid=0zbfAI6DyH|2RQZtZ6J|1RD|3w1SqFRV; header_theme_version=CLOSE; LIVE_BUVID=AUTO4217286542998787; PVID=2; fingerprint=0885da303e16d96e4d000078be62ed7c; buvid_fp_plain=undefined; buvid_fp=0885da303e16d96e4d000078be62ed7c; CURRENT_QUALITY=80; home_feed_column=5; Hm_lvt_8a6e55dbd2870f0f5bc9194cddf32a02=1736585546; is-2022-channel=1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzcwNDQzODQsImlhdCI6MTczNjc4NTEyNCwicGx0IjotMX0.E3N6QLPyr2QOUa_SznLEi_OebWYZtSctEeESC1gaYaU; bili_ticket_expires=1737044324; _tea_utm_cache_586864={%22creative_id%22:181369634}; bmg_af_switch=1; bmg_src_def_domain=i2.hdslb.com; b_lsid=B25E12E7_1946E157497; bp_t_offset_86137069=1022955905899036672; SESSDATA=e70ece10%2C1752565964%2Ce7773%2A11CjAUZOZDf_Fahj1lREUun8kFRt3RdO1rgwAgN0-iTl1uCm20EGshRtJ8FWAHNYbkyJYSVkxXRURJbEw1eExyV2F4VGxhdC0xZzBuaFR5NVBlc1ZIYkxYakVZSXVJOVJFQWNTclo4MlNPSjVZcVhHelI4YUlzcE1sbHAwQi11aDFZSUE5NURKM0pBIIEC; bili_jct=ecf77afd88f60c8336a7589038a15ac0; DedeUserID=71951017; DedeUserID__ckMd5=a97d5c02401bdcd2; sid=5f7wdbjl; CURRENT_FNVAL=4048; browser_resolution=1536-310',
]

# 视频分 p
page = 1

# 指定时间段开始，YYYY-MM-DD 格式，为 None，表示从视频发布时间开始
start = None

# 指定时间段结束，YYYY-MM-DD 格式，为 None，表示至当前时间结束
end = '2025-01-01'

# 每次请求的延迟时间，建议大于 1s
delay = 3

# 转存的文件格式，默认为 csv，支持 csv，xlsx，json
file_format = 'csv'

# 转存的文件名称列表，必须与 aids/bvids 中提供的视频个数一致
save_name = [
    '茜特拉莉弹幕',
]

# 转存的文件夹，默认为当前目录下的 Data 文件夹中
save_dir = './Data'
