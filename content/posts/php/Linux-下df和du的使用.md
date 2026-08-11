---
title: "Linux下df和du的使用"
date: "2025-06-26 10:32:15"
slug: "linux-xia-df-he-du-de-shi-yong"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/06/26/Linux下df和du的使用/"
  - "/2025/06/26/Linux下df和du的使用.html"
  - "/Linux下df和du的使用/"
  - "/Linux下df和du的使用.html"
  - "/2025/06/26/Linux-下df和du的使用/"
  - "/2025/06/26/Linux-下df和du的使用.html"
  - "/2025/06/26/linux-xia-df-he-du-de-shi-yong/"
  - "/2025/06/26/linux-xia-df-he-du-de-shi-yong.html"
  - "/linux-xia-df-he-du-de-shi-yong.html"
---
df命令的简单使用，可以显示目前所有文件系统的可用空间及使用情形，命令如下：

```bash
df -h
```

gowhich得到的结果是

```bash
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/xvda1      20903812 2378972  17476368  12% /
udev             2015444       4   2015440   1% /dev
tmpfs             757268     268    757000   1% /run
none                5120       0      5120   0% /run/lock
none             1893168       0   1893168   0% /run/shm
/dev/xvdb       51606140 1915528  47069172   4% /wwwroot
```

---

du命令的简单的使用，查询文件或文件夹的磁盘使用空间。可以指定目录进行查询。

如果当前目录下文件和文件夹很多，使用不带参数du的命令，可以循环列出所有文件和文件夹所使用的空间。这对查看究竟是那个地方过大是不利的，所以得指定深入目录的层数，参数：--max-depth=，这是个极为有用的参数！如下，注意使用“\*”，可以得到文件的使用空间大小.

```bash
du -h --max-depth=1 /
```

---

得到的结果是

```bash
4.0K	/opt
18M	/home
6.8M	/sbin
8.0K	/media
203M	/lib
du: cannot access `/proc/29005/task/29005/fd/4': No such file or directory
du: cannot access `/proc/29005/task/29005/fdinfo/4': No such file or directory
du: cannot access `/proc/29005/fd/4': No such file or directory
du: cannot access `/proc/29005/fdinfo/4': No such file or directory
0	/proc
4.0K	/lib64
16K	/lost+found
0	/sys
4.0K	/dev
4.0K	/selinux
4.0K	/srv
5.2M	/etc
268K	/run
1.7G	/wwwroot
27M	/boot
```

---

参考的文章：

http://www.yayu.org/look.php?id=162

