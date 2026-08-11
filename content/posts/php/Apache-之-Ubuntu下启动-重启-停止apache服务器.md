---
title: "Apache 之 Ubuntu下启动/重启/停止apache服务器"
date: "2025-06-26 11:16:00"
slug: "apache-zhi-ubuntu-xia-qi-dong-chong-qi-ting-zhi-apache-fu-wu-qi"
categories: ["技术"]
tags: ["Apache", "Ubuntu"]
aliases:
  - "/2025/06/26/Apache-之-Ubuntu下启动/重启/停止apache服务器/"
  - "/2025/06/26/Apache-之-Ubuntu下启动/重启/停止apache服务器.html"
  - "/Apache-之-Ubuntu下启动/重启/停止apache服务器/"
  - "/Apache-之-Ubuntu下启动/重启/停止apache服务器.html"
  - "/2025/06/26/Apache-之-Ubuntu下启动-重启-停止apache服务器/"
  - "/2025/06/26/Apache-之-Ubuntu下启动-重启-停止apache服务器.html"
  - "/2025/06/26/apache-zhi-ubuntu-xia-qi-dong-chong-qi-ting-zhi-apache-fu-wu-qi/"
  - "/2025/06/26/apache-zhi-ubuntu-xia-qi-dong-chong-qi-ting-zhi-apache-fu-wu-qi.html"
  - "/apache-zhi-ubuntu-xia-qi-dong-chong-qi-ting-zhi-apache-fu-wu-qi.html"
---
一直不想使用Apache，因为我周边的人觉得不好，我也觉得既然别人说的不好，也就没有尝试的必要，但是由于其普遍性，在帮别人做项目的时候，还是需要使用一下的Apache的，这里简单的记录一下，Apache的启动和停止的命令操作。

Task: Start Apache 2 Server /启动apache服务

```bash
# /etc/init.d/apache2 start
```

or

```bash
$ sudo /etc/init.d/apache2 start
```

Task: Restart Apache 2 Server /重启apache服务

```bash
# /etc/init.d/apache2 restart
```

or

```bash
$ sudo /etc/init.d/apache2 restart
```

Task: Stop Apache 2 Server /停止apache服务

```bash
# /etc/init.d/apache2 stop
```

or

```bash
$ sudo /etc/init.d/apache2 stop
```

---

参考文章:

http://bbs.phpchina.com/home.php?mod=space&uid=3950&do=blog&id=48934

