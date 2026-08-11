---
title: "Android webview中的页面出现的部分Bug及解决方案"
date: "2025-07-03 11:07:40"
slug: "android-webview-zhong-de-ye-mian-chu-xian-de-bu-fen-bug-ji-jie-jue-fang-an"
categories: ["技术"]
tags: ["Android"]
aliases:
  - "/2025/07/03/Android-webview中的页面出现的部分Bug及解决方案/"
  - "/2025/07/03/Android-webview中的页面出现的部分Bug及解决方案.html"
  - "/Android-webview中的页面出现的部分Bug及解决方案/"
  - "/Android-webview中的页面出现的部分Bug及解决方案.html"
  - "/2025/07/03/android-webview-zhong-de-ye-mian-chu-xian-de-bu-fen-bug-ji-jie-jue-fang-an/"
  - "/2025/07/03/android-webview-zhong-de-ye-mian-chu-xian-de-bu-fen-bug-ji-jie-jue-fang-an.html"
  - "/android-webview-zhong-de-ye-mian-chu-xian-de-bu-fen-bug-ji-jie-jue-fang-an.html"
---
写移动页面时给一个图片添加样式如下

```css
img{
  border: .05rem solid #5c0008;
  border-radius: 1rem;
}
```

在IOS上正常，部分安卓的手机却不能正常显示（例如vivo手机），查阅了资料后发现在安卓低版本的手机上border-radius这个css 属性确实存在该问题以及发现一些其他的问题，特此记下！

一、Android2.3 自带浏览器不支持%

通常我们实现一个圆只需要`border-radius：50%`就可以了，但是在Android2.3中是不支持百分比的，要兼容的话我们只能使用一个较大值例如`border-radius：999px;`

二、Android及Safari低版本img的圆角问题（就是本文开头提到的问题）

当img元素有border时设置border-radius会导致圆角变形（如图）

border-radius在Android低版本的bug

解决办法就是在外面嵌套一个父元素然后设置其border和border-radius即可解决。

三、android 4.2.x背景色溢出和不支持border-radius 缩写

在Android4.2.x系统自带浏览器中，同时设置了border-radius和背景色的时候，背景色会溢出到圆角外，需要使用`background-clip:padding-box;`来修复。

android 4.2.x不支持border-radius 缩写解决办法就是使用border-radius的四个扩写属性，缩写属性放在后面。如下(自己借了几个手机并没发现这个问题)

```css
.s{
  border-top-left-radius: 999px;  
  border-top-right-radius: 999px;  
  border- bottom-right-radius: 999px;  
  border-bottom-left-radius: 999px;  
  border-radius: 999px;
}
```


