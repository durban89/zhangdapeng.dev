---
title: "NGINX server_name 正则匹配"
date: "2025-07-15 09:50:53"
slug: "nginx-server-name-zheng-ze-pi-pei"
categories: ["技术"]
tags: ["NGINX"]
aliases:
  - "/2025/07/15/NGINX-server-name-正则匹配/"
  - "/2025/07/15/NGINX-server-name-正则匹配.html"
  - "/NGINX-server-name-正则匹配/"
  - "/NGINX-server-name-正则匹配.html"
  - "/2025/07/15/nginx-server-name-zheng-ze-pi-pei/"
  - "/2025/07/15/nginx-server-name-zheng-ze-pi-pei.html"
  - "/nginx-server-name-zheng-ze-pi-pei.html"
---
测试服务器动态绑定多个域名

比如我现在有一个

```bash
api.domain.com
```

但是测试需要给不同分支代码绑定一个不同的域名方便访问

需求类似如下

```bash
api1.domain.com
api2.domain.com
api2.domain.com
```

可以像下面这样添加nginx配置

```bash
server {
    listen 80;
    server_name ~^api(?<which_domain_id>\d*)\.domain\.com$;
    access_log  logs/api.domain.com.access.log main;
    error_log   logs/api.domain.error.log;

}
```

```bash
server {
    listen 443 ssl;
    server_name ~^api(?<which_domain_id>\d*)\.domain\.com$;
    access_log  logs/api.domain.com.443.access.log main;
    error_log   logs/api.domain.443.error.log;
}
```

这样我们就可以拿到`$which_domain_id`变量，为后面的测试提供用途

比如upstream的配置

比如root的配置

比如我们配置三个upsteam

```bash
upsteam api1 {
    // ...
}

upsteam api2 {
    // ...
}

upstream api3 {
    // ...
}
```

在用location做转发的时候，可以像下面这样使用了

```bash
location = /api/xxx/info {
    proxy_pass http://api$which_domain_id;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $host;
    proxy_send_timeout 120s;
    proxy_read_timeout 120s;
    keepalive_timeout 0;
}
```

不过你如果用到了`proxy_redirect`的话，就不能`proxy_redirect default`这样的配置了，可以改为类似下面的配置

```bash
location = /api/xxx/info {
    proxy_pass http://api$which_domain_id;
    proxy_redirect /api/xxx/info /api/xxx/info;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $host;
    proxy_send_timeout 120s;
    proxy_read_timeout 120s;
    keepalive_timeout 0;
}
```

像上面如果是转发到同一个路由的话其实也可以不用加`proxy_redirect`的

```bash
location = /api/xxx/info {
    proxy_pass http://api$which_domain_id;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header Host $host;
    proxy_send_timeout 120s;
    proxy_read_timeout 120s;
    keepalive_timeout 0;
}
```

在配置root的时候可以参考下面

```bash
server {
    listen       80;
    server_name  ~^api(?<which_domain_id>\d*)\.domain\.com$;
    root  /var/www/api.domain.com/$which_domain_id/public/;
    index  index.html index.htm index.php;

    error_log   logs/api.domain.access.log main;
    error_log   logs/api.domain.error.log;

    client_max_body_size 3M;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        fastcgi_pass   php:9000;
        fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include        fastcgi_params;
    }
}
```

最后声明这个`which_domain_id`只是我这里的需要可以用作id操作，你可以改为字符串参数

文章参考：http://nginx.org/en/docs/http/server\_names.html
