---
title: "iOS Push机制"
date: "2025-06-23 16:26:36"
slug: "ios-push-ji-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/23/iOS-Push机制/"
  - "/2025/06/23/iOS-Push机制.html"
  - "/iOS-Push机制/"
  - "/iOS-Push机制.html"
  - "/2025/06/23/ios-push-ji-zhi/"
  - "/2025/06/23/ios-push-ji-zhi.html"
  - "/ios-push-ji-zhi.html"
---
今天看了一下关于IOS的Push的机制，对于初学者我看了一下，顺便在自己的博客中进行记录一下

### [Push机制的介绍](#1)

iPhone 对于应用程序在后台运行有诸多限制（除非你越狱）。因此，当用户切换到其他程序后，原先的程序无法保持运行状态。对于那些需要保持持续连接状态的应用程序（比如社区网络应用），将不能收到实时的信息。

为解决这一限制，苹果推出了APNs（苹果推送通知服务）。APNs 允许设备与苹果的推送通知服务器保持常连接状态。当你想发送一个推送通知给某个用户的iPhone上的应用程序时，你可以使用 APNs 发送一个推送消息给目标设备上已安装的某个应用程序。

Push机制的类型：

四种：徽章、提示框、声音和横幅

Push机制的4个组件

***Provider***

***APNS***

***iPhone设备***

***Client App***

其中APNS（Apple Push Notification Service）是由苹果提供的消息推送服务中心，所有的消息都经由这里转发给相应的设备。

Provider和Device与APNS进行通信时，时建立在SSL/TLS安全连接之上的。如下面的两个图所示（TSL的建立过程）

Provider与APNS之间的通信还需要-----DeviceToken

DeviceToken是设备令牌，有APNS生成，并返回给设备，再由设备提供给Provider。

### [Push机制的使用](#2)

Push通知的使用可以分为以下几个步骤。其中前4个步骤相当于准备工作，也非常重要。

接下来，我们就一个步骤一个步骤的进行讲解。

a 证书请求：

证书请求制作的目的是为了获取ssl证书。通过在“钥匙串访问”程序中来创建证书请求，具体的操作过程，建议大家看看本文开头给出的视频连接。

b 创建appid

appid在制作ssl证书和profile文件会用到。具体创建过程看如下图（建议大家看看本文开头给出的视频连接。）

登录网站<https://developer.apple.com/devcenter/ios/>

c 生成ssl证书

ssl证书的一个主要作用就是运行程序接收从apns发送过来的消息

具体生成过程，看下面的图，当然，这里也建议观看本文开头给出的视频

d 创建profile文件

profile文件的主要作用是运行程序可以被安装在手机上（push测试需要在真机上进行）

### [Push故障排除](#3)

### [Demo示例代码打包在如下文件中](#4)

[PushMeBaby.rar](http://gowhich.com/resource#tab-IOS)

[PushClient.rar](http://gowhich.com/resource#tab-IOS)

[apn.rar](http://gowhich.com/resource#tab-IOS)

参考地址：http://www.devdiv.com/iOS_iPhone-_ios_push_-thread-130543-1-1.html

DevDiv视频地址：http://www.devdiv.com/article-4042-1.html

Youku视频地址：<http://v.youku.com/v_show/id_XNDI5ODExNzMy.html>

### [服务器端步骤](#5)

生成app在服务端需要的许可证

1）进入Provisioning Portal, 下载Certificates在development下的证书。

2） 找到需要测试的app id,然后enable它在development下的Apple Push Notification service: Development Push SSL Certificate。需要输入1）中的签名证书才可以生成一个aps_developer_identity.cer.

3) 双击aps_developer_identity.cer，会打开系统的key chain.

在My certificates下找到Apple Development Push Services。需要为certificate和它之下的private key各自export出一个.p12文件。(会出现设置密码过程)

4）需要将上面的2个.p12文件转成.pem格式：

```bash
openssl pkcs12 -clcerts -nokeys -out cert.pem -in cert.p12
openssl pkcs12 -nocerts -out key.pem -in key.p12
```

5）如果需要对 key不进行加密：

```bash
openssl rsa -in key.pem -out key.unencrypted.pem
```

6）然后就可以 合并两个.pem文件, 这个ck.pem就是服务端需要的证书了。

```bash
cat cert.pem key.unencrypted.pem > ck.pem
```

4个pem，另外加上php文件，打包放到服务器上

[apn_pem.zip](http://gowhich.com/resource#tab-IOS)
