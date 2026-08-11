---
title: "PhoneGap在Mac环境下使用问题小结"
date: "2025-06-27 14:14:44"
slug: "phonegap-zai-mac-huan-jing-xia-shi-yong-wen-ti-xiao-jie"
categories: ["技术"]
tags: ["PhoneGap"]
aliases:
  - "/2025/06/27/PhoneGap在Mac环境下使用问题小结/"
  - "/2025/06/27/PhoneGap在Mac环境下使用问题小结.html"
  - "/PhoneGap在Mac环境下使用问题小结/"
  - "/PhoneGap在Mac环境下使用问题小结.html"
  - "/2025/06/27/phonegap-zai-mac-huan-jing-xia-shi-yong-wen-ti-xiao-jie/"
  - "/2025/06/27/phonegap-zai-mac-huan-jing-xia-shi-yong-wen-ti-xiao-jie.html"
  - "/phonegap-zai-mac-huan-jing-xia-shi-yong-wen-ti-xiao-jie.html"
---
PhoneGap在Mac环境下使用问题小结  
1，问题一：在执行命令phonegap run ios出现“Cordova needs ios-sim version 1.7 or greater, you have version”  

解决办法：在命令下运行`sudo npm install -g ios-sim  `
  
2，问题二：在执行命令phonegap build android出现“Error: ERROR : executing command 'ant', make sure you have ant installed and added to your path.”  

解决办法：下载apache-ant:http://ant.apache.org/index.html ,然后解压到`/usr/local[/usr/local/ant]`,然后进入这个目录。  
执行命令:
```bash
export ANT_HOME=/usr/local/ant  

export PATH=$PATH:${ANT_HOME}/bin  

sudo ant -f fetch.xml -Ddest=system[fetch.xml就是当前目录下面的文件，不会没有的，可以参看一下文档]
```

