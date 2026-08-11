---
title: "如何在iOS设备上安装调试多个App"
date: "2025-06-13 15:33:17"
slug: "ru-he-zai-ios-she-bei-shang-an-zhuang-tiao-shi-duo-ge-app"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/如何在iOS设备上安装调试多个App/"
  - "/2025/06/13/如何在iOS设备上安装调试多个App.html"
  - "/如何在iOS设备上安装调试多个App/"
  - "/如何在iOS设备上安装调试多个App.html"
  - "/2025/06/13/ru-he-zai-ios-she-bei-shang-an-zhuang-tiao-shi-duo-ge-app/"
  - "/2025/06/13/ru-he-zai-ios-she-bei-shang-an-zhuang-tiao-shi-duo-ge-app.html"
  - "/ru-he-zai-ios-she-bei-shang-an-zhuang-tiao-shi-duo-ge-app.html"
---
### [如何在iOS设备上安装调试多个App](#1)

这个话题很重要，经过我的不断关注，在一个高手博客里面找到了，简单的贴到我这里了哈

作为iOS开发工程师， 在发布app之前，你需要在真机上调试、测试，所以需要将app 下载到真机上。 如果想同时下载多个App ，怎么办呢？  我们先来看看App 的工作原理。  
  
Appstore上的每个app 都有一个唯一的ID。 这个ID，如同人们的身份证一样，每个App 都不是不同的。 但作为iOS开发者来说，在App 调试阶段，你可以自行设置多个App ID。 因为这些App 还没有发布到Appstore 上，你只需要保证自己开发的App 设置不同的App ID 即可。  
  
只要App ID 不同， 你就可以在同一部iOS设备上，安装不同的App。  
  
具体到开发层面， 你需要在xcode 的 info.plist 文件的 Bunlde Identifier 设置 App ID。  
  
举例来说：  
  
如果你的 mobileprovisioning Proifle （dev_any_profile）文件对应的 Bunld ID 为： `com.leopard.*`  这个 `*` 就是一个通配符。 你可以用不同的字符替换。  
  
在 info.plist 文件的 Bunlde Identifier 中，填写 com.leopard.app1 ,  在 project -> build setting -> code siging 中，将对应的 dev_any_profile 关联起来， 这样就生成了一个 app id 为 app1 的 App；  
  
同理，在 info.plist 文件的 Bunlde Identifier 中，填写 com.leopard.app2, 在 project -> build setting -> code siging 中，将对应的 dev_any_profile 关联起来， 这样就生成了一个 app id 为 app2 的 App；  
  
以此类推， 便可以生成多个App。 因为它们的 app id 不同， 便可以同时安装在同一部iOS设备上。  
