---
title: "Swift集合类型高阶函数（三）"
date: "2025-07-15 09:51:10"
slug: "swift-ji-he-lei-xing-gao-jie-han-shu-san"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/15/Swift集合类型高阶函数（三）/"
  - "/2025/07/15/Swift集合类型高阶函数（三）.html"
  - "/Swift集合类型高阶函数（三）/"
  - "/Swift集合类型高阶函数（三）.html"
  - "/2025/07/15/Swift集合类型高阶函数-三/"
  - "/2025/07/15/Swift集合类型高阶函数-三.html"
  - "/2025/07/15/swift-ji-he-lei-xing-gao-jie-han-shu-san/"
  - "/2025/07/15/swift-ji-he-lei-xing-gao-jie-han-shu-san.html"
  - "/swift-ji-he-lei-xing-gao-jie-han-shu-san.html"
---
filter、reduce （swift 5.3）的使用

### filter

过滤，可以对数组中的元素按照某种规则进行一次过滤。

```objectivec
let numbers = [1, 3, 5, 7, 9]
let filterNumbers = numbers.filter { $0 < 5 }
print(filterNumbers)
```

输出结果如下

```bash
[1, 3]
```

### reduce

计算，可以对数组的元素进行计算

```objectivec
let animals1 = ["Dog", "Cat", "Pig"]
let string = animals1.reduce("Dog", {
    // $0: result, $1: 数组的值
    return $0 == "Cat" ? $1 : $0 + "," + $1
})
print(string)
```

输出的结果如下

```bash
Dog,Dog,Cat,Pig
```
