# 2017.10.22

创建了css 样式。
可以得到简易的卡片。


如何将模板格式化的卡片 与 后端的数据内容结合起来呢？


先定义几层框架。
在container 中
放置：
1.header ,logo
2.news panel

这就分为3个类。

container: 包含一切
news panel:
包含新闻数据，图片以及一些小按钮 。



## React 类如何得到数据的？
通过请求后端的数据，比如
API
返回JSON 格式的数据。
然后整理，填充到 news panel 类中。


接下来的任务：
1.界面设计
样式设计。
container 、news pannel 类。

news pannel 类
会使用fetch 方法获取json 数据。request,res  http://javascript.ruanyifeng.com/bom/ajax.html#toc27
类似JQuery


2.接口设计
搭好后端网页框架，如express。设计API接口格式，

设计路由，在特定网页返回json数据。先联调接口。


# 2017.10.23

后端采用 koa ，阮一峰。
例程 http://www.ruanyifeng.com/blog/2017/08/koa.html
先简单使得服务器端返回json 数据。


# 10.24
遇到浏览器端不能跨域访问的问题。No 'Access-Control-Allow-Origin' header is present on the requested resource
index.js 是用Python搭的服务器，端口8001

node.js 使用koa 搭建，端口 3000


直接使用koa 搭建全套。
koa 使用模板文件，加上路由即可。使得某一路由对应json 解析。


# 10.25
可以正常通过 fetch + react 访问localhost 端口，
koa-route 正常实现 JSON API的功能，提供 json 数据返回。



如何在后端组装JSON 数据，请求时带参数。
url-api 即带参数，
在route 时即解析参数，并使用RPC调用远程函数。得到相应的新闻。

1.koa-route 实现url 参数解析
2.实现RPC 远程调用 实现简单的加法函数


# 10.26
使用Python 搭了一个rpc server
用 jayson 做了一个 client
单文件测试成功

# 10.31
前后端分离是怎么个分离法？
react 和 koa 是怎么运行起来的？

使用 node koa.js 然后后端的服务器就搭好了，前端有什么请求就渲染相应的页面。

使用Bash 做自动化的启动时，先是
node ./server/koa/04.js
然后会无法找到 template文件。应该是寻址问题。因为当前文件路径并不是 ./server/koa/
cd ./server/koa/
node 04.js 即可

下回任务materialize css 的样式设计。
滚动刷新的实现。

# 11.4
需要重新构建一下文件的结构。做一些顶层的设计方便后续的开发以及测试。零碎小模块太多。
create-react-app 与网页上直接手写react 代码的区别是？
代码的组织结构

了解到webpack .
webpack 是一个模块打包器。简单来说就是各种网站资源编译到整合到一起。网页服务器只用展示编译后的
文件即可。

使用npm install react 而不是直接应用编译后的react

前后端是如何运行的？如何运行一个react 网站？

# 11.17

create-react-app 将 babel,webpack 等都集合在一起了。并且，create-react-app 并没有假定
后端一定要使用 node.

前后端的运行：
方案A
前端占用一个端口，后端占用一个端口。后端其实只负责数据API，前端需要的不同数据通过不同的API接口
调用接口。koa/express等框架都只负责 API的数据以及路由即可咯。还有一些比如登陆
信息等数据的传递。

参考资料
create-react-app with a server
https://www.fullstackreact.com/articles/using-create-react-app-with-a-server/

# 11.18
感觉有一段时间没接着做，需要花点时间才能缓存之前的进度。这说明文档设计的不够好。应该做好顶层的设计
不断的细化。运用结构化得思维去设计整个体系，并记录好文档工作。
