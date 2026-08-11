---
title: "SVN Can't connect to host问题"
date: "2025-06-20 10:36:21"
slug: "svn-cant-connect-to-host-wen-ti"
categories: ["技术"]
tags: ["SVN"]
aliases:
  - "/2025/06/20/SVN-Can't-connect-to-host问题/"
  - "/2025/06/20/SVN-Can't-connect-to-host问题.html"
  - "/SVN-Can't-connect-to-host问题/"
  - "/SVN-Can't-connect-to-host问题.html"
  - "/2025/06/20/SVN-Can-connect-to-host问题/"
  - "/2025/06/20/SVN-Can-connect-to-host问题.html"
  - "/2025/06/20/svn-cant-connect-to-host-wen-ti/"
  - "/2025/06/20/svn-cant-connect-to-host-wen-ti.html"
  - "/svn-cant-connect-to-host-wen-ti.html"
---
> 当出现'目标机器积极拒绝，无法连接'或svn: Can't connect to host ...时，应依次检查下面各项
>
> 1，服务器有没有运行，有没有打开相应端口
>
> 如果服务器是svnserve，检查有没有运行svnserve，有没有打开3690端口
>
> 如果服务器是apache，检查apahce是否运行，是否打开80端口
>
> 检查时可以在服务器运行netstat -na看看相应端口是否在LISTEN
>
> 2，防火墙有没有开放相应端口
>
> 3，客户端是否可以连接服务器的相应端口
>
> 使用命令telnet 服务器IP 相应端口
>
> 如：telnet 192.168.0.1 3690

我的服务器是ubuntu的，里面使用的是ufw来作防火墙的，因此可以判定我的这儿端口没有开

执行

```bash
sudo ufw allow 3690
```
