---
title: "supervisor + uwsgi + flask"
date: "2025-07-04 11:48:04"
slug: "supervisor-uwsgi-flask"
categories: ["技术"]
tags: ["Supervisor", "uWSGI", "Flask"]
aliases:
  - "/2025/07/04/supervisor-+-uwsgi-+-flask/"
  - "/2025/07/04/supervisor-+-uwsgi-+-flask.html"
  - "/supervisor-+-uwsgi-+-flask/"
  - "/supervisor-+-uwsgi-+-flask.html"
  - "/2025/07/04/supervisor-uwsgi-flask/"
  - "/2025/07/04/supervisor-uwsgi-flask.html"
  - "/supervisor-uwsgi-flask.html"
---
supervisor启动flask项目中，配置了uwsgi，即通过supervisor启动uwsgi，uwsgi再启动flask项目  
这个过程中uwsgi是个坑

```xml
<uwsgi>
  <chdir>/relativeProjectPath</chdir>
  <module>wsgi_handler</module>
  <socket>/tmp/walkerfree-uwsgi.sock</socket> 
  <daemonize>/tmp/uwsgi.walkerfree.log</daemonize>
  <master>4</master>
  <chmod-socket>666</chmod-socket>
  <enable-threads />
  <processes>4</processes>
  <harakiri>30</harakiri>
  <workers>6</workers>
  <memory-report />
  <vacuum/>
</uwsgi>
```

这个是我的初始配置文件，如果单独使用uwsgi启动是没有问题的，但是放在supervisor就有问题，会启动很多个uwsgi进程，而且supersior也会报错  
我见到的错误如下几种  
1】ERROR (spawn error)  
2】BACKOFF Exited too quickly (process log may have details)

先给下最终的uwsgi配置方案,如下

```xml
<uwsgi>
  <chdir>relativeProjectPath</chdir>
  <module>wsgi_handler</module>
  <socket>/tmp/walkerfree_uwsgi.sock</socket> 
  <logto>/tmp/walkerfree_uwsgi.log</logto>
  <chmod-socket>666</chmod-socket>
  <enable-threads />
  <processes>1</processes>
  <harakiri>30</harakiri>
  <memory-report />
  <vacuum/>
</uwsgi>
```

具体有几个坑吧，我试了两种，具体有一下几个方法  
第一个:  
**修改daemonize为logto**  
第二个:  
去掉master【这项可以不用去掉，如果不起作用可以试试】  
去掉workers【这项可以不用去掉，如果不起作用可以试试】  
修改processes为1

supervisor中项目的配置如下

```ini
[program:walkerfree]
# http://supervisord.org/configuration.html#program-x-section-example
command=/projectPath/env/bin/uwsgi -x /projectPath/uwsgi.xml
autostart=true
autorestart=true
stdout_logfile=/projectPath/supervisor/out.log
stderr_logfile=/projectPath/supervisor/err.log
```
