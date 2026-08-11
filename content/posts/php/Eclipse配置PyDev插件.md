---
title: "Eclipse配置PyDev插件"
date: "2025-06-12 09:40:36"
slug: "eclipse-pei-zhi-pydev-cha-jian"
categories: ["技术"]
tags: ["Eclipse"]
aliases:
  - "/2025/06/12/Eclipse配置PyDev插件/"
  - "/2025/06/12/Eclipse配置PyDev插件.html"
  - "/Eclipse配置PyDev插件/"
  - "/Eclipse配置PyDev插件.html"
  - "/2025/06/12/eclipse-pei-zhi-pydev-cha-jian/"
  - "/2025/06/12/eclipse-pei-zhi-pydev-cha-jian.html"
  - "/eclipse-pei-zhi-pydev-cha-jian.html"
---
### [安装python解释器(略)](#1) 
### [安装PyDev](#2)

首先需要去Eclipse官网下载：http://www.eclipse.org/ ，Eclipse需要JDK支持，如果Eclipse无法正常运行，请到Java官网下载JDK安装：http://www.oracle.com/technetwork/java/javase/downloads。  
打开Eclipse，找到Help菜单栏，进入Install New Software…选项。  
点击work with:输入框的旁边点击Add…，Name可以随便是什么，我输入的是PyDev，Location是 http://pydev.org/updates 点击OK。  
等待一下，便可以在选择栏里看到各个选项。  
选择PyDev，然后一路Next，进入安装路径选择界面，使用默认设置，然后 Finish。Eclipse将下载 PyDev，可以从 Eclipse任务栏中看到下载的进度。  
PyDev安装好后，需要重启Eclipse。  

### [配置PyDev](#3)

PyDev安装好之后，需要配置解释器。在 Eclipse 菜单栏中，选择Window > Preferences > Pydev > Interpreter – Python，在此配置 Python。首先需要添加已安装的解释器。如果没有下载安装Python，请到官网下载2.x或者3.x版本：http://www.python.org/ 
我使用的是Python2.7版本。单击 New，进入对话框。Interpreter Name可以随便命名，  
Interpreter Executable选择Python解释器/usr/bin/python。  
点击OK后跳出一个有很多复选框的窗口，选择需要加入SYSTEM pythonpath的选项，点击Ok。  
然后在Python Interpreters的窗口，再次点击OK，即完成了Python解释器的配置。  
到此PyDev就已经完成了配置，可以使用Eclipse开始编写Python。  
Hola World：  
在 Eclipse 菜单栏中，选择File > New > Pydev > Project…，在窗口中选择PyDev Project，有三种项目可以创建，选择PyDev Project。  
点击Next，输入项目名，选择相应的项目类型，以及所使用的Python语法版本和Python解释器。  
创建成功后，进入透视图，右击src图标，选择New->Pydev Package，创建一个新的包。系统将自动生成\_\_init\_\_.py 文件，该文件不包含任何内容。再右键单击创建的包，选择 New->Pydev Module，创建你一个新的Python模块，单击Finish。  

这样我们就可以开始创建第一个.py文件了。

### [更好的方法](#4)

在这个也页面 http://pydev.org/download.html ，你会看到某个软件已经预安装了这个扩展，她就是“Aptana Studio 3”

