---
title: "Wordpress版本的手动升级步骤"
date: "2025-06-24 15:29:33"
slug: "wordpress-ban-ben-de-shou-dong-sheng-ji-bu-zhou"
categories: ["技术"]
tags: ["Wordpress"]
aliases:
  - "/2025/06/24/Wordpress版本的手动升级步骤/"
  - "/2025/06/24/Wordpress版本的手动升级步骤.html"
  - "/Wordpress版本的手动升级步骤/"
  - "/Wordpress版本的手动升级步骤.html"
  - "/2025/06/24/wordpress-ban-ben-de-shou-dong-sheng-ji-bu-zhou/"
  - "/2025/06/24/wordpress-ban-ben-de-shou-dong-sheng-ji-bu-zhou.html"
  - "/wordpress-ban-ben-de-shou-dong-sheng-ji-bu-zhou.html"
---
最近在看看Wordpress的模板开发，在后台遇到了一个问题就是要升级，但是我的是虚拟机，所以无法试下ftp，至少我现在还木有找到实现的方法。再者就是自己的网络慢，还是先下载之后进行手动升级吧。

下面给出手动升级的步骤，希望对大家有些作用。

### [第一步、备份程序文件和数据库](#1)

不备份升级后出现问题的可能性也不大，但是为了以防万一还是备份一下吧，养成个好习惯也少后悔。

### [第二步、登录后台关闭所有插件](#2)

网友提醒补充的一条，升级的时候别忘了哦。

### [第三步、下载最新wordpress安装包](#3)

这个就简单了，cn.wordpress.org去下。

### [第四步、解压安装包更新数据](#4)

将网站根目录下wp-admin和wp-includes两个目录中的文件换成最新下载的程序文件，我都是将原来的文件删除后再拷贝新文件进去，直接覆盖也可以（直接覆盖有些工具会弄不全），随便你了。

### [第五步、更新根目录下除wp-config.php文件以外的文件](#5)

wp-config.php文件是wp配置文件，包括数据库连接设置等，所以千万不要把此文件删除了。另外wp-content文件夹内的内容不用更改，这里面放的是主题文件，插件文件等，不在升级范围内，运行http://你的博客地址/wp-admin/upgrade.php ，将你的博客地址填入路径中执行升级程序。

整个环节下来，其实是很简单的，ok啦，其实说实话，Wordpress升级很简单的。

