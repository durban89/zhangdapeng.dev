---
title: "Swift集合类型高阶函数（二）"
date: "2025-07-15 09:51:07"
slug: "swift-ji-he-lei-xing-gao-jie-han-shu-er"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/15/Swift集合类型高阶函数（二）/"
  - "/2025/07/15/Swift集合类型高阶函数（二）.html"
  - "/Swift集合类型高阶函数（二）/"
  - "/Swift集合类型高阶函数（二）.html"
  - "/2025/07/15/Swift集合类型高阶函数-二/"
  - "/2025/07/15/Swift集合类型高阶函数-二.html"
  - "/2025/07/15/swift-ji-he-lei-xing-gao-jie-han-shu-er/"
  - "/2025/07/15/swift-ji-he-lei-xing-gao-jie-han-shu-er.html"
  - "/swift-ji-he-lei-xing-gao-jie-han-shu-er.html"
---
flatMap/compactMap （swift 5.3）的使用

### - 不返回nil

flatMap/compactMap处理返回后的数组不存在nil，同时它会把Optional解包

看下map和flatMap/compactMap实现方式如下

```objectivec
let colors = ["red", "yellow", "green", ""]
let colorsOfMap = colors.map { item -> Int? in
    let length = item.count
    guard length > 0 else {
        return nil
    }

    return length
}

print(colorsOfMap)
```

结果是

```bash
[Optional(3), Optional(6), Optional(5), nil]
```

flatMap/compactMap实现方式如下

- flatMap

```objectivec
let colorsOfFlatMap = colors.flatMap { item ->Int? in
    let length = item.count
    guard length > 0 else {
        return nil
    }

    return length
}

print(colorsOfFlatMap)
```

- compactMap

```objectivec
let colorsOfFlatMap = colors.compactMap { item ->Int? in
    let length = item.count
    guard length > 0 else {
        return nil
    }

    return length
}

print(colorsOfFlatMap)
```

这里之所以用compactMap，是因为`'flatMap' is deprecated Please use compactMap(_:)`

结果是

```bash
[3, 6, 5]
```

### - 打开数组

compactMap能把（二维、N维）数组一同打开变成一个新的数组

```objectivec
let array = [[1,2,3],[4,5,6],[7,8,9]]

// 对比
let arr1 = array.map { $0 }
print(arr1)

let arr2 = array.flatMap { $0 }
print(arr2)
```

结果分别是

```bash
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### - 合并数组

compactMap能把不同的数组合并为一个数组，合并后的数组的个数是要合并两个数组个数的乘积

```objectivec
let animals = ["cat", "dog", "pig"]
let counts = [1,2,3]

let newArray = counts.flatMap { count in
    animals.map({ animal in
        return animal + "\(count)"
    })
}

print(newArray)
```

结果是

```bash
["cat1", "dog1", "pig1", "cat2", "dog2", "pig2", "cat3", "dog3", "pig3"]
```
