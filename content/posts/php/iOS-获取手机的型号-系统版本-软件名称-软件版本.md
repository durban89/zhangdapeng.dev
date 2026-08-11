---
title: "iOS 获取手机的型号，系统版本，软件名称，软件版本"
date: "2025-06-17 16:45:59"
slug: "ios-huo-qu-shou-ji-de-xing-hao-xi-tong-ban-ben-ruan-jian-ming-cheng-ruan-jian-ban-ben"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS-获取手机的型号，系统版本，软件名称，软件版本/"
  - "/2025/06/17/iOS-获取手机的型号，系统版本，软件名称，软件版本.html"
  - "/iOS-获取手机的型号，系统版本，软件名称，软件版本/"
  - "/iOS-获取手机的型号，系统版本，软件名称，软件版本.html"
  - "/2025/06/17/iOS-获取手机的型号-系统版本-软件名称-软件版本/"
  - "/2025/06/17/iOS-获取手机的型号-系统版本-软件名称-软件版本.html"
  - "/2025/06/17/ios-huo-qu-shou-ji-de-xing-hao-xi-tong-ban-ben-ruan-jian-ming-cheng-ruan-jian-ban-ben/"
  - "/2025/06/17/ios-huo-qu-shou-ji-de-xing-hao-xi-tong-ban-ben-ruan-jian-ming-cheng-ruan-jian-ban-b.html"
  - "/ios-huo-qu-shou-ji-de-xing-hao-xi-tong-ban-ben-ruan-jian-ming-cheng-ruan-jian-ban-ben.html"
---
```objectivec
//手机序列号
NSString* identifierNumber = [[UIDevice currentDevice] uniqueIdentifier];
NSLog(@"手机序列号: %@",identifierNumber);
//手机别名： 用户定义的名称
NSString* userPhoneName = [[UIDevice currentDevice] name];
NSLog(@"手机别名: %@", userPhoneName);
//设备名称
NSString* deviceName = [[UIDevice currentDevice] systemName];
NSLog(@"设备名称: %@",deviceName );
//手机系统版本
NSString* phoneVersion = [[UIDevice currentDevice] systemVersion];
NSLog(@"手机系统版本: %@", phoneVersion);
//手机型号
NSString* phoneModel = [[UIDevice currentDevice] model];
NSLog(@"手机型号: %@",phoneModel );
//地方型号  （国际化区域名称）
NSString* localPhoneModel = [[UIDevice currentDevice] localizedModel];
NSLog(@"国际化区域名称: %@",localPhoneModel );

NSDictionary *infoDictionary = [[NSBundle mainBundle] infoDictionary];
// 当前应用名称
NSString *appCurName = [infoDictionary objectForKey:@"CFBundleDisplayName"];
NSLog(@"当前应用名称：%@",appCurName);
// 当前应用软件版本  比如：1.0.1
NSString *appCurVersion = [infoDictionary objectForKey:@"CFBundleShortVersionString"];
NSLog(@"当前应用软件版本:%@",appCurVersion);
// 当前应用版本号码   int类型
NSString *appCurVersionNum = [infoDictionary objectForKey:@"CFBundleVersion"];
NSLog(@"当前应用版本号码：%@",appCurVersionNum);
```

输入的结果：

```bash
2013-06-27 18:08:30.608 xx[21014:c07] 手机序列号: ef4dd99784b05114b4d894964599892c00000000
2013-06-27 18:08:30.610 xx[21014:c07] 手机别名: iPhone Simulator
2013-06-27 18:08:30.610 xx[21014:c07] 设备名称: iPhone OS
2013-06-27 18:08:30.611 xx[21014:c07] 手机系统版本: 6.1
2013-06-27 18:08:30.612 xx[21014:c07] 手机型号: iPhone Simulator
2013-06-27 18:08:30.612 xx[21014:c07] 国际化区域名称: iPhone Simulator
2013-06-27 18:08:30.613 xx[21014:c07] 当前应用名称：寻艺
2013-06-27 18:08:30.614 xx[21014:c07] 当前应用软件版本:1.0
2013-06-27 18:08:30.614 xx[21014:c07] 当前应用版本号码：1
```
