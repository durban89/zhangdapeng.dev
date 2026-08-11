---
title: "更新证书错误Code Sign error: Provisioning profile 'XXXX' can't be found"
date: "2025-06-17 17:20:08"
slug: "geng-xin-zheng-shu-cuo-wu-code-sign-error-provisioning-profile-xxxx-cant-be-found"
categories: ["技术"]
tags: ["iOS", "Xcode"]
aliases:
  - "/2025/06/17/更新证书错误Code-Sign-error:-Provisioning-profile-'XXXX'-can't-be-found/"
  - "/2025/06/17/更新证书错误Code-Sign-error:-Provisioning-profile-'XXXX'-can't-be-found.html"
  - "/更新证书错误Code-Sign-error:-Provisioning-profile-'XXXX'-can't-be-found/"
  - "/更新证书错误Code-Sign-error:-Provisioning-profile-'XXXX'-can't-be-found.html"
  - "/2025/06/17/更新证书错误Code-Sign-error-Provisioning-profile-be-found/"
  - "/2025/06/17/更新证书错误Code-Sign-error-Provisioning-profile-be-found.html"
  - "/2025/06/17/geng-xin-zheng-shu-cuo-wu-code-sign-error-provisioning-profile-xxxx-cant-be-found/"
  - "/2025/06/17/geng-xin-zheng-shu-cuo-wu-code-sign-error-provisioning-profile-xxxx-cant-be-found.html"
  - "/geng-xin-zheng-shu-cuo-wu-code-sign-error-provisioning-profile-xxxx-cant-be-found.html"
---
在Xcode中当你在更新了你得证书而再重新编译你的程序，真机调试一直会出现 Code Sign error: Provisioning profile ‘XXXX’ can't be found是不是会另你很恼火。下面说说解决方法，让你很好的解决这个问题。  
  
1.关闭你的项目，找到项目文件XXXX.xcodeproj，在文件上点击右键，选择“显示包内容”（Show Package Contents）。会新打开一个Finder。注：其实XXXX.xcodeproj就是一个文件夹，这里新打开的一个Finder里面的三个文件就是该XXXX.xcodeproj文件夹里面的文件。  
  
2.在新打开的Finder中找到project.pbxproj，并且打开。在这之中找到你之前的证书的编码信息。我之前报的错误信息是  
  
Code Sign error: Provisioning profile '37D44E7F-0339-4277-9A82-C146A944CD46'，所以我用查找的方式找到了所有包括37D44E7F-0339-4277-9A82-C146A944CD46的行，并且删除。

3.保存，重新启动你的项目，再编译。就OK了。

参考：http://www.douban.com/note/131009422/
