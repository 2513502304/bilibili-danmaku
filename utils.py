import logging
from typing import Callable

from rich.logging import RichHandler

# ------------------------------------------- 日志 -------------------------------------------

# 日志记录
logging.basicConfig(
    format='%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    handlers=[RichHandler()],
)
logger = logging.getLogger('bilibili-danmaku')

# ------------------------------------------- 编解码 -------------------------------------------

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


base58encode: Callable[[str], str] = av2bv
base58decode: Callable[[str], str] = bv2av

# midHash 反查用户信息
'''
midHash 反查用户信息
- bilibili 弹幕中的 midHash 是通过将 uid 经过 CRC32A (ITU I.363.5) 算法进行哈希处理与 16 进制转换后得到的
- 如 uid = 86137069，经过 hex(crc32(uid)) 转换后的 midHash = 4e902d62
- 一个简单的方法是采用暴力破解，通过构建存储 uid 和 midHash 对应关系的字典表，并反向查找以确定对应 midHash 的 uid，但这需要大量的存储空间和时间。若想保证查找的准确率和召回率，则需要构建一个至少包含 10 亿个数据的字典表
- 用于反匿名破解 CRC32A 的高效算法以及 JS 实现：https://github.com/MoePus/bilibili_danmaku_AntiAnonym
- 考虑到哈希碰撞，可能会出现多个 uid 对应同一个 midHash 的情况，因此反查出的用户信息可能并不准确

CRC32
- 循环冗余校验是对数据执行完整性检查的常用方法。它是一个简单的哈希函数，可确保数据未损坏，并广泛用于数据通信和数据存储应用程序
- CRC 不适用于防止有意修改数据。它是一种密码较弱的算法，很容易被逆转

Reference:
- CRC32：https://www.itu.int/rec/T-REC-I.363.5-199608-I/en
- 爬虫分析：通过弹幕查找发送者：https://www.bilibili.com/opus/155443177204924005
- B站弹幕解析：https://zhuanlan.zhihu.com/p/499708255
'''
'''将用于反匿名破解 CRC32A 的高效算法以及 JS 实现转换为 Python 实现：https://github.com/MoePus/bilibili_danmaku_AntiAnonym'''
# CRC32A 多项式
CRCPOLYNOMIAL = 0xEDB88320
# CRC32A 查找表
crctable = [0 for _ in range(256)]
# 生成 CRC32A 查找表
for i in range(256):
    crcreg = i
    for _ in range(8):
        if (crcreg & 1) != 0:
            crcreg = CRCPOLYNOMIAL ^ (crcreg >> 1)
        else:
            crcreg = crcreg >> 1
    crctable[i] = crcreg


def crc32(text: str) -> int:
    crcstart = 0xFFFFFFFF
    for i in range(len(str(text))):
        index = (crcstart ^ ord(str(text)[i])) & 0xff
        crcstart = (crcstart >> 8) ^ crctable[index]
    return crcstart


def crc32_last_index(text: str) -> int:
    crcstart = 0xFFFFFFFF
    for i in range(len(str(text))):
        index = (crcstart ^ ord(str(text)[i])) & 0xff
        crcstart = (crcstart >> 8) ^ crctable[index]
    return index


def get_crc_index(t: int) -> int:
    for i in range(256):
        if crctable[i] >> 24 == t:
            return i
    return -1


def deep_check(i: int, index: int) -> list[int] | list[int, str]:
    tc = 0x00
    text = ''
    hashcode = crc32(str(i))
    tc = hashcode & 0xff ^ index[2]
    if not (tc <= 57 and tc >= 48):
        return [0]
    text += str(tc - 48)
    hashcode = crctable[index[2]] ^ (hashcode >> 8)
    tc = hashcode & 0xff ^ index[1]
    if not (tc <= 57 and tc >= 48):
        return [0]
    text += str(tc - 48)
    hashcode = crctable[index[1]] ^ (hashcode >> 8)
    tc = hashcode & 0xff ^ index[0]
    if not (tc <= 57 and tc >= 48):
        return [0]
    text += str(tc - 48)
    hashcode = crctable[index[0]] ^ (hashcode >> 8)
    return [1, text]


def crack(text: str) -> str:
    """
    反匿名破解 bilibili 弹幕中，经过 CRC32A 算法处理后的 midHash 值，返回对应的 uid

    Args:
        text (str): midHash 值

    Returns:
        str: 对应的 uid
    """
    index = [0 for _ in range(4)]
    i = 0
    ht = int(f'0x{text}', 16) ^ 0xffffffff
    for i in range(3, -1, -1):
        index[3 - i] = get_crc_index(ht >> (i * 8))
        snum = crctable[index[3 - i]]
        ht ^= snum >> ((3 - i) * 8)
    for i in range(100_000_000):  #!1 亿次循环，理论上足够了，若查找不到对应 uid 则放弃查找
        lastindex = crc32_last_index(i)
        if lastindex == index[3]:
            deepCheckData = deep_check(i, index)
            if deepCheckData[0]:
                break
    if i == 100_000_000:
        return -1
    return f'{i}{deepCheckData[1]}'


if __name__ == '__main__':
    print('aid:', aid, '-> bvid:', av2bv(aid))
    print('bvid:', bvid, '-> aid:', bv2av(bvid))
