---
title: "Composer更新时openssl证书异常处理"
date: "2025-07-15 10:28:58"
slug: "composer-geng-xin-shi-openssl-zheng-shu-yi-chang-chu-li"
categories: ["技术"]
tags: ["Composer"]
aliases:
  - "/2025/07/15/Composer更新时openssl证书异常处理/"
  - "/2025/07/15/Composer更新时openssl证书异常处理.html"
  - "/Composer更新时openssl证书异常处理/"
  - "/Composer更新时openssl证书异常处理.html"
  - "/2025/07/15/composer-geng-xin-shi-openssl-zheng-shu-yi-chang-chu-li/"
  - "/2025/07/15/composer-geng-xin-shi-openssl-zheng-shu-yi-chang-chu-li.html"
  - "/composer-geng-xin-shi-openssl-zheng-shu-yi-chang-chu-li.html"
---
![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1675930021/2023-02-09_15-44.png)

**composer install**或者**composer update** 时出现下面错误

> OpenSSL Error messages: error:14090086:SSL routines:ssl3\_get\_server\_certificate:certificate verify failed
>
> 说明需要ssl 证书没有配置或者配置的有问题

首先去下载证书

```bash
wget http://curl.haxx.se/ca/cacert.pem
```

然后将证书配置到指定目录

```bash
mv cacert.pem /usr/local/openssl/cert.pem
```

之后在修改php.ini文件中openssl的配置

```bash
openssl.cafile=/usr/local/openssl/cert.pem
```
