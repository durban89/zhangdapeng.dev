---
title: "记一次CentOS 8安装完mosh后locale问题"
date: "2025-07-11 10:28:37"
slug: "ji-yi-ci-centos-8-an-zhuang-wan-mosh-hou-locale-wen-ti"
categories: ["技术"]
tags: ["CentOS"]
aliases:
  - "/2025/07/11/记一次CentOS-8安装完mosh后locale问题/"
  - "/2025/07/11/记一次CentOS-8安装完mosh后locale问题.html"
  - "/记一次CentOS-8安装完mosh后locale问题/"
  - "/记一次CentOS-8安装完mosh后locale问题.html"
  - "/2025/07/11/ji-yi-ci-centos-8-an-zhuang-wan-mosh-hou-locale-wen-ti/"
  - "/2025/07/11/ji-yi-ci-centos-8-an-zhuang-wan-mosh-hou-locale-wen-ti.html"
  - "/ji-yi-ci-centos-8-an-zhuang-wan-mosh-hou-locale-wen-ti.html"
---
事情是这样子的，之前一直使用linode的服务器，但是这家伙隔几天就给我发个信息说是物理磁盘在干什么事情，然后我的服务器就挂了，好赖也通知我了，但是经不起你这么折腾呀，一个月搞了我好几次，我一个小小站长，做个博客本来就不容易，还没事来搞我，于是一气之下放弃了linode。

转而看了许多，最后选择[vultr.com](https://www.vultr.com/?ref=8386777-6G)，让我意外的发现，vultr支持的支付方式还是满多的，大喜

随后选了好几个区的服务器，试了好几个，都不太理想，毕竟国外的快的也都被商家玩坏了，好的吧也就慢一些，真的就是慢一些吗？我不信

我还是选择了日本的，毕竟是在亚洲，如果中国访问不了，亚洲其他的区还是可以访问的，比如香港、台湾等

而且如果哪天路线畅通了，还是比较快的，另外我为什么不选择香港，我只能说点不公道的话了，为什么人家国外的便宜，就买香港的大陆的都会贵个10几块钱呢。

本来就不容易为啥还要搞我们呢，其实不针对你，放弃这种想法吧，要从国家策略着想。

接下来配置服务器，不小心选择了Centos 8，在模糊的不知道是几的情况下，反正基本部署完了，部署完才发现是Centos 8.

接下来使用mosh登录后，提示如下信息

```bash
The locale requested by LANG=zh_CN.UTF-8 isn't available here.
Running `locale-gen zh_CN.UTF-8' may be necessary.

mosh-server needs a UTF-8 native locale to run.

Unfortunately, the local environment ([no charset variables]) specifies
the character set "US-ASCII",

The client-supplied environment (LANG=zh_CN.UTF-8) specifies
the character set "US-ASCII".

locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
LANG=zh_CN.UTF-8
LC_CTYPE="zh_CN.UTF-8"
LC_NUMERIC="zh_CN.UTF-8"
LC_TIME="zh_CN.UTF-8"
LC_COLLATE="zh_CN.UTF-8"
LC_MONETARY="zh_CN.UTF-8"
LC_MESSAGES="zh_CN.UTF-8"
LC_PAPER="zh_CN.UTF-8"
LC_NAME="zh_CN.UTF-8"
LC_ADDRESS="zh_CN.UTF-8"
LC_TELEPHONE="zh_CN.UTF-8"
LC_MEASUREMENT="zh_CN.UTF-8"
LC_IDENTIFICATION="zh_CN.UTF-8"
LC_ALL=
```

执行命令

```bash
locale-gen zh_CN.UTF-8
```

提示你

```bash
command not found: locale-gen
```

网上很多copy来copy去的帖子，都是一路的，看一遍差不多也就够了，基本上没啥解决的方案，因为都是CentOS 8之前的系统的帖子

截止今天，好像CentOS 8系统的普及还不是很多，反正在vultr.com上是没有具体的使用指南的。

我说下我是怎么解决的吧，可能能帮到你

```bash
sudo yum search Chinese
```

找到这个`langpacks-zh_CN.noarch`名的包，然后执行

```bash
sudo yum install langpacks-zh_CN
```

再然后执行

```bash
localedef -c -f UTF-8 -i zh_CN zh_CN.UTF-8
```

修改下`~/.bashrc`，添加如下代码

```bash
export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
```

不过我觉得好像不需要，其实就是少安装了中文支持的包，也许你遇到的并不是这最基础的没有安装支持包的问题。
