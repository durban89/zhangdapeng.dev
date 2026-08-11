---
title: "NGINX + Nodejs (110: Connection timed) 错误处理"
date: "2025-07-03 11:58:19"
slug: "nginx-nodejs-110-connection-timed-cuo-wu-chu-li"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/07/03/NGINX-+-Nodejs-(110:-Connection-timed)-错误处理/"
  - "/2025/07/03/NGINX-+-Nodejs-(110:-Connection-timed)-错误处理.html"
  - "/NGINX-+-Nodejs-(110:-Connection-timed)-错误处理/"
  - "/NGINX-+-Nodejs-(110:-Connection-timed)-错误处理.html"
  - "/2025/07/03/NGINX-+-Nodejs-110-Connection-timed-错误处理/"
  - "/2025/07/03/NGINX-+-Nodejs-110-Connection-timed-错误处理.html"
  - "/2025/07/03/nginx-nodejs-110-connection-timed-cuo-wu-chu-li/"
  - "/2025/07/03/nginx-nodejs-110-connection-timed-cuo-wu-chu-li.html"
  - "/nginx-nodejs-110-connection-timed-cuo-wu-chu-li.html"
---
最近服务器出现问题了，error.log日志里面多了很多的（110: Connection timed）这个错误。

开始以为是Nodejs的脚本有问题，再请求的时候会有超时的问题，但是检查了一下，并没有发现问题，因为已经对出现问题的错误做了sysError的日志记录，但是在日志里面并没有找到对应的错误信息，很奇怪。也是google下找到了对应的解决方案。

参考：http://stackoverflow.com/questions/10395807/nginx-close-upstream-connection-after-request

```bash
location / {
    proxy_http_version 1.1;
    proxy_set_header Connection "";
}
```

本来我的upstream中只加了server这段信息的，现在参考了这里的话，也加了下keepalive;

```bash
upstream backend {
    server 127.0.0.1:2222;
    keepalive 128;
}
```

然后重启以下nginx；

```bash
sudo nginx -s reload
```

这个命令执行完，似乎没有立刻起作用，于是

```bash
sudo nginx -s reopen
```

这样就可以了。

