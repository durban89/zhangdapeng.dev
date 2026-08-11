---
title: "Ubuntu 14.04 LTS Wifi/Network 网络连接,输入法状态没有了,很可能是这样子的"
date: "2025-06-30 15:57:30"
slug: "ubuntu-1404-lts-wifinetwork-wang-luo-lian-jie-shu-ru-fa-zhuang-tai-mei-you-le-hen-ke-neng-shi-zhe-yang-zi-de"
categories: ["技术"]
tags: ["Ubuntu", "Linux"]
aliases:
  - "/2025/06/30/Ubuntu-14.04-LTS-Wifi/Network-网络连接,输入法状态没有了,很可能是这样子的/"
  - "/2025/06/30/Ubuntu-14.04-LTS-Wifi/Network-网络连接,输入法状态没有了,很可能是这样子的.html"
  - "/Ubuntu-14.04-LTS-Wifi/Network-网络连接,输入法状态没有了,很可能是这样子的/"
  - "/Ubuntu-14.04-LTS-Wifi/Network-网络连接,输入法状态没有了,很可能是这样子的.html"
  - "/2025/06/30/Ubuntu-14-04-LTS-Wifi-Network-网络连接-输入法状态没有了-很可能是这样子的/"
  - "/2025/06/30/Ubuntu-14-04-LTS-Wifi-Network-网络连接-输入法状态没有了-很可能是这样子的.html"
  - "/2025/06/30/ubuntu-1404-lts-wifinetwork-wang-luo-lian-jie-shu-ru-fa-zhuang-tai-mei-you-le-hen-ke-ne/"
  - "/2025/06/30/ubuntu-1404-lts-wifinetwork-wang-luo-lian-jie-shu-ru-fa-zhuang-tai-mei-you-le-hen-k.html"
  - "/ubuntu-1404-lts-wifinetwork-wang-luo-lian-jie-shu-ru-fa-zhuang-tai-mei-you-le-hen-ke-neng-shi-.html"
---
Ubuntu 14.04 LTS Wifi/Network 网络连接,输入法状态没有了,很可能是这样子的:

网络上的大概都很久远了,也许我这个也是很久远了,但是可以尝试一下.

> Google chrome wanna remove 3 packages: Ubuntu-Desktop,
> Indicator-application and network-management-indicator before install so
> after install it you will be confused LOL

这个引自一篇外文的文章:

解决办法是:

```bash
sudo apt-get install indicator-application
```

不信的自己测试一下好了.

