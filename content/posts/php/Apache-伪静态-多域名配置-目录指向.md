---
title: "Apache 伪静态  多域名配置 目录指向"
date: "2025-06-27 10:59:49"
slug: "apache-wei-jing-tai-duo-yu-ming-pei-zhi-mu-lu-zhi-xiang"
categories: ["技术"]
tags: ["Apache"]
aliases:
  - "/2025/06/27/Apache-伪静态-多域名配置-目录指向/"
  - "/2025/06/27/Apache-伪静态-多域名配置-目录指向.html"
  - "/Apache-伪静态-多域名配置-目录指向/"
  - "/Apache-伪静态-多域名配置-目录指向.html"
  - "/2025/06/27/apache-wei-jing-tai-duo-yu-ming-pei-zhi-mu-lu-zhi-xiang/"
  - "/2025/06/27/apache-wei-jing-tai-duo-yu-ming-pei-zhi-mu-lu-zhi-xiang.html"
  - "/apache-wei-jing-tai-duo-yu-ming-pei-zhi-mu-lu-zhi-xiang.html"
---
Apache 伪静态  多域名配置 目录指向

第一步：域名绑定

```bash
<VirtualHost *:80>
    DocumentRoot "D:\wwwroot\xinfushi"
    ServerName woying.365use.com
    ServerAlias m.woyingcaifu.com.cn m.woyingcaifu.cn m.woyingcaifu.com m.woyingwm.com.cn m.woyingwm.cn m.woyingwm.com woyingcaifu.com.cn woyingcaifu.cn woyingcaifu.com woyingwm.com.cn woyingwm.cn woyingwm.com www.woyingcaifu.com.cn www.woyingcaifu.cn www.woyingcaifu.com www.woyingwm.com.cn www.woyingwm.cn www.woyingwm.com
    <Directory "D:/wwwroot/xinfushi"> 
      Options FollowSymLinks
      AllowOverride All
      Order allow,deny
      Allow from all
    </Directory>
</VirtualHost>
```

第二步：伪静态

```bash
# 将 RewriteEngine 模式打开
RewriteEngine On
RewriteBase /

RewriteCond %{HTTP_HOST} ^m\.woyingwm\.com$ [OR]
RewriteCond %{HTTP_HOST} ^m\.woyingwm\.cn$ [OR]
RewriteCond %{HTTP_HOST} ^m\.woyingwm\.com\.cn$ [OR]
RewriteCond %{HTTP_HOST} ^m\.woyingcaifu\.com$ [OR]
RewriteCond %{HTTP_HOST} ^m\.woyingcaifu\.cn$ [OR]
RewriteCond %{HTTP_HOST} ^m\.woyingcaifu\.com\.cn$
RewriteRule ^(.*)$ /wap/$1 [L]

RewriteRule ^(/)?$ /index.php [L]
RewriteRule ^/(\w+).php$ /$1.php [QSA,L]
RewriteRule ^(\w+).html$ /index.php?controller=$1 [QSA,L]
RewriteRule ^(\w+)\/(\w+).html$ /index.php?controller=$1&action=$2 [QSA,L]
RewriteRule ^(\w+)\/(\w+)\/([\w\-\=\&\/a-zA-Z0-9_%]+).html$ /index.php?controller=$1&action=$2&arguments=$3 [QSA,L]
```

这里提示一下，注意最后的[OR]不要多加OR不然会不起作用的。

