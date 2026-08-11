---
title: "Django 执行 uwsgi进行自动删除进程id并进行重启  防止多个进行 导致服务器挂掉"
date: "2025-06-20 14:13:23"
slug: "django-zhi-xing-uwsgi-jin-xing-zi-dong-shan-chu-jin-cheng-id-bing-jin-xing-chong-qi-fang-zhi-duo-ge-jin-xing-dao-zhi-fu-wu-qi-gua-diao"
categories: ["技术"]
tags: ["Django", "uWSGI"]
aliases:
  - "/2025/06/20/Django-执行-uwsgi进行自动删除进程id并进行重启-防止多个进行-导致服务器挂掉/"
  - "/2025/06/20/Django-执行-uwsgi进行自动删除进程id并进行重启-防止多个进行-导致服务器挂掉.html"
  - "/Django-执行-uwsgi进行自动删除进程id并进行重启-防止多个进行-导致服务器挂掉/"
  - "/Django-执行-uwsgi进行自动删除进程id并进行重启-防止多个进行-导致服务器挂掉.html"
  - "/2025/06/20/django-zhi-xing-uwsgi-jin-xing-zi-dong-shan-chu-jin-cheng-id-bing-jin-xing-chong-qi-fan/"
  - "/2025/06/20/django-zhi-xing-uwsgi-jin-xing-zi-dong-shan-chu-jin-cheng-id-bing-jin-xing-chong-qi.html"
  - "/django-zhi-xing-uwsgi-jin-xing-zi-dong-shan-chu-jin-cheng-id-bing-jin-xing-chong-qi-fang-zhi-d.html"
---
django 执行 uwsgi进行自动删除进程id并进行重启  防止多个进行 导致服务器挂掉

最近使用django+uwsgi+虚拟机（ubuntu），每次进行uwsgi重启的时候都会增加一个进程的，导致自己的mysql无意间挂掉了，莫名其妙，结果才发现，有大量的uwsgi的进程，但是每次启动的时候都去删除，手动肯定很麻烦，于是自己就google后，写了一个自己的脚本。

脚本如下，仅供参考

```bash
#!/bin/sh
NAME="walkerfree"
if [ ! -n "$NAME" ];then
    echo "no arguments"
    exit;
fi

echo $NAME
ID=`ps -ef | grep "$NAME" | grep -v "$0" | grep -v "grep" | awk '{print $2}'`
echo $ID
echo "################################################"
for id in $ID
do
kill -9 $id
echo "kill $id"
done
echo  "################################################"
uwsgi --ini /usr/local/etc/uwsgi/walkerfree-uwsgi.ini
```

