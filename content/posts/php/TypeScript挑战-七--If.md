---
title: "TypeScript挑战（七） - If"
date: "2025-07-14 16:21:53"
slug: "typescript-tiao-zhan-qi-if"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript挑战（七）-If/"
  - "/2025/07/14/TypeScript挑战（七）-If.html"
  - "/TypeScript挑战（七）-If/"
  - "/TypeScript挑战（七）-If.html"
  - "/2025/07/14/TypeScript挑战-七-If/"
  - "/2025/07/14/TypeScript挑战-七-If.html"
  - "/2025/07/14/typescript-tiao-zhan-qi-if/"
  - "/2025/07/14/typescript-tiao-zhan-qi-if.html"
  - "/typescript-tiao-zhan-qi-if.html"
---
学习记录 - If

题目

---

实现一个utils If，它接受条件C，True返回类型T，以及False返回类型F。 C可以是True或False，而T和F可以是任何类型。

比如

```javascript
type A = If<true, 'a', 'b'>  // expected to be 'a'
type B = If<false, 'a', 'b'> // expected to be 'b'
```

---

测试用例

---

```javascript
import { Equal, Expect } from '@type-challenges/utils'

type cases = [
  Expect<Equal<If<true, 'a', 'b'>, 'a'>>,
  Expect<Equal<If<false, 'a', 2>, 2>>,
]

// @ts-expect-error
type error = If<null, 'a', 'b'>
```

---

答案

---

```javascript
type If<C, T, F> = C extends true ? T : F
```
