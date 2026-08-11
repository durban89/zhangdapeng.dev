---
title: "Python 技巧 - 抓取页面并保存为PDF"
date: "2025-07-30T11:43:55.199115+08:00"
draft: false
image: "https://res.cloudinary.com/dy5dvcuc1/image/upload/v1565854753/walkerfree/python.jpg"
slug: "python-ji-qiao-zhua-qu-ye-mian-bing-bao-cun-wei-pdf"
categories: ["技术"]
tags: ["Python", "PDF"]
aliases:
  - "/2025/07/30/python-技巧-抓取页面并保存为pdf"
  - "/2025/07/30/python-技巧-抓取页面并保存为pdf/"
---

技巧要点记录

1、requests和parsel库的安装

2、获取网页内容

发送一个请求

```python

url = ''

headers = {
    'Host': '',
    'Referer': '',
    'User-Agent': ''
}

cookie = {
    'Cookie': ''
}

response = requests.get(url, headers=headers, cookie=cookie)

print(response.text)
```

获取到内容

3、pdfkit、wkhtmltopdf库的安装

```bash

pip install pdfkit
```

wkhtmltopdf 请去官网下载 https://wkhtmltopdf.org/downloads.html

4、转换为PDF

pdfkit、wkhtmltopdf库的安装

```python

import pdfkit

config = pdfkit.configuration(wkhtmltopdf='xxx/xxx/wkhtmltopdf.exe')

pdfkit.from_file('xx.html', 'xxx.pdf', configuration=config)
```
