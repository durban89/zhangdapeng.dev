---
title: "iOS webView 中 代码控制滚动条的位置"
date: "2025-06-25 11:34:35"
slug: "ios-webview-zhong-dai-ma-kong-zhi-gun-dong-tiao-de-wei-zhi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/25/iOS-webView-中-代码控制滚动条的位置/"
  - "/2025/06/25/iOS-webView-中-代码控制滚动条的位置.html"
  - "/iOS-webView-中-代码控制滚动条的位置/"
  - "/iOS-webView-中-代码控制滚动条的位置.html"
  - "/2025/06/25/ios-webview-zhong-dai-ma-kong-zhi-gun-dong-tiao-de-wei-zhi/"
  - "/2025/06/25/ios-webview-zhong-dai-ma-kong-zhi-gun-dong-tiao-de-wei-zhi.html"
  - "/ios-webview-zhong-dai-ma-kong-zhi-gun-dong-tiao-de-wei-zhi.html"
---
得到当前webView 中 Scroll的坐标

```objectivec
int scrollPosition = [[DataWebView stringByEvaluatingJavaScriptFromString:@"window.pageYOffset"] intValue];
```

得到当前webView页

```objectivec
int sizePage = [[DataWebView stringByEvaluatingJavaScriptFromString:@"document.getElementById(\"foo\").offsetHeight;"] intValue];
```

跳到你指定的位置

```objectivec
[DataWebView stringByEvaluatingJavaScriptFromString: [NSString stringWithFormat:@"window.scrollBy(0,%d);", 200] ];
```

`0，200`改为你所要改的坐标

