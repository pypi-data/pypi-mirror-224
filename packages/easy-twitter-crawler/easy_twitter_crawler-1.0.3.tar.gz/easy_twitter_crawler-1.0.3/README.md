# easy_twitter_crawler

推特（Twitter）采集程序，支持用户，发文，评论采集，希望能为使用者带来益处。如果您也想贡献好的代码片段，请将代码以及描述，通过邮箱（ [xinkonghan@gmail.com](mailto:hanxinkong<xinkonghan@gmail.com>)
）发送给我。代码格式是遵循自我主观，如存在不足敬请指出！

## 推特三件套（有需要可自行安装）

- `easy_twitter_publisher` 推特发帖,回帖,转载 https://pypi.org/project/easy_twitter_publisher
- `easy_twitter_crawler` 推特采集 https://pypi.org/project/easy-twitter-crawler
- `easy_twitter_interactors` 推特互动（点赞,刷阅读量等） https://pypi.org/project/easy_twitter_interactors

## 安装

```shell
pip install easy-twitter-crawler
```

## 主要功能

- `search_crawler` 关键词搜索采集（支持热门,用户,最新,视频,照片;支持条件过滤）
- `user_crawler` 用户采集（支持用户信息,用户发文,用户回复）
- `common_crawler` 通用采集（支持发文,评论）

## 简单使用

设置代理及cookie (关键词,用户发文,用户回复,粉丝,关注,评论需要设置cookie)

```python
proxy = {
    'http': 'http://127.0.0.1:10808',
    'https': 'http://127.0.0.1:10808'
}
cookie = 'auth_token=686fa28f49400698820d0a3c344c51efdeeaf73a; ct0=5bed99b7faad9dcc742eda564ddbcf37888f8794abd6d4d736919234440be2172da1e9a9fc48bb068db1951d1748ba5467db2bc3e768f122794265da0a9fa6135b4ef40763e7fd91f730d0bb1298136b'
```

关键词采集使用案例（对关键词指定条件采集10条数据）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, search_crawler, TwitterFilter

key_word = 'elonmusk'

twitter_filter = TwitterFilter(key_word)
twitter_filter.word_category(lang='en')
twitter_filter.account_category(filter_from='', to='', at='')
twitter_filter.filter_category(only_replies=None, only_links=None, exclude_replies=None, exclude_links=None)
twitter_filter.interact_category(min_replies='', min_faves='', min_retweets='')
twitter_filter.date_category(since='', until='')
key_word = twitter_filter.filter_join()

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in search_crawler(
        key_word,
        data_type='Top',
        count=10,
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
```

关键词采集参数说明

| 字段名       | 类型     | 必须 | 描述                                                      |
|-----------|--------|----|---------------------------------------------------------|
| key_word  | string | 是  | 关键词                                                     |
| data_type | string | 否  | 指定采集的板块（热门：Top 用户：People 最新：Latest 视频：Videos 照片：Photos） |
| count     | int    | 否  | 采集的数量（默认不采集：-1，采集全部：0，采集指定的数量：>0）                       |                                 

关键词过滤参数说明（对标推特搜索功能，同一参数多个值间用空格隔开）

| 所属类别              | 字段名             | 类型     | 必须 | 描述                       |
|-------------------|-----------------|--------|----|--------------------------|
| word_category     | exact           | string | 否  | 精确短语                     |
| word_category     | filter_any      | string | 否  | 任何一词（支持多个)               |
| word_category     | exclude         | string | 否  | 排除这些词语 (支持多个) 示例：dog cat |
| word_category     | tab             | string | 否  | 这些话题标签（支持多个)             |
| word_category     | lang            | string | 否  | 语言（文档后附语言可选范围）           |   
| account_category  | filter_from     | string | 否  | 来自这些账号（支持多个)             |
| account_category  | to              | string | 否  | 发给这些账号（支持多个)             |
| account_category  | at              | string | 否  | 提及这些账号（支持多个)             |
| filter_category   | only_replies    | bool   | 否  | 仅回复                      |
| filter_category   | only_links      | bool   | 否  | 仅链接                      |
| filter_category   | exclude_replies | bool   | 否  | 排除回复                     |
| filter_category   | exclude_links   | bool   | 否  | 排除链接                     |
| interact_category | min_replies     | int    | 否  | 最少回复次数                   |
| interact_category | min_faves       | int    | 否  | 最少喜欢次数                   |
| interact_category | min_retweets    | int    | 否  | 最少转推次数                   |
| date_category     | since           | string | 否  | 开始日期（'2023-07-20'）       |
| date_category     | until           | string | 否  | 结束日期（'2023-08-20'）       |

----

用户信息采集使用案例（采集该用户信息及10条文章，10条回复，10个粉丝信息，10个关注信息）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, user_crawler

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in user_crawler(
        'elonmusk',
        article_count=10,
        reply_count=10,
        following_count=10,
        followers_count=10,
        # start_time='2023-07-20 00:00:00',
        # end_time='2023-07-27 00:00:00',
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
    print(f"文章数：{len(info.get('article', []))}")
    print(f"粉丝数：{len(info.get('followers', []))}")
    print(f"关注数：{len(info.get('following', []))}")
    print(f"回复数：{len(info.get('reply', []))}")
```

用户信息采集参数说明

| 字段名             | 类型     | 必须 | 描述                                            |
|-----------------|--------|----|-----------------------------------------------|
| user_id         | string | 是  | 用户名（https://twitter.com/elonmusk 中的 elonmusk） |
| article_count   | int    | 否  | 采集文章数（默认不采集：-1，采集全部：0，采集指定的数量：>0）             |             
| reply_count     | int    | 否  | 采集回复数 （默认不采集：-1，采集全部：0，采集指定的数量：>0）            |              
| following_count | int    | 否  | 采集关注数 （默认不采集：-1，采集全部：0，采集指定的数量：>0）            |                
| followers_count | int    | 否  | 采集粉丝数 （默认不采集：-1，采集全部：0，采集指定的数量：>0）            |                
| start_time      | string | 否  | 数据截取开始时间 （仅当采集文章或回复时有效）                       |                   
| end_time        | string | 否  | 数据截取结束时间（仅当采集文章或回复时有效）                        |                  

___

通用采集使用案例（已知文章id，采集此文章信息）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, common_crawler

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in common_crawler(
        '1684447438864785409',
        data_type='article',
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
```

通用采集使用案例（已知文章id，采集此文章下10条评论）

```python
from easy_spider_tool import cookie_to_dic, format_json
from easy_twitter_crawler import set_proxy, set_cookie, common_crawler

set_proxy(proxy)
set_cookie(cookie_to_dic(cookie))

for info in common_crawler(
        '1684447438864785409',
        data_type='comment',
        comment_count=10,
):
    set_proxy(proxy)
    set_cookie(cookie_to_dic(cookie))
    print(format_json(info))
```

通用采集参数说明

| 字段名           | 类型     | 必须 | 描述                                                                                   |
|---------------|--------|----|--------------------------------------------------------------------------------------|
| task_id       | string | 是  | 文章id（https://twitter.com/elonmusk/status/1690164670441586688 中的 1690164670441586688） |
| data_type     | string | 是  | 采集类型（文章：article 评论：comment）                                                          |             
| comment_count | int    | 否  | 采集评论数量（仅当data_type为comment时有效；默认不采集：-1，采集全部：0，采集指定的数量：>0）                            |             

___

## 语言表

有时间再补充

## 链接

Github：https://github.com/hanxinkong/easy_twitter_crawler

在线文档：https://easy_twitter_crawler.xink.top

## 贡献者
