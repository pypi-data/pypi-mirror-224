# easy_twitter_interactors

推特（Twitter）点赞,刷阅读量程序，希望能为使用者带来益处。如果您也想贡献好的代码片段，请将代码以及描述，通过邮箱（ [xinkonghan@gmail.com](mailto:hanxinkong<xinkonghan@gmail.com>)
）发送给我。代码格式是遵循自我主观，如存在不足敬请指出！

## 推特三件套（有需要可自行安装）

- `easy_twitter_publisher` 推特发帖,回帖,转载 https://pypi.org/project/easy_twitter_publisher
- `easy_twitter_crawler` 推特采集 https://pypi.org/project/easy-twitter-crawler
- `easy_twitter_interactors` 推特互动（点赞,刷阅读量等） https://pypi.org/project/easy_twitter_interactors

## 安装

```shell
pip install easy-twitter-interactors
```

## 主要功能

- `likes` 对指定帖子点赞
- `reads` 对指定帖子刷阅读量（暂无）

## 简单使用

设置代理及cookie (点赞和阅读均需要设置cookie)

```python
proxy = {
    'http': 'http://127.0.0.1:10808',
    'https': 'http://127.0.0.1:10808'
}
cookie = 'auth_token=686fa28f49400698820d0a3c344c51efdeeaf73a; ct0=5bed99b7faad9dcc742eda564ddbcf37888f8794abd6d4d736919234440be2172da1e9a9fc48bb068db1951d1748ba5467db2bc3e768f122794265da0a9fa6135b4ef40763e7fd91f730d0bb1298136b'
```

点赞使用案例（对指定帖子点赞）

```python
from easy_spider_tool import format_json
from easy_twitter_interactors import TwitterLikes, get_headers

twitter_likes = TwitterLikes()
twitter_likes.set_proxy(proxy)
twitter_likes.set_headers(get_headers(cookie))
likes_info = twitter_likes.likes('1690065356495421444')
print(format_json(likes_info))
```

点赞参数说明

| 字段名         | 类型     | 必须 | 描述                                                                                     |
|-------------|--------|----|----------------------------------------------------------------------------------------|
| to_tweet_id | string | 是  | 目标帖子id（https://twitter.com/elonmusk/status/1690164670441586688 中的 1690164670441586688） |

___

## 链接

Github：https://github.com/hanxinkong/easy_twitter_interactors

在线文档：https://easy_twitter_interactors.xink.top

## 贡献者
