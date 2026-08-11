---
title: "Mac系统下端口占用解决方案(netstat/lsof)"
date: "2025-07-10 11:52:54"
slug: "mac-xi-tong-xia-duan-kou-zhan-yong-jie-jue-fang-an-netstatlsof"
categories: ["技术"]
tags: ["MacOS"]
aliases:
  - "/2025/07/10/Mac系统下端口占用解决方案(netstat/lsof)/"
  - "/2025/07/10/Mac系统下端口占用解决方案(netstat/lsof).html"
  - "/Mac系统下端口占用解决方案(netstat/lsof)/"
  - "/Mac系统下端口占用解决方案(netstat/lsof).html"
  - "/2025/07/10/Mac系统下端口占用解决方案-netstat-lsof/"
  - "/2025/07/10/Mac系统下端口占用解决方案-netstat-lsof.html"
  - "/2025/07/10/mac-xi-tong-xia-duan-kou-zhan-yong-jie-jue-fang-an-netstatlsof/"
  - "/2025/07/10/mac-xi-tong-xia-duan-kou-zhan-yong-jie-jue-fang-an-netstatlsof.html"
  - "/mac-xi-tong-xia-duan-kou-zhan-yong-jie-jue-fang-an-netstatlsof.html"
---
最近启动nginx，总是提示我8080端口内占用了，但是我就想知道具体是哪个程序占用了这个端口，这个技术点困扰了我很久，一想我又不搞服务器部署，出问题肯定会有人处理的，怎奈我自己的服务器也遇到了这个问题，没办法，必须解决掉。本以为都是命令直接搜索一个拿来用用不就可以了嘛，但是！但是！但是！在不同系统的环境下，命令的使用方式居然不一样。

先看个常用的命令

```bash
$ netstat -anvp |grep 8080
netstat: option requires an argument -- p
Usage:	netstat [-AaLlnW] [-f address_family | -p protocol]
	netstat [-gilns] [-f address_family]
	netstat -i | -I interface [-w wait] [-abdgRtS]
	netstat -s [-s] [-f address_family | -p protocol] [-w wait]
	netstat -i | -I interface -s [-f address_family | -p protocol]
	netstat -m [-m]
	netstat -r [-Aaln] [-f address_family]
	netstat -rs [-s]
```

这个命令提示我`netstat: option requires an argument -- p`

其实是缺少协议

在Mac上正确使用的方法是：即-f需要加上地址族，-p需要加上协议TCP或者UDP等

* 如果要查询inet - 命令使用 `netstat -anvf inet`
* 如果要查询tcp - 命令使用 `netstat -anvp tcp`
* 如果要查询udp - 命令使用 `netstat -anvp udp`

于是将上面的命令调整为下面

```bash
$ netstat -anvp tcp |grep 8080
tcp4       0      0  172.18.0.71.56891      180.163.32.172.8080    ESTABLISHED 262144 131920  51388      0
tcp4       0      0  172.18.0.71.56816      114.221.144.160.8080   ESTABLISHED 262144 131072  98268      0
tcp46      0      0  *.8080                 *.*                    LISTEN      131072 131072  45216      0
```

当然`netstat`只是查找占用端口命令中的一个命令而已

下面看看另外一个命令`lsof`

**lsof** 是一个列出当前系统打开文件的工具

使用 lsof 如果不传任何参数会列出所有端口占用的列表，不过不建议直接使用lsof，太多看不过来 可以使用`lsof | less`，然后一下一下点击空格键，会一屏一屏的列出

如果查询占用的端口号，可以使用如下命令

```bash
lsod -i:8080
```

比如我当前占用8080端口的程序

```bash
$ lsof -i:8080
COMMAND     PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
QQBrowser 51388 durban  106u  IPv4 0xeed752c692289c43      0t0  TCP 172.18.0.71:56891->180.163.32.172:http-alt (ESTABLISHED)
QQBrowser 51388 durban  115u  IPv4 0xeed752c692289c43      0t0  TCP 172.18.0.71:56891->180.163.32.172:http-alt (ESTABLISHED)
QQ        98268 durban   17u  IPv4 0xeed752c6923d2213      0t0  TCP 172.18.0.71:56816->114.221.144.160:http-alt (ESTABLISHED)
QQ
```

这里只要拿到PID就可以进行kill或者是其他的操作了。
