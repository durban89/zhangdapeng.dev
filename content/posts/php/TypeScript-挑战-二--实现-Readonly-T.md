---
title: "TypeScript 挑战（二）- 实现 Readonly<T>"
date: "2025-07-14 14:53:43"
slug: "typescript-tiao-zhan-er-shi-xian-readonlyt"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript-挑战（二）-实现-Readonly<T>/"
  - "/2025/07/14/TypeScript-挑战（二）-实现-Readonly<T>.html"
  - "/TypeScript-挑战（二）-实现-Readonly<T>/"
  - "/TypeScript-挑战（二）-实现-Readonly<T>.html"
  - "/2025/07/14/TypeScript-挑战-二-实现-Readonly-T/"
  - "/2025/07/14/TypeScript-挑战-二-实现-Readonly-T.html"
  - "/2025/07/14/typescript-tiao-zhan-er-shi-xian-readonlyt/"
  - "/2025/07/14/typescript-tiao-zhan-er-shi-xian-readonlyt.html"
  - "/typescript-tiao-zhan-er-shi-xian-readonlyt.html"
---
实现 Readonly<T>，学习记录

题目简介

---

无需使用内置的`Readonly<T>`泛型即可。

构造一个类型，并将T的所有属性设置为只读，这意味着无法重新分配所构造类型的属性。

例如

```javascript
interface Todo {
  title: string
  description: string
}

const todo: MyReadonly<Todo> = {
  title: "Hey",
  description: "foobar"
}

todo.title = "Hello" // Error: cannot reassign a readonly property
todo.description = "barFoo" // Error: cannot reassign a readonly property
```

测试用例如下

```javascript
import { Equal, Expect } from '@type-challenges/utils'

type cases = [
  Expect<Equal<MyReadonly<Todo1>, Readonly<Todo1>>>,
]

interface Todo1 {
  title: string
  description: string
  completed: boolean
}
```

答案如下

```javascript
type MyReadonly<T> = { readonly [K in keyof T]: T[K] }
```
