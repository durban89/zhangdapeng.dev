---
title: "Apache 伪静态处理跳转中传递参数"
date: "2025-06-27 14:14:57"
slug: "apache-wei-jing-tai-chu-li-tiao-zhuan-zhong-chuan-di-can-shu"
categories: ["技术"]
tags: ["Apache"]
aliases:
  - "/2025/06/27/Apache-伪静态处理跳转中传递参数/"
  - "/2025/06/27/Apache-伪静态处理跳转中传递参数.html"
  - "/Apache-伪静态处理跳转中传递参数/"
  - "/Apache-伪静态处理跳转中传递参数.html"
  - "/2025/06/27/apache-wei-jing-tai-chu-li-tiao-zhuan-zhong-chuan-di-can-shu/"
  - "/2025/06/27/apache-wei-jing-tai-chu-li-tiao-zhuan-zhong-chuan-di-can-shu.html"
  - "/apache-wei-jing-tai-chu-li-tiao-zhuan-zhong-chuan-di-can-shu.html"
---
下面对比一下，看第一个配置文件

```bash
# 将 RewriteEngine 模式打开
RewriteEngine On
RewriteBase /
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(/)?$ /wap.php?%{QUERY_STRING} [L] # 获取后面跟随的参数
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^/(\w+).php$ /$1.php?%{QUERY_STRING} [L] # 获取后面跟随的参数
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(\w+).html$ /wap.php?controller=$1&%{QUERY_STRING} [L] # 获取后面跟随的参数
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(\w+)\/(\w+).html$ /wap.php?controller=$1&action=$2&%{QUERY_STRING} [L] # 获取后面跟随的参数
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(\w+)\/(\w+)\/([\w\-\=\&\/a-zA-Z0-9_%]+).html$ /wap.php?controller=$1&action=$2&arguments=$3&%{QUERY_STRING} [L]
 
RewriteRule ^app\/$ /app.php [L]
RewriteRule ^(/)?$ /index.php [L]
RewriteRule ^/(\w+).php$ /$1.php [QSA,L]
RewriteRule ^(\w+).html$ /index.php?controller=$1 [QSA,L]
RewriteRule ^(\w+)\/(\w+).html$ /index.php?controller=$1&action=$2 [QSA,L]
RewriteRule ^(\w+)\/(\w+)\/([\w\-\=\&\/a-zA-Z0-9_%]+).html$ /index.php?controller=$1&action=$2&arguments=$3 [QSA,L]
```

这个是一个完整，可以在进行伪静态处理后，获取到传入的参数

如：http://m.zcyy.dev/auction/index/type/auction.html?p=2

是可以获取到参数p的,p的值为2

再来看下第二个

```bash
# 将 RewriteEngine 模式打开
RewriteEngine On
RewriteBase /
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(/)?$ /wap.php [L]
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^/(\w+).php$ /$1.php [L]
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(\w+).html$ /wap.php?controller=$1 [L]
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(\w+)\/(\w+).html$ /wap.php?controller=$1&action=$2 [L]
 
RewriteCond %{HTTP_HOST} ^m.zcyy.dev [NC]
RewriteRule ^(\w+)\/(\w+)\/([\w\-\=\&\/a-zA-Z0-9_%]+).html$ /wap.php?controller=$1&action=$2&arguments=$3 [L]
 
RewriteRule ^app\/$ /app.php [L]
RewriteRule ^(/)?$ /index.php [L]
RewriteRule ^/(\w+).php$ /$1.php [QSA,L]
RewriteRule ^(\w+).html$ /index.php?controller=$1 [QSA,L]
RewriteRule ^(\w+)\/(\w+).html$ /index.php?controller=$1&action=$2 [QSA,L]
RewriteRule ^(\w+)\/(\w+)\/([\w\-\=\&\/a-zA-Z0-9_%]+).html$ /index.php?controller=$1&action=$2&arguments=$3 [QSA,L]
```

这个是有问题的，是获取不到参数的

如：http://m.zcyy.dev/auction/index/type/auction.html?p=2

是获取不到参数p的

但是，如果是这样的地址的话是可以的

如：http://www.zcyy.dev/auction/index/type/auction.html?p=2

是可以获取到参数p的,p的值为2

其主要原因是因为%{QUERY_STRING}这个地方起了作用，超赞的一个用法。


