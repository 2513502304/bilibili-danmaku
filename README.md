# ***bilibili-danmaku***
支持任意历史时间筛选的 `bilibili` 弹幕爬虫
---
支持设置起始时间参数 `start` 与结束时间参数 `end`，爬取 [start, end] 区间段的所有弹幕，每天最多获取 500 条弹幕数!!!

配置文件 `settings.py` 中需要设置的参数值
- `aids`：视频的 aid 列表，可选。若 aids 为空，则必须提供 bvids 参数。若设置了 file 参数，则忽略
- `bvids`：视频的 bvid 列表，可选。若 bvids 为空，则必须提供 aids 参数。若设置了 file 参数，则忽略
- `task`：任务名称，用于设置记录信息的文件名
- `cookies`：替换为你自己的 cookie，若提供多个 cookie，将在当前账号被监测到的时候自动替换为下一个账号
- `page`：视频分 p
- `start`：指定时间段开始，YYYY-MM-DD 格式，为 None，表示从视频发布时间开始
- `end`：指定时间段结束，YYYY-MM-DD 格式，为 None，表示至当前时间结束
- `delay`：每次请求的延迟时间，建议大于 1s
- `file_format`：转存的文件格式，支持 csv，xlsx，json
- `save_name`：转存的文件名称列表，必须与 aids/bvids 中提供的视频个数一致
- `save_dir`：转存的文件夹，默认为当前目录下的 Data 文件夹中

除此之外，若视频的 `aid`/`bvid` 列表来源自文件中的某一字段，则指定 `file` 参数中的各个键值对，以批量设置 `aids`/`bvids`/`save_name` 参数

可供参考获取视频的 `aid`/`bvid` 列表的项目：[MediaCrawler](https://github.com/NanmiCoder/MediaCrawler "MediaCrawler")

爬取到的各个字段如下

| 字段名    | 数据类型  | 说明                                                                 |
| --------- | --------- | -------------------------------------------------------------------- |
| id        | np.int64  | 弹幕 dmid。唯一，可用于操作参数                                      |
| progress  | np.int32  | 视频内弹幕出现时间。毫秒                                            |
| mode      | np.int32  | 弹幕类型。1 2 3：普通弹幕 4：底部弹幕 5：顶部弹幕 6：逆向弹幕 7：高级弹幕 8：代码弹幕 9：BAS 弹幕（仅限于特殊弹幕专包） |
| fontsize  | np.int32  | 弹幕字号。18：小 25：标准 36：大                                    |
| color     | np.uint32 | 弹幕颜色。十进制 RGB888 值                                          |
| midHash   | str       | 发送者 mid 的 HASH。用于屏蔽用户和查看用户发送的所有弹幕，也可反查用户 id |
| content   | str       | 弹幕内容。utf-8 编码                                                |
| ctime     | np.int64  | 弹幕发送时间。时间戳                                                |
| idStr     | str       | 弹幕 dmid。字串形式。唯一，可用于操作参数                            |
| attr      | np.int32  | 弹幕属性位。bit0：保护 bit1：直播 bit2：高赞                        |
| date      | str       | 弹幕发送日期。年/月/日                                             |
| time      | str       | 弹幕发送时间。时/分/秒                                             |

爬取到的结果文件如下
![image](https://github.com/user-attachments/assets/032d6b97-e5ee-41c3-a6de-05844664be00)
