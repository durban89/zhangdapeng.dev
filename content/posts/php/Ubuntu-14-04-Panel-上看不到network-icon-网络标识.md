---
title: "Ubuntu 14.04  Panel 上看不到network icon[网络标识]"
date: "2025-06-30 15:15:42"
slug: "ubuntu-1404-panel-shang-kan-bu-dao-network-icon-wang-luo-biao-shi"
categories: ["技术"]
tags: ["Ubuntu"]
aliases:
  - "/2025/06/30/Ubuntu-14.04-Panel-上看不到network-icon[网络标识]/"
  - "/2025/06/30/Ubuntu-14.04-Panel-上看不到network-icon[网络标识].html"
  - "/Ubuntu-14.04-Panel-上看不到network-icon[网络标识]/"
  - "/Ubuntu-14.04-Panel-上看不到network-icon[网络标识].html"
  - "/2025/06/30/Ubuntu-14-04-Panel-上看不到network-icon-网络标识/"
  - "/2025/06/30/Ubuntu-14-04-Panel-上看不到network-icon-网络标识.html"
  - "/2025/06/30/ubuntu-1404-panel-shang-kan-bu-dao-network-icon-wang-luo-biao-shi/"
  - "/2025/06/30/ubuntu-1404-panel-shang-kan-bu-dao-network-icon-wang-luo-biao-shi.html"
  - "/ubuntu-1404-panel-shang-kan-bu-dao-network-icon-wang-luo-biao-shi.html"
---
之前有写过一篇类似的文章，但是如果你安装了google的话，会依然有这种问题出现，主要问题是,在安装google的时候他卸载了**indicator-application**，所以网络标识消失了，就连输入法或者其他的第三方的标识也没有了。解决的办法就是重新安装回来就好了。

```bash
sudo apt-get install indicator-application
```


