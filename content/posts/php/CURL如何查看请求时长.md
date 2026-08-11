---
title: "CURL如何查看请求时长"
date: "2025-07-15 10:28:44"
slug: "curl-ru-he-cha-kan-qing-qiu-shi-chang"
categories: ["技术"]
tags: ["CURL"]
aliases:
  - "/2025/07/15/CURL如何查看请求时长/"
  - "/2025/07/15/CURL如何查看请求时长.html"
  - "/CURL如何查看请求时长/"
  - "/CURL如何查看请求时长.html"
  - "/2025/07/15/curl-ru-he-cha-kan-qing-qiu-shi-chang/"
  - "/2025/07/15/curl-ru-he-cha-kan-qing-qiu-shi-chang.html"
  - "/curl-ru-he-cha-kan-qing-qiu-shi-chang.html"
---
命令很简单

```bash
curl -o /dev/null -s -w %{http_code}---%{content_type}---%{time_namelookup}---%{time_namelookup}---%{time_connect}---%{time_starttransfer}---%{time_total}---%{speed_download}"\n" "http://www.baidu.com/"
```

把"http://www.baidu.com"替换一下就可以了

下面对参数进行下说明

-o /dev/null：把curl 返回的html、js 写到垃圾回收站[/dev/null]  
-s：去掉所有状态  
-w：按照后面的格式写出rt

http\_code http：状态码

content\_type：类型

time\_namelookup：DNS解析域名的时间

time\_commect：client和server端建立TCP连接的时间

time\_starttransfer：从client发出请求，到web的server响应第一个字节的时间

time\_total：client发出请求，到web的server发送回所有的相应数据的时间

speed\_download：下载速度 单位 byte/s

--- 分隔符号
