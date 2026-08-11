---
title: "Apache 域名跳转"
date: "2025-06-27 14:13:59"
slug: "apache-yu-ming-tiao-zhuan"
categories: ["技术"]
tags: ["Apache"]
aliases:
  - "/2025/06/27/Apache-域名跳转/"
  - "/2025/06/27/Apache-域名跳转.html"
  - "/Apache-域名跳转/"
  - "/Apache-域名跳转.html"
  - "/2025/06/27/apache-yu-ming-tiao-zhuan/"
  - "/2025/06/27/apache-yu-ming-tiao-zhuan.html"
  - "/apache-yu-ming-tiao-zhuan.html"
---
如果想要实现访问jingguan.365use.com时，跳转到<http://www.landscapemedia.cn ，可以做如下操作>

```bash
<VirtualHost *:80>
    ServerName jingguan.365use.com
    RewriteEngine on
    RewriteCond %{HTTP_HOST} ^jingguan.365use.com  [NC]
    RewriteRule ^(.*) http://www.landscapemedia.cn$1 [R=permanent,L]
</VirtualHost>
```

