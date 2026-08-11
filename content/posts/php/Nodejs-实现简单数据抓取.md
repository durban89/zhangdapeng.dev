---
title: "Nodejs 实现简单数据抓取"
date: "2025-06-30 14:31:16"
slug: "nodejs-shi-xian-jian-dan-shu-ju-zhua-qu"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/Nodejs-实现简单数据抓取/"
  - "/2025/06/30/Nodejs-实现简单数据抓取.html"
  - "/Nodejs-实现简单数据抓取/"
  - "/Nodejs-实现简单数据抓取.html"
  - "/2025/06/30/nodejs-shi-xian-jian-dan-shu-ju-zhua-qu/"
  - "/2025/06/30/nodejs-shi-xian-jian-dan-shu-ju-zhua-qu.html"
  - "/nodejs-shi-xian-jian-dan-shu-ju-zhua-qu.html"
---
近期使用Nodejs，突然想起来以前做过数据抓取，于是为了练手，就开始了数据抓取的旅程，结果在网上搜索，已经有人在做了，于是就抄袭了一下，修改了一下，结果就出来自己的东西了，顺便加上了数据库的数据存储，这里使用的是mysql，为了使得能与自己的服务器想兼容，就没有去折腾其他的数据库了。在这里重点说一下定时任务，Nodejs有自己的Crontab哦，测试了一下，目前还没有发现什么问题。想要使用的可以直接执行安装命令

```bash
sudo cnpm install cron
```

代码我放在了git.oschina.net。懒得在写代码了，喜欢的可以去代码查看，我认为那里看代码更方便一点。代码如下：


