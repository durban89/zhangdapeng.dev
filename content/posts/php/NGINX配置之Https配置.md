---
title: "NGINX配置之Https配置"
date: "2025-07-03 17:37:34"
slug: "nginx-pei-zhi-zhi-https-pei-zhi"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/07/03/NGINX配置之Https配置/"
  - "/2025/07/03/NGINX配置之Https配置.html"
  - "/NGINX配置之Https配置/"
  - "/NGINX配置之Https配置.html"
  - "/2025/07/03/nginx-pei-zhi-zhi-https-pei-zhi/"
  - "/2025/07/03/nginx-pei-zhi-zhi-https-pei-zhi.html"
  - "/nginx-pei-zhi-zhi-https-pei-zhi.html"
---
现在的https越来越流行，这个未来应该是必备技能了，下面举个Yii2的项目，进行https配置，https证书自己需要准备好，不会的可以看我的文章  
下面就是示例配置【仅供参考】

```bash
server {
    listen 443 ssl http2;

    ssl_certificate /etc/letsencrypt/live/gowhich.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/gowhich.com/privkey.pem;

    ssl_session_timeout 10m;
    ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
    ssl_prefer_server_ciphers on;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_session_cache builtin:1000 shared:SSL:10m;

    resolver 8.8.8.8 8.8.4.4 valid=300s;

    resolver_timeout 5s;

    server_name www.gowhich.com gowhich.com;

    access_log  /home/wwwlogs/www.gowhich.com.log  access;
    error_log  /home/wwwlogs/www.gowhich.com.error.log;

    index index.html index.htm index.php default.html default.htm default.php;
    root  /home/wwwroot/www1.gowhich.com/web;

    include yii.conf;

    if ($host = 'gowhich.com') {
        rewrite ^/(.*)$ https://www.gowhich.com/$1 permanent;
    }

    location ~ [^/]\.php(/|$) {
        # comment try_files $uri =404; to enable pathinfo
        try_files $uri =404;
        fastcgi_pass  unix:/tmp/php-cgi.sock;
        fastcgi_index index.php;
        include fastcgi.conf;
        #include pathinfo.conf;
    }

    location ~ .*\.(gif|jpg|jpeg|png|bmp|swf)$ {
        expires      30d;
    }

    location ~ .*\.(js|css)?$ {
        expires      12h;
    }
}
```
