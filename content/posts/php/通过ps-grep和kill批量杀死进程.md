---
title: "通过ps、grep和kill批量杀死进程"
date: "2025-07-01 11:36:15"
slug: "tong-guo-ps-grep-he-kill-pi-liang-sha-si-jin-cheng"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/07/01/通过ps、grep和kill批量杀死进程/"
  - "/2025/07/01/通过ps、grep和kill批量杀死进程.html"
  - "/通过ps、grep和kill批量杀死进程/"
  - "/通过ps、grep和kill批量杀死进程.html"
  - "/2025/07/01/通过ps-grep和kill批量杀死进程/"
  - "/2025/07/01/通过ps-grep和kill批量杀死进程.html"
  - "/2025/07/01/tong-guo-ps-grep-he-kill-pi-liang-sha-si-jin-cheng/"
  - "/2025/07/01/tong-guo-ps-grep-he-kill-pi-liang-sha-si-jin-cheng.html"
  - "/tong-guo-ps-grep-he-kill-pi-liang-sha-si-jin-cheng.html"
---
这两天Node的程序kill到手都软了，网上查了一个很好的方法，直接拿来用了。

功能：杀死进程名称中包含node的所有进程

```bash
ps -ef | grep node | awk '{print $2}' | xargs kill -9
```


