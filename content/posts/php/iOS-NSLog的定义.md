---
title: "iOS NSLog的定义"
date: "2025-06-10 10:01:36"
slug: "ios-nslog-de-ding-yi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-NSLog的定义/"
  - "/2025/06/10/iOS-NSLog的定义.html"
  - "/iOS-NSLog的定义/"
  - "/iOS-NSLog的定义.html"
  - "/2025/06/10/ios-nslog-de-ding-yi/"
  - "/2025/06/10/ios-nslog-de-ding-yi.html"
  - "/ios-nslog-de-ding-yi.html"
---
```objectivec
void NSLog(NSString *format, …);
```

基本上，NSLog很像printf，同样会在console中输出显示结果。不同的是，传递进去的格式化字符是NSString的对象，而不是char \*这种字符串指针。

实例：

NSLog可以如下面的方法使用：

```objectivec
NSLog (@"this is a test");
NSLog (@"string is :%@", string);
NSLog (@"x=%d, y=%d", 10, 20);
```

但是下面的写法是不行的：

```objectivec
int i = 12345;
NSLog( @"%@", i );
```

原因是， %@需要显示对象，而int i明显不是一个对象，要想正确显示，要写成：

```objectivec
int i = 12345;
NSLog( @"%d", i )；
```

格式：

NSLog的格式如下所示：

- %@ 对象

- %d, %i 整数

- %u 无符整形

- %f 浮点/双字

- %x, %X 二进制整数

- %o 八进制整数

- %zu size\_t%p 指针

- %e 浮点/双字 （科学计算）

- %g 浮点/双字

- %s C 字符串

- %.\*s Pascal字符串

- %c 字符

- %C unicha

- r%lld 64位长整数

- （long long）%llu 无符64位长整数

- %Lf 64位双字
