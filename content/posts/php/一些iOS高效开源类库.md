---
title: "一些iOS高效开源类库"
date: "2025-06-10 13:43:48"
slug: "yi-xie-ios-gao-xiao-kai-yuan-lei-ku"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/一些iOS高效开源类库/"
  - "/2025/06/10/一些iOS高效开源类库.html"
  - "/一些iOS高效开源类库/"
  - "/一些iOS高效开源类库.html"
  - "/2025/06/10/yi-xie-ios-gao-xiao-kai-yuan-lei-ku/"
  - "/2025/06/10/yi-xie-ios-gao-xiao-kai-yuan-lei-ku.html"
  - "/yi-xie-ios-gao-xiao-kai-yuan-lei-ku.html"
---
- KissXml——xml解析库  
相关教程：http://www.iteye.com/topic/625849  
http://sencho.blog.163.com/blog/static/83056228201151743110540/  
很方便的一个xml解析器，支持Xpath查询。  
  
- skpsmtpmessage——Quick SMTP邮件发送  
svn checkout http://skpsmtpmessage.googlecode.com/svn/trunk/ skpsmtpmessage-read-only  
github:   git clone https://github.com/kailoa/iphone-smtp.git  
相关教程：http://disanji.net/2011/01/28/skpsmtpmessage-open-source-framework/  
skpsmtpmessage 是由Skorpiostech, Inc.为我们带来的一个SMTP协议的开源实现，使用Objective-c 实现，iOS系统的项目可以直接调用。  
  
- jsonframework——JSON支持  
相关教程：http://blog.csdn.net/xiaoguan2008/article/details/6732683  
它是一个开源框架，基于BSD协议发布。由于json-framework是开放源代码的，当你需要使用它时你只需将json的源代码加入到你的工程中。  
  
- ASIHttpRequest——HTTP Network库  
ASIHttpRequest库极大的简化了网络通 信，提供更先进的工具，例如文件上传工具，重定向处理工具、验证工具、等等。  
  
- MBProgressHUD——进展指示符库  
苹果的应用程序一般都会用一种优雅的，半透明的进度显示效果，不过这个API是不公开的，因此你要是用了，很可能被清除出AppStore。而 MBProgressHUD提供了一个替代方案，而且在用户角度上，实现的效果根本看不出和官方程序有什么差别。同时还提供了其他附加功能，比如虚拟进展 指示符，以及完成提示信息。整合到项目里也很容易，这里不细谈了。  
  
- zxing——二维码扫描库  
支持条形码/二维码扫描的图形处理库，这是一个java库，在android上的功能比较完整。同时该库也支持ios，但只能支持二位条形码的扫描。  
  
- kal——iPhone日历控件  
一个类似于ios系统默认日历开源日历库，支持添加事件，自定义日历样式等功能。  
  
- Facebook iOS SDK——Facebook API类库  
大体来讲就是iPhone上的Facebook login，完全支持Facebook Graph API和the older REST api。  
  
- shareKit——分享库  
相关demo：http://www.cocoachina.com/bbs/read.php?tid-71760.html  
分享到开心，豆瓣，腾讯，新浪微博的api所用到的强大的分享库。  
  
- SDWebImage——简化网络图片处理  
用SDWebImage调用网站上的图片，跟本地调用内置在应用包里的图片一样简单。操作也很简单。  
  
- GData client——iPhone上所有Google相关服务的类库  
名字就说明一切了。跟Google相关的，值得一提的是，这个项目很开放。有很多示例程序供下载。  
  
- CorePlot——2D图形绘图仪  
CorePlot有很多解决方案将你的数据可视。同时也会提供各种迷人的图形效果，比如棒状图、饼状图、线状图等等，在他们网站上也提供了大量的范例图形，很多股票价格应用，游戏分数，个人财务管理都在用。  
  
- Three20——类似于Facebook的优秀的UI库  
Three20类库是Facebook自己做的，大而全是他最大的特色。把他整合到已有的项目中可能得费点周折，不过如果一开始你就用上了Three20，尤其是牵扯到很多web相关的项目的时候，你就能深刻体会到神马叫给力了。  
  
- FMDatabase——SQLite的Objective-C封装
是SQLite的C API對初學者來說實在太麻煩太瑣碎，難度太高。FMDB說穿了其實只是把C API包裝成簡單易用的Objective-C类。對于SQLite初學者來說，大大減低了上手的難度。有了FMDB，寫程式時只要專心在SQLite的語法上，而不用去理那堆有看沒有懂的C API，實在是件快樂的事情。

来源:http://blog.csdn.net/jiarusun000/article/details/7170577
