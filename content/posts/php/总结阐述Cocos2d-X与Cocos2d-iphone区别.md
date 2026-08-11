---
title: "总结阐述Cocos2d-X与Cocos2d-iphone区别"
date: "2025-06-24 11:24:34"
slug: "zong-jie-chan-shu-cocos2d-x-yu-cocos2d-iphone-qu-bie"
categories: ["技术"]
tags: ["iOS", "Cocos2d-x"]
aliases:
  - "/2025/06/24/总结阐述Cocos2d-X与Cocos2d-iphone区别/"
  - "/2025/06/24/总结阐述Cocos2d-X与Cocos2d-iphone区别.html"
  - "/总结阐述Cocos2d-X与Cocos2d-iphone区别/"
  - "/总结阐述Cocos2d-X与Cocos2d-iphone区别.html"
  - "/2025/06/24/zong-jie-chan-shu-cocos2d-x-yu-cocos2d-iphone-qu-bie/"
  - "/2025/06/24/zong-jie-chan-shu-cocos2d-x-yu-cocos2d-iphone-qu-bie.html"
  - "/zong-jie-chan-shu-cocos2d-x-yu-cocos2d-iphone-qu-bie.html"
---
最近开始学习cocos2d, 查阅资料发现有个Cocos2d-X和Cocos2d-iphone, 不解，为什么会有两种

不得不说要说总结，因为Cocos2d-X的代码和Cocos2d-iphone两个引擎除了语言不同外（Cocos2d-X使用C++，Cocos2d-iphone使用Object-C）可以说没有其他差异。

下面Himi举例对比几段代码来说明吧：

### [创建添加一个精灵代码对比：](#1)

***使用Cocos2d-X***：

```objectivec
//---------Cocos2d-X代码部分--  
//创建一个精灵  
CCSprite *spriteTemp =CCSprite::spriteWithFile("icon.png");  
//设置精灵的坐标  
spriteTemp->setPosition(ccp(size.width*0.5,size.height*0.5));  
//将精灵添加到layer中  
this->addChild(spriteTemp,1);
```

***使用Cocos2d-iphone***：

```objectivec
//---------Cocos2d-iphone代码部分--  
//创建一个精灵  
CCSprite *spriteTemp =[CCSprite spriteWithFile:@"icon.png"];  
//设置精灵的坐标  
spriteTemp.position=ccp(size.width*0.5,size.height*0.5);  
//将精灵添加到layer中  
[self addChild:spriteTemp z:0 tag:1];
```

### [添加一个粒子代码对比:](#2)

***使用Cocos2d-X***：

```objectivec
//---------Cocos2d-X代码部分--   
CCParticleSystem *tempSystem =ARCH_OPTIMAL_PARTICLE_SYSTEM::particleWithFile("himi.plist");     
tempSystem->setPosition(ccp(100,100));      
this->addChild(tempSystem);
```

*使用Cocos2d-iphone：*

```objectivec
//---------Cocos2d-iphone代码部分--  
CCParticleSystem *tempSystem =[ARCH_OPTIMAL_PARTICLE_SYSTEM particleWithFile:@"himi.plist"];     
tempSystem.position=ccp(100,100);      
[self addChild:tempSystem];
```

OK，不在举例了，通过以上随便举例的两段代码童鞋们很清楚的看出来，基本上没有差异。。So～这也是Himi没有在更新Cocos2d-X博文的必要，以后主要会继续更新Cocos2d（Cocos2d-iphone）博文的，以后童鞋们不管是做Cocos2d-X还是做Cocos2d-iphone都可以看我的【iOS-Cocos2d游戏开发系列博文的】谁让它们通用呢

### [这里还有三点要说下：](#3)

* 第一：现在很多游戏公司都趋向于Cocos2d-X引擎开发游戏的趋势，不得不说Cocos2d-X多平台平移确实很诱惑人，而且通过网龙《91部落》手机网游的成功发布，不得不说Cocos2d-X已成熟！
* 第二：不少童鞋肯定会很想知道Cocos2d-X能多平台平移，那么平移稳定性如何？

  通过Himi的了解，Cocos2d-X开发都会使用统一的C++语言开发，例如在iOS开发中使用Xcode+cocos2d-X，在Android上一般使用Eclipse+Android NDK+ADT....

其实总结一句，Cocos2d-iphone并不像很多童鞋认为的只要的一人开发就可打包多平台包这样子～ 如果说用一句话更贴切的形容Cocos2d-X，Himi会用“Cocos2d-X代码通用”来形容；

从CC（CocoChina）上我看到王哲walzer（cocos2d-x 游戏引擎作者）在回复一童鞋问题时候这么说的：

问：关于如何打包cocos2d-x程序的问题   本人新手，想请教一下如何将Cocos2d-x win32的程序打包成iphone能够运行的程序，请各位大大不吝赐教!谢谢！

王哲walzer 答：win32上只是让你调试方便，要发布到appstore上，你还是得有个mac机，装好cocos2d-x template，新建工程，然后把win32上代码拷过来，手工地加入xcode工程里面，编译运行

从上面的对话可以证实Himi所说的Cocos2d-X是代码通用！

