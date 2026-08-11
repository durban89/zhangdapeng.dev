---
title: "iOS中NSUserDefaults的简单使用"
date: "2025-06-17 18:51:22"
slug: "ios-zhong-nsuserdefaults-de-jian-dan-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS中NSUserDefaults的简单使用/"
  - "/2025/06/17/iOS中NSUserDefaults的简单使用.html"
  - "/iOS中NSUserDefaults的简单使用/"
  - "/iOS中NSUserDefaults的简单使用.html"
  - "/2025/06/17/ios-zhong-nsuserdefaults-de-jian-dan-shi-yong/"
  - "/2025/06/17/ios-zhong-nsuserdefaults-de-jian-dan-shi-yong.html"
  - "/ios-zhong-nsuserdefaults-de-jian-dan-shi-yong.html"
---
创建一个user defaults方法有多个，最简单得快速创建方法:

```objectivec
NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
```

添加数据到 user defaults:

```objectivec
[accountDefaults setObject:nameField.text forKey:UserDefaultNameKey];
```

也可以添加基本数据类型int, float, bool等，有相应得方法

```objectivec
[accountDefaults setBool:YES forKey:UserDefaultBoolKey];
```

实例代码：

```objectivec
NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
[accountDefaults setObject:@"yes" forKey:@"login"];
[accountDefaults setBool:YES forKey:@"login_state"];
```

从user defaults中获取数据:

```objectivec
[accountDefaults objectForKey:NCUserDefaultNameKey]
[accountDefaults boolForKey: UserDefaultBoolKey];
```

实例代码：

```objectivec
NSUserDefaults *accountDefaults = [NSUserDefaults standardUserDefaults];
NSLog(@"login = %@",[accountDefaults objectForKey:@"login"]);
NSLog(@"login_state = %d",[accountDefaults boolForKey: @"login_state"]);
```

要点： NSUserDefaults非常好用，并不需要用户在程序中设置NSUserDefaults的全局变量，需要在哪里使用NSUserDefaults的数据，那么就在哪里创建一个NSUserDefaults对象，然后进行读或者写操作。

针对同一个关键字对应的对象或者数据，可以对它进行重写，重写之后关键字就对应新的对象或者数据，旧的对象或者数据会被自动清理。

参考文章：http://blog.csdn.net/binyanye1/article/details/7633728
