---
title: "使用Paros监控iPhone发出的HTTP请求"
date: "2025-06-17 14:43:22"
slug: "shi-yong-paros-jian-kong-iphone-fa-chu-de-http-qing-qiu"
categories: ["技术"]
tags: ["Paros", "iOS"]
aliases:
  - "/2025/06/17/使用Paros监控iPhone发出的HTTP请求/"
  - "/2025/06/17/使用Paros监控iPhone发出的HTTP请求.html"
  - "/使用Paros监控iPhone发出的HTTP请求/"
  - "/使用Paros监控iPhone发出的HTTP请求.html"
  - "/2025/06/17/shi-yong-paros-jian-kong-iphone-fa-chu-de-http-qing-qiu/"
  - "/2025/06/17/shi-yong-paros-jian-kong-iphone-fa-chu-de-http-qing-qiu.html"
  - "/shi-yong-paros-jian-kong-iphone-fa-chu-de-http-qing-qiu.html"
---
电脑上的许多软件可以监控浏览器发出的HTTP请求, iPhone上有许多连网程序但没有自带软件可以实现监控, 为了方便测试这些请求是否正确而省去在程序中记录请求日志并逐一查找的麻烦, 可以利用Paros这个监控软件来实现.

以下是实现在Mac上监控iPhone发出的HTTP请求的具体步骤:

1. 查看无线局域网IP:

```bash
davidzhang@davidzhang:~/Downloads/tools$ ifconfig
```

2. 安装Paros

下载安装直接运行可执行文件即可，有两个文件，一个是.bat文件，一个是.sh文件，可以根据自己系统的环境不同运行不同的文件

下载地址1：http://sourceforge.net/projects/paros/

下载地址2：http://vdisk.weibo.com/s/G6wyY

3. 设置Paros本地代理:

Paros->Tools->Options->Local proxy, Address填上”169.254.242.107″, 端口默认为8080

4. 设置iPhone上网代理:

iPhone上: 设置->WiFi找到链接的网络->下拉找到HTTP代理->->手动->服务器填”169.254.242.107″, 端口填”8080″

5. 查看HTTP请求:

iPhone打开访问任何连网程序, 可以在Paros的Sites下看到访问的网站, 右边可以选Reques/Response等信息.
