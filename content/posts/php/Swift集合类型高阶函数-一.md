---
title: "Swift集合类型高阶函数（一）"
date: "2025-07-15 09:51:03"
slug: "swift-ji-he-lei-xing-gao-jie-han-shu-yi"
categories: ["技术"]
tags: ["Swift"]
aliases:
  - "/2025/07/15/Swift集合类型高阶函数（一）/"
  - "/2025/07/15/Swift集合类型高阶函数（一）.html"
  - "/Swift集合类型高阶函数（一）/"
  - "/Swift集合类型高阶函数（一）.html"
  - "/2025/07/15/Swift集合类型高阶函数-一/"
  - "/2025/07/15/Swift集合类型高阶函数-一.html"
  - "/2025/07/15/swift-ji-he-lei-xing-gao-jie-han-shu-yi/"
  - "/2025/07/15/swift-ji-he-lei-xing-gao-jie-han-shu-yi.html"
  - "/swift-ji-he-lei-xing-gao-jie-han-shu-yi.html"
---
Map（swift 5.3）的使用

对集合类型中的每一个元素做一次处理，转换为新数组

### 数组系列

- 案例1 - 遍历每个元素

```objectivec
let colors = ["red", "yellow", "green", "blue"]
let counts = colors.map { (color: String) -> Int in
    return color.count
}

print(counts)
```

结果是 [3,6,5,4]

- 案例2 - 更加简单的方法

```objectivec
let counts1 = colors.map { $0.count }
print(counts1)
```

结果也是 [3,6,5,4]

- 案例3 - 转换为对象数组（请问下转换为对象数组干啥用）

```objectivec
class Color {
    var name: String
    init(name: String) {
        self.name = name
    }
}

let colorsObj = colors.map { return Color(name: $0) }

for obj in colorsObj {
    print(obj.name)
}
```

结果是

```bash
red
yellow
green
blue
```

### 集合系列

```objectivec
let ColorsSet: Set = ["red", "yellow", "green", "blue"]
let colorsCount = ColorsSet.map { $0.count }
print(colorsCount)
```

结果是**[3, 6, 4, 5]**

### 字典系列

```objectivec
let dict = [2: "red", 4: "yellow", 6: "green", 8: "blue"]
let keys = dict.map { $0.key }
print(keys)
let values = dict.map { $0.value }
print(values)
```

结果分别是

**[2, 8, 6, 4]**

**["red", "blue", "green", "yellow"]**
