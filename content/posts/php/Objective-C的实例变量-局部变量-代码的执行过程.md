---
title: "Objective-C的实例变量，局部变量，代码的执行过程"
date: "2025-06-19 10:29:17"
slug: "objective-c-de-shi-li-bian-liang-ju-bu-bian-liang-dai-ma-de-zhi-xing-guo-cheng"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/19/Objective-C的实例变量，局部变量，代码的执行过程/"
  - "/2025/06/19/Objective-C的实例变量，局部变量，代码的执行过程.html"
  - "/Objective-C的实例变量，局部变量，代码的执行过程/"
  - "/Objective-C的实例变量，局部变量，代码的执行过程.html"
  - "/2025/06/19/Objective-C的实例变量-局部变量-代码的执行过程/"
  - "/2025/06/19/Objective-C的实例变量-局部变量-代码的执行过程.html"
  - "/2025/06/19/objective-c-de-shi-li-bian-liang-ju-bu-bian-liang-dai-ma-de-zhi-xing-guo-cheng/"
  - "/2025/06/19/objective-c-de-shi-li-bian-liang-ju-bu-bian-liang-dai-ma-de-zhi-xing-guo-cheng.html"
  - "/objective-c-de-shi-li-bian-liang-ju-bu-bian-liang-dai-ma-de-zhi-xing-guo-cheng.html"
---
实例变量是在类里面的变量  
比如：

```objectivec
@implementation FindPerformersViewController{
    int i;
}
```

i就是实例变量

局部变量是在方法里面的变量  
比如：

```objectivec
-(void) getVariable {
    int i = 0;
}
```

这里的i就是局部变量
