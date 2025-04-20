'''
转存文件
'''

from crawl import get_user_information
from utils import logger, crack
from typing import Any, Callable
from rich.progress import track
import pandas as pd
import os


def load(file_path: str, field: str) -> pd.Series:
    '''
    加载文件中的指定字段，以 pandas.Series 返回
    ---
    :param file_path: 完整文件路径，支持 csv，xlsx，json 文件格式
    :param field: 字段名称
    :return: 包含指定字段的 pandas.Series 对象
    '''
    file_format = file_path.split('.')[-1].lower()
    match file_format:
        case 'csv':
            return pd.read_csv(file_path)[field]
        case 'xlsx':
            return pd.read_excel(file_path)[field]
        case 'json':
            return pd.read_json(file_path)[field]
        case _:
            raise ValueError('不受支持的文件格式，可用的文件格式为 csv，xlsx 和 json')


def get_aid_form_file(file_path: str, field: str) -> list[str]:
    '''
    加载文件中的 aid 字段，以包含 aid 字符串的列表形式返回
    ---
    :param file_path: 完整文件路径，支持 csv，xlsx，json 文件格式
    :param field: aid 字段名称
    :return: 包含指定 aid 字符串的列表对象
    '''
    return load(file_path=file_path, field=field).astype(str).tolist()


def get_bvid_form_file(file_path: str, field: str) -> list[str]:
    '''
    加载文件中的 bvid 字段，以包含 bvid 字符串的列表形式返回
    ---
    :param file_path: 完整文件路径，支持 csv，xlsx，json 文件格式
    :param field: bvid 字段名称
    :return: 包含指定 bvid 字符串的列表对象
    '''
    return load(file_path=file_path, field=field).astype(str).tolist()


def add_datetime_field(df: pd.DataFrame) -> pd.DataFrame:
    '''
    添加 bilibili 弹幕时间字段
    ---
    :param df: pandas.DataFrame
    :return: pandas.DataFrame
    '''
    # 将 ctime 时间戳转换为 datetime64[ns]
    t = pd.to_datetime(df['ctime'].astype(int), unit='s')
    # 取年月日赋值给 date 字段
    df['date'] = t.dt.date
    # 取时分秒赋值给 time 字段
    df['time'] = t.dt.time
    return df

def add_user_information_field(df: pd.DataFrame) -> pd.DataFrame:
    """
    添加 bilibili 弹幕用户信息字段

    Args:
        df (pd.DataFrame): pandas.DataFrame

    Returns:
        pd.DataFrame: pandas.DataFrame
    """
    # 反匿名化 midHash，获取 uid 列表，并添加对应 uid 信息字段
    for index, row in track(df.iterrows(), description='反匿名化中...', total=len(df)):
        # 当前行出现的 midHash 值
        midHash = row['midHash']
        # 先前行出现的 midHash 值
        pre_midHash = df.iloc[:index]['midHash']
        # 判断先前行中是否出现重复数据
        duplicates = pre_midHash[pre_midHash == midHash]
        # 如果有重复行，则使用先前行中重复出现的数据作为当前行的内容
        if not duplicates.empty:
            df.loc[index, :] = df.loc[index, :].fillna(df.loc[duplicates.index[0], :])
            logger.info(f'第 {index} 行，{midHash = } 在第 {duplicates.index[0]} 行中重复出现，将使用第 {duplicates.index[0]} 行的数据填充第 {index} 行中缺失值')
            continue
        # 如果没有重复行
        # 获取 uid
        uid = crack(midHash)
        # 添加 uid 字段
        df.loc[index, 'uid'] = uid
        # 获取用户名片信息
        user_info = get_user_information(mid=uid, photo=True)
            
        # 解析获取到的数据
        if user_info['code'] == 0:  # response right
            data = user_info['data']  # 信息本体
            archive_count = data['archive_count']  # 用户稿件数
            article_count = data['article_count']  # 0
            card = data['card']  # 卡片信息
            followers = data['follower']  # 粉丝数
            following = data['following']  # 是否关注此用户（true：已关注；false：未关注，需要登录（Cookie）未登录为 false）
            likes = data['like_num']  # 点赞数
            space = data['space']  # 主页头图

            DisplayRank = card['DisplayRank']  # 0
            Official = card['Official']  # 认证信息
            approve = card['approve']  # false
            article = card['article']  # 0
            attentions = card['attentions']  # 空
            birthday = card['birthday']  # 空
            description = card['description']  # 空
            face = card['face']  # 用户头像链接
            face_nft = card['face_nft']  # 是否为 NFT 头像（0：不是 NFT 头像；1：是 NFT 头像）
            face_nft_type = card['face_nft_type']  # NFT 头像类型
            fans = card['fans']  # 粉丝数
            friend = card['friend']  # 关注数
            is_senior_member = card['is_senior_member']  # 是否为硬核会员（0：否；1：是）
            level_info = card['level_info']  # 等级
            mid = card['mid']  # 用户 mid
            name = card['name']  # 用户昵称
            name_render = card['name_render']  # 用户昵称渲染（有效时：obj；无效时：null）
            nameplate = card['nameplate']  # 勋章信息（有效时：obj；无效时：null）
            official_verify = card['official_verify']  # 认证信息2
            pendant = card['pendant']  # 挂件
            place = card['place']  # 空
            rank = card['rank']  # 用户权限等级（目前应该无任何作用：5000：0 级未答题；10000：普通会员；20000：字幕君；25000：VIP；30000：真·职人；32000：管理员）
            regtime = card['regtime']  # 0
            sex = card['sex']  # 用户性别
            sign = card['sign']  # 用户签名
            spacesta = card['spacesta']  # 用户状态（0：正常；-2：被封禁）
            vip = card['vip']  # 大会员状态
            
            # 添加对应字段
            df.loc[index,'user_space_link'] = 'https://space.bilibili.com/' + uid  # 用户空间链接
            df.loc[index, 'name'] = name  # 用户昵称
            df.loc[index, 'sex'] = sex  # 用户性别
            df.loc[index, 'archive_count'] = archive_count  # 用户稿件数
            df.loc[index, 'fans'] = fans  # 粉丝数
            df.loc[index, 'friend'] = friend  # 关注数
            df.loc[index, 'likes'] = likes  # 点赞数
            df.loc[index, 'face'] = face  # 用户头像链接
            df.loc[index, 'is_senior_member'] = '否' if str(is_senior_member) == '0' else '是' # 是否为硬核会员（0：否；1：是）
            df.loc[index, 'level'] = level_info['current_level']  # 用户等级
            df.loc[index, 'sign'] = sign  # 用户签名    
            df.loc[index, 'spacesta'] = '正常' if str(spacesta) == '0' else '被封禁'  # 用户状态（0：正常；-2：被封禁）
            # TODO
        else:  # response error（除了当前账号被检测以外，还有可能是视频不存在的情况）
            logger.error(f'第 {index} 行，{midHash = }; {uid = }: {user_info["message"]}')
    return df

def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    '''
    去重 bilibili 弹幕字段
    ---
    :param df: pandas.DataFrame
    :return: pandas.DataFrame
    '''
    return df.drop_duplicates(ignore_index=True)

def dump(df: pd.DataFrame, save_name: str = '', save_dir: str = './Data', file_format: str = 'csv') -> None:
    '''
    将 pandas.DataFrame 转存为指定格式
    ---
    :param df: pandas.DataFrame
    :param save_name: 转存的文件名称，默认为空字符串 ''
    :param save_dir: 转存的文件夹，可选。默认为当前目录下的 Data 文件夹中
    :param file_format: 转存的文件格式，可选。默认为 csv，支持 csv，xlsx，json
    :return: None
    '''
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    save_path = os.path.join(save_dir, save_name)
    match file_format:
        case 'csv':
            df.to_csv(save_path + '.csv')
        case 'xlsx':
            df.to_excel(save_path + '.xlsx', engine='xlsxwriter')
        case 'json':
            df.to_json(save_path + '.json')
        case _:
            raise ValueError('请输入有效的 format，可用的 format 为 csv，xlsx 和 json')


PRETREATMENT: list[Callable] = [add_datetime_field, drop_duplicates]

def dump_history_danmaku(data: Any, save_name: str = '', save_dir: str = './Data', file_format: str = 'csv', callbacks: list[Callable] = PRETREATMENT) -> None:
    '''
    转存历史弹幕
    ---
    :param data: 能够被 pandas 读取的任意数据，该数据将在函数内部被转换为 pandas.DataFrame 对象
    :param save_name: 转存的文件名称，默认为空字符串 ''
    :param save_dir: 转存的文件夹，可选。默认为当前目录下的 Data 文件夹中
    :param file_format: 转存的文件格式，可选。默认为 csv，支持 csv，xlsx，json
    :param callbacks: 回调函数列表，列表元素接受一个类型为 pandas.DataFrame 的参数，用于执行转存数据前的预处理操作，并返回 pandas.DataFrame。默认为 PRETREATMENT
    :return: None
    '''
    df = pd.DataFrame(data)
    if not df.empty:
        if callbacks:
            for callback in callbacks:
                df = callback(df)
    # 转存为指定格式
    return dump(df, save_name=save_name, save_dir=save_dir, file_format=file_format)
