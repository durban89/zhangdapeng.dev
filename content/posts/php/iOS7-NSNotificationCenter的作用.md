---
title: "iOS7 NSNotificationCenter的作用"
date: "2025-06-26 11:15:52"
slug: "ios7-nsnotificationcenter-de-zuo-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-NSNotificationCenter的作用/"
  - "/2025/06/26/iOS7-NSNotificationCenter的作用.html"
  - "/iOS7-NSNotificationCenter的作用/"
  - "/iOS7-NSNotificationCenter的作用.html"
  - "/2025/06/26/ios7-nsnotificationcenter-de-zuo-yong/"
  - "/2025/06/26/ios7-nsnotificationcenter-de-zuo-yong.html"
  - "/ios7-nsnotificationcenter-de-zuo-yong.html"
---
关于NSNotificationCenter的使用，之前一直想使用一下，结果今天就真的使用上了。

> NSNotificationCenter有什么作用，简单说之，就是两个不相干的对象之间可以通过他来传递消息，只要你把相关发送的消息和处理的事件在他那里注册就行了。
>
> 我们可以这样理解：NSNotificationCenter就是一个信息中心，有很多用户已经声明他们需要这些信息。当有信息更新的时候，通过这个NSNotificationCenter就可以以广播的形式，将信息更新的消息在整个应用程序中间广播，对于那些注册消息侦听的用户就可以受到该消息，没有注册的用户就无法接收该消息。

使用方法如下：

第一步：定义一个方法，当注册信息侦听的对象，接受到消息后就调用该函数作为消息相应的函数

```objectivec
-(void)update:(NSNotificationCenter*)notification
{
    [self addHeadImage];
    [[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:@"updateMe"
                                                  object:nil];
}
```

第二步：对象注册，并关连消息。实质上也就是注册事件的侦听，可以单独调用，也可以放在自己的函数内部进行调用。

```objectivec
[[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(update:)
                                                 name:@"updateMe"
                                               object:nil];
```

在函数中进行调用

```objectivec
-(void) sinaLogin:(id)sender
{
    [[NSNotificationCenter defaultCenter] addObserver:self
                                             selector:@selector(update:)
                                                 name:@"updateMe"
                                               object:nil];
    
    WBAuthorizeRequest *request = [WBAuthorizeRequest request];
    request.redirectURI = kRedirectURI;
    request.scope = @"all";
    [WeiboSDK sendRequest:request];
}
```

第三步：在要发出通知消息的地方调用。

```objectivec
[[NSNotificationCenter defaultCenter] postNotificationName:@"updateMe"
                                                            object:nil];
```

第四步：使用完后，别忘了注销掉该消息的侦听函数

```objectivec
[[NSNotificationCenter defaultCenter] removeObserver:self
                                                    name:@"updateMe"
                                                  object:nil];
```

其实这里我是放在了我的调用函数里面，如果你觉的你的函数在调用完之后不去注销，也可以去掉的，然后在其他的地方进行注销。

---

参考文章：

http://blog.csdn.net/sjzsp/article/details/6777700

