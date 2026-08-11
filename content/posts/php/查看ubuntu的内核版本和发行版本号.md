---
title: "查看ubuntu的内核版本和发行版本号"
date: "2025-06-24 14:45:52"
slug: "cha-kan-ubuntu-de-nei-he-ban-ben-he-fa-xing-ban-ben-hao"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/06/24/查看ubuntu的内核版本和发行版本号/"
  - "/2025/06/24/查看ubuntu的内核版本和发行版本号.html"
  - "/查看ubuntu的内核版本和发行版本号/"
  - "/查看ubuntu的内核版本和发行版本号.html"
  - "/2025/06/24/cha-kan-ubuntu-de-nei-he-ban-ben-he-fa-xing-ban-ben-hao/"
  - "/2025/06/24/cha-kan-ubuntu-de-nei-he-ban-ben-he-fa-xing-ban-ben-hao.html"
  - "/cha-kan-ubuntu-de-nei-he-ban-ben-he-fa-xing-ban-ben-hao.html"
---
### [查看发行版本号](#1)

方法一

终端执行下列指令：

```bash
cat /etc/issue
```

其输出结果类似下面的内容：

```bash
Ubuntu 12.04.1 LTS \n \l
```

方法二

执行指令如下：

```bash
sudo lsb_release -a
```

输出结果：

```bash
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 12.04.1 LTS
Release:	12.04
Codename:	precise
```

### [查看内核版本号](#2)

终端执行指令：

```bash
uname -r
```

输出如下结果：

```bash
3.2.0-23-generic-pae
```
