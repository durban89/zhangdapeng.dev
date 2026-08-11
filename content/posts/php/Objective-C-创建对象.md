---
title: "Objective-C 创建对象"
date: "2025-06-03 17:03:50"
slug: "objective-c-chuang-jian-dui-xiang"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/03/Objective-C-创建对象/"
  - "/2025/06/03/Objective-C-创建对象.html"
  - "/Objective-C-创建对象/"
  - "/Objective-C-创建对象.html"
  - "/2025/06/03/objective-c-chuang-jian-dui-xiang/"
  - "/2025/06/03/objective-c-chuang-jian-dui-xiang.html"
  - "/objective-c-chuang-jian-dui-xiang.html"
---
## [Objective-C中创建对象的方法](#Objective-C)：

Objective-C 创建对象需通过 alloc 以及 init。alloc的作用是分配内存，init 则是初始化对象。 init 与 alloc 都是定义在 NSObject 里的方法，父对象收到这两个信息并做出正确回应后，新对象才创建完毕。以下为范例：

```c
MyObject * my = [[MyObject alloc] init];
```

在 Objective-C 2.0 里，若创建对象不需要参数，则可直接使用 new

```c
MyObject * my = [MyObject new];
```

这仅仅是语法上的精简，效果完全相同。

若要自己定义初始化的过程，可以重写 init 方法，来添加额外的工作。(用途类似 C++ 的构造函数 constructor)
```c
- (id) init {
    if ( self=[super init] ) {   // 必须调用父类的 init
        // do something here ...
    }
    return self;
}
```
