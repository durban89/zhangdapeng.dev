---
title: "Objective-C 类型的声明与实现"
date: "2025-06-03 16:45:02"
slug: "objective-c-lei-xing-de-sheng-ming-yu-shi-xian"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/03/Objective-C-类型的声明与实现/"
  - "/2025/06/03/Objective-C-类型的声明与实现.html"
  - "/Objective-C-类型的声明与实现/"
  - "/Objective-C-类型的声明与实现.html"
  - "/2025/06/03/objective-c-lei-xing-de-sheng-ming-yu-shi-xian/"
  - "/2025/06/03/objective-c-lei-xing-de-sheng-ming-yu-shi-xian.html"
  - "/objective-c-lei-xing-de-sheng-ming-yu-shi-xian.html"
---
Objective-C 类型要求区分接口（interface）与实现（implementation）为两个程序区块，这是强制性的。

类型的接口通常放置于头文件内，依C语言的惯例以.h作为扩展名；类型的实现则放于以.m为扩展名。

 

## [Interface](#Interface)

接口区段里头清楚定义了类型的名称，实体变量（instance variable），以及方法。 以关键字@interface作为区段起头，@end退出区段。

```c
@interface MyObject : NSObject {
    int memberVar1; // 实体变量
    id  memberVar2;
}
+(return_type) class_method;            // 类别分类
 
-(return_type) instance_method1;        // 实体方法
-(return_type) instance_method2: (int) p1;
-(return_type) instance_method3: (int) p1 andPar: (int) p2;
@end
```

方法前面的+/-号代表方法的类型：`加号（+）`代表类型方法（class method），不需要实体就可以调用，近于C++的静态成员函数（static member function）。`减号（-）`即是一般的实体方法（instance method）。 这里提供了一份意义相近的C++语法对照，如下：
```c
class MyObject : public NSObject {
  protected:
    int memberVar1;  // 实体变量
    void * memberVar2;
 
  public:
    static return_type class_method(); // 类别方法
 
    return_type instance_method1();    // 实体方法
    return_type instance_method2( int p1 );
    return_type instance_method3( int p1, int p2 );
}
```

Objective-C定义一个新的方法时，名称内的冒号（:）代表参数传递，不同于C语言以数学函数的括号来传递参数。Objective-C方法的参数也不必全部都附缀于方法名称的尾端，也可以夹杂于名称中间，提高程序可读性。以一个设置颜色RGB值的方法为例:

```c
- (void) setColorToRed: (float)red Green: (float)green Blue:(float)blue; /* 声明方法 */

[myColor setColorToRed: 1.0 Green: 0.8 Blue: 0.2]; /* 调用方法 */
```

这个方法的全名是setColorToRed:Green:Blue:。每个冒号后面都带着一个形态为float的参数，分别代表红，绿，蓝三色。

## [Implementation](#Implementation)

实现区段则撰写方法实际运行的程序。以关键字@implementation作为区段起头，@end结尾。

```c
@implementation MyObject {
  int memberVar3; //私有实体变量
}
 
+(return_type) class_method {
    .... //method implementation
}
-(return_type) instance_method1 {
     ....
}
-(return_type) instance_method2: (int) p1 {
    ....
}
-(return_type) instance_method3: (int) p1 andPar: (int) p2 {
    ....
}
@end
```

值得一提的是不只interface区段开头可以声明实体变量，implementation区段开头也可以声明实体变量，两者的差别在于成员访问权限， 声明于interface区段内的实体变量默认权限为protected，声明于implementation区段的实体变量则默认为private，基 于面向对象的封装原则，仅供类型内部使用的变量请尽可能声明于implementation区段(.m档)内，不需要曝露于interface(.h档) 中。
