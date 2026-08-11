---
title: "Android SDK Manager 下载缓慢解决办法"
date: "2025-06-27 14:14:40"
slug: "android-sdk-manager-xia-zai-huan-man-jie-jue-ban-fa"
categories: ["技术"]
tags: ["Android"]
aliases:
  - "/2025/06/27/Android-SDK-Manager-下载缓慢解决办法/"
  - "/2025/06/27/Android-SDK-Manager-下载缓慢解决办法.html"
  - "/Android-SDK-Manager-下载缓慢解决办法/"
  - "/Android-SDK-Manager-下载缓慢解决办法.html"
  - "/2025/06/27/android-sdk-manager-xia-zai-huan-man-jie-jue-ban-fa/"
  - "/2025/06/27/android-sdk-manager-xia-zai-huan-man-jie-jue-ban-fa.html"
  - "/android-sdk-manager-xia-zai-huan-man-jie-jue-ban-fa.html"
---
在网上找了些资料，分析了下载Log，发现各个Package可以使用迅雷等工具下载。下载链接如下：

https://dl-ssl.google.com/android/repository/ + 包名

包名命名方式：

> Documentation for Android SDK: docs-xx_r0x.zip
>
> SDK Platform: android-xxx_r0x.zip
>
> Samples for SDK: samples-xx_r0x.zip
>
> ARM EABI v7a System Image: sysimg_armv7a-xx_r0x.zip
>
> Google API: google_apis-xx_r0x.zip
>
> Sources for Android SDK: sources-xx_r0x.zip

xx、x分别是API版本及版本号，例如 Android 4.4 API版本为19，版本号为1。那么其Sources for Android SDK对应的下载连接：

https://dl-ssl.google.com/android/repository/sources-19_r01.zip

下载好的包放入SDK下的temp目录，启动Android SDK Manager勾选对应的包，正常安装即可。

