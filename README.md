# ***bilibili-danmaku***

支持任意历史时间筛选的 `bilibili` 弹幕爬虫。

---

## 功能简介

- **弹幕历史筛选**：支持设置起始时间参数 `start` 与结束时间参数 `end`，用以爬取 [start, end] 时间段内的所有弹幕。
- **弹幕全量获取**：鉴于使用的 b 站接口每天至多返回 500 条弹幕，若某天的弹幕数超过 500，则多余的弹幕会依次安排至往后的天数返回，若将 `start` 与 `end` 参数均设置为 `None`，则可以完全爬取当前视频的全部弹幕。
- **多格式导出**：支持 csv、xlsx、json 等多种格式导出弹幕数据。
- **用户信息爬取**：可选参数 `user_info`，用以在爬取视频弹幕后，通过弹幕中的 midHash 字段反查用户信息，继而获取弹幕发送者的用户详细。
- **多账号自动切换**：支持配置多个 cookie，账号被风控时自动切换。
- **批量任务支持**：支持 aid/bvid 批量导入，适合大规模弹幕数据采集。
- **任务断点续传**：支持在某次任务中断后，继续根据上次爬取的进度增量式爬取，避免重复爬取所带来的时间损耗以及数据浪费。

---

## 示例展示

### 爬取 b 站视频 `BV1ft6hYxE75` 的全部弹幕，爬取到的各个字段如下：

| 字段名   | 数据类型  | 说明                                                                                                                    |
| -------- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| id       | np.int64  | 弹幕 dmid。唯一，可用于操作参数                                                                                         |
| progress | np.int32  | 视频内弹幕出现时间。毫秒                                                                                                |
| mode     | np.int32  | 弹幕类型。1 2 3：普通弹幕 4：底部弹幕 5：顶部弹幕 6：逆向弹幕 7：高级弹幕 8：代码弹幕 9：BAS 弹幕（仅限于特殊弹幕专包） |
| fontsize | np.int32  | 弹幕字号。18：小 25：标准 36：大                                                                                        |
| color    | np.uint32 | 弹幕颜色。十进制 RGB888 值                                                                                              |
| midHash  | str       | 发送者 mid 的 HASH。用于屏蔽用户和查看用户发送的所有弹幕，也可反查用户 id                                               |
| content  | str       | 弹幕内容。utf-8 编码                                                                                                    |
| ctime    | np.int64  | 弹幕发送时间。时间戳                                                                                                    |
| idStr    | str       | 弹幕 dmid。字串形式。唯一，可用于操作参数                                                                               |
| attr     | np.int32  | 弹幕属性位。bit0：保护 bit1：直播 bit2：高赞                                                                            |
| date     | str       | 弹幕发送日期。年/月/日                                                                                                  |
| time     | str       | 弹幕发送时间。时/分/秒                                                                                                  |

### 爬取到的结果文件如下：

![image](https://github.com/user-attachments/assets/b8ab1354-52c8-414a-9fb2-c19fa484e235)

### 若 `user_info` 为 True，则还会为各个弹幕添加与用户信息相关的字段，爬取到的各个字段如下：
> **注意**：开启该功能可能会导致处理时间过长，因为涉及到通过 midHash 反查用户信息以及额外的网络请求，建议非必要不要开启此选项

| 字段名           | 数据类型  | 说明                                                                                                                    |
| ---------------- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| id               | np.int64  | 弹幕 dmid。唯一，可用于操作参数                                                                                         |
| progress         | np.int32  | 视频内弹幕出现时间。毫秒                                                                                                |
| mode             | np.int32  | 弹幕类型。1 2 3：普通弹幕 4：底部弹幕 5：顶部弹幕 6：逆向弹幕 7：高级弹幕 8：代码弹幕 9：BAS 弹幕（仅限于特殊弹幕专包） |
| fontsize         | np.int32  | 弹幕字号。18：小 25：标准 36：大                                                                                        |
| color            | np.uint32 | 弹幕颜色。十进制 RGB888 值                                                                                              |
| midHash          | str       | 发送者 mid 的 HASH。用于屏蔽用户和查看用户发送的所有弹幕，也可反查用户 id                                               |
| content          | str       | 弹幕内容。utf-8 编码                                                                                                    |
| ctime            | np.int64  | 弹幕发送时间。时间戳                                                                                                    |
| idStr            | str       | 弹幕 dmid。字串形式。唯一，可用于操作参数                                                                               |
| attr             | np.int32  | 弹幕属性位。bit0：保护 bit1：直播 bit2：高赞                                                                            |
| date             | str       | 弹幕发送日期。年/月/日                                                                                                  |
| time             | str       | 弹幕发送时间。时/分/秒                                                                                                  |
| uid              | int       | 用户 mid                                                                                                                |
| user_space_link  | str       | 用户空间链接                                                                                                            |
| name             | str       | 用户昵称                                                                                                                |
| sex              | str       | 用户性别                                                                                                                |
| archive_count    | int       | 用户稿件数                                                                                                              |
| fans             | int       | 粉丝数                                                                                                                  |
| friend           | int       | 关注数                                                                                                                  |
| likes            | int       | 点赞数                                                                                                                  |
| face             | str       | 用户头像链接                                                                                                            |
| is_senior_member | str       | 是否为硬核会员。0：否；1：是                                                                                            |
| level            | int       | 用户等级                                                                                                                |
| sign             | str       | 用户签名                                                                                                                |
| spacesta         | str       | 用户状态。0：正常；-2：被封禁                                                                                           |

### 爬取到的结果文件如下：
![image](https://github.com/user-attachments/assets/0f10d3bc-99a3-4075-9ec5-4c6e154974f7)

---

## 使用方法

1. **安装依赖**：
   ```bash
   pip install -r requirements.txt
   ```
   
2. **配置参数**：
   在 settings.py 文件中修改以下参数：
   - `aids`：视频的 aid 列表，可选。若 aids 为空，则必须提供 bvids 参数。若 from_file 参数为 True，且正确配置了 file 参数，则忽略
   - `bvids`：视频的 bvid 列表，可选。若 bvids 为空，则必须提供 aids 参数。若 from_file 参数为 True，且正确配置了 file 参数，则忽略
   - `task`：任务名称，用于设置记录信息的文件名
   - `cookies`：替换为你自己的 cookie，若提供多个 cookie，将在当前账号被监测到的时候自动替换为下一个账号
   - `page`：视频分 p
   - `start`：指定时间段开始，YYYY-MM-DD 格式，为 None，表示从视频发布时间开始
   - `end`：指定时间段结束，YYYY-MM-DD 格式，为 None，表示至当前时间结束
   - `delay`：每次请求的延迟时间，建议大于 1s
   - `file_format`：转存的文件格式，支持 csv，xlsx，json
   - `save_name`：转存的文件名称列表，必须与 aids/bvids 中提供的视频个数一致
   - `save_dir`：转存的文件夹，默认为当前目录下的 Data 文件夹中
   - `user_info`：是否添加 bilibili 弹幕用户信息字段。开启该功能可能会导致处理时间过长，因为涉及到通过 midHash 反查用户信息以及额外的网络请求，建议非必要不要开启此选项

   除此之外，若视频的 `aid`/`bvid` 列表来源自文件中的某一字段，则指定 `file` 参数中的各个键值对，以**批量**设置 `aids`/`bvids`/`save_name` 参数

   可供参考用以获取**特定关键字搜索**下的视频 `aid`/`bvid` 列表的 `github` 开源项目：[**MediaCrawler**](https://github.com/NanmiCoder/MediaCrawler "MediaCrawler")

3. **运行程序**：
   ```bash
   python main.py
   ```
   
---

## 依赖环境

- Python 3.9 或更高版本

---

## 注意事项

- 建议合理设置请求延迟，避免账号被风控。
- 批量处理建议使用文件导入模式。
- 开启用户信息爬取时，处理速度会显著下降。

---

## 贡献指南

欢迎对本项目提出建议或贡献代码！请通过以下步骤参与贡献：

1. Fork 本仓库。

2. 创建新分支：
   ```bash
   git checkout -b feature/your-feature-name
   ```
   
3. 提交更改并推送到你的分支：
   ```bash
   git commit -m "Add your commit message"
   git push origin feature/your-feature-name
   ```

4. 提交 Pull Request。

---

## 许可证

本项目基于 MIT License 开源。

---

## 联系方式

如有任何问题或建议，请联系作者：
- **Email**: 2513502304@qq.com
