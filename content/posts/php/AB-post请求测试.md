---
title: "AB post请求测试"
date: "2025-07-02 16:01:37"
slug: "ab-post-qing-qiu-ce-shi"
categories: ["技术"]
tags: ["AB"]
aliases:
  - "/2025/07/02/AB-post请求测试/"
  - "/2025/07/02/AB-post请求测试.html"
  - "/AB-post请求测试/"
  - "/AB-post请求测试.html"
  - "/2025/07/02/ab-post-qing-qiu-ce-shi/"
  - "/2025/07/02/ab-post-qing-qiu-ce-shi.html"
  - "/ab-post-qing-qiu-ce-shi.html"
---
ab post请求测试

```bash
ab -c 200 -n 1000 -T 'application/x-www-form-urlencoded' -p postdata.txt http://domain/test.php
```

以前不知道的你，很震惊

postdata.txt的内容类似如下

```bash
third=1&third_params={"uid":"12345","openid":"12345","name":"12345","gender":"0","iconurl":"12345"}&idfa=12345&device_imei12345&app_client_version=2.3.2.0&platform=android
```

这里注意下-c和-n的参数，两个参数的值是成倍数关系的，如果这样设置

```bash
ab -c 2 -n 4 -T 'application/x-www-form-urlencoded' -p postdata.txt http://domain/test.php
```

会提示参数错误

类似如下

```bash
ab: wrong number of arguments
```

-n和-c参数说明

```
-n：在测试会话中所执行的请求个数。默认时，仅执行一个请求。

-c：一次产生的请求个数。默认是一次一个。
```


