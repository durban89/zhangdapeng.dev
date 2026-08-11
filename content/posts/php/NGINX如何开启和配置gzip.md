---
title: "NGINX如何开启和配置gzip"
date: "2025-06-09 11:52:26"
slug: "nginx-ru-he-kai-qi-he-pei-zhi-gzip"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/06/09/NGINX如何开启和配置gzip/"
  - "/2025/06/09/NGINX如何开启和配置gzip.html"
  - "/NGINX如何开启和配置gzip/"
  - "/NGINX如何开启和配置gzip.html"
  - "/2025/06/09/nginx-ru-he-kai-qi-he-pei-zhi-gzip/"
  - "/2025/06/09/nginx-ru-he-kai-qi-he-pei-zhi-gzip.html"
  - "/nginx-ru-he-kai-qi-he-pei-zhi-gzip.html"
---
gzip是GNU zip的缩写，它是一个GNU自由软件的文件压缩程序，可以极大的加速网站.有时压缩比率高到80%,近来测试了一下,最少都有40%以上,还是相当不错的。大道至简，知易行难，悟者大成。

> gzip

决定是否开启gzip模块
`example:gzip on;`

> gzip_buffers 

设置gzip申请内存的大小,其作用是按块大小的倍数申请内存空间
param2:int(k) 后面单位是k
`example: gzip_buffers 4 8k;`

> gzip_comp_level

设置gzip压缩等级，等级越底压缩速度越快文件压缩比越小，反之速度越慢文件压缩比越大
param:1-9
`example:gzip_com_level 1;`

> gzip_min_length

当返回内容大于此值时才会使用gzip进行压缩,以K为单位,当值为0时，所有页面都进行压缩
param:int
`example:gzip_min_length 1000;`

> gzip_http_version

用于识别http协议的版本，早期的浏览器不支持gzip压缩，用户会看到乱码，所以为了支持前期版本加了此选项,目前此项基本可以忽略
param: 1.0|1.1
`example:gzip_http_version 1.0`

> gzip_proxied

Nginx做为反向代理的时候启用，
param:off|expired|no-cache|no-sotre|private|no_last_modified|no_etag|auth|any]
`expample:gzip_proxied no-cache;`
off – 关闭所有的代理结果数据压缩
expired – 启用压缩，如果header中包含”Expires”头信息
no-cache – 启用压缩，如果header中包含”Cache-Control:no-cache”头信息
no-store – 启用压缩，如果header中包含”Cache-Control:no-store”头信息
private – 启用压缩，如果header中包含”Cache-Control:private”头信息
no_last_modified – 启用压缩，如果header中包含”Last_Modified”头信息
no_etag – 启用压缩，如果header中包含“ETag”头信息
auth – 启用压缩，如果header中包含“Authorization”头信息
any – 无条件压缩所有结果数据

> gzip_types

设置需要压缩的MIME类型,非设置值不进行压缩
param:text/html|application/x-javascript|text/css|application/xml
`example:gzip_types text/html;`

Demo
```c
gzip on;
gzip_min_length 1000;
gzip_buffers 4 8k;
gzip_types text/html application/x-javascript text/css application/xml;
```
