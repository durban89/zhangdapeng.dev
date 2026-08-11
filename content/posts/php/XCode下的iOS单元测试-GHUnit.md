---
title: "XCode下的iOS单元测试 GHUnit"
date: "2025-06-19 10:24:13"
slug: "xcode-xia-de-ios-dan-yuan-ce-shi-ghunit"
categories: ["技术"]
tags: ["Xcode", "iOS"]
aliases:
  - "/2025/06/19/XCode下的iOS单元测试-GHUnit/"
  - "/2025/06/19/XCode下的iOS单元测试-GHUnit.html"
  - "/XCode下的iOS单元测试-GHUnit/"
  - "/XCode下的iOS单元测试-GHUnit.html"
  - "/2025/06/19/xcode-xia-de-ios-dan-yuan-ce-shi-ghunit/"
  - "/2025/06/19/xcode-xia-de-ios-dan-yuan-ce-shi-ghunit.html"
  - "/xcode-xia-de-ios-dan-yuan-ce-shi-ghunit.html"
---
关于GHUnit的使用，我是摘自一篇比较不错的文章，里面即讲到了Xcode本身自带的测试工具OCUnit，同时也介绍了GHUnit，看完后很是受益呀。

XCode 内置了 OCUnit 单元测试框架，但目前最好用的测试框架应该是 GHUnit。通过 GHUnit + OCMock 组合，我们可以在 iOS 下进行较强大的单元测试功能。本文将演示如何在 XCode 4.2 下使用 OCUnit， GHUnit 和 OCMock 进行单元测试。

### [OCUnit](#1)

在 XCode 下新建一个 OCUnitProject 工程，选中 Include Unit Tests 选择框，  
  
OCUnit 框架则会为我们自动添加 Unit Test 框架代码：  
  
XCode 在 OCUnitProjectTests.m 中为我们自动生成了一个 Fail 的测试：

```objectivec
- (void)testExample
{
    STFail(@"Unit tests are not implemented yet in OCUnitProjectTests");
}
```

让我们来运行 Test，看看效果：  
  
从图中的红色下划线部分可以看出，测试没有通过，符合预期。我们只要像类 OCUnitProjectTests 一样编写继承自 SenTestCase 类的子类，在其中添加形式如：- (void) testXXX(); 的测试函数既可，注意必须是一个无参无返回类型且名称是以 test 为前缀的函数。  
  
OCUnit 的有点是官方支持，于 XCode 集成的比较好。

### [GHUnit](#2)

GHUnit 是一个开源的单元测试框架，具有可视化界面，功能亦相当强大。Mark 写了一篇 OCUnit vs GHUnit 的文章，有兴趣的童鞋可以看一看。OCMock 是由 Mulle Kybernetik 为 OS X 和 iOS 平台编写的遵循 mock object 理念的单元测试框架。  
  
下面来介绍如何配置 GHUnit 和 OCMock  
  
1，首先，创建一个名为 GHUnitProject 的单视图应用程序，注意：不要选中 Include Unit Tests 选择框。然后运行，应该出现白屏。

2，添加新的 test target，选中左边的工程名，点击右侧的 Add Target，新增一个名为 Tests 的 Empty Application 应用程序，让其附属于 GHUnitProject注意：不要选中 Include Unit Tests 选择框。

3，向 Tests 工程中（注意是 Tests 工程）添加 GHUnitIOS Framework。首先下载与 XCode 版本对应的 GHUnitIOS Framework。英文好的可以直接查看官方 iOS 版的安装文档：点此查看，跳过此第 3 节；否则请接着看。

3.1，解压 GHUnitIOS 框架到 GHUnitProject 下，让 GHUnitIOS.framework 与 Tests 在同一目录下。

3.2，回到 XCode，右击工程中的 Frameworks group，选中 Add Files to...菜单，选取 GHUnitIOS.framework ，注意 targets 要选择 Tests。

3.3，设置 Tests 的 Build Settings：在 Other Linker Flags 中增加两个 flag： -ObjC 和 -all\_load。

3.4，删除 Tests 工程中的 UTSAppDelegate.h 和  UTSAppDelegate.m 两个文件；

3.5，修改 Tests 工程中的 main.m 为:

```
#import <UIKit/UIKit.h>

#import <GHUnitIOS/GHUnitIOSAppDelegate.h>

int main(int argc, char *argv[])
{
    @autoreleasepool {
        return UIApplicationMain(argc, argv, nil, NSStringFromClass([GHUnitIOSAppDelegate class]));
    }
}
```

3.6，选择编译目标 Tests>iPhone 5.0 Simulator，编译运行，应该能得到如下效果。目前我们还没有编写任何实际测试，所以列表为空。  
  
4，编写 GHUnit 测试。向 Tests 工程中添加名为 GHUnitSampleTest 的 Objective C class。其内容如下：  
  


```objectivec GHUnitSampleTest.h
#import <GHUnitIOS/GHUnit.h>

@interface GHUnitSampleTest: GHTestCase

{

}

@end
```


```objectivec GHUnitSampleTest.m

#import "GHUnitSampleTest.h"

@implementation GHUnitSampleTest

- (void)testStrings

{       

    NSString *string1 = @"a string";

    GHTestLog(@"I can log to the GHUnit test console: %@", string1);

     // Assert string1 is not NULL, with no custom error description

    GHAssertNotNULL(string1, nil);

     // Assert equal objects, add custom error description

    NSString *string2 = @"a string";

    GHAssertEqualObjects(string1, string2, @"A custom error message. string1 should be equal to: %@.", string2);

}

@end
```

然后编译运行，点击 Run，效果如下：

图中的 All 栏显示所以的测试，Failed 栏显示没有通过的测试。强大吧，GHUnit。你可以向 GHUnitSampleTest 添加新的测试，比如：

```objectivec
- (void)testSimpleFail

{

    GHAssertTrue(NO, nil);

}
```

我们可以向 Tests 添加更多测试类，只要该类是继承自 GHTestCase，且其中的测试方法都是无参无返回值且方法名字是以 test 为前缀即可

是不是有种感觉就是，以后再多的bug都不怕啦。哦也
