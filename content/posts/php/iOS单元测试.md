---
title: "iOS单元测试"
date: "2025-06-19 09:58:33"
slug: "ios-dan-yuan-ce-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/iOS单元测试/"
  - "/2025/06/19/iOS单元测试.html"
  - "/iOS单元测试/"
  - "/iOS单元测试.html"
  - "/2025/06/19/ios-dan-yuan-ce-shi/"
  - "/2025/06/19/ios-dan-yuan-ce-shi.html"
  - "/ios-dan-yuan-ce-shi.html"
---
关于这篇文章，要源于自己的一个测试，因为在一边学ios开发和学习的过程中，遇到一个问题就是做测试，但是测试的时候不知道为什么老是提示，没有test单元什么的错误，回到家，好好的琢磨了一下，发现了，这个是测试单元是可以自己创建的，我这里转载的一篇文章，来csdn，里面说的很详细，是如何进行测试单元的创建，的同时也解决了我的一个问题，就是“Unit tests are not implemented yet in WalkerUITests”这个问题，呵呵，笑死我啦，其实这个是一个测试单元建立成功的提示，接下来，做这个测试就很容易啦。

1、创建单元测试的target

选择工程，点击Add Target，添加ios-Other下的Cocoa Touch Unit Testing Bundle类型target。（网上一些资料说，target后缀必须是Tests，但实际测试同名字无关系，可能是Xcode版本原因）。

此时工程目录下会多一个Unistest8文件夹，Unistest8类是一个测试用例类Test8的一个实例。

2、添加SenTestingKit.framework

选中测试的Target，本项目中即Unitest8，查看Build Phases选项卡下的Link Binary With Libraries，会发现项目中缺少对SenTestingKit.framework库的引用，将其添加。

3、运行Unistest8测试

在Scheme中选择Unitest8，生成时一定要选择Product-Test，如果选择Run，则会出现“The scheme 'Unitest8' is not configured for Running”的错误。

成功运行后，发现输出错误，错误信息如下：

```bash
Unitest8.m:29: error: -[Unitest8 testExample] : Unit tests are not implemented       yet in Unitest8    



    Test Case '-[Unitest8 testExample]' failed (0.057 seconds).    
```

打开**Unitest8.m**，会发现在**Unitest8**类的实现文件中默认添加了一个测试函数testExample，并添加一个执行失败的提示，如下：

```objectivec
- (void)testExample{    
    STFail(@"Unit tests are not implemented yet in Unitest8");
}  
```

看到这个错误，整个测试的准备工作已经完成，接下来就可以在测试用例的类实例中添加测试函数，测试函数的名称就不能随意了，必须以test为前缀。在测试文件夹中还可以添加多个测试用例进行测试。

4、添加测试对象类，进行测试

完成步骤3后，可以开始对项目中具体的类进行方法测试。除了在相应的测试用例中添加该类的引用外，首先得将这个类引用加入该测试的Target（很2地因为这个问题卡了许久），在本项目里即为Unitest8。添加引用的方式是，点击测试target()，选择面板Build Phases，打开Compile Sources，选中项目中要测试类的.m实现文件将其拖入Compile Sources就ok。否则会产生如下error:

```bash
Undefined symbols for architecture i386:    
  "_OBJC_CLASS_$_测试类名", referenced from:    
      objc-class-ref inUnitest8.o    
ld: symbol(s) not found for architecture i386  
```

如果测试的类存在nib文件则需要将nib文件拖入Build Phases--Copy Bundle Resources中。

以上就是参考的文章的主要内容，这里介绍给大家，希望对自己有用，对自己也有用。

参考文章：http://blog.csdn.net/catandrat111/article/details/7819284
