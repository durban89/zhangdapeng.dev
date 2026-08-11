---
title: "CentOS搭建 使用uwsgi+nginx 配置django"
date: "2025-06-20 11:07:34"
slug: "centos-da-jian-shi-yong-uwsginginx-pei-zhi-django"
categories: ["技术"]
tags: ["CentOS", "Django", "uWSGI", "NGINX"]
aliases:
  - "/2025/06/20/CentOS搭建-使用uwsgi+nginx-配置django/"
  - "/2025/06/20/CentOS搭建-使用uwsgi+nginx-配置django.html"
  - "/CentOS搭建-使用uwsgi+nginx-配置django/"
  - "/CentOS搭建-使用uwsgi+nginx-配置django.html"
  - "/2025/06/20/CentOS搭建-使用uwsgi-nginx-配置django/"
  - "/2025/06/20/CentOS搭建-使用uwsgi-nginx-配置django.html"
  - "/2025/06/20/centos-da-jian-shi-yong-uwsginginx-pei-zhi-django/"
  - "/2025/06/20/centos-da-jian-shi-yong-uwsginginx-pei-zhi-django.html"
  - "/centos-da-jian-shi-yong-uwsginginx-pei-zhi-django.html"
---
记录这篇文章的前提是，uwsgi的环境，nginx的环境和django框架都已经搭建完毕了。不会的自己可以去google

1，项目创建

```bash
sudo django-admin.py startproject walkerfree
```

2,配置nginx server

```nginx
server
        {
                listen       80;
                server_name www.walkerfree.com;
                index index.html index.htm default.html default.htm;
                root  /home/wwwroot/walkerfree/walkerfree;

                access_log /home/wwwlogs/www.walkerfree.access.log;
                error_log /home/wwwlogs/www.walkerfree.error.log;

                location / {
                        include uwsgi_params;
                        uwsgi_pass      unix://tmp/walkerfree.socket;
                }

                location ^~ /static/ {
                        root    /home/wwwroot/walkerfree/;
                }

                location ~ ^.+\.(gif|jpg|png|ico|jpeg)$ {
                        expires 3d;
                }

                location ~ ^.+\.(css|js)$ {
                   expires 12h;
                }
        }
```

3,配置项目的uwsgi启动设置

```ini
[uwsgi]
socket = /tmp/walkerfree.socket
#http=127.0.0.1:9090
chdir=/home/wwwroot/walkerfree
module=walkerfree.wsgi
master=True
pidfile=/tmp/uwsgi.pid
vacuum=True
max-requests=5000
daemonize=/home/wwwlogs/walkerfree-uwsgi.log
```

4，启动uwsgi，启动nginx(root角色)

```bash
nginx -s reload
uwsgi --ini /usr/local/etc/uwsgi/walkerfree-uwsgi.ini
```

5,启动成功
