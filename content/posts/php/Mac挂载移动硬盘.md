---
title: "Mac挂载移动硬盘"
date: "2025-07-14 14:54:46"
slug: "mac-gua-zai-yi-dong-ying-pan"
categories: ["技术"]
tags: ["MacOS"]
aliases:
  - "/2025/07/14/Mac挂载移动硬盘/"
  - "/2025/07/14/Mac挂载移动硬盘.html"
  - "/Mac挂载移动硬盘/"
  - "/Mac挂载移动硬盘.html"
  - "/2025/07/14/mac-gua-zai-yi-dong-ying-pan/"
  - "/2025/07/14/mac-gua-zai-yi-dong-ying-pan.html"
  - "/mac-gua-zai-yi-dong-ying-pan.html"
---
mac下挂载移动硬盘

对于支持mac读写格式的硬盘，本记录应该不值得参考

本记录只要针对于window下格式化的硬盘挂载到mac下，导致无法写入的问题

1、确认下是否有mount\_ntfs这个工具

```bash
$ mount_ntfs -h
mount_ntfs: usage: mount_ntfs [-s] [-o options] special-device filesystem-node
```

2、将硬盘插入use接口（type-c的没有确认过），运行下面命令查看挂载信息

```bash
$ mount | grep ntfs
/dev/disk2s1 on /Volumes/Elements SE (ntfs, local, nodev, nosuid, read-only, noowners)
```

3、使用unmount命令，将硬盘软解除挂载

```bash
sudo umount /dev/disk2s1
```

4、本地创建一个挂载目录，然后使用mount\_ntfs再次挂载

```bash
mkdir ~/mnt
```

```bash
sudo mount_ntfs -o rw,nobrowse /dev/disk2s1  ~/mnt
```
