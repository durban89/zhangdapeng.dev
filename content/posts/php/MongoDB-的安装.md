---
title: "MongoDB 的安装"
date: "2025-06-24 14:46:15"
slug: "mongodb-de-an-zhuang"
categories: ["技术"]
tags: ["MongoDB"]
aliases:
  - "/2025/06/24/MongoDB-的安装/"
  - "/2025/06/24/MongoDB-的安装.html"
  - "/MongoDB-的安装/"
  - "/MongoDB-的安装.html"
  - "/2025/06/24/mongodb-de-an-zhuang/"
  - "/2025/06/24/mongodb-de-an-zhuang.html"
  - "/mongodb-de-an-zhuang.html"
---
## [Ubuntu 12.04 LTS环境：](#1)

第一步：下载

下载地址：<http://fastdl.mongodb.org/linux/mongodb-linux-i686-2.4.6.tgz>

```bash
wget http://fastdl.mongodb.org/linux/mongodb-linux-i686-2.4.6.tgz
```

第二步：解压

```bash
tar -zxvf ./mongodb-linux-i686-2.4.6.tgz 
cd mongodb-linux-i686-2.4.6/bin
cp ./* /usr/local/bin
```

安装完毕

第三步：MongoDB部署

```bash
sudo mkdir /var/lib/mongodb
```

配置mongod.conf

```bash
fork = true
bind_ip = 127.0.0.1
port = 27017
quiet = true
dbpath = /srv/mongodb
logpath = /var/log/mongodb/mongod.log
logappend = true
journal = false
```

创建日志目录：

```bash
sudo mkdir /var/log/mongodb
```

开启进程

```bash
sudo /usr/local/bin/mongod --config /etc/mongodb.conf
```

如果有这个提示：

> about to fork child process, waiting until server is ready for connections.
>
> forked process: 11159
>
> all output going to: /var/log/mongodb/mongod.log
>
> child process started successfully, parent exiting

表示安装成功。

尝试一下登陆

```bash
xx@xx:~$ mongo
MongoDB shell version: 2.4.6
connecting to: test
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
http://docs.mongodb.org/
Questions? Try the support group
http://groups.google.com/group/mongodb-user
Server has startup warnings: 
Tue Oct 15 12:42:00.747 [initandlisten] 
Tue Oct 15 12:42:00.747 [initandlisten] ** NOTE: This is a 32 bit MongoDB binary.
Tue Oct 15 12:42:00.747 [initandlisten] **       32 bit builds are limited to less than 2GB of data (or less with --journal).
Tue Oct 15 12:42:00.747 [initandlisten] **       See http://dochub.mongodb.org/core/32bit
Tue Oct 15 12:42:00.748 [initandlisten] 
>
```

---

## [CentOS release 6.4 (Final)环境：](#2)

第一步：下载

下载地址：<http://fastdl.mongodb.org/linux/mongodb-linux-i686-2.4.6.tgz>

```bash
wget http://fastdl.mongodb.org/linux/mongodb-linux-i686-2.4.6.tgz
```

第二步：解压

```bash
tar -zxvf ./mongodb-linux-i686-2.4.6.tgz 
cd mongodb-linux-i686-2.4.6/bin
cp ./* /usr/local/bin
```

安装完毕

第三步：MongoDB部署

```bash
sudo mkdir /var/lib/mongodb
```

配置mongod.conf

```bash
fork = true
bind_ip = 127.0.0.1
port = 27017
quiet = true
dbpath = /srv/mongodb
logpath = /var/log/mongodb/mongod.log
logappend = true
journal = false
```

创建日志目录：

```bash
sudo mkdir /var/log/mongodb
```

开启进程

```bash
sudo /usr/local/bin/mongod --config /etc/mongodb.conf
```

如果有这个提示：

> about to fork child process, waiting until server is ready for connections.
>
> forked process: 11159
>
> all output going to: /var/log/mongodb/mongod.log
>
> child process started successfully, parent exiting

表示安装成功。

尝试一下登陆

```bash
[davidzhang@colud mongodb]$ mongo
MongoDB shell version: 2.4.6
connecting to: test
Welcome to the MongoDB shell.
For interactive help, type "help".
For more comprehensive documentation, see
http://docs.mongodb.org/
Questions? Try the support group
http://groups.google.com/group/mongodb-user
Server has startup warnings: 
Tue Oct 15 12:51:13.884 [initandlisten] 
Tue Oct 15 12:51:13.884 [initandlisten] ** NOTE: This is a 32 bit MongoDB binary.
Tue Oct 15 12:51:13.884 [initandlisten] **       32 bit builds are limited to less than 2GB of data (or less with --journal).
Tue Oct 15 12:51:13.884 [initandlisten] **       Note that journaling defaults to off for 32 bit and is currently off.
Tue Oct 15 12:51:13.884 [initandlisten] **       See http://dochub.mongodb.org/core/32bit
Tue Oct 15 12:51:13.884 [initandlisten] 
>
```

参考文章：

<http://f.dataguru.cn/thread-107361-1-1.html>

<http://docs.mongodb.org/manual/reference/configuration-options/>

<http://docs.mongodb.org/manual/tutorial/install-mongodb-on-linux/>

<http://docs.mongodb.org/manual/administration/configuration/>

<http://www.cnblogs.com/TankMa/archive/2011/06/08/2074947.html>

