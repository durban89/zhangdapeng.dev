---
title: "Ubuntu14.04 出现输入法或者网络连接不显示的主要问题，在这里"
date: "2025-06-30 15:15:26"
slug: "ubuntu1404-chu-xian-shu-ru-fa-huo-zhe-wang-luo-lian-jie-bu-xian-shi-de-zhu-yao-wen-ti-zai-zhe-li"
categories: ["技术"]
tags: ["Ubuntu"]
aliases:
  - "/2025/06/30/Ubuntu14.04-出现输入法或者网络连接不显示的主要问题，在这里/"
  - "/2025/06/30/Ubuntu14.04-出现输入法或者网络连接不显示的主要问题，在这里.html"
  - "/Ubuntu14.04-出现输入法或者网络连接不显示的主要问题，在这里/"
  - "/Ubuntu14.04-出现输入法或者网络连接不显示的主要问题，在这里.html"
  - "/2025/06/30/Ubuntu-14-04-出现输入法或者网络连接不显示的主要问题-在这里/"
  - "/2025/06/30/Ubuntu-14-04-出现输入法或者网络连接不显示的主要问题-在这里.html"
  - "/2025/06/30/ubuntu1404-chu-xian-shu-ru-fa-huo-zhe-wang-luo-lian-jie-bu-xian-shi-de-zhu-yao-wen-ti-z/"
  - "/2025/06/30/ubuntu1404-chu-xian-shu-ru-fa-huo-zhe-wang-luo-lian-jie-bu-xian-shi-de-zhu-yao-wen-.html"
  - "/ubuntu1404-chu-xian-shu-ru-fa-huo-zhe-wang-luo-lian-jie-bu-xian-shi-de-zhu-yao-wen-ti-zai-zhe-.html"
---
可以忠诚的告诉你，如果你发现你安装完ubuntu 14.04后，发现输入法或者网络链接的状态没有了，或者两个都没有了，我来告诉你，是因为什么，也是经验啊，是因为有个叫nm-appet.desktop的文件导致的，不行你可以打看自己看下，在`/etc/xdg/autostart/`下面，发现有一行是没有提示的，居然都没有空格，肯定不符合desktop的标准，说明是出了问题的，可以使用下面这行代码，在使用之前需要自己进行备份一样，以防万一。

```bash
[Desktop Entry]
Name=Network
Comment=Manage your network connections
Icon=nm-device-wireless
Exec=nm-applet
Terminal=false
Type=Application
NoDisplay=true
NotShowIn=KDE;
X-GNOME-Bugzilla-Bugzilla=GNOME
X-GNOME-Bugzilla-Product=NetworkManager
X-GNOME-Bugzilla-Component=general
X-GNOME-Autostart-enabled=true
```

保存后重新启动试试吧。

