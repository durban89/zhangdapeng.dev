---
title: "Objective-C与Smalltalk类似的动态类型"
date: "2025-06-04 17:14:58"
slug: "objective-c-yu-smalltalk-lei-si-de-dong-tai-lei-xing"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/04/Objective-C与Smalltalk类似的动态类型/"
  - "/2025/06/04/Objective-C与Smalltalk类似的动态类型.html"
  - "/Objective-C与Smalltalk类似的动态类型/"
  - "/Objective-C与Smalltalk类似的动态类型.html"
  - "/2025/06/04/objective-c-yu-smalltalk-lei-si-de-dong-tai-lei-xing/"
  - "/2025/06/04/objective-c-yu-smalltalk-lei-si-de-dong-tai-lei-xing.html"
  - "/objective-c-yu-smalltalk-lei-si-de-dong-tai-lei-xing.html"
---
## [动态类型](#dongtaileixing)
 
类似于Smalltalk，Objective-C具备动态类型： 即消息可以发送给任何对象实体，无论该对象实体的公开接口中有没有对应的方法。在C++这种静态类型的语言里，不可能对一个(void*)指针调用任何方 法，编译器会挡下该调用行为。但在Objective-C中，你可以对id发送任何信息(id很像void*，但是被严格限制只能使用在对象上)，编译器 仅会发出“该对象可能无法回应信息”的警告，程序同样可以通过编译，而实际发生的事则取决于运行期该对象的真正形态，若该对象的确可以回应消息，则依旧运 行对应的方法。

这种特性可以增加语言的灵活性，因为它允许对象“捕捉”消息，再将消息转送到另一个可以正确处理该消息的对象，形同消息“转发”给另一个对象。

一个对象收到信息之后，他有三种处理信息的可能手段，第一是回应该消息并运行方法，若无法回应，则可以转发消息给其他对象，若以上两者均无，就要处 理无法回应而抛出的例外。只要进行三者之其一，该消息就算完成任务而被丢弃。若对“nil”（空对象指针）发送消息，该消息通常会被忽略，取决于编译器选 项可能会抛出例外。

虽然Objective-C具备动态类型的能力，但编译期的静态类型检查依旧可以应用到变量上。以下三种声明在运行时效力是完全相同的，但是三种声明提供了一个比一个更明显的类型信息，附加的类型信息让编译器在编译时可以检查变量类型，并对类型不符的变量提出警告。

下面三个方法，差异仅在于参数的形态：

```c
- setMyValue:(id) foo;
```

id形态表示参数“foo”可以是任何类的实例。

```c
- setMyValue:(id <aProtocol>) foo;
```

`id <aProtocol>`表示“foo”可以是任何类的实例，但必须采纳“aProtocol”协议。

```c
- setMyValue:(NSNumber*) foo;
```

该声明表示“foo”必须是“NSNumber”的实例。

动态类型是一种强大的特性。在缺少泛型的静态类型语言（如Java 5以前的版本）中实现容器类时，程序员需要写一种针对通用类型对象的容器类，然后在通用类型和实际类型中不停的强制类型转换。无论如何，类型转换会破坏静态类型，例如写入一个“整数”而将其读取为“字符串”会产生运行时错误。这样的问题被泛型解决，但容器类需要其内容对象的类型一致，而对于动态类型语言则完全没有这方面的问题。

[资料：[维基百科](https://zh.wikipedia.org/wiki/Objective-C#.E5.8A.A8.E6.80.81.E7.B1.BB.E5.9E.8B)]
