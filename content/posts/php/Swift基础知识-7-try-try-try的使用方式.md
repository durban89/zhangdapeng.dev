---
title: "Swift基础知识（7）- try、try?、try!的使用方式"
date: "2025-07-15 09:51:40"
slug: "swift-ji-chu-zhi-shi-7-try-try-try-de-shi-yong-fang-shi"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/15/Swift基础知识（7）-try、try?、try!的使用方式/"
  - "/2025/07/15/Swift基础知识（7）-try、try?、try!的使用方式.html"
  - "/Swift基础知识（7）-try、try?、try!的使用方式/"
  - "/Swift基础知识（7）-try、try?、try!的使用方式.html"
  - "/2025/07/15/Swift基础知识-7-try-try-try的使用方式/"
  - "/2025/07/15/Swift基础知识-7-try-try-try的使用方式.html"
  - "/2025/07/15/swift-ji-chu-zhi-shi-7-try-try-try-de-shi-yong-fang-shi/"
  - "/2025/07/15/swift-ji-chu-zhi-shi-7-try-try-try-de-shi-yong-fang-shi.html"
  - "/swift-ji-chu-zhi-shi-7-try-try-try-de-shi-yong-fang-shi.html"
---
try 第一种使用方式 try do catch

```cpp
let data: Data = Data()

do {
    let responseJSON = try JSONSerialization.jsonObject(with: data, options: []) as! [[String: Any]]
    print(responseJSON)
} catch {
    print("something is wrong here. Try connecting to the wifi.")
}
```

try 第二种使用方式 try?

```cpp
let data: Data = Data()

let responseJSON = try? JSONSerialization.jsonObject(with: data, options: []) as? [[String: Any]]

if responseJSON != nil {
    print("Yeah, We have just unwrapped responseJSON!")
} else {
    print(responseJSON ?? "")
}
```

try 第三种使用方式 guard try?

```cpp
let data: Data = Data()

func getResponseJSON() {
    guard let responseJSON = try? (JSONSerialization.jsonObject(with: data, options: []) as! [[String: Any]]) else {
        return
    }

    print(responseJSON)
}
```

try 第四种使用方式 try!

```cpp
let data: Data = Data()

let responseJSON = try! JSONSerialization.jsonObject(with: data, options: []) as! [[String: Any]]
print(responseJSON)
```

总结

try 需要与 do...catch配合使用，这种方式可以使用更详细的错误处理方法

try? 忽略我们的错误，如果碰巧发生，会将它们设置为nil

try! 打开您的代码，并保证我们的函数永远不会遇到错误。在我们的函数确实抛出错误的情况下，我们的应用只会崩溃，这种方式用的时候一定要小心
