---
title: "SVN 提交的时候提示'No space left on device'"
date: "2025-06-26 11:16:04"
slug: "svn-ti-jiao-de-shi-hou-ti-shi-no-space-left-on-device"
categories: ["技术"]
tags: ["SVN"]
aliases:
  - "/2025/06/26/SVN-提交的时候提示'No-space-left-on-device'/"
  - "/2025/06/26/SVN-提交的时候提示'No-space-left-on-device'.html"
  - "/SVN-提交的时候提示'No-space-left-on-device'/"
  - "/SVN-提交的时候提示'No-space-left-on-device'.html"
  - "/2025/06/26/SVN-提交的时候提示-No-space-left-on-device/"
  - "/2025/06/26/SVN-提交的时候提示-No-space-left-on-device.html"
  - "/2025/06/26/svn-ti-jiao-de-shi-hou-ti-shi-no-space-left-on-device/"
  - "/2025/06/26/svn-ti-jiao-de-shi-hou-ti-shi-no-space-left-on-device.html"
  - "/svn-ti-jiao-de-shi-hou-ti-shi-no-space-left-on-device.html"
---
第一次遇到一个比较奇怪的问题就是svn报了一个错误“No space left on device”，这个错误第一次遇到。看到这个错误，第一个反应是磁盘空间满了；但 df 一看，每个分区的空间都还富余的很。从 munin 的监控图表上看 Filesystem usage 也很平稳，但下面的 Inode usage 就有问题了，其中一个分区的 usage 已经到了100%。赶紧跑到服务器上 `df -i` 检查，果然是 Inode 耗尽。原来这个分区是用来扔各种日志和临时文件的，其中有某个程序产生的临时文件又小又多，又没有进行定时回滚，造成在磁盘空间耗尽之前文件系统的 Inode 就被用光了。超出系统中同时运行的最大 message queue 个数限制 ： 在 root 下用 `sysctl kernel.msgmni` 检查该参数，`sysctl -w kernel.msgmni=XXX` 重新设定即可。

我这边正在尝试，大家也可以尝试一下。

如果不起作用，可以重启一下svn。

---

参考文章：

http://www.cnblogs.com/xiaofan21/archive/2013/05/21/3090447.html

