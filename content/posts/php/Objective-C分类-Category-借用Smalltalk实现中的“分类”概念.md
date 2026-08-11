---
title: "Objective-C分类(Category)借用Smalltalk实现中的“分类”概念"
date: "2025-06-05 10:26:00"
slug: "objective-c-fen-lei-category-jie-yong-smalltalk-shi-xian-zhong-de-fen-lei-gai-nian"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/05/Objective-C分类(Category)借用Smalltalk实现中的“分类”概念/"
  - "/2025/06/05/Objective-C分类(Category)借用Smalltalk实现中的“分类”概念.html"
  - "/Objective-C分类(Category)借用Smalltalk实现中的“分类”概念/"
  - "/Objective-C分类(Category)借用Smalltalk实现中的“分类”概念.html"
  - "/2025/06/05/Objective-C分类-Category-借用Smalltalk实现中的“分类”概念/"
  - "/2025/06/05/Objective-C分类-Category-借用Smalltalk实现中的“分类”概念.html"
  - "/2025/06/05/objective-c-fen-lei-category-jie-yong-smalltalk-shi-xian-zhong-de-fen-lei-gai-nian/"
  - "/2025/06/05/objective-c-fen-lei-category-jie-yong-smalltalk-shi-xian-zhong-de-fen-lei-gai-nian.html"
  - "/objective-c-fen-lei-category-jie-yong-smalltalk-shi-xian-zhong-de-fen-lei-gai-nian.html"
---
在Objective-C的设计中，一个主要的考虑即为大型代码框架的维护。结构化编程的经验显示，改进代码的一种主要方法即为将其分解为更小的片段。Objective-C借用并扩展了Smalltalk实现中的“分类”概念，用以帮助达到分解代码的目的。[1]

一个分类可以将方法的实现分解进一系列分离的文件。程序员可以将一组相关的方法放进一个分类，使程序更具可读性。举例来讲，可以在字符串类中增加一个名为“拼写检查”的分类，并将拼写检查的相关代码放进这个分类中。


进一步的，分类中的方法是在运行时被加入类中的，这一特性允许程序员向现存的类中增加方法，而无需持有原有的代码，或是重新编译原有的类。例如若系统提供的字符串类的实现中不包含拼写检查的功能，可以增加这样的功能而无需更改原有的字符串类的代码。

在运行时，分类中的方法与类原有的方法并无区别，其代码可以访问包括私有类成员变量在内的所有成员变量。

若分类声明了与类中原有方法同名的函数，则分类中的方法会被调用。因此分类不仅可以增加类的方法，也可以代替原有的方法。这个特性可以用于修正原有代码中的错误，更可以从根本上改变程序中原有类的行为。若两个分类中的方法同名，则被调用的方法是不可预测的。

其它语言也尝试了通过不同方法增加这一语言特性。TOM在这方面走的更远，不仅允许增加方法，更允许增加成员变量。也有其它语言使用面向声明的解决方案，其中最值得注意的是Self语言。

C#与Visual Basic.NET语言以扩展函数的与不完全类的方式实现了类似的功能。Ruby与一些动态语言则以"monkey patch"的名字称呼这种技术。

使用分类的例子

这个例子创建了Integer类，其本身只定义了integer属性，然后增加了两个分类Arithmetic与Display以扩展类的功能。虽然分类可以访问类的私有成员，但通常利用属性的访问方法来访问是一种更好的做法，可以使得分类与原有类更加独立。这是分类的一种典型应用—另外的应用是利用分类来替换原有类中的方法，虽然用分类而不是继承来替换方法不被认为是一种好的做法。

```c Integer.h

#import <objc/Object.h>
 
@interface Integer : Object
{
@private
    int integer;
}
 
@property (assign, nonatomic) integer;
 
@end
```

```c Integer.m

#import "Integer.h"
 
@implementation Integer
 
@synthesize integer;
 
@end
```

```c Arithmetic.h

#import "Integer.h"
 
@interface Integer (Arithmetic)
- (id) add: (Integer *) addend;
- (id) sub: (Integer *) subtrahend;
@end
```

```c Arithmetic.m

#import "Arithmetic.h"
@implementation Integer (Arithmetic)
- (id) add: (Integer *) addend{
    self.integer = self.integer + addend.integer;
    return self;
}
 
- (id) sub: (Integer *) subtrahend{
    self.integer = self.integer - subtrahend.integer;
    return self;
}
@end
```

```c Display.h

 

#import "Integer.h"
@interface Integer (Display)
- (id) showstars;
- (id) showint;
@end
```

```c Display.m

#import "Display.h"
@implementation Integer (Display)
- (id) showstars{
    int i, x = self.integer;
    for(i=0; i < x; i++)
       printf("*");
    printf("\n");
 
    return self;
}
 
- (id) showint{
    printf("%d\n", self.integer);
 
    return self;
}
@end
```

```c main.m

 

#import "Integer.h"
#import "Arithmetic.h"
#import "Display.h"
int 
main(void){
    Integer *num1 = [Integer new], *num2 = [Integer new];
    int x;
 
    printf("Enter an integer: ");
    scanf("%d", &x);
 
    num1.integer = x;
    [num1 showstars];
 
    printf("Enter an integer: ");
    scanf("%d", &x);
 
    num2.integer = x;
    [num2 showstars];
 
    [num1 add:num2];
    [num1 showint];
 
    return 0;
}
```

注释

可以利用以下命令来编译：
```shell
gcc -x objective-c main.m Integer.m Arithmetic.m Display.m -lobjc
```

在编译时间，可以利用省略`#import "Arithmetic.h"`与`[num1 add:num2]`命令，以及Arithmetic.m文件来实验。程序仍然可以运行，这表明了允许动态的、按需的加载分类；若不需要某一分类提供的功能，可以简单的不编译之。

源自：[维基百科](https://zh.wikipedia.org/wiki/Objective-C#.E5.88.86.E9.A1.9E_.28Category.29)
