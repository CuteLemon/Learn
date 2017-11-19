# Learn

一键运行
bash auto.sh

本项目是为了练习各种技术栈。
Python/nodejs/react/rabbitmq/TensorFlow/MachineLearning


根据bitiger的图纸制造的。bitiger 链接

一个类似今日头条的新闻应用。有以下几个有趣的点：
1. 新闻数据的获取通过Python调用API接口来获得，处理的数据会放入MongoDB中存储。
2. 前端使用react制作，即一个可以不断下拉刷新的App,由于使用materializeCSS，手机和网页端都能很好适配。
3. 后端采用koa 主要负责数据API，
4. 采用RPC 进行微服务的架构设计
5. 新闻去重，采用简单的向量化方法，设定一定的相似度阈值。
6. 推荐系统 采用TensorFlow 根据用户对新闻的反馈来推荐合适的内容。初期冷启动采用分类推荐的办法，
即推荐用户系统的新闻类别。

基础功能
下拉刷新新闻，记录用户行为数据。

进阶功能
新闻去重与推荐



如何运行
git clone

运行条件
npm node python
