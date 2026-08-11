---
title: "svn update报no such revision * 的解决办法"
date: "2025-06-27 09:45:52"
slug: "svn-update-bao-no-such-revision-de-jie-jue-ban-fa"
categories: ["技术"]
tags: ["SVN"]
aliases:
  - "/2025/06/27/svn-update报no-such-revision-*-的解决办法/"
  - "/2025/06/27/svn-update报no-such-revision-*-的解决办法.html"
  - "/svn-update报no-such-revision-*-的解决办法/"
  - "/svn-update报no-such-revision-*-的解决办法.html"
  - "/2025/06/27/SVN-update报no-such-revision-的解决办法/"
  - "/2025/06/27/SVN-update报no-such-revision-的解决办法.html"
  - "/2025/06/27/svn-update-bao-no-such-revision-de-jie-jue-ban-fa/"
  - "/2025/06/27/svn-update-bao-no-such-revision-de-jie-jue-ban-fa.html"
  - "/svn-update-bao-no-such-revision-de-jie-jue-ban-fa.html"
---
#### [出现问题的原因](#1)

1，版本库因断电等出错；这个通过svn verify来验证服务器是否有问题，如果验证么有错误，那么服务器需要版本修正，如果没有错误，则是客户端的问题；

2，客户端可能由于文件自动变化等原因等出现；具体不是非常清楚；

#### [解决的办法](#2)

a,checkout 一个版本库到临时文件夹`/tmp/`

b,复制`/tmp/`工作副本中的`.svn/`目录到正式工作目录

c, 在正式工作目录执行`svn update`，OK 了

---

参考文章：

http://www.myexception.cn/powerdesigner/549246.html

