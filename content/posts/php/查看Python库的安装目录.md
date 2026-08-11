---
title: "查看Python库的安装目录"
date: "2025-06-23 16:27:01"
slug: "cha-kan-python-ku-de-an-zhuang-mu-lu"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/23/查看Python库的安装目录/"
  - "/2025/06/23/查看Python库的安装目录.html"
  - "/查看Python库的安装目录/"
  - "/查看Python库的安装目录.html"
  - "/2025/06/23/cha-kan-python-ku-de-an-zhuang-mu-lu/"
  - "/2025/06/23/cha-kan-python-ku-de-an-zhuang-mu-lu.html"
  - "/cha-kan-python-ku-de-an-zhuang-mu-lu.html"
---
查看python中库的位置，其实就是几个命里行的方法

我这里的方法是：

```bash
davidzhang@192:/Library$ python
Python 2.7.2 (default, Oct 11 2012, 20:14:37) 
[GCC 4.2.1 Compatible Apple Clang 4.0 (tags/Apple/clang-418.0.60)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import ftplib
>>> reload(ftplib)
<module 'ftplib' from '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/ftplib.py'>
>>>
```

