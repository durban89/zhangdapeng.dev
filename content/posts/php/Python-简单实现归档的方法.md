---
title: "Python 简单实现归档的方法"
date: "2025-06-25 09:57:30"
slug: "python-jian-dan-shi-xian-gui-dang-de-fang-fa"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/06/25/Python-简单实现归档的方法/"
  - "/2025/06/25/Python-简单实现归档的方法.html"
  - "/Python-简单实现归档的方法/"
  - "/Python-简单实现归档的方法.html"
  - "/2025/06/25/python-jian-dan-shi-xian-gui-dang-de-fang-fa/"
  - "/2025/06/25/python-jian-dan-shi-xian-gui-dang-de-fang-fa.html"
  - "/python-jian-dan-shi-xian-gui-dang-de-fang-fa.html"
---
对于归档的方法，我这里使用python做个简单的小例子

使用了三个例子来做显示，这个三个例子从上倒下是逐个进行完善的

### [第一个例子](#1)

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#Filename:backup_ver1.py
import os
import time
source = [
'/Users/davidzhang/python/python_project/data_struct/test',
'/Users/davidzhang/python/python_project/data_struct/tes1'
]
target_dir = '/Users/davidzhang/python/python_project/data_struct/backup/'
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
# print target
zip_command = 'zip -qr "%s" %s' % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print 'Successful backup to ',target
else:
    print 'Backup FAILED'
```

### [第二个例子](#2)

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#Filename:backup_ver2.py
import os
import time
source = [
    '/Users/davidzhang/python/python_project/data_struct/test',
    '/Users/davidzhang/python/python_project/data_struct/tes1'
]
target_dir = '/Users/davidzhang/python/python_project/data_struct/backup/'
today = target_dir + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory ', today 
    
target = today + os.sep + now + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print 'Successful backup to ', target
else:
    print 'Backup FAILED'
```

### [第三个例子](#3)

```python
#!/usr/bin/env python
#!-*- coding=utf-8 -*-
#Filename:backup_ver3.py
import os
import time
source = [
    '/Users/davidzhang/python/python_project/data_struct/test',
    '/Users/davidzhang/python/python_project/data_struct/tes1'
]
target_dir = '/Users/davidzhang/python/python_project/data_struct/backup/'
today = target_dir + time.strftime("%Y%m%d")
now = time.strftime("%H%M%S")
comment = raw_input("Enter a comment -->")
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'
if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory ', today
    
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))
if os.system(zip_command) == 0:
    print 'Successful backup to ', target
else:
    print 'Backup FAILED'
```

第一个例子实现的很简单的功能，第二个例子考虑了文件夹的问题，没有则进行创建，第三更加人性化，为了进行人性化的管理，加入了给文件添加分类的注视

这里面只是简单的练习。

***最理想的创建这些归档的方法是分别使用zipfile和tarfile。它们是Python标准库的一部分，可以供你使用。使用这些库就避免了使用os.system这个不推荐使用的函数，它容易引发严重的错误。***

