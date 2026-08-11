---
title: "关于typedef的用法总结"
date: "2025-06-11 13:53:59"
slug: "guan-yu-typedef-de-yong-fa-zong-jie"
categories: ["技术"]
tags: ["C"]
aliases:
  - "/2025/06/11/关于typedef的用法总结/"
  - "/2025/06/11/关于typedef的用法总结.html"
  - "/关于typedef的用法总结/"
  - "/关于typedef的用法总结.html"
  - "/2025/06/11/guan-yu-typedef-de-yong-fa-zong-jie/"
  - "/2025/06/11/guan-yu-typedef-de-yong-fa-zong-jie.html"
  - "/guan-yu-typedef-de-yong-fa-zong-jie.html"
---
不管是在C还是C++代码中，typedef这个词都不少见，当然出现频率较高的还是在C代码中。typedef与#define有些相似，但更多的是不同，  
特别是在一些复杂的用法上，就完全不同了。

### [用途一](#1)

定义一种类型的别名，而不只是简单的宏替换。可以用作同时声明指针型的多个对象。比如：

```c
char* pa, pb; // 这多数不符合我们的意图，它只声明了一个指向字符变量的指针，和一个字符变量；
```

以下则可行：

```c
typedef char* PCHAR;
PCHAR pa, pb;
```

这种用法很有用，特别是char\* pa, pb的定义，初学者往往认为是定义了两个字符型指针，其实不是，而用typedef char\* PCHAR就不会出现这样的问题，减少了错误的发生。

### [用途二](#2)

用在旧的C代码中，帮助struct。以前的代码中，声明struct新对象时，必须要带上struct，即形式为： struct 结构名对象名，如：

```c
struct tagPOINT1
{
    int x;
    int y;
};
```

struct tagPOINT1 p1;  
而在C++中，则可以直接写：结构名对象名，即：tagPOINT1 p1;

```c
typedef struct tagPOINT
{
    int x;
    int y;
}POINT;
```

这样就比原来的方式少写了一个struct，比较省事，尤其在大量使用的时候,

```c
POINT p1;
```

或许，在C++中，typedef的这种用途二不是很大，但是理解了它，对掌握以前的旧代码还是有帮助的，毕竟我们在项目中有可能会遇到较早些年代遗留下来的代码。

### [用途三](#3)

用typedef来定义与平台无关的类型。  
比如定义一个叫 REAL 的浮点类型，在目标平台一上，让它表示最高精度的类型为：

```c
typedef long double REAL;
```

在不支持 long double 的平台二上，改为：

```c
typedef double REAL;
```

在连 double 都不支持的平台三上，改为：

```c
typedef float REAL;
```

也就是说，当跨平台时，只要改下 typedef 本身就行，不用对其他源码做任何修改。  
标准库就广泛使用了这个技巧，比如size\_t。另外，因为typedef是定义了一种类型的新别名，不是简单的字符串替换，所以它比宏来得稳健。  
这个优点在我们写代码的过程中可以减少不少代码量哦！

### [用途四](#4)

为复杂的声明定义一个新的简单的别名。方法是：在原来的声明里逐步用别名替换一部  
分复杂声明，如此循环，把带变量名的部分留到最后替换，得到的就是原声明的最简化版。  
举例：  
原声明：`void (*b[10]) (void (*)());`  
变量名为b，先替换右边部分括号里的，pFunParam为别名一：

```c
typedef void (*pFunParam)();
```

再替换左边的变量b，pFunx为别名二：

```c
typedef void (*pFunx)(pFunParam);
```

原声明的最简化版：

```c
pFunx b[10];
```

原声明：`doube(*)() (*e)[9];`
变量名为e，先替换左边部分，pFuny为别名一：

```c
typedef double(*pFuny)();
```

再替换右边的变量e，pFunParamy为别名二

```c
typedef pFuny (*pFunParamy)[9];
```

原声明的最简化版：

```c
pFunParamy e;
```

理解复杂声明可用的“右左法则”：从变量名看起，先往右，再往左，碰到一个圆括号  
就调转阅读的方向；括号内分析完就跳出括号，还是按先右后左的顺序，如此循环，直到整个声明分析完。  
举例：

```c
int (*func)(int *p);
```

首先找到变量名func，外面有一对圆括号，而且左边是一个\*号，这说明func是一个指针；  
然后跳出这个圆括号，先看右边，又遇到圆括号，这说明(\*func)是一个函数，所以func是一个指向这类函数的指针，即函数指针，  
这类函数具有int\*类型的形参，返回值类型是int。

```c
int (*func[5])(int *);
```

func右边是一个[]运算符，说明func是具有5个元素的数组；func的左边有一个\*，说明  
func的元素是指针（注意这里的\*不是修饰func，而是修饰func[5]的，原因是[]运算符  
优先级比\*高，func先跟[]结合）。跳出这个括号，看右边，又遇到圆括号，说明func数  
组的元素是函数类型的指针，它指向的函数具有int\*类型的形参，返回值类型为int。
