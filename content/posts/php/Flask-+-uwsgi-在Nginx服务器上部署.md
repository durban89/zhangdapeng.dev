---
title: "Flask + uwsgi 在Nginx服务器上部署"
date: "2025-06-30 14:30:51"
slug: "flask-uwsgi-zai-nginx-fu-wu-qi-shang-bu-shu"
categories: ["技术"]
tags: ["Flask", "uWSGI", "NGINX"]
aliases:
  - "/2025/06/30/Flask-+-uwsgi-在Nginx服务器上部署/"
  - "/2025/06/30/Flask-+-uwsgi-在Nginx服务器上部署.html"
  - "/Flask-+-uwsgi-在Nginx服务器上部署/"
  - "/Flask-+-uwsgi-在Nginx服务器上部署.html"
  - "/2025/06/30/flask-uwsgi-zai-nginx-fu-wu-qi-shang-bu-shu/"
  - "/2025/06/30/flask-uwsgi-zai-nginx-fu-wu-qi-shang-bu-shu.html"
  - "/flask-uwsgi-zai-nginx-fu-wu-qi-shang-bu-shu.html"
---
Nginx配置如下：

```bash
server {
    listen   80; ## listen for ipv4; this line is default and implied
    #listen   [::]:80 default ipv6only=on; ## listen for ipv6

    server_name flask.blog.gowhich.dev;

    location / {
        include uwsgi_params;
        uwsgi_pass 0.0.0.0:3032;
    }
}
```

uwsgi 【uwsgi.xml】配置如下：

```bash
<uwsgi>
    <chdir>/xxx/xxx/python/python_project/flask_blog_small_1</chdir>
    <module>flask_blog</module>
    <callable>app</callable>
    <socket>0.0.0.0:3032</socket> 
    <daemonize>/var/log/uwsgi.flask.blog.log</daemonize>
    <master/>
    <processes>4</processes>
    <memory-report/>
</uwsgi>
```

启动uwsgi和nginx便可完成部署;

这里的端口号只要保证与uwsgi的端口号一直就可以，不用考虑flask自己运行的脚本


