---
title: "TypeScript 挑战（一）- 实现Pick<T, K>"
date: "2025-07-14 14:53:28"
slug: "typescript-tiao-zhan-yi-shi-xian-pickt-k"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript-挑战（一）-实现Pick<T,-K>/"
  - "/2025/07/14/TypeScript-挑战（一）-实现Pick<T,-K>.html"
  - "/TypeScript-挑战（一）-实现Pick<T,-K>/"
  - "/TypeScript-挑战（一）-实现Pick<T,-K>.html"
  - "/2025/07/14/TypeScript-挑战-一-实现Pick-T-K/"
  - "/2025/07/14/TypeScript-挑战-一-实现Pick-T-K.html"
  - "/2025/07/14/typescript-tiao-zhan-yi-shi-xian-pickt-k/"
  - "/2025/07/14/typescript-tiao-zhan-yi-shi-xian-pickt-k.html"
  - "/typescript-tiao-zhan-yi-shi-xian-pickt-k.html"
---
记录下学习过程

题目是这样的

---

无需使用内置的`Pick<T, K>`泛型即可。

通过从``K``中选择属性``T``来构造类型

例如

```javascript
interface Todo {
  title: string
  description: string
  completed: boolean
}

type TodoPreview = MyPick<Todo, 'title' | 'completed'>

const todo: TodoPreview = {
    title: 'Clean room',
    completed: false,
}
```

---

继续之前推荐大家去typescript官网的playground，因为里面提供了自动语法检测的功能

比如上面的题目，可以去[这里](https://tsch.js.org/4/play/zh-CN)，点击这里打开就能跳转过去

默认情况下，测试用例如下

```javascript
/* _____________ 测试用例 _____________ */
import { Equal, Expect } from '@type-challenges/utils'

type cases = [
  Expect<Equal<Expected1, MyPick<Todo, 'title'>>>,
  Expect<Equal<Expected2, MyPick<Todo, 'title' | 'completed'>>>,
  // @ts-expect-error
  MyPick<Todo, 'title' | 'completed' | 'invalid'>,
]

interface Todo {
  title: string
  description: string
  completed: boolean
}

interface Expected1 {
  title: string
}

interface Expected2 {
  title: string
  completed: boolean
}
```

然后需要我们完成的代码如下

```javascript
/* _____________ 你的代码 _____________ */

type MyPick<T, K> = any
```

只要完成“你的代码部分”，测试用例部分的错误提示就会消失

答案我公布下，参考别人的

这个值得仔细斟酌下，我感觉我都看不懂了

```javascript
type MyPick<T, K extends number | string | symbol> = { [k in K]: k extends keyof T ? T[k] : never}
```
