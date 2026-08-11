---
title: "Ubuntu 12.04 LTS 安装 postgresql-9.3.1 全过程"
date: "2025-06-24 14:45:57"
slug: "ubuntu-1204-lts-an-zhuang-postgresql-931-quan-guo-cheng"
categories: ["技术"]
tags: ["PostgreSQL", "Ubuntu", "Linux"]
aliases:
  - "/2025/06/24/Ubuntu-12.04-LTS-安装-postgresql-9.3.1-全过程/"
  - "/2025/06/24/Ubuntu-12.04-LTS-安装-postgresql-9.3.1-全过程.html"
  - "/Ubuntu-12.04-LTS-安装-postgresql-9.3.1-全过程/"
  - "/Ubuntu-12.04-LTS-安装-postgresql-9.3.1-全过程.html"
  - "/2025/06/24/ubuntu-1204-lts-an-zhuang-postgresql-931-quan-guo-cheng/"
  - "/2025/06/24/ubuntu-1204-lts-an-zhuang-postgresql-931-quan-guo-cheng.html"
  - "/ubuntu-1204-lts-an-zhuang-postgresql-931-quan-guo-cheng.html"
---
我的安装是源码安装，

首先下载postgresql

下载地址：<http://www.postgresql.org/download/linux/ubuntu/>

我下载的是postgresql-9.3.1这个版本的

下载回来后直接解压

```bash
tar -zxvf postgresql-9.3.1.tar.gz
cd postgresql-9.3.1
```

执行下面指令：

```bash
./configure
```

这里有时候会遇到问题，我这里出现了下面这个错误提示

> configure: error: readline library not found  
> If you have readline already installed, see config.log for details on the  
> failure.  It is possible the compiler isnt looking in the proper directory.  
> Use --without-readline to disable readline support.

经过我的半天的 折腾我终于找到了一个方法。

第一步：更新Ubuntu的源

去这里[源列表](http://wiki.ubuntu.org.cn/%E6%BA%90%E5%88%97%E8%A1%A8)，这里有更新源的方法，按照操作找到速度最快的源(在这里我选择的是***网易163更新服务器***)，然后修改source.list

```bash
sudo vi /etc/source.list
```

执行下面的指令：

```bash
sudo apt-get update
```

执行完之后，执行命令：

```bash
sudo apt-get install libreadline5-dev
```

会安装完我们需要的readline

然后再执行下面指令：

```bash
./configure
make
make install
```

最后会提示

PostgreSQL installation complete.

说明安装成功了。

参考文章：

<http://wiki.ubuntu.org.cn/PostgreSQL>

<http://www.postgresql.org/download/linux/ubuntu/>

<http://wiki.ubuntu.org.cn/PostgreSQL>

<http://blog.csdn.net/wypblog/article/details/6863342>

<http://blog.chinaunix.net/uid-23242876-id-2480272.html>

<http://wiki.ubuntu.org.cn/%E6%BA%90%E5%88%97%E8%A1%A8>

