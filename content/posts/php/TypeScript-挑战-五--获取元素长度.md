---
title: "TypeScript 挑战（五）- 获取元素长度"
date: "2025-07-14 16:21:45"
slug: "typescript-tiao-zhan-wu-huo-qu-yuan-su-chang-du"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/14/TypeScript-挑战（五）-获取元素长度/"
  - "/2025/07/14/TypeScript-挑战（五）-获取元素长度.html"
  - "/TypeScript-挑战（五）-获取元素长度/"
  - "/TypeScript-挑战（五）-获取元素长度.html"
  - "/2025/07/14/TypeScript-挑战-五-获取元素长度/"
  - "/2025/07/14/TypeScript-挑战-五-获取元素长度.html"
  - "/2025/07/14/typescript-tiao-zhan-wu-huo-qu-yuan-su-chang-du/"
  - "/2025/07/14/typescript-tiao-zhan-wu-huo-qu-yuan-su-chang-du.html"
  - "/typescript-tiao-zhan-wu-huo-qu-yuan-su-chang-du.html"
---
学习记录 - 获取元素长度 - 对于给定的元组，您需要创建一个通用的Length，选择元组的长度

题目简介

---

对于给定的元组，您需要创建一个通用的`Length`，选择元组的长度

例如

```javascript
type tesla = ['tesla', 'model 3', 'model X', 'model Y']
type spaceX = ['FALCON 9', 'FALCON HEAVY', 'DRAGON', 'STARSHIP', 'HUMAN SPACEFLIGHT']

type teslaLength = Length<tesla>  // expected 4
type spaceXLength = Length<spaceX> // expected 5
```

---

测试用例

---

```javascript
import { Equal, Expect } from '@type-challenges/utils'

const tesla = ['tesla', 'model 3', 'model X', 'model Y'] as const
const spaceX = ['FALCON 9', 'FALCON HEAVY', 'DRAGON', 'STARSHIP', 'HUMAN SPACEFLIGHT'] as const

type cases = [
  Expect<Equal<Length<typeof tesla>, 4>>,
  Expect<Equal<Length<typeof spaceX>, 5>>,
]
```

---

答案

---

```javascript
type Length<T extends any> = T extends ArrayLike<any> ? T["length"] : never
```
