---
title: "Swift基础知识（3） - private和fileprivate的区别"
date: "2025-07-11 11:15:48"
slug: "swift-ji-chu-zhi-shi-3-private-he-fileprivate-de-qu-bie"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/11/Swift基础知识（3）-private和fileprivate的区别/"
  - "/2025/07/11/Swift基础知识（3）-private和fileprivate的区别.html"
  - "/Swift基础知识（3）-private和fileprivate的区别/"
  - "/Swift基础知识（3）-private和fileprivate的区别.html"
  - "/2025/07/11/Swift基础知识-3-private和fileprivate的区别/"
  - "/2025/07/11/Swift基础知识-3-private和fileprivate的区别.html"
  - "/2025/07/11/swift-ji-chu-zhi-shi-3-private-he-fileprivate-de-qu-bie/"
  - "/2025/07/11/swift-ji-chu-zhi-shi-3-private-he-fileprivate-de-qu-bie.html"
  - "/swift-ji-chu-zhi-shi-3-private-he-fileprivate-de-qu-bie.html"
---
private和fileprivate的区别，private在类中代表是私有的，只能本类使用

但是在swift也有，除此之外还有一个fileprivate

其实这两种访问控制形式相似，但是有两个区别。  
如果标记了文件专用文件，则可以在声明的文件中的任何位置读取该文件（即使在类型之外）。  
另一方面，私有属性只能在声明它的类型内部或在同一文件中创建的该类型的扩展内部读取。  
在实践中，您可能会发现private的使用明显多于fileprivate。

简单通过实例看下private和fileprivate的区别


```swift
import Cocoa

class A {
    private func foo() {}
    fileprivate func bar() {}

    func baz() {
        foo()
        bar()
    }
}

extension A {
    func test() {
        foo()
        bar()
    }
}

let a = A()
a.foo() // 'foo' is inaccessible due to 'private' protection level
a.bar()
a.test()
a.baz()
```
