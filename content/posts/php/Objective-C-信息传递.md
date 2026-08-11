---
title: "Objective-C 信息传递"
date: "2025-06-03 15:14:54"
slug: "objective-c-xin-xi-chuan-di"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/03/Objective-C-信息传递/"
  - "/2025/06/03/Objective-C-信息传递.html"
  - "/Objective-C-信息传递/"
  - "/Objective-C-信息传递.html"
  - "/2025/06/03/objective-c-xin-xi-chuan-di/"
  - "/2025/06/03/objective-c-xin-xi-chuan-di.html"
  - "/objective-c-xin-xi-chuan-di.html"
---
Objective-C最大的特色是承自Smalltalk的信息传递模型（message passing），与今日主流的C++差异甚大。Objective-C里，与其说对象互相调用方法，不如说对象之间互相传递信息更为精确。此二种风格的差异主要在于程序如何看待调用方法/传送信息这个动作。C++里类型与方法的关系非常严格清楚，一个方法必定属于一个类型，而且在编译时（compile time）就已经紧密绑定，你不可能去调用一个不存在类型里的方法。但在Objective-C，类型与信息的关系比较松散，调用方法视为对对象发送信息，所有方法都被视为对信息的回应。所有信息处理直到运行时（runtime）才会动态决定，并交由类型自行决定如何处理收到的信息。也就是说，一个类型不保证一定会回应收到的信息，如果类型收到了一个无法处理的信息，程序只会抛出一个Exception，不会出错或当掉。

C++里，送一个信息给对象（或者说调用一个方法）的语法如下:
```c
obj->method(argument);
```

Objective-C则写成:

```c
[obj method: argument];
```
此二者并不仅仅是语法上的差异，还有基本行为上的不同。

这里以一个汽车类（car class）的简单例子来解释Objective-C的信息传递特性：

```c
[car fly];
```

典型的C++意义解读是“调用car类型的fly方法”。若car类型里头没有定义fly方法，那编译肯定不会通过。但是Objective-C里，我们应当解读为“发提交一个fly的信息给car对象”，fly是信息，而car是信息的接收者。car收到信息后会决定如何回应这个信息，若car类型内定义有fly方法就运行此段程序，若car内不存在fly方法，这里不会产生编译错误，它仅仅是抛出Exception。

此二种风格各有优劣。C++的编译期绑定使得函数调用非常快速，强制要求所有的方法都必须有对应的动作。缺点是不支持动态绑定（除非手动加上 virtual关键字）。Objective-C天生即是动态绑定，运行期才处理信息，允许传送未知信息给对象。可以送信息给整个对象集合而不需要一一检 查每个对象的型态，天生具备消息转送机制。同时空对象nil也可以接受信息，但是默认不做事，所以送信息给nil也不用担心程序崩溃。

Objective-C的方法调用因为运行期才动态解析信息，一开始信息比C++ virtual成员函数调用速度慢上三倍。但经由IMP高速缓存改善，目前已经比C++的virtual function快上50％。
