from typing import TypeAlias
import logging

# 启用调试于 http.client 级别 (requests->urllib3->http.client)
# 你将能看到 REQUEST，包括 HEADERS 和 DATA，以及包含 HEADERS 但不包含 DATA 的 RESPONSE
# 唯一缺少的是 response.body，它不会被 log 记录
try:  # for Python 3
    from http.client import HTTPConnection
except ImportError:
    from httplib import HTTPConnection

HTTPConnection.debuglevel = 0  # 大于 0 开启调试，日志冗余信息过多，不建议开启

# 日志记录
logging.basicConfig(
    format='%(asctime)s %(name)s %(levelname)s (%(filename)s %(funcName)s %(lineno)d): %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
)
logger = logging.getLogger('bilibili-danmaku')

# bilibili aid 与 bvid 相互转换
'''
2020 年 03 月 18 日 【升级公告】 AV 号全面升级至 BV 号：https://www.bilibili.com/opus/369825052444936486
- 旧版 AV 号，如 https://www.bilibili.com/video/av2/
- 新版 BV 号，如 https://www.bilibili.com/video/BV1ft6hYxE75/
算法说明：
- https://socialsisteryi.github.io/bilibili-API-collect/docs/misc/bvid_desc.html
'''

aid = '113736958350047'
bvid = 'BV1ft6hYxE75'

# 按位与
AND = (1 << 51) - 1
# 异或
XOR = 23442827791579

# 最大 aid，为 2 的 51 次幂
max_aid = 1 << 51

# 转换表
alphabet = "FcwAPNKTMug3GV5Lj7EJnHpWsx4tb8haYeviqBz6rkCy12mUSDQX9RdoZf"
# 转换表长度
base = len(alphabet)

# bvid 编码表，9 位
encode_map = [8, 7, 0, 5, 1, 3, 2, 4, 6]
# bvid 解码表，9 位
decode_map = list(reversed(encode_map))


def av2bv(aid: str) -> str:
    '''
    aid 转 bvid
    ---
    :param aid: 要转换的 aid
    :return: 转换后的 bvid
    '''
    if aid[:2] == 'av':
        aid = list(aid[2:])
    bvid = [''] * 9
    temp = (max_aid | int(aid)) ^ XOR
    for i in range(len(encode_map)):
        bvid[encode_map[i]] = alphabet[int(temp % base)]
        temp /= base
    return 'BV1' + ''.join(bvid)


def bv2av(bvid: str) -> str:
    '''
    bvid 转 aid
    ---
    :param bvid: 要转换的 bvid
    :return: 转换后的 aid
    '''
    if bvid[:3] == 'BV1':
        bvid = list(bvid[3:])
    temp = 0
    for i in range(len(decode_map)):
        idx = alphabet.index(bvid[decode_map[i]])
        temp = temp * base + idx
    return (temp & AND) ^ XOR


base58encode: TypeAlias = av2bv
base58decode: TypeAlias = bv2av

if __name__ == '__main__':
    av2bv(aid), bv2av(bvid)
