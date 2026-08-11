---
title: "PHP大量Session的散列及过期回收"
date: "2025-06-19 13:54:31"
slug: "php-da-liang-session-de-san-lie-ji-guo-qi-hui-shou"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/19/PHP大量Session的散列及过期回收/"
  - "/2025/06/19/PHP大量Session的散列及过期回收.html"
  - "/PHP大量Session的散列及过期回收/"
  - "/PHP大量Session的散列及过期回收.html"
  - "/2025/06/19/php-da-liang-session-de-san-lie-ji-guo-qi-hui-shou/"
  - "/2025/06/19/php-da-liang-session-de-san-lie-ji-guo-qi-hui-shou.html"
  - "/php-da-liang-session-de-san-lie-ji-guo-qi-hui-shou.html"
---
最近服务器登录不了啦，登录后就退出来了，为什么？看下面吧

一台服务器流量比较大，因为程序的需要，session的过期时间设置的是3小时，导致/tmp下堆积了近20万的session文件。进而导致内核占用 的cpu急剧上升。因为session的读写涉及到大量小文件的随机读写，并且是集中在一个目录下，iowait也急剧升高。

### [首先考虑将session放入内存中](#1)

最简单的办法莫过于将/tmp挂载为 tmpfs文件系统，也就是内存中

### [将session存储到不通的目录中](#2)

php本身支持session的多级散列  
  
在php.ini中，将

```bash
;session.save_path = /tmp
```

改为

```bash
session.save_path = "2;/tmp/session"
```

表示将session存储到 `/tmp/session`这个文件夹中，并且是用2及散列。  
  
保存退出，等第三步结束后重启php

### [创建session存储文件夹](#3)

php并不会自动去创建这些文件夹，不过在源文件中提供了一些创建文件夹的脚本。下面这个脚本也好用

```bash
I="0 1 2 3 4 5 6 7 8 9 a b c d e f"
for acm in $I;
do
for x in $I;
do
mkdir -p /tmp/session/$acm/$x;
done;
done
chown -R nobody:nobody /tmp/session
chmod -R 1777 /tmp/session
```

因为/tmp是用的内存，服务器重启后，里面的所有文件都会丢失，所以，需要把上面的脚本加入到 `/etc/rc.local`中，并且要放在启动php之前

### [session的回收](#4)

session在经过`session.gc_maxlifetime`后会过期，但并不会马上被删除，时间长了以后会造成`/tmp`空间占用很大。具体的删除算法懒得去研究。下面这个命令可以删除过期的session，我这里定义的过期时间是3小时。

```bash
find /tmp/session -amin +180 -exec rm -rf {} \;
```

放入cron中，10分钟执行一次，完事。

其中有些步骤本网站已经有说明，但是缺少的是如果删除生成的session文件，娘炮哦，我原因为它会自动删除生成的session文件的哈，结果，跟我想的逆天啦。

关于php.ini文件的配置和session文件的目录的设置，这篇文章有讲到的

[`session.save_path`目录大量session临时文件带来的服务器效率问题](https://www.gowhich.com/blog/272)

可以去看下，我这里主要记录下，关于删除生成的session文件的处理办法

很简单的：

```bash
find /tmp/session -mtime +1 -type f -exec rm -rf {} \;
```

就是这条语句，想知道如何理解这行命令吗？要不继续往下看，要不就自己google去吧。
