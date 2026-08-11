---
title: "Objective-C对象发送消息[转发]"
date: "2025-06-04 16:54:17"
slug: "objective-c-dui-xiang-fa-song-xiao-xi-zhuan-fa"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/04/Objective-C对象发送消息[转发]/"
  - "/2025/06/04/Objective-C对象发送消息[转发].html"
  - "/Objective-C对象发送消息[转发]/"
  - "/Objective-C对象发送消息[转发].html"
  - "/2025/06/04/Objective-C对象发送消息-转发/"
  - "/2025/06/04/Objective-C对象发送消息-转发.html"
  - "/2025/06/04/objective-c-dui-xiang-fa-song-xiao-xi-zhuan-fa/"
  - "/2025/06/04/objective-c-dui-xiang-fa-song-xiao-xi-zhuan-fa.html"
  - "/objective-c-dui-xiang-fa-song-xiao-xi-zhuan-fa.html"
---
Objective-C允许对一个对象发送消息，不管它是否能够响应之。除了响应或丢弃消息以外，对象也可以将消息转发到可以响应该消息的对象。转发可以用于简化特定的设计模式，例如观测器模式或代理模式。

Objective-C运行时在Object中定义了一对方法：

A.转发方法:
```c
- (retval_t) forward:(SEL) sel :(arglist_t) args; // with GCC
- (id) forward:(SEL) sel :(marg_list) args; // with NeXT/Apple systems
```

B.响应方法:
```c
- (retval_t) performv:(SEL) sel :(arglist_t) args;  // with GCC
- (id) performv:(SEL) sel :(marg_list) args; // with NeXT/Apple systems
```
希望实现转发的对象只需用新的方法覆盖以上方法来定义其转发行为。无需重写响应方法performv::，由于该方法只是单纯的对响应对象发送消息并传递参数。其中，SEL类型是Objective-C中消息的类型。

例子

这里包括了一个演示转发的基本概念的程序示例。(代码来源：[维基百科Objective-C](https://zh.wikipedia.org/wiki/Objective-C))


```c Forwarder.h
#import <objc/Object.h>
 
@interface Forwarder : Object{
    id recipient; //该对象是我们希望转发到的对象。
}
 
@property (assign, nonatomic) id recipient;
 
@end
```


```c Forwarder.m
#import "Forwarder.h"
 
@implementation Forwarder
 
@synthesize recipient;
 
- (retval_t) forward: (SEL) sel : (arglist_t) args
{
    /*
     *检查转发对象是否响应该消息。
     *若转发对象不响应该消息，则不会转发，而产生一个错误。
     */
    if([recipient respondsTo:sel])
       return [recipient performv: sel : args];
    else
       return [self error:"Recipient does not respond"];
}
```

```c Recipient.h

#import <objc/Object.h>
 
// A simple Recipient object.
@interface Recipient : Object
- (id) hello;
@end
```

```c Recipient.m

#import "Recipient.h"
 
@implementation Recipient
 
- (id) hello{
    printf("Recipient says hello!\n");
 
    return self;
}
 
@end
```


```c main.m

#import "Forwarder.h"
#import "Recipient.h"
 
int main(void){
    Forwarder *forwarder = [Forwarder new];
    Recipient *recipient = [Recipient new];
 
    forwarder.recipient = recipient; //Set the recipient.
    /*
     *转发者不响应hello消息！该消息将被转发到转发对象。
     * (若转发对象响应该消息)
     */
    [forwarder hello];
 
    return 0;
}
```

脚注

利用GCC编译时，编译器报告：

```shell
$ gcc -x objective-c -Wno-import Forwarder.m Recipient.m main.m -lobjc
main.m: In function `main':
main.m:12: warning: `Forwarder' does not respond to `hello'

```

如前文所提到的，编译器报告Forwarder类不响应hello消息。在这种情况下，由于实现了转发，可以忽略这个警告。 运行该程序产生如下输出：

```shell
$ ./a.out
Recipient says hello!
```
