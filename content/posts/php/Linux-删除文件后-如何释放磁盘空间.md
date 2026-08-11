---
title: "Linux 删除文件后，如何释放磁盘空间"
date: "2025-07-01 15:24:44"
slug: "linux-shan-chu-wen-jian-hou-ru-he-shi-fang-ci-pan-kong-jian"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/07/01/Linux-删除文件后，如何释放磁盘空间/"
  - "/2025/07/01/Linux-删除文件后，如何释放磁盘空间.html"
  - "/Linux-删除文件后，如何释放磁盘空间/"
  - "/Linux-删除文件后，如何释放磁盘空间.html"
  - "/2025/07/01/Linux-删除文件后-如何释放磁盘空间/"
  - "/2025/07/01/Linux-删除文件后-如何释放磁盘空间.html"
  - "/2025/07/01/linux-shan-chu-wen-jian-hou-ru-he-shi-fang-ci-pan-kong-jian/"
  - "/2025/07/01/linux-shan-chu-wen-jian-hou-ru-he-shi-fang-ci-pan-kong-jian.html"
  - "/linux-shan-chu-wen-jian-hou-ru-he-shi-fang-ci-pan-kong-jian.html"
---
关于磁盘空间会有一个问题就是磁盘空间满了，但是删除对应的文件后【你删除的没有错误】 ，通过

```bash
du -h --max-depth=1
```

查看后

```bash
16K    ./lost+found
26M    ./test.zhidetou.net
88K    ./spider
62M    ./mocker.qeeniao.com
4.6M    ./www.zhidetou.net
12G    ./elasticsearch
12G    .
```

这里显示是12G啦，总磁盘大小是20G，也应该是60%  
发现文件是减少了，但是df -h 发现还是没有减少。

```bash
Filesystem      Size  Used Avail Use% Mounted on
/dev/xvda1       20G   11G  8.1G  57% /
tmpfs           1.9G     0  1.9G   0% /dev/shm
/dev/xvdb1       20G   15G  3.7G  81% /data
```

仍然是81%  
原因就是因为某个程序还在占用此文件，文件句柄没有释放，所以即使你rm -rf磁盘空间也不会被释放。  
解决办法就是找到使用这个文件的进程，然后重启或者是直接kill掉后，再重启对应进程。


