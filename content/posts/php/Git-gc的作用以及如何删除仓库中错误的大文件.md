---
title: "Git gc的作用以及如何删除仓库中错误的大文件"
date: "2025-07-14 14:45:18"
slug: "git-gc-de-zuo-yong-yi-ji-ru-he-shan-chu-cang-ku-zhong-cuo-wu-de-da-wen-jian"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/07/14/Git-gc的作用以及如何删除仓库中错误的大文件/"
  - "/2025/07/14/Git-gc的作用以及如何删除仓库中错误的大文件.html"
  - "/Git-gc的作用以及如何删除仓库中错误的大文件/"
  - "/Git-gc的作用以及如何删除仓库中错误的大文件.html"
  - "/2025/07/14/git-gc-de-zuo-yong-yi-ji-ru-he-shan-chu-cang-ku-zhong-cuo-wu-de-da-wen-jian/"
  - "/2025/07/14/git-gc-de-zuo-yong-yi-ji-ru-he-shan-chu-cang-ku-zhong-cuo-wu-de-da-wen-jian.html"
  - "/git-gc-de-zuo-yong-yi-ji-ru-he-shan-chu-cang-ku-zhong-cuo-wu-de-da-wen-jian.html"
---
之前对`gc`一直不了解，这玩意是个bug吧

为什么`git pull`的时候会出现一个`git gc`的命令，还提示我可以自己运行

回忆下，第一次遇到这个问题的时候就是这个状态，然后就一直没理会

最近测试服务器部署代码的时候，经常会遇到这个命令在执行

于是搜搜了下，才发现这个命令是对大文件进行压缩的

同时如果出现这个命令的执行或者提示你让你去执行这个gc的命令

说明你的项目真的很大了

或者说明你的项目存在非常大的文件

原理就是压缩了下，创建了一个包文件和一个索引文件，方便后面更快的对文件的更改进行对比（`diff`）操作，不然文件很大的话读取再对比其实是很慢的，这样可以理解的通透了

另外需要对git的原理有更多的理解

就是我们每次对一个文件进行更改的时候`git`都会生成一个全新的对象来存储新的文件内容。

推荐一篇文章，[点这里](https://www.jianshu.com/p/7231b509c279)，具体介绍了如何删除大文件，同时对`git gc`有更详细的了解
