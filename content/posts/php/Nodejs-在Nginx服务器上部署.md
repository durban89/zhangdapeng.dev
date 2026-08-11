---
title: "Nodejs 在Nginx服务器上部署"
date: "2025-06-30 14:09:19"
slug: "nodejs-zai-nginx-fu-wu-qi-shang-bu-shu"
categories: ["技术"]
tags: ["NGINX", "NodeJS"]
aliases:
  - "/2025/06/30/Nodejs-在Nginx服务器上部署/"
  - "/2025/06/30/Nodejs-在Nginx服务器上部署.html"
  - "/Nodejs-在Nginx服务器上部署/"
  - "/Nodejs-在Nginx服务器上部署.html"
  - "/2025/06/30/nodejs-zai-nginx-fu-wu-qi-shang-bu-shu/"
  - "/2025/06/30/nodejs-zai-nginx-fu-wu-qi-shang-bu-shu.html"
  - "/nodejs-zai-nginx-fu-wu-qi-shang-bu-shu.html"
---
nginx配置如下：

```bash
upstream nodejs_upstream {
    server    127.0.0.1:3030;
    keepalive 64;
}


server {
    listen   80; ## listen for ipv4; this line is default and implied
    #listen   [::]:80 default ipv6only=on; ## listen for ipv6

    server_name node.blog.gowhich.dev;

    location / {
        proxy_set_header    X-Real-IP    $remote_addr;
        proxy_set_header    X-Forwarded-For    $proxy_add_x_forwarded_for;
        proxy_set_header    Host    $http_host;    
        proxy_set_header    X-NginX-Proxy    true;
        proxy_set_header    Connection    "";
        proxy_http_version    1.1;
        proxy_pass    http://nodejs_upstream;
    }
}
```

使用pm2启动nodejs项目，方便管理项目;

此处的3030是跟你nodejs项目启动的端口号是一致的。


