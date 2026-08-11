---
title: "MariaDB使用记录"
date: "2025-07-15 10:29:12"
slug: "mariadb-shi-yong-ji-lu"
categories: ["技术"]
tags: ["MariaDB"]
aliases:
  - "/2025/07/15/MariaDB使用记录/"
  - "/2025/07/15/MariaDB使用记录.html"
  - "/MariaDB使用记录/"
  - "/MariaDB使用记录.html"
  - "/2025/07/15/mariadb-shi-yong-ji-lu/"
  - "/2025/07/15/mariadb-shi-yong-ji-lu.html"
  - "/mariadb-shi-yong-ji-lu.html"
---
### 前提条件

安装的版本

> mariadb-5.5.68-linux-systemd-x86\_64.tar.gz

由于最新的mysql不再适合我的古老项目，也没有升级，服务器上部署的是mysql5.7，本机器是ubuntu 22.04，apt安装的话的是mysql 8.0，降低版本安装暂时没有找到好的办法  
而且想试试mariadb于是就搞了一个，其实把这种东西看作是软件就好了，毕竟这个报下载下来我就执行能运行了，不用再安装其他的依赖了。

安装解压后按照文件夹中INSTALL-BINARY进行安装使用就好了

### 配置文件修改

以前没注意，安装我看了下/etc/mysql目录，居然有这么多好东西

```bash
$ ll /etc/mysql     
总计 32K
drwxr-xr-x 2 root root 4.0K 10月 19 13:34 conf.d
-rw------- 1 root root  317  3月 14 09:35 debian.cnf
-rwxr-xr-x 1 root root  120  1月 28 22:44 debian-start
-rw-r--r-- 1 root root 1.1K  3月 15 18:15 mariadb.cnf
drwxr-xr-x 2 root root 4.0K  6月 17  2022 mariadb.conf.d
lrwxrwxrwx 1 root root   24 10月 19 13:34 my.cnf -> /etc/alternatives/my.cnf
-rw-r--r-- 1 root root  839 10月 20  2020 my.cnf.fallback
-rw-r--r-- 1 root root  682  3月 11  2021 mysql.cnf
drwxr-xr-x 2 root root 4.0K  3月 14 09:35 mysql.conf.d
```

然后我就改了mariadb.cnf

```bash
port = 3307
socket = /run/mysqld/mysqld.sock
```

主要是这两项，端口3307是为了跟mysql 8.0启动的端口做个区分

### 启动方式

```bash
cd /usr/local/mysql
sudo ./support-files/mysql.server start
```

启动后

```bash
mysql     120523       1  0 14:39 ?        00:00:05 /usr/sbin/mysqld
root      121333       1  0 14:42 ?        00:00:00 /bin/sh /usr/local/mysql/bin/mysqld_safe --datadir=/usr/local/mysql/data --pid-file=/usr/local/mysql/data/durban-workspace.pid
mysql     121464  121333  0 14:42 ?        00:00:00 /usr/local/mysql/bin/mysqld --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data --plugin-dir=/usr/local/mysql/lib/plugin --user=mysql --log-error=/usr/local/mysql/data/durban-workspace.err --pid-file=/usr/local/mysql/data/durban-workspace.pid --socket=/run/mysqld/mysqld.sock --port=3307
```

奇怪的是如何用起来 mariadb.cnf 这个配置文件的 我看了./support-files/mysql.server其实是使用的/etc/mysql/my.cnf

原来是软链接过去的

```bash
my.cnf -> /etc/alternatives/my.cnf
/etc/alternatives/my.cnf -> /etc/mysql/mariadb.cnf
```

这个操作没搞懂，不过不记得了，应该是在安装mariadb的时候操作的，具体细节忘记留意了
