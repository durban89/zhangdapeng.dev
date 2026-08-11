---
title: "TypeScript基础入门之Javascript文件类型检查(三)"
date: "2025-07-10 10:56:33"
slug: "typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(三)/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(三).html"
  - "/TypeScript基础入门之Javascript文件类型检查(三)/"
  - "/TypeScript基础入门之Javascript文件类型检查(三).html"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-三/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-三.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-san/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-san.html"
  - "/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-san.html"
---
继续上篇文章【[TypeScript基础入门之Javascript文件类型检查(二)](https://www.gowhich.com/blog/960)】

### 支持JSDoc

下面的列表概述了使用JSDoc注释在JavaScript文件中提供类型信息时当前支持的构造。

请注意，尚不支持下面未明确列出的任何标记（例如[@async](https://github.com/async)）。

* [@type](https://github.com/type)
* [@param](https://github.com/param) (or [@arg](https://github.com/arg) or [@argument](https://github.com/argument))
* [@returns](https://github.com/returns) (or [@return](https://github.com/return))
* [@typedef](https://github.com/typedef)
* [@callback](https://github.com/callback)
* [@template](https://github.com/template)
* [@class](https://github.com/class) (or [@constructor](https://github.com/constructor))
* [@this](https://github.com/this)
* [@extends](https://github.com/extends) (or [@augments](https://github.com/augments))
* [@enum](https://github.com/enum)

含义通常与usejsdoc.org上给出的标记含义相同或超​​集。下面的代码描述了这些差异，并给出了每个标记的一些示例用法。

**[@type](https://github.com/type)**

您可以使用”[@type](https://github.com/type)“标记并引用类型名称（原语，在TypeScript声明中定义，或在JSDoc”[@typedef](https://github.com/typedef)“标记中）。您可以使用任何Typescript类型和大多数JSDoc类型。

```ts
/**
 * @type {string}
 */
var s;

/** @type {Window} */
var win;

/** @type {PromiseLike<string>} */
var promisedString;

// You can specify an HTML Element with DOM properties
/** @type {HTMLElement} */
var myElement = document.querySelector(selector);
element.dataset.myData = '';
```

@type可以指定联合类型 - 例如，某些东西可以是字符串或布尔值。

```ts
/**
 * @type {(string | boolean)}
 */
var sb;
```

请注意，括号对于联合类型是可选的。

```ts
/**
 * @type {string | boolean}
 */
var sb;
```

您可以使用各种语法指定数组类型：

```ts
/** @type {number[]} */
var ns;
/** @type {Array.<number>} */
var nds;
/** @type {Array<number>} */
var nas;
```

您还可以指定对象文字类型。例如，具有属性’a’（字符串）和’b’（数字）的对象使用以下语法：

```ts
/** @type {{ a: string, b: number }} */
var var9;
```

您可以使用标准JSDoc语法或Typescript语法，使用字符串和数字索引签名指定类似地图和类似数组的对象。

```ts
/**
 * A map-like object that maps arbitrary `string` properties to `number`s.
 *
 * @type {Object.<string, number>}
 */
var stringToNumber;

/** @type {Object.<number, object>} */
var arrayLike;
```

前两种类型等同于Typescript类型{ [x: string]: number }和{ [x: number]: any }。编译器理解这两种语法。

您可以使用Typescript或Closure语法指定函数类型：

```ts
/** @type {function(string, boolean): number} Closure syntax */
var sbn;
/** @type {(s: string, b: boolean) => number} Typescript syntax */
var sbn2;
```

或者您可以使用未指定的函数类型：

```ts
/** @type {Function} */
var fn7;
/** @type {function} */
var fn6;
```

Closure的其他类型也有效：

```ts
/**
 * @type {*} - can be 'any' type
 */
var star;
/**
 * @type {?} - unknown type (same as 'any')
 */
var question;
```

*类型转换*

Typescript借用了Closure的强制语法。这允许您通过在任何带括号的表达式之前添加@type标记将类型转换为其他类型。

```ts
/**
 * @type {number | string}
 */
var numberOrString = Math.random() < 0.5 ? "hello" : 100;
var typeAssertedNumber = /** @type {number} */ (numberOrString)
```

*导入类型*

您还可以使用导入类型从其他文件导入声明。此语法是特定于Typescript的，与JSDoc标准不同：

```ts
/**
 * @param p { import("./a").Pet }
 */
function walk(p) {
    console.log(`Walking ${p.name}...`);
}
```

导入类型也可以在类型别名声明中使用：

```ts
/**
 * @typedef Pet { import("./a").Pet }
 */

/**
 * @type {Pet}
 */
var myPet;
myPet.name;
```

如果你不知道类型，或者它有一个令人讨厌的大型类型，可以使用import类型从模块中获取值的类型：

```ts
/**
 * @type {typeof import("./a").x }
 */
var x = require("./a").x;
```

未完待续…
