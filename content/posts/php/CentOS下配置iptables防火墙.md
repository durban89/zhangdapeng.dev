---
title: "CentOS下配置iptables防火墙"
date: "2025-06-23 15:27:59"
slug: "centos-xia-pei-zhi-iptables-fang-huo-qiang"
categories: ["技术"]
tags: ["CentOS", "Linux"]
aliases:
  - "/2025/06/23/CentOS下配置iptables防火墙/"
  - "/2025/06/23/CentOS下配置iptables防火墙.html"
  - "/CentOS下配置iptables防火墙/"
  - "/CentOS下配置iptables防火墙.html"
  - "/2025/06/23/centos-xia-pei-zhi-iptables-fang-huo-qiang/"
  - "/2025/06/23/centos-xia-pei-zhi-iptables-fang-huo-qiang.html"
  - "/centos-xia-pei-zhi-iptables-fang-huo-qiang.html"
---
在CentOS下配置iptables防火墙，是非常必要的。来我们学习如何配置！

在Linux中设置防火墙，以CentOS为例，打开iptables的配置文件：

```bash
vi /etc/sysconfig/iptables
```

通过/etc/init.d/iptables status命令查询是否有打开80端口，如果没有可通过两种方式处理：

1.修改vi /etc/sysconfig/iptables命令添加使防火墙开放80端口

```bash
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 80 -j ACCEPT
```

2.关闭/开启/重启防火墙

```bash
/etc/init.d/iptables stop   #start 开启   #restart 重启
```

3.永久性关闭防火墙

```bash
chkconfig --level 35 iptables off   /etc/init.d/iptables stop   iptables -P INPUT DROP
```

4.打开主动模式21端口

```bash
iptables -A INPUT -p tcp --dport 21 -j ACCEPT
```

5.打开被动模式49152~65534之间的端口

```bash
iptables -A INPUT -p tcp --dport 49152:65534 -j ACCEPT   
iptables -A INPUT -i lo -j ACCEPT   
iptables -A INPUT -m state --state ESTABLISHED -j ACCEPT
```

注意：

一定要给自己留好后路,留VNC一个管理端口和SSh的管理端口

需要注意的是，你必须根据自己服务器的情况来修改这个文件。

全部修改完之后重启iptables:

```bash
service iptables restart
```

你可以验证一下是否规则都已经生效：

```bash
iptables -L -a
```

