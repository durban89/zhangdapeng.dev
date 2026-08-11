---
title: "iOS 点击屏幕任意空白处，键盘消失"
date: "2025-06-13 11:34:44"
slug: "ios-dian-ji-ping-mu-ren-yi-kong-bai-chu-jian-pan-xiao-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/13/iOS-点击屏幕任意空白处，键盘消失/"
  - "/2025/06/13/iOS-点击屏幕任意空白处，键盘消失.html"
  - "/iOS-点击屏幕任意空白处，键盘消失/"
  - "/iOS-点击屏幕任意空白处，键盘消失.html"
  - "/2025/06/13/iOS-点击屏幕任意空白处-键盘消失/"
  - "/2025/06/13/iOS-点击屏幕任意空白处-键盘消失.html"
  - "/2025/06/13/ios-dian-ji-ping-mu-ren-yi-kong-bai-chu-jian-pan-xiao-shi/"
  - "/2025/06/13/ios-dian-ji-ping-mu-ren-yi-kong-bai-chu-jian-pan-xiao-shi.html"
  - "/ios-dian-ji-ping-mu-ren-yi-kong-bai-chu-jian-pan-xiao-shi.html"
---
点击屏幕任意空白处，键盘消失的方法：

在这个方法里面实现就好了：

```objectivec
-(void) touchesBegan:(NSSet *)touches withEvent:(UIEvent *)event
{
    [self.teleplayDescription resignFirstResponder];
    [self.teleplayTitle resignFirstResponder];
    [self.teleplayContactPeople resignFirstResponder];
    [self.teleplayContactPeoplePhone resignFirstResponder];
}
```
