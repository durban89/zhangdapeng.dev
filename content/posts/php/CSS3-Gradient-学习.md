---
title: "CSS3 Gradient 学习"
date: "2025-06-12 09:56:40"
slug: "css3-gradient-xue-xi"
categories: ["技术"]
tags: ["CSS"]
aliases:
  - "/2025/06/12/CSS3-Gradient-学习/"
  - "/2025/06/12/CSS3-Gradient-学习.html"
  - "/CSS3-Gradient-学习/"
  - "/CSS3-Gradient-学习.html"
  - "/2025/06/12/css3-gradient-xue-xi/"
  - "/2025/06/12/css3-gradient-xue-xi.html"
  - "/css3-gradient-xue-xi.html"
---
CSS3发布很久了，现在在国外的一些页面上常能看到他的身影，这让我羡慕已久，只可惜在国内为了兼容IE，让这一项技术受到很大的限制，很多Web前端人员都望而止步。虽然如此但还是有很多朋友在钻研CSS3在web中的应用，为了不被淘汰，我也开始向CSS3进发，争取跟上技术的前沿。从现在开始我会不断的发布一些CSS3的应用，和大家一起分享，今天我们首先要看的就是:CSS3： Gradient─CSS3渐变。  
  
CSS3 Gradient分为linear-gradient(线性渐变)和radial-gradient(径向渐变)。而我们今天主要是针对线性渐变来剖析其具体的用法。为了更好的应用CSS3 Gradient,我们需要先了解一下目前的几种现代浏览器的内核，主流内容主要有Mozilla（熟悉的有Firefox，Flock等浏览器）、WebKit（熟悉的有Safari、Chrome等浏览器）、Opera（Opera浏览器）、Trident（讨厌的IE浏览器）。本文照常忽略IE不管，我们主要看看在Mozilla、Webkit、Opera下的应用，当然在IE下也可以实现，他需要通过IE特有的滤镜来实现，在后面会列出滤镜的使用语法，但不会具体介绍如何实用，感兴趣的可以搜索相关技术文档。那我们了解了这些，现在就开始今天的主题吧。

节选如下：

#### [CSS3的线性渐变](#1)

**一、线性渐变在Mozilla下的应用**  
语法：  
`-moz-linear-gradient( [<point> || <angle>,]? <stop>, <stop> [, <stop>]* )`
参数：其共有三个参数，第一个参数表示线性渐变的方向，top是从上到下、left是从左到右，如果定义成left top，那就是从左上角到右下角。第二个和第三个参数分别是起点颜色和终点颜色。你还可以在它们之间插入更多的参数，表示多种颜色的渐变。  
注：这个效果暂时只有在Mozilla内核的浏览器下才能正常显示。  
**二、线性渐变在Webkit下的应用**  
语法：  
`-webkit-linear-gradient( [<point> || <angle>,]? <stop>, <stop> [, <stop>]* )//最新发布书写语法`
`-webkit-gradient(<type>, <point> [, <radius>]?, <point> [, <radius>]? [, <stop>]*) //老式语法书写规则`
参数：-webkit-gradient是webkit引擎对渐变的实现参数，一共有五个。第一个参数表示渐变类型（type），可以是linear（线性渐变）或者radial（径向渐变）。第二个参数和第三个参数，都是一对值，分别表示渐变起点和终点。这对值可以用坐标形式表示，也可以用关键值表示，比如 left top（左上角）和left bottom（左下角）。第四个和第五个参数，分别是两个color-stop函数。color-stop函数接受两个参数，第一个表示渐变的位置，0为起点，0.5为中点，1为结束点；第二个表示该点的颜色。  
**三、线性渐变在Opera下的应用**  
语法：  
`-o-linear-gradient([<point> || <angle>,]? <stop>, <stop> [, <stop>]); /* Opera 11.10+ */`
参数：-o-linear-gradient有三个参数。第一个参数表示线性渐变的方向，top是从上到下、left是从左到右，如果定义成left top，那就是从左上角到右下角。第二个和第三个参数分别是起点颜色和终点颜色。你还可以在它们之间插入更多的参数，表示多种颜色的渐变。（注：Opera支持的版本有限，本例测试都是在Opera11.1版本下，后面不在提示）。  
**四、线性渐变在Trident (IE)下的应用**  
语法：  
`filter: progid:DXImageTransform.Microsoft.gradient(GradientType=0, startColorstr=#1471da, endColorstr=#1C85FB);/*IE<9>*/  
-ms-filter: "progid:DXImageTransform.Microsoft.gradient (GradientType=0, startColorstr=#1471da, endColorstr=#1C85FB)";/*IE8+*/`
IE依靠滤镜实现渐变。startColorstr表示起点的颜色，endColorstr表示终点颜色。GradientType表示渐变类型，0为缺省值，表示垂直渐变，1表示水平渐变。

详细的自己去参考吧。

来源：http://www.w3cplus.com/content/css3-gradient
