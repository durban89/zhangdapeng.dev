---
title: "Objective-C 学习 Objective-C枚举和结构体"
date: "2025-06-17 16:46:03"
slug: "objective-c-xue-xi-objective-c-mei-ju-he-jie-gou-ti"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/17/Objective-C-学习-Objective-C枚举和结构体/"
  - "/2025/06/17/Objective-C-学习-Objective-C枚举和结构体.html"
  - "/Objective-C-学习-Objective-C枚举和结构体/"
  - "/Objective-C-学习-Objective-C枚举和结构体.html"
  - "/2025/06/17/objective-c-xue-xi-objective-c-mei-ju-he-jie-gou-ti/"
  - "/2025/06/17/objective-c-xue-xi-objective-c-mei-ju-he-jie-gou-ti.html"
  - "/objective-c-xue-xi-objective-c-mei-ju-he-jie-gou-ti.html"
---
struct结构体中的数据不能赋初值,所以赋值只能通过声明加入的方式。

```objectivec
#import <Foundation/Foundation.h>
enum sex{
    male=0,
    female=1
};
typedef enum{
    c=3,
    d=4
}test2;
struct student {
    char* name;
    enum sex sex;
    int age;
};
typedef struct student stu;
int main(int argc, const char * argv[])
{
    stu su;
    su.name="wen";
    su.sex=male;
    NSLog(@"name=%s,sex=%d",su.name,su.sex);
    @autoreleasepool {
        
        // insert code here...
        NSLog(@"Hello, World!");
        
    }
    return 0;
}
```

参考：http://blog.csdn.net/wenwei19861106/article/details/8958800
