---
title: "TypeScript挑战（八）- 获取函数返回类型"
date: "2025-07-14 16:22:20"
slug: "typescript-tiao-zhan-ba-huo-qu-han-shu-fan-hui-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript挑战（八）-获取函数返回类型/"
  - "/2025/07/14/TypeScript挑战（八）-获取函数返回类型.html"
  - "/TypeScript挑战（八）-获取函数返回类型/"
  - "/TypeScript挑战（八）-获取函数返回类型.html"
  - "/2025/07/14/TypeScript挑战-八-获取函数返回类型/"
  - "/2025/07/14/TypeScript挑战-八-获取函数返回类型.html"
  - "/2025/07/14/typescript-tiao-zhan-ba-huo-qu-han-shu-fan-hui-lei-xing/"
  - "/2025/07/14/typescript-tiao-zhan-ba-huo-qu-han-shu-fan-hui-lei-xing.html"
  - "/typescript-tiao-zhan-ba-huo-qu-han-shu-fan-hui-lei-xing.html"
---
TypesScript Challenge 学习记录 - 获取函数返回类型

题目

---

不使用 `ReturnType` 实现 TypeScript 的 `ReturnType<T>` 范型。

例如：

```javascript
const fn = (v: boolean) => {
  if (v)
    return 1
  else
    return 2
}

type a = MyReturnType<typeof fn> // 应推导出 "1 | 2"
```

---

测试用例

---

```javascript
import { Equal, Expect } from '@type-challenges/utils'

type cases = [
  Expect<Equal<string, MyReturnType<() => string>>>,
  Expect<Equal<123, MyReturnType<() => 123>>>,
  Expect<Equal<ComplexObject, MyReturnType<() => ComplexObject>>>,
  Expect<Equal<Promise<boolean>, MyReturnType<() => Promise<boolean>>>>,
  Expect<Equal<() => 'foo', MyReturnType<() => () => 'foo'>>>,
  Expect<Equal<1 | 2, MyReturnType<typeof fn>>>,
  Expect<Equal<1 | 2, MyReturnType<typeof fn1>>>,
]

type ComplexObject = {
  a: [12, 'foo']
  bar: 'hello'
  prev(): number
}

const fn = (v: boolean) => v ? 1 : 2
const fn1 = (v: boolean, w: any) => v ? 1 : 2
```

---

答案

---

```javascript
type MyReturnType<T> = T extends (...args: []) => infer P ? P : never
```
