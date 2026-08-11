---
title: "TypeScript 挑战（三）- 实现元组转换为对象"
date: "2025-07-14 14:54:31"
slug: "typescript-tiao-zhan-san-shi-xian-yuan-zu-zhuan-huan-wei-dui-xiang"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript-挑战（三）-实现元组转换为对象/"
  - "/2025/07/14/TypeScript-挑战（三）-实现元组转换为对象.html"
  - "/TypeScript-挑战（三）-实现元组转换为对象/"
  - "/TypeScript-挑战（三）-实现元组转换为对象.html"
  - "/2025/07/14/TypeScript-挑战-三-实现元组转换为对象/"
  - "/2025/07/14/TypeScript-挑战-三-实现元组转换为对象.html"
  - "/2025/07/14/typescript-tiao-zhan-san-shi-xian-yuan-zu-zhuan-huan-wei-dui-xiang/"
  - "/2025/07/14/typescript-tiao-zhan-san-shi-xian-yuan-zu-zhuan-huan-wei-dui-xiang.html"
  - "/typescript-tiao-zhan-san-shi-xian-yuan-zu-zhuan-huan-wei-dui-xiang.html"
---
实现元组转换为对象，学习记录

题目简介

---

给定数组，转换为对象类型，键/值必须在给定数组中。

例如

```javascript
const tuple = ['tesla', 'model 3', 'model X', 'model Y'] as const

const result: TupleToObject<typeof tuple> // expected { tesla: 'tesla', 'model 3': 'model 3', 'model X': 'model X', 'model Y': 'model Y'}
```

测试用例

---

```javascript
import { Equal, Expect } from '@type-challenges/utils'

const tuple = ['tesla', 'model 3', 'model X', 'model Y'] as const

type cases = [
  Expect<Equal<TupleToObject<typeof tuple>, { tesla: 'tesla'; 'model 3': 'model 3'; 'model X': 'model X'; 'model Y': 'model Y'}>>,
]
```

答案

---

```javascript
type TupleToObject<T extends readonly any[]> = {
  [k in T[number]]: k
}
```

看完这个答案我是蒙蔽状态
