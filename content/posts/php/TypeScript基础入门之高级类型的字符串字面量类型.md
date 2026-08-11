---
title: "TypeScript基础入门之高级类型的字符串字面量类型"
date: "2025-07-09 10:42:30"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-zi-fu-chuan-zi-mian-liang-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的字符串字面量类型/"
  - "/2025/07/09/TypeScript基础入门之高级类型的字符串字面量类型.html"
  - "/TypeScript基础入门之高级类型的字符串字面量类型/"
  - "/TypeScript基础入门之高级类型的字符串字面量类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-zi-fu-chuan-zi-mian-liang-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-zi-fu-chuan-zi-mian-liang-lei-xing.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-zi-fu-chuan-zi-mian-liang-lei-xing.html"
---
## 高级类型

### 字符串字面量类型

字符串字面量类型允许你指定字符串必须的固定值。 在实际应用中，字符串字面量类型可以与联合类型，类型保护和类型别名很好的配合。 通过结合使用这些特性，你可以实现类似枚举类型的字符串。

```ts
type Easing = "ease-in" | "ease-out" | "ease-in-out";
class UIElement {
    animate(dx: number, dy: number, easing: Easing) {
        if (easing === "ease-in") {
            // ...
        }
        else if (easing === "ease-out") {
        }
        else if (easing === "ease-in-out") {
        }
        else {
            // error! should not pass null or undefined.
        }
    }
}

let button = new UIElement();
button.animate(0, 0, "ease-in");
button.animate(0, 0, "uneasy"); // error: "uneasy" is not allowed here
```

你只能从三种允许的字符中选择其一来做为参数传递，传入其它值则会产生错误。

```bash
Argument of type '"uneasy"' is not assignable to parameter of type '"ease-in" | "ease-out" | "ease-in-out"'
```

字符串字面量类型还可以用于区分函数重载：

```ts
function createElement(tagName: "img"): HTMLImageElement;
function createElement(tagName: "input"): HTMLInputElement;
// ... more overloads ...
function createElement(tagName: string): Element {
    // ... code goes here ...
}
```

### 数字字面量类型

TypeScript还具有数字字面量类型。

```ts
function rollDie(): 1 | 2 | 3 | 4 | 5 | 6 {
    // ...
}
```

我们很少直接这样使用，但它们可以用在缩小范围调试bug的时候：

```ts
function foo(x: number) {
    if (x !== 1 || x !== 2) {
        //         ~~~~~~~
        // Operator '!==' cannot be applied to types '1' and '2'.
    }
}
```

换句话说，当x与2进行比较的时候，它的值必须为1，这就意味着上面的比较检查是非法的。

### 枚举成员类型

如我们在 枚举一节里提到的，当每个枚举成员都是用字面量初始化的时候枚举成员是具有类型的。

在我们谈及“单例类型”的时候，多数是指枚举成员类型和数字/字符串字面量类型，尽管大多数用户会互换使用“单例类型”和“字面量类型”。
