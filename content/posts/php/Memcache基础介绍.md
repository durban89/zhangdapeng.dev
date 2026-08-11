---
title: "Memcache基础介绍"
date: "2025-06-09 16:22:04"
slug: "memcache-ji-chu-jie-shao"
categories: ["技术"]
tags: ["Memcache"]
aliases:
  - "/2025/06/09/Memcache基础介绍/"
  - "/2025/06/09/Memcache基础介绍.html"
  - "/Memcache基础介绍/"
  - "/Memcache基础介绍.html"
  - "/2025/06/09/memcache-ji-chu-jie-shao/"
  - "/2025/06/09/memcache-ji-chu-jie-shao.html"
  - "/memcache-ji-chu-jie-shao.html"
---
memcached 是以LiveJournal 旗下Danga Interactive 公司的Brad Fitzpatric 为首开发的一款软件。现在已成为 mixi、 hatena、 Facebook、 Vox、LiveJournal等众多服务中 提高Web应用扩展性的重要因素。

许多Web应用都将数据保存到RDBMS中，应用服务器从中读取数据并在浏览器中显示。 但随着数据量的增大、访问的集中，就会出现RDBMS的负担加重、数据库响应恶化、 网站显示延迟等重大影响。

这时就该memcached大显身手了。memcached是高性能的分布式内存缓存服务器。 一般的使用目的是，通过缓存数据库查询结果，减少数据库访问次数，以提高动态Web应用的速度、 提高可扩展性。

 

### [memcached的特征](#1)

memcached作为高速运行的分布式缓存服务器，具有以下的特点。

1. 协议简单
2. 基于libevent的事件处理
3. 内置内存存储方式
4. memcached不互相通信的分布式

#### [协议简单](#11)

memcached的服务器客户端通信并不使用复杂的XML等格式， 而使用简单的基于文本行的协议。因此，通过telnet 也能在memcached上保存数据、取得数据。下面是例子。

```shell
$ telnet localhost 11211
Trying 127.0.0.1...
Connected to localhost.localdomain (127.0.0.1).
Escape character is '^]'.
set foo 0 0 3     （保存命令）
bar               （数据）
STORED            （结果）
get foo           （取得命令）
VALUE foo 0 3     （数据）
bar               （数据）
```

协议文档位于memcached的源代码内，也可以参考以下的URL。

http://code.sixapart.com/svn/memcached/trunk/server/doc/protocol.txt

#### [基于libevent的事件处理](#12)

libevent是个程序库，它将Linux的epoll、BSD类操作系统的kqueue等事件处理功能 封装成统一的接口。即使对服务器的连接数增加，也能发挥O(1)的性能。 memcached使用这个libevent库，因此能在Linux、BSD、Solaris等操作系统上发挥其高性能。 可以参考Dan Kegel的The C10K Problem。

libevent: http://www.monkey.org/~provos/libevent/
The C10K Problem: http://www.kegel.com/c10k.html

#### [内置内存存储方式](#13)

为了提高性能，memcached中保存的数据都存储在memcached内置的内存存储空间中。 由于数据仅存在于内存中，因此重启memcached、重启操作系统会导致全部数据消失。 另外，内容容量达到指定值之后，就基于LRU(Least Recently Used)算法自动删除不使用的缓存。 memcached本身是为缓存而设计的服务器，因此并没有过多考虑数据的永久性问题。

#### [memcached不互相通信的分布式](#14)

memcached尽管是“分布式”缓存服务器，但服务器端并没有分布式功能。 各个memcached不会互相通信以共享信息。那么，怎样进行分布式呢？ 这完全取决于客户端的实现。

接下来简单介绍一下memcached的使用方法。

### [安装memcached](#2)

memcached的安装比较简单，这里稍加说明。

memcached支持许多平台。 * Linux * FreeBSD * Solaris (memcached 1.2.5以上版本) * Mac OS X

另外也能安装在Windows上。这里使用Fedora Core 8进行说明。

memcached的安装
运行memcached需要本文开头介绍的libevent库。Fedora 8中有现成的rpm包， 通过yum命令安装即可。

`$ sudo yum install libevent libevent-devel`

memcached的源代码可以从memcached网站上下载。本文执笔时的最新版本为1.2.5。 Fedora 8虽然也包含了memcached的rpm，但版本比较老。因为源代码安装并不困难， 这里就不使用rpm了。

下载memcached：http://www.danga.com/memcached/download.bml

memcached安装与一般应用程序相同，configure、make、make install就行了。

```shell
$ wget http://www.danga.com/memcached/dist/memcached-1.2.5.tar.gz
$ tar zxf memcached-1.2.5.tar.gz
$ cd memcached-1.2.5
$ ./configure
$ make
$ sudo make install
```

默认情况下memcached安装到/usr/local/bin下。

### [memcached的启动](#3)

从终端输入以下命令，启动memcached。

```shell
$ /usr/local/bin/memcached -p 11211 -m 64m -vv
slab class   1: chunk size     88 perslab 11915
slab class   2: chunk size    112 perslab  9362
slab class   3: chunk size    144 perslab  7281

中间省略...

slab class  38: chunk size 391224 perslab     2
slab class  39: chunk size 489032 perslab     2
<23 server listening
<24 send buffer was 110592, now 268435456
<24 server listening (udp)
<24 server listening (udp)
<24 server listening (udp)
<24 server listening (udp)
```

这里显示了调试信息。这样就在前台启动了memcached，监听TCP端口11211 最大内存使用量为64M。

作为daemon后台启动时，只需

```shell
$ /usr/local/bin/memcached -p 11211 -m 64m -d
```

这里使用的memcached启动选项的内容如下。

>选项  说明
>-p  使用的TCP端口。默认为11211
>-m  最大内存大小。默认为64M
>-vv 用very vrebose模式启动，调试信息和错误输出到控制台
>-d  作为daemon在后台启动

上面四个是常用的启动选项，其他还有很多，通过

```shell
$ /usr/local/bin/memcached -h
```
命令可以显示。许多选项可以改变memcached的各种行为， 推荐读一读。
