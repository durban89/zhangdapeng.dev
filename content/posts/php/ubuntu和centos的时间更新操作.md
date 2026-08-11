---
title: "ubuntu和centos的时间更新操作"
date: "2025-05-29 10:38:04"
slug: "ubuntu-he-centos-de-shi-jian-geng-xin-cao-zuo"
categories: ["技术"]
tags: ["Linux"]
aliases:
  - "/2025/05/29/ubuntu和centos的时间更新操作/"
  - "/2025/05/29/ubuntu和centos的时间更新操作.html"
  - "/ubuntu和centos的时间更新操作/"
  - "/ubuntu和centos的时间更新操作.html"
  - "/2025/05/29/ubuntu-he-centos-de-shi-jian-geng-xin-cao-zuo/"
  - "/2025/05/29/ubuntu-he-centos-de-shi-jian-geng-xin-cao-zuo.html"
  - "/ubuntu-he-centos-de-shi-jian-geng-xin-cao-zuo.html"
---
在Ubuntu Server上，设置NTP时间同步非常简单，就如下几步：

第一，可以先进行手动更新一次时间（可选）：

`sudo ntpdate ntp.ubuntu.com`

第二，创建一个定时执行的文件：

`sudo vim /etc/cron.daily/ntpdate`

然后在其中添加一行：`ntpdate ntp.ubuntu.com`，保存退出。

第三，修改这个定时执行文件的权限，使其变成可执行文件：

`sudo chmod 755 /etc/cron.daily/ntpdate`

==========================================

下面解析一下,第一句是把当前时区调整为上海就是+8区,想改其他时区也可以去看看/usr/share/zoneinfo目录;

然后第二句是利用ntpdate同步标准时间.

没有安装ntpdate的可以yum一下:

`yum install -y ntpdate`

加入定时计划任务，每隔10分钟同步一下时钟

`crontab -e`

`0-59/10 * * * * /usr/sbin/ntpdate us.pool.ntp.org | logger -t NTP`

这样，我们就可以来解决在CentOS系统中时间不准确的问题了。

 
如果执行命令出现一下错误
{% blockquote %}
　　1.提示：7 Dec 19:24:55 ntpdate[2120]: the NTP socket is in use, exiting

　　这个是你linux机器上已经存在这个进程，输入：ps -ef | grep ntpd

　　Kill掉ntp的进程

　　2.提示：No Server suitable for synchronization found

　　这个是最容易出现的问题，比较常见的是配置好服务器并启动服务器进程后，马上

　　启动客户进程，那么客户进程就会报错。解决方法是，在大约3-5分钟以后启动进程就行
{% endblockquote %}
