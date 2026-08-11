---
title: "Mac OS X 的安全睡眠"
date: "2025-06-11 13:53:52"
slug: "mac-os-x-de-an-quan-shui-mian"
categories: ["技术"]
tags: ["Unix", "MacOS"]
aliases:
  - "/2025/06/11/Mac-OS-X-的安全睡眠/"
  - "/2025/06/11/Mac-OS-X-的安全睡眠.html"
  - "/Mac-OS-X-的安全睡眠/"
  - "/Mac-OS-X-的安全睡眠.html"
  - "/2025/06/11/mac-os-x-de-an-quan-shui-mian/"
  - "/2025/06/11/mac-os-x-de-an-quan-shui-mian.html"
  - "/mac-os-x-de-an-quan-shui-mian.html"
---
Mac OS X 默认是使用普通睡眠+安全睡眠（在 Windows 中称为休眠）。

安全睡眠会在计算机进入睡眠状态时把内存（RAM）中的数据保存到硬盘上的「/private/var/vm/sleepimage」文件，然后计算机才进入普通睡眠。这样做的好处是如果计算机完全没电了，那原来内存中的内容还可以从硬盘上恢复。

但这样也带来了不利之处，每当进入睡眠的时候都要写入内存容量大小的数据到硬盘上，这无疑延长了进入睡眠所需的时间（通常需要20秒-1分钟）；硬盘上还要使用内存容量大小的空间来存储睡眠文件，像笔者的 MacBook 有 4GB 的内存，那就要使用 4GB 的磁盘空间来存储睡眠文件，这对于磁盘空间比较紧张的笔记本用户来说就不太值得了。

可使用如下的命令进行查看：

```sh
ls -lh /private/var/vm/
```

可以在「应用程序-实用程序-终端」中使用以下命令禁止安全睡眠：

```sh
$ sudo pmset -a hibernatemode 0
$ sudo nvram “use-nvramrc?”=false
```

以上设置需要在计算机重启后才能生效。生效后就可以使用下面的命令删除睡眠文件了：

```sh
$ sudo rm -f /private/var/vm/sleepimage
```

如果需要恢复安全睡眠，可以使用下面的命令：

```sh
$ sudo pmset -a hibernatemode 3
$ sudo nvram “use-nvramrc?”=true
```

然后重启计算机即可。
