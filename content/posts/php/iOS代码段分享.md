---
title: "iOS代码段分享"
date: "2025-06-09 11:49:52"
slug: "ios-dai-ma-duan-fen-xiang"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/09/iOS代码段分享/"
  - "/2025/06/09/iOS代码段分享.html"
  - "/iOS代码段分享/"
  - "/iOS代码段分享.html"
  - "/2025/06/09/ios-dai-ma-duan-fen-xiang/"
  - "/2025/06/09/ios-dai-ma-duan-fen-xiang.html"
  - "/ios-dai-ma-duan-fen-xiang.html"
---
收集的一些实用的ios代码段

### [去除顶部状态栏后的分辨率](#1)

```c
CGRect frame = [[UIScreen mainScreen] applicationFrame];
```

### [获取当前SIM卡的手机号码（私有API）](#2)

首先引入官方的CoreTelephony库，然后使用如下函数返回用户手机号码即可：

```c
extern NSString *CTSettingCopyMyPhoneNumber();
NSString *telNum = CTSettingCopyMyPhoneNumber();
```

### [获取当前运营商名称及相关描述信息](#3)

首先引入官方的CoreTelephony库，然后添加相应的头文件：

```c
#import <CoreTelephony/CTCarrier.h>
#import <CoreTelephony/CTTelephonyNetworkInfo.h>
```

接着使用CTTelephonyNetworkInfo与CTCarrier这两个类获取运营商相关信息，并将其保存到一个CTCarrier对象中：

```c
CTTelephonyNetworkInfo *info = [[CTTelephonyNetworkInfo alloc] init];
CTCarrier *carrier = info.subscriberCellularProvider;
NSLog(@”description:%@”,[carrier description]);
NSLog(@”carrier:%@”, carrier.carrierName);
```

输出为：

```shell
CTCarrier (0x1a0200) {
Carrier name: [中国联通]
Mobile Country Code: [460]
Mobile Network Code:[01]
ISO Country Code:[cn]
Allows VOIP? [YES]
}

carrier:中国联通
```
