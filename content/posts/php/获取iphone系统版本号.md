---
title: "获取iphone系统版本号"
date: "2025-06-12 17:18:38"
slug: "huo-qu-iphone-xi-tong-ban-ben-hao"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/获取iphone系统版本号/"
  - "/2025/06/12/获取iphone系统版本号.html"
  - "/获取iphone系统版本号/"
  - "/获取iphone系统版本号.html"
  - "/2025/06/12/huo-qu-iphone-xi-tong-ban-ben-hao/"
  - "/2025/06/12/huo-qu-iphone-xi-tong-ban-ben-hao.html"
  - "/huo-qu-iphone-xi-tong-ban-ben-hao.html"
---
为了使用版本号的问题，我搜了点资料，做点记录

```objectivec
NSLog([[UIDevice currentDevice] name]); // Name of the phone as named by user
NSLog([[UIDevice currentDevice] uniqueIdentifier]); // A GUID like string
NSLog([[UIDevice currentDevice] systemName]); // "iPhone OS"
NSLog([[UIDevice currentDevice] systemVersion]); // "2.2.1"
NSLog([[UIDevice currentDevice] model]); // "iPhone" on both devices
NSLog([[UIDevice currentDevice] localizedModel]); // "iPhone" on both devices
float version = [[[UIDevice currentDevice] systemVersion] floatValue];
if (version >= 4.0)
{
// iPhone 4.0 code here
}
```
