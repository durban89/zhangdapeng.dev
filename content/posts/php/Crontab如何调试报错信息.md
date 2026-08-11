---
title: "Crontab如何调试报错信息"
date: "2025-07-03 11:59:06"
slug: "crontab-ru-he-tiao-shi-bao-cuo-xin-xi"
categories: ["技术"]
tags: ["Crontab"]
aliases:
  - "/2025/07/03/Crontab如何调试报错信息/"
  - "/2025/07/03/Crontab如何调试报错信息.html"
  - "/Crontab如何调试报错信息/"
  - "/Crontab如何调试报错信息.html"
  - "/2025/07/03/crontab-ru-he-tiao-shi-bao-cuo-xin-xi/"
  - "/2025/07/03/crontab-ru-he-tiao-shi-bao-cuo-xin-xi.html"
  - "/crontab-ru-he-tiao-shi-bao-cuo-xin-xi.html"
---
看下面这个crontab

```bash
* * * * * /usr/bin/python /home/zhangdapeng/del.py > /dev/null 2>&1
```

一般的比较安全的，无困扰的情况下是这样的

但是调试很不方便，报错了，不知道为啥报错了，找不到原因，改一下

```bash
* * * * * /usr/bin/python /home/zhangdapeng/del.py > /path/result.log 2>&1
```

这样的话就能在result.log知道原因了。


