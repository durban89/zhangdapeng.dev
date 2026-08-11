---
title: "iOS RegexKitLite 正则匹配 提取匹配的内容"
date: "2025-06-17 11:59:52"
slug: "ios-regexkitlite-zheng-ze-pi-pei-ti-qu-pi-pei-de-nei-rong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS-RegexKitLite-正则匹配-提取匹配的内容/"
  - "/2025/06/17/iOS-RegexKitLite-正则匹配-提取匹配的内容.html"
  - "/iOS-RegexKitLite-正则匹配-提取匹配的内容/"
  - "/iOS-RegexKitLite-正则匹配-提取匹配的内容.html"
  - "/2025/06/17/ios-regexkitlite-zheng-ze-pi-pei-ti-qu-pi-pei-de-nei-rong/"
  - "/2025/06/17/ios-regexkitlite-zheng-ze-pi-pei-ti-qu-pi-pei-de-nei-rong.html"
  - "/ios-regexkitlite-zheng-ze-pi-pei-ti-qu-pi-pei-de-nei-rong.html"
---
使用RegexKitLite正则表达式需要以下工作：  
1.RegexKitLite官方网址（内含使用教程）：http://regexkit.sourceforge.net/RegexKitLite  
2.下载地址：http://downloads.sourceforge.net/regexkit/RegexKitLite-4.0.tar.bz2  
3.将RegexKitLite.h和RegexKitLite.m引入到工程中。  
4.引入"libicucore.dylib"框架  
5.需要在处理的类中导入"RegexKitLite.h"  
  
言归正传，用正则表达式提取匹配的内容（此例子中讲述匹配字符串中的手机号码）：

```objectivec
NSString *searchString = @"15200000000,1234,12012345678,13400000000"; // 要提取的字符串
NSString *regexString  = @"\\b(13|15|18)([0-9]{9})\\b";  // 手机号码的正则表达式（由于15和18号段的不太熟悉，索性就干脆都算上了，你懂的。）
NSArray  *matchArray  = [searchString componentsMatchedByRegex:regexString];  // 匹配结果以数组形式返回
NSLog(@"%@",matchArray); // 进行输出
NSLog(@"%@",matchArray);
```

输出结果如下：

```bash
2011-08-23 14:39:23.356 ZQRegex[6726:207] (
    15200000000,
    13400000000
)
```
