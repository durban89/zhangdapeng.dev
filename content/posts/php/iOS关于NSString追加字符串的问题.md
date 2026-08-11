---
title: "iOS关于NSString追加字符串的问题"
date: "2025-06-13 11:34:48"
slug: "ios-guan-yu-nsstring-zhui-jia-zi-fu-chuan-de-wen-ti"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS关于NSString追加字符串的问题/"
  - "/2025/06/13/iOS关于NSString追加字符串的问题.html"
  - "/iOS关于NSString追加字符串的问题/"
  - "/iOS关于NSString追加字符串的问题.html"
  - "/2025/06/13/ios-guan-yu-nsstring-zhui-jia-zi-fu-chuan-de-wen-ti/"
  - "/2025/06/13/ios-guan-yu-nsstring-zhui-jia-zi-fu-chuan-de-wen-ti.html"
  - "/ios-guan-yu-nsstring-zhui-jia-zi-fu-chuan-de-wen-ti.html"
---
IOS关于NSString追加字符串的问题，网上也有不少的做法，比较多的做法是：

```objectivec
NSMutableString *str=[[NSMutableStringalloc] initWithString:@"dd"];
[str stringByAppendingString:@"eee" ];  //问题行
NSLog(str);
//一开始的时候怎样修改都追加不上，类型也换了
//应该是：把追加后的值回传给要追加的原对象
str=[str stringByAppendingString:@"eee" ]; //正确
```

但是使用上面的方法，我不知道你们有没有遇到有类型不对的提示，总之我这里是有的，于是我将上面这样改了一下：

```objectivec
NSString *str=[[NSMutableStringalloc] initWithString:@"dd"];
[str stringByAppendingString:@"eee" ];  //问题行
NSLog(str);
```

一开始的时候怎样修改都追加不上，类型也换了
应该是：把追加后的值回传给要追加的原对象
```objectivec
str=[str stringByAppendingString:@"eee" ]; //正确
```

警告消失了。
