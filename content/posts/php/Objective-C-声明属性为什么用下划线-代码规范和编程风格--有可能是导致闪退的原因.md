---
title: "Objective-C 声明属性为什么用下划线，代码规范和编程风格 ,有可能是导致闪退的原因"
date: "2025-06-17 18:57:15"
slug: "objective-c-sheng-ming-shu-xing-wei-shen-me-yong-xia-hua-xian-dai-ma-gui-fan-he-bian-cheng-feng-ge-you-ke-neng-shi-dao-zhi-shan-tui-de-yuan-yin"
categories: ["技术"]
tags: ["Objective-C"]
aliases:
  - "/2025/06/17/Objective-C-声明属性为什么用下划线，代码规范和编程风格-,有可能是导致闪退的原因/"
  - "/2025/06/17/Objective-C-声明属性为什么用下划线，代码规范和编程风格-,有可能是导致闪退的原因.html"
  - "/Objective-C-声明属性为什么用下划线，代码规范和编程风格-,有可能是导致闪退的原因/"
  - "/Objective-C-声明属性为什么用下划线，代码规范和编程风格-,有可能是导致闪退的原因.html"
  - "/2025/06/17/Objective-C-声明属性为什么用下划线-代码规范和编程风格-有可能是导致闪退的原因/"
  - "/2025/06/17/Objective-C-声明属性为什么用下划线-代码规范和编程风格-有可能是导致闪退的原因.html"
  - "/2025/06/17/objective-c-sheng-ming-shu-xing-wei-shen-me-yong-xia-hua-xian-dai-ma-gui-fan-he-bian-ch/"
  - "/2025/06/17/objective-c-sheng-ming-shu-xing-wei-shen-me-yong-xia-hua-xian-dai-ma-gui-fan-he-bia.html"
  - "/objective-c-sheng-ming-shu-xing-wei-shen-me-yong-xia-hua-xian-dai-ma-gui-fan-he-bian-cheng-fen.html"
---
在阅读和书写关于iPhone编程的代码的时候，发现有很多这样的情况：  
看到很多源代码里面，使用前面带下划线变量，然后在@synthesize 语句中在用一个不带下划线的变量名。  
  
这样做，到底有什么作用？  
  
因为我常常是以这种方式来做的：  
`*.h`中申明变量

```objectivec
#import <UIKit/UIKit.h>

@interface NewPlayerController : UIViewController{
    NSString *test;
}

@property(nonatomic,retain) NSString *test;

@end
```

在`*.m`中

```objectivec
#import "NewPlayerController.h"

@implementation NewPlayerController

@synthesize test;


- (void)viewDidLoad{

    [super viewDidLoad];

    test=[[NSString alloc] initWithFormat:@"test"];
}
@end
```

但是，发现很多别人写的代码是这样子的：  
`*.h`中申明变量

```objectivec
#import <UIKit/UIKit.h>

@interface NewPlayerController : UIViewController{
    NSString* _test;
}

@property(nonatomic,retain) NSString *test;

@end
```

在`*.m`中

```objectivec
#import "NewPlayerController.h"

@implementation NewPlayerController

@synthesize test=_test;

- (void)viewDidLoad{

    [super viewDidLoad];

    _test=[[NSString alloc] initWithFormat:@"test"];

    // 或者这样
    self.test=[[NSString alloc] initWithFormat:@"test"];
}

@end
```

这两种方式到底有什么区别？用那种好？  
  
带着这个疑问，我去网上搜索"代码风格"，“编码规范”，“下划线公约”。解释太宽泛了，根本没有一个定论。  
  
于是只有理论+实践自己在走一回吧。  
  
开始：  
第一种方式，就是平常我们说的不带下划线的那种方式：

```objectivec
self.test=[[NSString alloc] initWithFormat:@"test"];
NSLog(@"self.test的应用计数:%d",[self.test retainCount]);
NSLog(@"test的应用计数:%d",[test retainCount]);
```

但是，我惊奇的发现，输出竟然这样：

```objectivec
2012-11-17 15:52:29.604 ArtTV[901:14303] self.test的应用计数:2
2012-11-17 15:52:33.264 ArtTV[901:14303] test的应用计数:2
```

self.test和test的地址是相同的，说明是同一个对象的应用，但为什么，应用计数会是2呢？  
  
于是，代码变成这样写（仅仅是，self.test换成test）：

```objectivec
test=[[NSString alloc] initWithFormat:@"test"];
NSLog(@"self.test的应用计数:%d",[self.test retainCount]);
NSLog(@"test的应用计数:%d",[test retainCount]);
```

输出：

```objectivec
2012-11-17 15:59:58.274 ArtTV[954:14303] self.test的应用计数:1
2012-11-17 15:59:59.718 ArtTV[954:14303] test的应用计数:1
```

这才是我们所期望的。应用计数应该为1才对，为什么会变成2呢？  
恍然大悟了！原来原因出在这里：我们申明test时，用的属性修饰符retain。  
当我们，使用self.test时，就使用了编译器为我们生成的setXXX方法。在该方法中retainCount被加1，所以，变为2.  
这样的花，如果，我们在代码中，直接用  
`self.test=[[NSString alloc] initWithFormat:@"test"]; ` 
这行代码后，test变量的应用计数变成了2：  
相当于：  
首先，声明一个字符串对象，这时候，引用计数为1.  
其次，再将test的值赋给self.test。（相当于，使用了setXXX方法，让retainCount，加1），导致应用计数变成2.  
所以，在类中，如果，仅仅是指针赋值，（将一个对象的指针赋给另一个指针）尽量避免使用self.test进行赋值。这样会引起引用计数+1，容易引起释放内存泄漏。而直接用test来赋值。  
也就是，在方法中，使用self.xxxx,进行赋值，就会使用编译器生成的setXXX方法，从而根据申明对象时的属性（copy，retain，assign）进行调用setXXX方法。  
如果，只用属性之间来赋值（test= newValue;，就是不带self），那么，仅仅是指针之间的赋值。  
第二种方式，就是带下划线的那种方式：  
这样，让我们验证：  
代码中，我们这么写：

```objectivec
test=[[NSString alloc] initWithFormat:@"test"];
```

我们会收到一个错误提示：

Object-C <wbr>声明属性为什么用下划线，代码规范和编程风格

看来，不能直接访问，test，而要用`_test`来代替。

不管它，那就用它推荐的方法，继续写完：

```objectivec
self.test=[[NSString alloc] initWithFormat:@"test"];
NSLog(@"self.test的应用计数:%d",[self.test retainCount]);
NSLog(@"_test的应用计数:%d",[_test retainCount]);
```

运行代码，输出如下：

```objectivec
2012-11-17 16:30:39.525 ArtTV[1042:14303] self.test的应用计数:2
2012-11-17 16:30:41.553 ArtTV[1042:14303] _test的应用计数:2
```

运行输出，很显然，应用计数为2，不是我们想要的结果。原因，跟我们讨论的第一种情况，是一样的。  
这仅仅是一种调用的另一种方式：  
默认情况，调用test，当我们申明`test=_test`;时候，那么在类内部使用`_test`。  
在使用`_test`，时候，也仅仅是指针的赋值。  
使用`self.test`，就是要调用编译器生成的响应的getXXX，setXXX方法了。  
为了证明我们的想法，我们将代码修改成这样：

```objectivec
_test=[[NSString alloc] initWithFormat:@"test"];
NSLog(@"self.test的应用计数:%d",[self.test retainCount]);
NSLog(@"_test的应用计数:%d",[_test retainCount]);
```

输出如下：

```objectivec
2012-11-17 16:36:09.089 ArtTV[1074:14303] self.test的应用计数:1
2012-11-17 16:36:10.701 ArtTV[1074:14303] _test的应用计数:1
```

关于，使用方式，我们就将到这里吧。亲自动手，实验一下。就明白其中的奥妙了！  
但是，还没有结束！  
另一个疑惑，也随之而来。  
我们用那种方式好呢？？？？  
我看了一些帖子，说，苹果不提倡在我们定义的类中使用“`_xxxx`”，这种形式的属性声明，因为，在很多苹果提供的框架中，大量使用“`_xxxx`”这种属性声明。  
  
——————————————————————————————————————  
Cocoa编码指南: 编程公约:  
  
避免使用下划线作为前缀，特别是在私有方法中。苹果公司保留并使用本公约。使用第三方可能会导致命名空间冲突；自己不知不觉中，可能会覆盖现有的私有方法，带来灾难性的后果。  
——————————————————————————————————————  
  
打开一个看看：  
  
Object-C <wbr>声明属性为什么用下划线，代码规范和编程风格  
确实，如此啊！  
在这种情况下，如果，我们，继承了某个框架类，并且无意间声明的“`_xxxx`”属性跟父类的相同，那么可能就会覆盖掉，从而引发不可估计的后果！  
但是，我看苹果帮助文档中写的许多例子也在用“`_xxxx`”这种方式啊！所以，我觉的可以用，但要注意！Object-C <wbr>声明属性为什么用下划线，代码规范和编程风格  
为什么是可以用呢？  
  
因为个人感觉：“`_xxxx`”确实很好用！  
1.从风格上表明类的内部变量。  
2.意在指明这个变量是内部变量（类外部不会使用。。。）  
3.外部访问用obj.xxxxx, 避免对类变量的直接访问。  
4.这样的话，要是需要直接引用变量就用`_xxxx`，当需要用get，set方法时，就用self.xxx。  
汇成一句话：  
下划线和非下划线的使用，可以说是一种习惯问题吧。不用太过于纠结！  
默认情况下，@synthesize name;编译器为我们生成的get，set方法中所使用的变量名称，跟我们申明的变量名称时一样的（仅仅用self.name和name来区分确实不够理想）。  
但是，当我们用`@synthesize name=_name;`时，就为属性取了一个别名，那样的话，指针变量，跟编译器生成的get，set方法为属性赋值时就容易区分了！  
文章参考:http://blog.csdn.net/qq515383106/article/details/8508611
