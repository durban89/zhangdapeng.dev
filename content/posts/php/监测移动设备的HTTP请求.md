---
title: "监测移动设备的HTTP请求"
date: "2025-06-17 12:01:22"
slug: "jian-ce-yi-dong-she-bei-de-http-qing-qiu"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/17/监测移动设备的HTTP请求/"
  - "/2025/06/17/监测移动设备的HTTP请求.html"
  - "/监测移动设备的HTTP请求/"
  - "/监测移动设备的HTTP请求.html"
  - "/2025/06/17/jian-ce-yi-dong-she-bei-de-http-qing-qiu/"
  - "/2025/06/17/jian-ce-yi-dong-she-bei-de-http-qing-qiu.html"
  - "/jian-ce-yi-dong-she-bei-de-http-qing-qiu.html"
---
在PC上监测web页面的HTTP请求是一件非常简单的事，我们有大量的软件可以来做，甚至浏览器就自带了有这样功能的开发插件。但是在移动设备上就没那么简单了，没有软件，权限控制……下面将介绍2种监测移动设备HTTP请求的方式。

## [使用Charles](#1)

在连上WIFI的前提下，android和ios设备都可以通过Charles来监测HTTP请求，原理是通过Charles在PC上架设一个代理，手机访问这个代理，Charles记录网络请求。ios设备，在“设置”-“无线局域网络”里可以直接设置代理，而android没有设置代理的功能，需要取得root权限后安装第三方软件来实现。  
  
操作步骤：  
下载Charles（http://www.charlesproxy.com/download/），安装完成后打开软件  
通过菜单上的“Proxy”-“Proxy Settings…”，进入代理设置见面  
“Port”填默认的“8888”即可，勾选“Enable transparent HTTP proxying”，点“OK”确认  
设置手机的代理，端口（Port）写Charles中的端口设置，即“8888”，IP填你PC的IP地址  
用手机发起任意HTTP请求，Charles会弹出一个提示框，点“Allow”，好了HTTP请求都出现在Charles里了

全选所有请求，并选择右侧的“Chart”选项卡就能看到整个HTTP请求瀑布图了：

![](http://www.zhouqicf.com/wp-uploads/2012/01/charles.jpg)

Android手机设置代理的方式：  
安装“z4root”软件，进入软件后选择第二项，等待一段时间后，自动重启，取得root权限完成  
安装“Transparent Proxy”，进入“Proxy Host”设置PC的IP地址，进入“Proxy Port”设置端口号，即“8888”，勾选“Proxy”，设置完成

## [使用TCPDUMP和Wireshark](#2)

Android手机，可以使用TCPDUMP输出网络请求的LOG文件，然后用Wireshark打开该文件，进行统计分析。  
  
操作步骤：  
下载TCPDUMP（http://www.strazzere.com/android/tcpdump），放到D根目录盘下  
下载安装Wireshark（http://www.wireshark.org/）  
root手机，方法如上所述  
用usb连上手机  
打开命令行工具CMD，依次输入如下命令：  
adb push d:\tcpdump /data/local/tcpdump  
adb shell chmod 6755 /data/local/tcpdump  
adb shell tcpdump -p -vv -s 0 -w /sdcard/capture.pcap -Z root  
停止抓包：按Ctrl+c  
导出抓包得到的文件到d盘根目录：adb pull /sdcard/capture.pcap d:/  
双击capture.pcap文件，wireshark启动

![](http://www.zhouqicf.com/wp-uploads/2012/01/wireshark.jpg)

参考：http://www.zhouqicf.com/others/mobile-network-requests-monitor
