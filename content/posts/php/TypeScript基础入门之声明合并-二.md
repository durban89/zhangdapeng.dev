---
title: "TypeScript基础入门之声明合并(二)"
date: "2025-07-10 10:23:46"
slug: "typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之声明合并(二)/"
  - "/2025/07/10/TypeScript基础入门之声明合并(二).html"
  - "/TypeScript基础入门之声明合并(二)/"
  - "/TypeScript基础入门之声明合并(二).html"
  - "/2025/07/10/TypeScript基础入门之声明合并-二/"
  - "/2025/07/10/TypeScript基础入门之声明合并-二.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-er/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-er.html"
  - "/typescript-ji-chu-ru-men-zhi-sheng-ming-he-bing-er.html"
---
## 声明合并

### 合并命名空间

与接口类似，同名的命名空间也将合并其成员。  
由于名称空间同时创建了名称空间和值，因此我们需要了解它们是如何合并的。

要合并命名空间，每个命名空间中声明的导出接口的类型定义本身已合并，形成一个内部具有合并接口定义的命名空间。

要合并命名空间值，在每个声明站点，如果已存在具有给定名称的命名空间，则通过获取现有命名空间并将第二个命名空间的导出成员添加到第一个命名空间来进一步扩展它。

在此示例中，Animals的声明合并：

```ts
namespace Animals {
    export class Zebra { }
}

namespace Animals {
    export interface Legged { numberOfLegs: number; }
    export class Dog { }
}
```

相当于：

```ts
namespace Animals {
    export interface Legged { numberOfLegs: number; }

    export class Zebra { }
    export class Dog { }
}
```

这种命名空间合并模型是一个有用的起点，但我们还需要了解非导出成员会发生什么。  
非导出成员仅在原始（未合并）命名空间中可见。  
这意味着在合并之后，来自其他声明的合并成员无法看到未导出的成员。

在这个例子中我们可以更清楚地看到这一点：

```ts
namespace Animal {
    let haveMuscles = true;

    export function animalsHaveMuscles() {
        return haveMuscles;
    }
}

namespace Animal {
    export function doAnimalsHaveMuscles() {
        return haveMuscles;  // Error, because haveMuscles is not accessible here
    }
}
```

由于未导出hasMuscles，因此只有共享相同未合并命名空间的animalsHaveMuscles函数才能看到该符号。  
doAnimalsHaveMuscles函数，即使它是合并的Animal命名空间的一部分，也无法看到此未导出的成员。

未完待续...
