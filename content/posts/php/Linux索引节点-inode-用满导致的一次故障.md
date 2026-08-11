---
title: "Linux索引节点(inode)用满导致的一次故障"
date: "2025-06-26 11:39:03"
slug: "linux-suo-yin-jie-dian-inode-yong-man-dao-zhi-de-yi-ci-gu-zhang"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/06/26/Linux索引节点(inode)用满导致的一次故障/"
  - "/2025/06/26/Linux索引节点(inode)用满导致的一次故障.html"
  - "/Linux索引节点(inode)用满导致的一次故障/"
  - "/Linux索引节点(inode)用满导致的一次故障.html"
  - "/2025/06/26/Linux索引节点-inode-用满导致的一次故障/"
  - "/2025/06/26/Linux索引节点-inode-用满导致的一次故障.html"
  - "/2025/06/26/linux-suo-yin-jie-dian-inode-yong-man-dao-zhi-de-yi-ci-gu-zhang/"
  - "/2025/06/26/linux-suo-yin-jie-dian-inode-yong-man-dao-zhi-de-yi-ci-gu-zhang.html"
  - "/linux-suo-yin-jie-dian-inode-yong-man-dao-zhi-de-yi-ci-gu-zhang.html"
---
之所以看到这篇文章也是自己出于好奇“inodes”,自己毕竟并非专业计算机出身，对这个不是很理解，但是知道这个东西也是需要空间，也是在容量满地时候，会倒是系统出现问题的。根据google的搜索，得到了张宴同志的一篇文章，如下：

一、发现问题：  
　　在一台配置较低的Linux服务器（内存、硬盘比较小）的/data分区内创建文件时，系统提示磁盘空间不足，用df -h命令查看了一下磁盘使用情况，发现/data分区只使用了66%，还有12G的剩余空间，按理说不会出现这种问题。  
二、分析问题：  
　　后来用df -i查看了一下/data分区的索引节点(inode)，发现已经用满(IUsed=100%)，导致系统无法创建新目录和文件。inode译成中文就是索引节点，每个存储设备（例如硬盘）或存储设备的分区被格式化为文件系统后，应该有两部份，一部份是inode，另一部份是Block，Block是用来存储数据用的。

而inode呢，就是用来存储这些数据的信息，这些信息包括文件大小、属主、归属的用户组、读写权限等。inode为每个文件进行信息索引，所以就有了inode的数值。

操作系统根据指令，能通过inode值最快的找到相对应的文件。而这台服务器的Block虽然还有剩余，但inode已经用满，因此在创建新目录或文件时，系统提示磁盘空间不足。

三、查找原因：

`/data/cache`目录中存在数量非常多的小字节缓存文件，占用的Block不多，但是占用了大量的inode。

四、解决方案：

> 　　1、删除`/data/cache`目录中的部分文件，释放出/data分区的一部分inode。  
>   
> 　　2、用软连接将空闲分区/opt中的newcache目录连接到/data/cache，使用/opt分区的inode来缓解/data分区inode不足的问题：  
> 　　`ln -s /opt/newcache /data/cache`
>   
> 　　3、更换服务器，用高配置的服务器替换低配置的服务器。很多时候用钱去解决问题比用技术更有效，堆在我办公桌上5台全新的 DELL PowerEdge 1950 服务器即将运往IDC机房。

---

参考文章：

http://blog.s135.com/post/295/

