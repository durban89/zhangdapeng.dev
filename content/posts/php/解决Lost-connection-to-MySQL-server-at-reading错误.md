---
title: "解决Lost connection to MySQL server at 'reading错误"
date: "2025-06-12 17:45:14"
slug: "jie-jue-lost-connection-to-mysql-server-at-reading-cuo-wu"
categories: ["技术"]
tags: ["MySQL"]
aliases:
  - "/2025/06/12/解决Lost-connection-to-MySQL-server-at-'reading错误/"
  - "/2025/06/12/解决Lost-connection-to-MySQL-server-at-'reading错误.html"
  - "/解决Lost-connection-to-MySQL-server-at-'reading错误/"
  - "/解决Lost-connection-to-MySQL-server-at-'reading错误.html"
  - "/2025/06/12/解决Lost-connection-to-MySQL-server-at-reading错误/"
  - "/2025/06/12/解决Lost-connection-to-MySQL-server-at-reading错误.html"
  - "/2025/06/12/jie-jue-lost-connection-to-mysql-server-at-reading-cuo-wu/"
  - "/2025/06/12/jie-jue-lost-connection-to-mysql-server-at-reading-cuo-wu.html"
  - "/jie-jue-lost-connection-to-mysql-server-at-reading-cuo-wu.html"
---
当通过 TCP/IP 连接 MySQL 远程主机时，出现 `ERROR 2013 (HY000): Lost connection to MySQL server at 'reading initial communication packet', system error: 104 `。

如果是在linux shell命令行中直接打 mysql 命令，能够顺利连上 MySQL，执行查询语句也比较正常，但如果执行 STOP SLAVE; 命令时就随机出现 `ERROR 2013 (HY000): Lost connection to MySQL server during query` 问题。而如果把操作命令写到脚本文件再去执行该脚本文件的话，则必然出现 `Lost connection to MySQL server at 'reading initial communication packet', system error: 111`

要是无论通过什么途径远程访问都出现错误可以认为是系统有防火墙之类的限制，但现在这种奇怪的抽筋现象让人百思不得其解。最后找到的解决方法是在 `my.cnf` 里面的 `[mysqld]` 段增加一个启动参数`skip-name-resolve` 问题消失。但原因还是想不出所以然。  
  
产生的原因是 my.cnf 中我设置了 `skip-name-resolve`，`skip-name-resolve`是禁用dns解析，所以在mysql的授权表中就不能使用主机名了，只能使用IP 。
