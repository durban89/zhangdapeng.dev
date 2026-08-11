---
title: "结合ISAPI_Rewrite 3 实现IIS6的伪静态配置"
date: "2025-06-27 14:14:16"
slug: "jie-he-isapi-rewrite-3-shi-xian-iis6-de-wei-jing-tai-pei-zhi"
categories: ["技术"]
tags: ["IIS"]
aliases:
  - "/2025/06/27/结合ISAPI-Rewrite-3-实现IIS6的伪静态配置/"
  - "/2025/06/27/结合ISAPI-Rewrite-3-实现IIS6的伪静态配置.html"
  - "/结合ISAPI-Rewrite-3-实现IIS6的伪静态配置/"
  - "/结合ISAPI-Rewrite-3-实现IIS6的伪静态配置.html"
  - "/2025/06/27/jie-he-isapi-rewrite-3-shi-xian-iis6-de-wei-jing-tai-pei-zhi/"
  - "/2025/06/27/jie-he-isapi-rewrite-3-shi-xian-iis6-de-wei-jing-tai-pei-zhi.html"
  - "/jie-he-isapi-rewrite-3-shi-xian-iis6-de-wei-jing-tai-pei-zhi.html"
---
结合ISAPI_Rewrite 3 [http://www.helicontech.com/isapi_rewrite/download.html]实现IIS6的伪静态配置，一般iis的筛选项启动成功就好了，其他问题多数是因为自己写的伪静态文件的规则有问题  
  
  
下面是一些相关的文件配置

```bash
# Helicon ISAPI_Rewrite configuration file
# Version 3.1.0.104

RewriteEngine On
RewriteCompatibility2 On
RepeatLimit 200
RewriteBase 
RewriteRule ^/(/)?$ /index\.php [L]
RewriteRule ^/(\w+)\.php$ /$1.php [L]
RewriteRule ^/(\w+)\.html$ /index\.php?controller=$1 [L]
RewriteRule ^/(\w+)\/(\w+)\.html$ /index\.php?controller=$1&action=$2 [L]
RewriteRule ^/(\w+)\/(\w+)\/([\w\-\=\&\/a-zA-Z0-9_%]+)\.html$ /index\.php?controller=$1&action=$2&arguments=$3 [L]
```


