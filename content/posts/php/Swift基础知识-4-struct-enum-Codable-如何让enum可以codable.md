---
title: "Swift基础知识（4） - struct enum Codable（如何让enum可以codable）"
date: "2025-07-11 11:16:03"
slug: "swift-ji-chu-zhi-shi-4-struct-enum-codable-ru-he-rang-enum-ke-yi-codable"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/11/Swift基础知识（4）-struct-enum-Codable（如何让enum可以codable）/"
  - "/2025/07/11/Swift基础知识（4）-struct-enum-Codable（如何让enum可以codable）.html"
  - "/Swift基础知识（4）-struct-enum-Codable（如何让enum可以codable）/"
  - "/Swift基础知识（4）-struct-enum-Codable（如何让enum可以codable）.html"
  - "/2025/07/11/Swift基础知识-4-struct-enum-Codable-如何让enum可以codable/"
  - "/2025/07/11/Swift基础知识-4-struct-enum-Codable-如何让enum可以codable.html"
  - "/2025/07/11/swift-ji-chu-zhi-shi-4-struct-enum-codable-ru-he-rang-enum-ke-yi-codable/"
  - "/2025/07/11/swift-ji-chu-zhi-shi-4-struct-enum-codable-ru-he-rang-enum-ke-yi-codable.html"
  - "/swift-ji-chu-zhi-shi-4-struct-enum-codable-ru-he-rang-enum-ke-yi-codable.html"
---
swift代码中时长会遇到codable的用法

但是不太理解其中的含义，也不太理解如何使用

于是google后发现了一篇比较好的文章，[点这里](https://stackoverflow.com/questions/44580719/how-do-i-make-an-enum-decodable-in-swift-4)

从代码中，或者实例中我们会遇到类似的使用方法

```swift
struct Landmark: Hashable, Codable
```

继承了`Codable`的话，就需要实现其中的协议方法

> It's pretty easy, just use String or Int raw values which are implicitly assigned.

看几个例子，引用了上面提到的文章中的例子

```swift
enum PostType: Int, Codable {
    case image, blob
}
```

这样用之后

image的值为0

blob的值为1

```swift
enum PostType: String, Codable {
    case image, blob
}
```

这样用之后

image的值为字符串 "image"

blob的值为字符串 "blob"

下面看下这个特殊的特性如何使用

```swift
enum PostType : Int, Codable {
    case count = 4
}

struct Post : Codable {
    var type : PostType
}

let jsonString = "{\"type\": 4}"

let jsonData = Data(jsonString.utf8)

do {
    let decoded = try JSONDecoder().decode(Post.self, from: jsonData)
    print("decoded:", decoded.type)
} catch {
    print(error)
}
```

如果这个例子能够看懂的话，那么下下面这个例子也是很容易理解的

```swift
struct Landmark: Hashable, Codable {
    var id: Int
    var name: String
    fileprivate var imageName: String
    fileprivate var coordinates: Coordinates

    var state: String
    var park: String
    var categroy: Category

    var locationCoordinate: CLLocationCoordinate2D {
        CLLocationCoordinate2D(latitude: coordinates.latitude, longitude: coordinates.longitude)
    }

    enum Category: String, Hashable {
        case featured = "Featured"
        case lakes = "Lakes"
        case rivers = "Rivers"
    }
}
```

运行后，会遇到如下错误

报错信息如下

```bash
Type 'Landmark' does not conform to protocol 'Decodable'
```

完整的，无问题的代码如下

```swift
struct Landmark: Hashable, Codable {
    var id: Int
    var name: String
    fileprivate var imageName: String
    fileprivate var coordinates: Coordinates

    var state: String
    var park: String
    var categroy: Category

    var locationCoordinate: CLLocationCoordinate2D {
        CLLocationCoordinate2D(latitude: coordinates.latitude, longitude: coordinates.longitude)
    }

    enum Category: String, Hashable, Codable {
        case featured = "Featured"
        case lakes = "Lakes"
        case rivers = "Rivers"
    }
}
```

从上面的例子中可以看出，Codable使用在struct和enum组合的使用方式中。
