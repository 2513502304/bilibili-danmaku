'''
转存文件
'''

from typing import Any
import pandas as pd
import os


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


def dump_history_danmaku(data: Any, save_name: str = '', save_dir: str = './Data', file_format: str = 'csv', callback: callable = add_datetime_field):
    '''
    转存历史弹幕
    ---
    :param data: 能够被 pandas 读取的任意数据，该数据将在函数内部被转换为 pandas.DataFrame 对象
    :param save_name: 转存的文件名称，默认为空字符串 ''
    :param save_dir: 转存的文件夹，可选。默认为当前目录下的 Data 文件夹中
    :param file_format: 转存的文件格式，可选。默认为 csv，支持 csv，xlsx，json
    :param callback: 回调函数，接受一个类型为 pandas.DataFrame 的参数，用于执行转存数据前的预处理操作，并返回 pandas.DataFrame。默认为 add_datetime_field
    :return: None
    '''
    df = pd.DataFrame(data)
    if not df.empty:
        if callback is not None:
            df = callback(df)
    # 转存为指定格式
    return dump(df, save_name=save_name, save_dir=save_dir, file_format=file_format)
