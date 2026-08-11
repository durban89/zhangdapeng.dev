---
title: "wordpress 突然跳到安装界面 修复frm表的问题（idbdata1文件必须存在）"
date: "2025-06-25 10:26:47"
slug: "wordpress-tu-ran-tiao-dao-an-zhuang-jie-mian-xiu-fu-frm-biao-de-wen-ti-idbdata1-wen-jian-bi-xu-cun-zai"
categories: ["技术"]
tags: ["Wordpress"]
aliases:
  - "/2025/06/25/wordpress-突然跳到安装界面-修复frm表的问题（idbdata1文件必须存在）/"
  - "/2025/06/25/wordpress-突然跳到安装界面-修复frm表的问题（idbdata1文件必须存在）.html"
  - "/wordpress-突然跳到安装界面-修复frm表的问题（idbdata1文件必须存在）/"
  - "/wordpress-突然跳到安装界面-修复frm表的问题（idbdata1文件必须存在）.html"
  - "/2025/06/25/wordpress-突然跳到安装界面-修复frm表的问题-idbdata1文件必须存在/"
  - "/2025/06/25/wordpress-突然跳到安装界面-修复frm表的问题-idbdata1文件必须存在.html"
  - "/2025/06/25/wordpress-tu-ran-tiao-dao-an-zhuang-jie-mian-xiu-fu-frm-biao-de-wen-ti-idbdata1-wen-jia/"
  - "/2025/06/25/wordpress-tu-ran-tiao-dao-an-zhuang-jie-mian-xiu-fu-frm-biao-de-wen-ti-idbdata1-wen.html"
  - "/wordpress-tu-ran-tiao-dao-an-zhuang-jie-mian-xiu-fu-frm-biao-de-wen-ti-idbdata1-wen-jian-bi-xu.html"
---
朋友一网站使用wordpress搭建的，我很少使用这种东西，突然出现这种情况还真的很难找，因为要去理解什么逻辑实现要重新安装表的结构，很苦恼啊，最终google找到一篇文章说是wordpress使用的表都是innodb引擎，表损坏导致的，于是我打算修复一下，可以使用phpMyAdmin打开数据库发现只有库没有表了，经过一番的折腾我找到了几篇帖子，具体过程就是先新建一个表，然后在新建的表里面建立所有wordpress需要的表，建立完所有需要的表之后，关闭mysql

```bash
service mysql stop
```

修改mysql的配置文件

```bash
innodb_force_recovery = 4
```

然后将旧库里面的表的结果copy一份到新库，之后修改两个库的名字，将两个库的名字对调。然后启动数据库

```bash
service mysql start
```

看看数据库的表里面的数据吧，全部都回来了。嘿嘿

再次关闭mysql

```bash
service mysql stop
```

将

```bash
innodb_force_recovery = 4
```

注释掉

重新启动mysql

```bash
service mysql start
```

回复完毕。

之后想了想，是以为最近一次服务器空间满了，当时误以为是表坏了，又由于对数据库的不了解，本来只是删除ib\_logfile0和ib\_logfile1两个文件，结果删除后还是没有用，于是将ibdata1做了一个临时备份，还好没有删掉，今天按照上面的操作做了多次，最后是将ibdata1文件重新copy回来后，数据才回来的。因为新的ibdata1没有相关数据的点，找不到数据吧，所以如果没有或者ibdata1这个文件不是原来的是无法恢复数据的。

参考文章：

[使用 ibdata 和 frm 文件恢复 MySQL 数据库](http://cnzhx.net/blog/restore-mysql-from-ibdata-and-frm/)

[如何从IBData中恢复MySQL数据库](http://www.itpub.net/thread-740932-1-1.html)

[Mysql ibdata 丢失或损坏如何通过frm&ibd 恢复数据](http://www.lanceyan.com/tech/mysql/lost-ibdata-recover-data.html)

