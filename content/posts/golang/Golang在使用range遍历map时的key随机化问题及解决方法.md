---
title: "Golang在使用range遍历map时的key随机化问题及解决方法"
date: "2025-08-01 11:35:11"
slug: "golang-zai-shi-yong-range-bian-li-map-shi-de-key-sui-ji-hua-wen-ti-ji-jie-jue-fang-fa"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/01/Golang在使用range遍历map时的key随机化问题及解决方法/"
  - "/2025/08/01/Golang在使用range遍历map时的key随机化问题及解决方法.html"
  - "/Golang在使用range遍历map时的key随机化问题及解决方法/"
  - "/Golang在使用range遍历map时的key随机化问题及解决方法.html"
  - "/2025/08/01/golang-zai-shi-yong-range-bian-li-map-shi-de-key-sui-ji-hua-wen-ti-ji-jie-jue-fang-fa/"
  - "/2025/08/01/golang-zai-shi-yong-range-bian-li-map-shi-de-key-sui-ji-hua-wen-ti-ji-jie-jue-fang-.html"
  - "/golang-zai-shi-yong-range-bian-li-map-shi-de-key-sui-ji-hua-wen-ti-ji-jie-jue-fang-fa.html"
---
Golang在使用range遍历map时的key随机化问题及解决方法

说到这个问题还真是奇葩，也有很多人遇到了

> https://blog.csdn.net/slvher/article/details/44779081

比如下面这个哥们就遇到了，也提出了很好的解决意见，因为最近我在用Golang搭建自己的博客，在数据库查询的时候，也遇到了，只是偶尔会遇到这个问题，结果改完也彻底结局了头痛多天的思路

思路其实很简单

### 第一步建立一个存储key的数组

```go
sortedKeys := make([]string, 0)
```

### 第二步将键值存入数组，并对数组进行排序

```go
s := map[string]string{
    "k1": "v1",
    "k2": "v2",
    "k3": "v3",
}

for k := range s {
    sortedKeys = append(sortedKeys, k)
}
sort.Strings(sortedKeys)
```

### 第三步通过数组循环来遍历map

```go
value := []string{}
for _, k := range sortedKeys {
    // key - k
    // value - s[k]
    fmt.Printf("%s = %s \n", k, s[k])
    value = append(value, s[k])
}
```
