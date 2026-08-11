---
title: "Python 删除指定日期的日志文件"
date: "2025-07-03 11:59:03"
slug: "python-shan-chu-zhi-ding-ri-qi-de-ri-zhi-wen-jian"
categories: ["技术"]
tags: ["Python"]
aliases:
  - "/2025/07/03/Python-删除指定日期的日志文件/"
  - "/2025/07/03/Python-删除指定日期的日志文件.html"
  - "/Python-删除指定日期的日志文件/"
  - "/Python-删除指定日期的日志文件.html"
  - "/2025/07/03/python-shan-chu-zhi-ding-ri-qi-de-ri-zhi-wen-jian/"
  - "/2025/07/03/python-shan-chu-zhi-ding-ri-qi-de-ri-zhi-wen-jian.html"
  - "/python-shan-chu-zhi-ding-ri-qi-de-ri-zhi-wen-jian.html"
---
python脚本执行shell，通过crontab执行python脚本

```python
#!/usr/bin/env python
#-*-coding:utf-8-*-

import os
import time
import datetime
import subprocess

today =datetime.date.today()
deltadays = datetime.timedelta(days=1)    #确定日期差额，如前天 days=2
yesterday = today - deltadays

month = yesterday.strftime('%b')
date = yesterday.strftime('%d')

command1 = "ls -hl /log1 | grep '%s %s' | awk '{print i$9}' i='/log1/' | xargs rm " % (month, date)
command11 = "ls -hl /log1 | grep '%s  %s' | awk '{print i$9}' i='/log1/' | xargs rm " % (month, date)
command2 = "ls -hl /log2 | grep '%s %s' | awk '{print i$9}' i='/log2/' | xargs rm " % (month, date)
command22 = "ls -hl /log2 | grep '%s  %s' | awk '{print i$9}' i='/log2/' | xargs rm " % (month, date)

os.system(command1)
os.system(command11)
os.system(command2)
os.system(command22)
```

***注意***

```bash
ls -hl /log2 | grep '%s  %s' | awk '{print i$9}' i='/log2/' | xargs rm
```

这段shell命令最好是通过python执行shell答应看下具体的文件列出来的格式，防止无效

```bash
print os.system("ls -hl /log2")
```

这样运行后就能得出结果。然后根据具体情况修改就好了。


