---
title: "Python 文件写入和读取操作"
date: "2025-06-25 09:57:57"
slug: "python-wen-jian-xie-ru-he-du-qu-cao-zuo"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/25/Python-文件写入和读取操作/"
  - "/2025/06/25/Python-文件写入和读取操作.html"
  - "/Python-文件写入和读取操作/"
  - "/Python-文件写入和读取操作.html"
  - "/2025/06/25/python-wen-jian-xie-ru-he-du-qu-cao-zuo/"
  - "/2025/06/25/python-wen-jian-xie-ru-he-du-qu-cao-zuo.html"
  - "/python-wen-jian-xie-ru-he-du-qu-cao-zuo.html"
---
python的文件写入和读取操作，是python自身携带的功能，不需要其他的import

简单的演示了写入和读取的操作

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#!Filename: using_file.py
__author__ = 'Durban Zhang'
poem = '''
Programming is fun When the work is done
if you wanna make your work also fun:
use Python!
'''
f = file('poem.txt','w')
f.write(poem)
f.close()
f = file('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break;
    print line, #消除自动换行
f.close()
```

读取的操作中使用了，readline的函数，还有消除自动换行的特殊用法
