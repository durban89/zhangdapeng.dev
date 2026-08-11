---
title: "Mac下配置cocos2d-x开发环境"
date: "2025-06-24 11:24:10"
slug: "mac-xia-pei-zhi-cocos2d-x-kai-fa-huan-jing"
categories: ["技术"]
tags: ["Cocos2d-x"]
aliases:
  - "/2025/06/24/Mac下配置cocos2d-x开发环境/"
  - "/2025/06/24/Mac下配置cocos2d-x开发环境.html"
  - "/Mac下配置cocos2d-x开发环境/"
  - "/Mac下配置cocos2d-x开发环境.html"
  - "/2025/06/24/mac-xia-pei-zhi-cocos2d-x-kai-fa-huan-jing/"
  - "/2025/06/24/mac-xia-pei-zhi-cocos2d-x-kai-fa-huan-jing.html"
  - "/mac-xia-pei-zhi-cocos2d-x-kai-fa-huan-jing.html"
---
### [一、下载cocos2d-x](#1)

[http://code.google.com/p/cocos2d-x/downloads/list](https://code.google.com/p/cocos2d-x/downloads/list)

cocos2d-x-3.0alpha0.zip  
  
我们可以看到最新版本的3.0alpha0，这个版本提供了一个用python命令来建立各平台的项目，十分便利  
  
下载，解压（建议解压到主目录下的）

### [二、下载python](#2)

[http://www.python.org/getit/](https://www.python.org/getit/)  
  
建议选择2.7.5版本的下载  
  
Python 2.7.5 Mac OS X 64-bit/32-bit x86-64/i386 Installer  
Python 2.7.5 Mac OS X 32-bit i386/PPC Installer  
  
下载，安装，然后在终端直接输入python，如果出现版本信息则安装成功

### [三、建立cocos2d-x项目](#3)

进入终端，执行以下命令

```bash
unzip cocos2d-x-3.0alpha0.zip
cd cocos2d-x-3.0alpha0
python ./create-multi-platform-projects.py -p walker -k com.walkerfree.walker -l cpp
```

`create-multi-platform-projects.py`要求提供3个参数（工程名：我这里是walker，包名：我这里是`com.walkerfree.walker`，语言：`cpp | js | lua`）  
  
执行成功会显示以下信息

```bash
proj.ios        : Done!
proj.android        : Done!
proj.win32        : Done!
proj.mac        : Done!
proj.linux        : Done!
New project has been created in this path: /Users/davidzhang/Downloads/ios/cocos2d/cocos2d-x-3.0alpha0/projects/walker
Have Fun!
```

进入walker目录，你可以看到这些项目

```bash
davidzhang@192:~/Downloads/ios/cocos2d/cocos2d-x-3.0alpha0$ cd projects/
davidzhang@192:~/Downloads/ios/cocos2d/cocos2d-x-3.0alpha0/projects$ ll
total 0
drwxr-xr-x   3 davidzhang  staff   102 10  8 15:51 .
drwx------@ 33 davidzhang  staff  1122 10  8 15:51 ..
drwxr-xr-x   8 davidzhang  staff   272  9 21 15:58 walker
davidzhang@192:~/Downloads/ios/cocos2d/cocos2d-x-3.0alpha0/projects$ cd walker/
davidzhang@192:~/Downloads/ios/cocos2d/cocos2d-x-3.0alpha0/projects/walker$ ll
total 0
drwxr-xr-x   8 davidzhang  staff  272  9 21 15:58 .
drwxr-xr-x   3 davidzhang  staff  102 10  8 15:51 ..
drwxr-xr-x   6 davidzhang  staff  204  9 21 15:58 Classes
drwxr-xr-x   6 davidzhang  staff  204  9 21 15:58 Resources
drwxr-xr-x  15 davidzhang  staff  510  9 21 15:58 proj.android
drwxr-xr-x   6 davidzhang  staff  204 10  8 15:53 proj.ios_mac
drwxr-xr-x   7 davidzhang  staff  238  9 21 15:58 proj.linux
drwxr-xr-x  11 davidzhang  staff  374  9 21 15:58 proj.win32
davidzhang@192:~/Downloads/ios/cocos2d/cocos2d-x-3.0alpha0/projects/walker$
```

怎么样，全平台都给你搭好了，而且共用一个Classes文件夹，也就是说你在一个平台更新了代码，全平台都得到了更新。

### [四、编辑ios项目](#4)

进入`walker/proj.ios_mac/`目录，直接双击打开HelloCpp.xcodeproj（别说你没装xcode，我这里是Xcode5）  
  
然后点run就可以跑起来了

参考文章：<http://www.cnblogs.com/ookcode/p/3214164.html>

