---
title: "NGINX禁止直接以IP访问"
date: "2025-06-19 10:29:20"
slug: "nginx-jin-zhi-zhi-jie-yi-ip-fang-wen"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/06/19/NGINX禁止直接以IP访问/"
  - "/2025/06/19/NGINX禁止直接以IP访问.html"
  - "/NGINX禁止直接以IP访问/"
  - "/NGINX禁止直接以IP访问.html"
  - "/2025/06/19/nginx-jin-zhi-zhi-jie-yi-ip-fang-wen/"
  - "/2025/06/19/nginx-jin-zhi-zhi-jie-yi-ip-fang-wen.html"
  - "/nginx-jin-zhi-zhi-jie-yi-ip-fang-wen.html"
---
今天搞了一下禁止nginx的ip访问，哈哈，找了一篇文章

看下面‍

在虚拟主机最前面加上如下即可，记住一定要以它开头（不然不生效）。如下,返回值404，可以改403等。

```nginx
server {
         server_name  _;  #default
         return 404;
         }


server{
    listen       80;
    server_name  .test.com;  #(域名前加点，不然可能访问不了)
    index main.php index.php;
    root  /var/htdocs/www/test;

    location ~ .*\.(php|php5)?${
      #fastcgi_pass  unix:/tmp/php-cgi.sock;
      fastcgi_pass  127.0.0.1:9000;
      fastcgi_index index.php;
      include fcgi.conf;
    }

    log_format  testlogs  '$remote_addr - $remote_user [$time_local] "$request" '
               '$status $body_bytes_sent "$http_referer" '
               '"$http_user_agent" $http_x_forwarded_for';
    access_log  /var/htdocs/logs/testlogs.log  testlogs;

}
```
