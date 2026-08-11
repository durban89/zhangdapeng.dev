---
title: "Objective-C Hello World实例"
date: "2025-06-03 15:12:55"
slug: "objective-c-hello-world-shi-li"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/03/Objective-C-Hello-World实例/"
  - "/2025/06/03/Objective-C-Hello-World实例.html"
  - "/Objective-C-Hello-World实例/"
  - "/Objective-C-Hello-World实例.html"
  - "/2025/06/03/objective-c-hello-world-shi-li/"
  - "/2025/06/03/objective-c-hello-world-shi-li.html"
  - "/objective-c-hello-world-shi-li.html"
---
这里示范一个基础的Hello World程序。

```c
#import<Foundation/Foundation.h>
 
int main(int argc, char *argv[]){
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
 
    NSLog(@"Hello World!");
 
    [pool drain];
    return 0;
}
```

以上是Xcode的旧版"Hello World"程序代码，在4.3.1 xcode的代码为:

```c
#import <Foundation/Foundation.h>
 
int main(int argc, char *argv[]){
    @autoreleasepool{
        NSLog(@"Hello World!");
    }
    return 0;
}
```
