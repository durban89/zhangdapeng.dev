---
title: "uWSGI启动和停止脚本"
date: "2025-06-12 11:46:37"
slug: "uwsgi-qi-dong-he-ting-zhi-jiao-ben"
categories: ["技术"]
tags: ["uWSGI"]
aliases:
  - "/2025/06/12/uWSGI启动和停止脚本/"
  - "/2025/06/12/uWSGI启动和停止脚本.html"
  - "/uWSGI启动和停止脚本/"
  - "/uWSGI启动和停止脚本.html"
  - "/2025/06/12/uwsgi启动和停止脚本/"
  - "/2025/06/12/uwsgi启动和停止脚本.html"
  - "/2025/06/12/uwsgi-qi-dong-he-ting-zhi-jiao-ben/"
  - "/2025/06/12/uwsgi-qi-dong-he-ting-zhi-jiao-ben.html"
  - "/uwsgi-qi-dong-he-ting-zhi-jiao-ben.html"
---
一晚上写的shell的脚本

uwsgi启动和停止脚本（代码如下）：

```sh
#!/bin/bash
if [ ! -n "$1" ]
then
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
    exit 0
fi

if [ $1 = start ]
then
    psid=`ps aux | grep "uwsgi" | grep -v "grep" | wc -l`
    if [ $psid -gt 4 ]
    then
        echo "uwsgi is running!"
        exit 0
    else
        uwsgi /etc/uwsgi.ini
        echo "Start uwsgi service [OK]"
    fi
    

elif [ $1 = stop ];then
    killall -9 uwsgi
    echo "Stop uwsgi service [OK]"
elif [ $1 = restart ];then
    killall -9 uwsgi
    /usr/bin/uwsgi --ini /etc/uwsgi.ini
    echo "Restart uwsgi service [OK]"

else
    echo "Usages: sh uwsgiserver.sh [start|stop|restart]"
fi
```
