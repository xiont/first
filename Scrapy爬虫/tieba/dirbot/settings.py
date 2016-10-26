#coding=utf-8
# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbot.spiders']
NEWSPIDER_MODULE = 'dirbot.spiders'
DEFAULT_ITEM_CLASS = 'dirbot.items.Website'

ITEM_PIPELINES = {
    'dirbot.pipelines.TiebaPipeline': 100,
    'dirbot.pipelines.PostPipeline': 200,
    'dirbot.pipelines.ReplyPipeline': 300,
    'dirbot.pipelines.CommentPipeline': 400,
    'dirbot.pipelines.MemberPipeline': 500,
    'dirbot.pipelines.UserAsMemberPipeline': 600,
    'dirbot.pipelines.FanPipeline': 700,
    'dirbot.pipelines.FollowPipeline': 800,
    'dirbot.pipelines.UserAsFollowPipeline': 850,
    'dirbot.pipelines.UserAsFanPipeline': 860,
    'dirbot.pipelines.UserPipeline': 870
}

DOWNLOAD_DELAY = 1
COOKIES_DEBUG = True

#cookie相关
BDUSS = '0gyREZUZ1RRQURWRUtKOXRGYmFXY3BQZ0RNdW1JVjU4cktBRzh4NkN6eDdqSU5XQVFBQUFBJCQAAAAAAAAAAAEAAADLt0ACanp0aGVrZWVwZXIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHv'
BAIDUID = '2A1D3A8123DDA2BAB5B74C370704F59D:FG=1'
TIEBA_USERTYPE = 'a4634cd4258757360e1e06aa'
TIEBAUID = '57f1b4ebc1f54535d094a24c'
LONGID = '37795787'
#数据库相关
MYSQL_HOST = 'localhost'
MYSQL_DBNAME = 'tieba'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'q'
#贴吧名称列表
TIEBA_NAMES_LIST = [
    #'心理',
    #'广东',
    '中国电影',
]
