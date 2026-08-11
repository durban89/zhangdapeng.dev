---
title: "TypeScript挑战（九）- 实现 Omit<T, K>"
date: "2025-07-14 16:22:42"
slug: "typescript-tiao-zhan-jiu-shi-xian-omitt-k"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript挑战（九）-实现-Omit<T,-K>/"
  - "/2025/07/14/TypeScript挑战（九）-实现-Omit<T,-K>.html"
  - "/TypeScript挑战（九）-实现-Omit<T,-K>/"
  - "/TypeScript挑战（九）-实现-Omit<T,-K>.html"
  - "/2025/07/14/TypeScript挑战-九-实现-Omit-T-K/"
  - "/2025/07/14/TypeScript挑战-九-实现-Omit-T-K.html"
  - "/2025/07/14/typescript-tiao-zhan-jiu-shi-xian-omitt-k/"
  - "/2025/07/14/typescript-tiao-zhan-jiu-shi-xian-omitt-k.html"
  - "/typescript-tiao-zhan-jiu-shi-xian-omitt-k.html"
---
TypeScript Challenge - 实现 Omit<T, K>

题目

---

实现 Omit<T, K>

不使用 `Omit` 实现 TypeScript 的 `Omit<T, K>` 范型。

`Omit` 会创建一个省略 `K` 中字段的 `T` 对象。

例如：

```javascript
interface Todo {
  title: string
  description: string
  completed: boolean
}

type TodoPreview = MyOmit<Todo, 'description' | 'title'>

const todo: TodoPreview = {
  completed: false,
}
```

---

测试用例

---

```javascript
import { Equal, Expect } from '@type-challenges/utils'

type cases = [
  Expect<Equal<Expected1, MyOmit<Todo, 'description'>>>,
  Expect<Equal<Expected2, MyOmit<Todo, 'description' | 'completed'>>>
]

interface Todo {
  title: string
  description: string
  completed: boolean
}

interface Expected1 {
  title: string
  completed: boolean
}

interface Expected2 {
  title: string
}
```

---

答案

```javascript
type MyOmit<T, K> = {
  [P in Exclude<keyof T,K>]: T[P]
}
```
