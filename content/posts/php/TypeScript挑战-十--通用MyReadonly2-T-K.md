---
title: "TypeScript挑战（十）- 通用MyReadonly2<T, K>"
date: "2025-07-14 16:28:08"
slug: "typescript-tiao-zhan-shi-tong-yong-myreadonly2t-k"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript挑战（十）-通用MyReadonly2<T,-K>/"
  - "/2025/07/14/TypeScript挑战（十）-通用MyReadonly2<T,-K>.html"
  - "/TypeScript挑战（十）-通用MyReadonly2<T,-K>/"
  - "/TypeScript挑战（十）-通用MyReadonly2<T,-K>.html"
  - "/2025/07/14/TypeScript挑战-十-通用MyReadonly2-T-K/"
  - "/2025/07/14/TypeScript挑战-十-通用MyReadonly2-T-K.html"
  - "/2025/07/14/typescript-tiao-zhan-shi-tong-yong-myreadonly2t-k/"
  - "/2025/07/14/typescript-tiao-zhan-shi-tong-yong-myreadonly2t-k.html"
  - "/typescript-tiao-zhan-shi-tong-yong-myreadonly2t-k.html"
---
TypeScript Challenge - 实现一个通用MyReadonly2<T, K>，它带有两种类型的参数T和K

题目

---

实现一个通用`MyReadonly2<T, K>`，它带有两种类型的参数`T`和`K`。

`K`指定应设置为Readonly的属性集（如果`T`）。如果未提供`K`，则应使所有属性都变为只读，就像普通的`Readonly<T>`一样。

例如

```javascript
interface Todo {
  title: string
  description: string
  completed: boolean
}

const todo: MyReadonly2<Todo, 'title' | 'description'> = {
  title: "Hey",
  description: "foobar",
  completed: false,
}

todo.title = "Hello" // Error: cannot reassign a readonly property
todo.description = "barFoo" // Error: cannot reassign a readonly property
todo.completed = true // OK
```

---

测试用例

---

```javascript
import { Alike, Expect } from '@type-challenges/utils'

type cases = [
  Expect<Alike<MyReadonly2<Todo1>, Readonly<Todo1>>>,
  Expect<Alike<MyReadonly2<Todo1, 'title' | 'description'>, Expected>>,
]

interface Todo1 {
  title: string
  description?: string
  completed: boolean
}

interface Expected {
  readonly title: string
  readonly description?: string
  completed: boolean
}
```

---

答案

---

```javascript
type MyReadonly2<T, K extends keyof T = keyof T> = {
  readonly [P in K]: T[P]
} & {
  [P in keyof T]: T[P]
}
```

蒙圈了
