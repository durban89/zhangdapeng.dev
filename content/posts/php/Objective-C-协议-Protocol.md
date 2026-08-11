---
title: "Objective-C 协议(Protocol)"
date: "2025-06-03 16:54:11"
slug: "objective-c-xie-yi-protocol"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/03/Objective-C-协议(Protocol)/"
  - "/2025/06/03/Objective-C-协议(Protocol).html"
  - "/Objective-C-协议(Protocol)/"
  - "/Objective-C-协议(Protocol).html"
  - "/2025/06/03/Objective-C-协议-Protocol/"
  - "/2025/06/03/Objective-C-协议-Protocol.html"
  - "/2025/06/03/objective-c-xie-yi-protocol/"
  - "/2025/06/03/objective-c-xie-yi-protocol.html"
  - "/objective-c-xie-yi-protocol.html"
---
协议是一组尚未实现的方法列表，任何的类均可采纳该协议并给出方法的具体实现。

Objective-C在NeXT时期曾经试图引入多重继承的概念，但由于协议的出现而没有实现。协议的功能类似于C++中的多重抽象基类继承或是Java与C#语言中的“接口”。在Objective-C中，包括两种定义协议的方式：由编译器保证的“正式协议”，以及为特定目的设定的“非正式协议”。

非正式协议为一个可以选择性实现的一系列方法列表。非正式协议虽名为协议，但实际上是挂于NSObject上的未实现分类 (Unimplemented Category)的一种称谓，Objetive-C语言机制上并没有非正式协议这种东西，OSX 10.6版本之后由于正式协议也可以通过@optional关键字达成相同功用，所以非正式协议已经被废弃不再使用。


正式协议则类似于Java中的"接口"，它是一系列方法的列表，任何类都可以声明自身实现了某个协议。在Objective-C 2.0之前，一个类必须实现它声明符合的协议中的所有方法，否则编译器会报告一个错误，表明这个类没有实现它声明符合的协议中的全部方法。 Objective-C 2.0版本允许标记协议中某些方法为可选的(Optional)，这样编译器就不会强制实现这些可选的方法。

协议经常应用于Cocoa 中的委托及事件触发。例如文本框类通常会包括一个委托 (delegate)对象，该对象可以实现一个协议，该协议中可能包含一个实现文字输入的自动完成方法。若这个委托对象实现了这个方法，那么文本框类就会在适当的时候触发自动完成事件，并调用这个方法用于自动完成功能。

Objective-C中协议的概念与Java中接口的概念并不完全相同，即一个类可以在不声明它符合某个协议的情况下，实现这个协议所包含的方 法，也即实质上符合这个协议，而这种差别对外部代码而言是不可见的。正式协议的声明不提供实现，它只是简单地表明符合该协议的类实现了该协议的方法，保证 调用端可以安全调用方法。

语法

协议以关键字@protocol作为区段起始，@end退出，中间为方法列表。

```c
@protocol Locking
- (void)lock;
- (void)unlock;
@end
```

这是一个协议的例子，多线程编程中经常要确保一份共享资源同时只有一个线程可以使用，会在使用前给该资源挂上锁 ，以上即为一个表明有“锁”的概念的协议，协议中有两个方法，只有名称但尚未实现。

下面的SomeClass宣称他采纳了Locking协议：

```c
@interface SomeClass : SomeSuperClass <Locking>
@end
一旦SomeClass表明他采纳了Locking协议，SomeClass就有义务实现Locking协议中的两个方法。

@implementation SomeClass
- (void)lock {
  // 实现lock方法...
}
- (void)unlock {
  // 实现unlock方法...
}
@end
```

由于SomeClass已经确实遵从了Locking协议，故调用端可以安全的发送lock或unlock信息给SomeClass实体变量，不需担心他没有办法回应信息。

插件是另一个使用抽象定义的例子，可以在不关心插件的实现的情况下定义其希望的行为。
