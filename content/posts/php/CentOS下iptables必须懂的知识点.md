---
title: "CentOS下iptables必须懂的知识点"
date: "2025-06-20 09:51:58"
slug: "centos-xia-iptables-bi-xu-dong-de-zhi-shi-dian"
categories: ["技术"]
tags: ["Linux", "CentOS"]
aliases:
  - "/2025/06/20/CentOS下iptables必须懂的知识点/"
  - "/2025/06/20/CentOS下iptables必须懂的知识点.html"
  - "/CentOS下iptables必须懂的知识点/"
  - "/CentOS下iptables必须懂的知识点.html"
  - "/2025/06/20/centos-xia-iptables-bi-xu-dong-de-zhi-shi-dian/"
  - "/2025/06/20/centos-xia-iptables-bi-xu-dong-de-zhi-shi-dian.html"
  - "/centos-xia-iptables-bi-xu-dong-de-zhi-shi-dian.html"
---
1. 基本操作：启用防火墙  
这里的指令都是从 Linux 控制终端（命令行）直接输入的。  
输入下面的两条指令来启用防火墙：

```bash
chkconfig iptables on
service iptables start
```

其中上一条是将 iptables 加入到系统服务，随系统启动而启动；下一条是直接启动 iptables 服务。  
重起防火墙：

```bash
service iptables restart
```

停止防火墙：

```bash
service iptables stop
```

2,配置 /etc/sysconfig/iptables 文件  
虽然可以通过 iptables 指令来编辑防火墙规则，可是对于大量的规则来说一条一条的输入总是很麻烦，实际上可以直接按照正确格式编辑 iptables 的配置文件，然后重新加载 iptables 即可使之生效。  
要编辑 /etc/sysconfig/iptables，输入：

```bash
# vi /etc/sysconfig/iptables
```

可以看到文件中存储的前述默认规则显示如下：

```bash
*filter
:INPUT ACCEPT [0:0]
:FORWARD ACCEPT [0:0]
:OUTPUT ACCEPT [0:0]
:RH-Firewall-1-INPUT - [0:0]
-A INPUT -j RH-Firewall-1-INPUT
-A FORWARD -j RH-Firewall-1-INPUT
-A RH-Firewall-1-INPUT -i lo -j ACCEPT
-A RH-Firewall-1-INPUT -p icmp --icmp-type any -j ACCEPT
-A RH-Firewall-1-INPUT -p udp --dport 5353 -d 1.2.3.4 -j ACCEPT
-A RH-Firewall-1-INPUT -p udp -m udp --dport 53 -j ACCEPT
-A RH-Firewall-1-INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 22 -j ACCEPT
-A RH-Firewall-1-INPUT -m state --state NEW -m tcp -p tcp --dport 53 -j ACCEPT
-A RH-Firewall-1-INPUT -j REJECT --reject-with icmp-host-prohibited
COMMIT
```

其中 -j 参数表示 jump 跳转到。  
  
可以看到其中的规则形式与我们通过命令行来输入的规则是一样的，因为启用 iptables 的时候就是将此文件中的指令一行一行的自动加载的，就像批处理一样。
