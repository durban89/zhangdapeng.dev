---
title: "NGINX - 禁止未设置的域名绑定到服务器端口"
date: "2025-07-15 09:51:28"
slug: "nginx-jin-zhi-wei-she-zhi-de-yu-ming-bang-ding-dao-fu-wu-qi-duan-kou"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/07/15/NGINX-禁止未设置的域名绑定到服务器端口/"
  - "/2025/07/15/NGINX-禁止未设置的域名绑定到服务器端口.html"
  - "/NGINX-禁止未设置的域名绑定到服务器端口/"
  - "/NGINX-禁止未设置的域名绑定到服务器端口.html"
  - "/2025/07/15/nginx-jin-zhi-wei-she-zhi-de-yu-ming-bang-ding-dao-fu-wu-qi-duan-kou/"
  - "/2025/07/15/nginx-jin-zhi-wei-she-zhi-de-yu-ming-bang-ding-dao-fu-wu-qi-duan-kou.html"
  - "/nginx-jin-zhi-wei-she-zhi-de-yu-ming-bang-ding-dao-fu-wu-qi-duan-kou.html"
---
nginx部署服务器

遇到点小问题

第一个域名解析：想把某个域名解析到指定服务器，`*.xxx.com -> xxx.xxx.xxx.xxx`，好处是，省去了在同一台服务器按需添加域名了，想使用啥二级域名直接配置

第二个不想未配置的域名访问服务器：配置了`a.xxx.com`，但是不想`b.xxx.com`也能访问，按照nginx的server\_name寻找配置规则，访问`b.xxx.com`会访问到`a.xxx.com`

第一个问题是个好问题，这样做没问题

第二个问题的解决办法其实也很简单

如果是80端口的话

```ini
server {
    listen 80 default_server;
    server_name _;
    return 500;
}
```

如果是443端口的话

```ini
server {
    listen 443 default_server;
    server_name _;
    ssl on;
    ssl_certificate      cert/x.xxx.xxx.pem;
    ssl_certificate_key  cert/x.xxx.xxxkey;
    return 500;
}
```

这里强调下443端口配置的时候一定要配置证书，不然需要使用https的域名会无法访问

同时注意下nginx的版本，不同nginx的版本针对ssl的配置也会有不同的语法
