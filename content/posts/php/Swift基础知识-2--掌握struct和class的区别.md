---
title: "Swift基础知识（2）- 掌握struct和class的区别"
date: "2025-07-11 11:15:32"
slug: "swift-ji-chu-zhi-shi-2-zhang-wo-struct-he-class-de-qu-bie"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/11/Swift基础知识（2）-掌握struct和class的区别/"
  - "/2025/07/11/Swift基础知识（2）-掌握struct和class的区别.html"
  - "/Swift基础知识（2）-掌握struct和class的区别/"
  - "/Swift基础知识（2）-掌握struct和class的区别.html"
  - "/2025/07/11/Swift基础知识-2-掌握struct和class的区别/"
  - "/2025/07/11/Swift基础知识-2-掌握struct和class的区别.html"
  - "/2025/07/11/swift-ji-chu-zhi-shi-2-zhang-wo-struct-he-class-de-qu-bie/"
  - "/2025/07/11/swift-ji-chu-zhi-shi-2-zhang-wo-struct-he-class-de-qu-bie.html"
  - "/swift-ji-chu-zhi-shi-2-zhang-wo-struct-he-class-de-qu-bie.html"
---
很多新手在进行macOS app开发的时候  
创建完项目后一般会遇到一个问题，就是我连swift都没有学过，或者我只是接触过语法，那么看到下面这个ContentView.swift文件的代码的时候，代码如下

```swift
struct ContentView: View {
    @State var name: String = "durban"
    var body: some View {
        Text("Hello, World").frame(maxWidth: .infinity, maxHeight: .infinity)
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
```

可能完全迷糊

如果是从object-c转过来了的，看到这个可能也比较迷糊，比如我

一般正常的可能认为  
应该有个controller结尾的文件，跟我们使用Object-c开发项目的逻辑一样

其实实际上则不然

通过对swift项目的初步接触  
我了解到一个struct的不同之处  
可以说是与class类似的一个特殊使用方法

这里引用官网的说明

> Structures and classes in Swift have many things in common. Both can:
>
> * Define properties to store values
> * Define methods to provide functionality
> * Define subscripts to provide access to their values using subscript syntax
> * Define initializers to set up their initial state
> * Be extended to expand their functionality beyond a default implementation
> * Conform to protocols to provide standard functionality of a certain kind
>
> For more information, see Properties, Methods, Subscripts, Initialization, Extensions, and Protocols.
>
> Classes have additional capabilities that structures don’t have:
>
> * Inheritance enables one class to inherit the characteristics of another.
> * Type casting enables you to check and interpret the type of a class instance at runtime.
> * Deinitializers enable an instance of a class to free up any resources it has assigned.
> * Reference counting allows more than one reference to a class instance.
>
> For more information, see Inheritance, Type Casting, Deinitialization, and Automatic Reference Counting.
>
> The additional capabilities that classes support come at the cost of increased complexity. As a general guideline, prefer structures because they’re easier to reason about, and use classes when they’re appropriate or necessary. In practice, this means most of the custom data types you define will be structures and enumerations. For a more detailed comparison, see Choosing Between Structures and Classes.

原文访问地址[点这里](https://docs.swift.org/swift-book/LanguageGuide/ClassesAndStructures.html)

我认为读懂此部分相当重要
