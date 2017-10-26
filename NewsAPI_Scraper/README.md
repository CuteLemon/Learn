# CNN News

V0.1
从新闻API处获得新闻的链接以及概述。
然后从原始新闻网站爬取对应的新闻。
新闻使用mongodb 存储，
前端采用React
后端使用nodejs

有一个新闻爬虫包 newspaper 可以方便的抓取新闻。但该包的python2版本已经废弃。


将API返回的数据存入MongoDB，按title+description 来去重。
