---
title: "Linux 查看文件和文件夹大小的df和du命令"
date: "2025-06-23 15:49:18"
slug: "linux-cha-kan-wen-jian-he-wen-jian-jia-da-xiao-de-df-he-du-ming-ling"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/06/23/Linux-查看文件和文件夹大小的df和du命令/"
  - "/2025/06/23/Linux-查看文件和文件夹大小的df和du命令.html"
  - "/Linux-查看文件和文件夹大小的df和du命令/"
  - "/Linux-查看文件和文件夹大小的df和du命令.html"
  - "/2025/06/23/linux-cha-kan-wen-jian-he-wen-jian-jia-da-xiao-de-df-he-du-ming-ling/"
  - "/2025/06/23/linux-cha-kan-wen-jian-he-wen-jian-jia-da-xiao-de-df-he-du-ming-ling.html"
  - "/linux-cha-kan-wen-jian-he-wen-jian-jia-da-xiao-de-df-he-du-ming-ling.html"
---
当磁盘大小超过标准时会有报警提示，这时如果掌握df和du命令是非常明智的选择。

df可以查看一级文件夹大小、使用比例、档案系统及其挂入点，但对文件却无能为力。

du可以查看文件及文件夹的大小。

两者配合使用，非常有效。比如用df查看哪个一级目录过大，然后用df查看文件夹或文件的大小，如此便可迅速确定症结。

## [下面分别简要介绍](#1)

### [df命令可以显示目前所有文件系统的可用空间及使用情形](#1-1)

请看下列这个例子：

```bash
[xx@xx]:~/php-oauth/itv_data_control$ df -h
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        64G   11G   50G  17% /
udev            367M  4.0K  367M   1% /dev
tmpfs           150M  4.2M  146M   3% /run
none            5.0M     0  5.0M   0% /run/lock
none            374M     0  374M   0% /run/shm
none            4.0T     0  4.0T   0% /media/psf
```

参数 -h 表示使用「Human-readable」的输出，也就是在档案系统大小使用 GB、MB 等易读的格式。

上面的命令输出的第一个字段（Filesystem）及最后一个字段（Mounted on）分别是档案系统及其挂入点。我们可以看到 /dev/sda1 这个分割区被挂在根目录下。

接下来的四个字段 Size、Used、Avail、及 Use% 分别是该分割区的容量、已使用的大小、剩下的大小、及使用的百分比。 FreeBSD下，当硬盘容量已满时，您可能会看到已使用的百分比超过 100%，因为 FreeBSD 会留一些空间给 root，让 root 在档案系统满时，还是可以写东西到该档案系统中，以进行管理。

### [du查询文件或文件夹的磁盘使用空间](#1-2)

如果当前目录下文件和文件夹很多，使用不带参数du的命令，可以循环列出所有文件和文件夹所使用的空间。这对查看究竟是那个地方过大是不利的，所以得指定深入目录的层数，参数：--max-depth=，这是个极为有用的参数！如下，注意使用“\*”，可以得到文件的使用空间大小.

**提醒**：一向命令比linux复杂的FreeBSD，它的du命令指定深入目录的层数却是比linux简化，为 -d。

```bash
[xx@xx]:~/php-oauth/itv_data_control$ du -h --max-depth=1 /home
2.6G	/home/davidzhang
2.6G	/home
```

```bash
[xx@xx]:~/vlinkage_itv_data$ du -h --max-depth=1 /home/davidzhang/vlinkage_itv_data/*
13M	/home/davidzhang/vlinkage_itv_data/文广快照.tsv
7.0M	/home/davidzhang/vlinkage_itv_data/深圳IP快照.tsv
```

```bash
[xx@xx]:~/vlinkage_itv_data$ du -h --max-depth=1 /home/davidzhang/vlinkage_itv_data/
20M	/home/davidzhang/vlinkage_itv_data/
```

值得注意的是，看见一个针对du和df命令异同的文章：《du df 差异导致文件系统误报解决》。

du 统计文件大小相加

df  统计数据块使用情况

如果有一个进程在打开一个大文件的时候,这个大文件直接被rm 或者mv掉，则du会更新统计数值，df不会更新统计数值,还是认为空间没有释放。直到这个打开大文件的进程被Kill掉。

如此一来在定期删除 /var/spool/clientmqueue下面的文件时，如果没有杀掉其进程，那么空间一直没有释放。

使用下面的命令杀掉进程之后，系统恢复。

```bash
fuser -u /var/spool/clientmqueue
```

