---
title: "TypeScript基础入门之Javascript文件类型检查(五)"
date: "2025-07-10 10:56:40"
slug: "typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-wu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(五)/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(五).html"
  - "/TypeScript基础入门之Javascript文件类型检查(五)/"
  - "/TypeScript基础入门之Javascript文件类型检查(五).html"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-五/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-五.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-wu/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-wu.html"
  - "/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-wu.html"
---
继续上篇文章【[TypeScript基础入门之Javascript文件类型检查(四)](https://www.gowhich.com/blog/962)】

**@constructor**

编译器根据此属性赋值推断构造函数，但如果添加@constructor标记，则可以更好地检查更严格和更好的建议：

```ts
/**
 * @constructor
 * @param {number} data
 */
function C(data) {
  this.size = 0;
  this.initialize(data); // Should error, initializer expects a string
}
/**
 * @param {string} s
 */
C.prototype.initialize = function (s) {
  this.size = s.length
}

var c = new C(0);
var result = C(1); // C should only be called with new
```

使用@constructor，在构造函数C中检查它，因此您将获得初始化方法的建议，如果您传递一个数字，则会出错。 如果您调用C而不是构造它，您也会收到错误。

不幸的是，这意味着也可以调用的构造函数不能使用@constructor。

**@this**

当编译器有一些上下文可以使用时，它通常可以找出它的类型。 如果没有，您可以使用@this显式指定此类型：

```ts
/**
 * @this {HTMLElement}
 * @param {*} e
 */
function callbackForLater(e) {
    this.clientHeight = parseInt(e) // should be fine!
}
```

**@extends**

当Javascript类扩展通用基类时，无处可指定类型参数应该是什么。 @extends标记为该类型参数提供了一个位置：

```ts
/**
 * @template T
 * @extends {Set<T>}
 */
class SortableSet extends Set {
  // ...
}
```

请注意，@ extends仅适用于类。 目前，构造函数没有办法扩展一个类。

**@enum**

@enum标记允许您创建一个对象文字，其成员都是指定的类型。 与Javascript中的大多数对象文字不同，它不允许其他成员。

```ts
/** @enum {number} */
const JSDocState = {
  BeginningOfLine: 0,
  SawAsterisk: 1,
  SavingComments: 2,
}
```

请注意，@enum与Typescript的枚举完全不同，并且简单得多。 但是，与Typescript的枚举不同，@enum可以有任何类型：

```ts
/** @enum {function(number): number} */
const Math = {
  add1: n => n + 1,
  id: n => -n,
  sub1: n => n - 1,
}
```

更多示例

```ts
var someObj = {
  /**
   * @param {string} param1 - Docs on property assignments work
   */
  x: function(param1){}
};

/**
 * As do docs on variable assignments
 * @return {Window}
 */
let someFunc = function(){};

/**
 * And class methods
 * @param {string} greeting The greeting to use
 */
Foo.prototype.sayHi = (greeting) => console.log("Hi!");

/**
 * And arrow functions expressions
 * @param {number} x - A multiplier
 */
let myArrow = x => x * x;

/**
 * Which means it works for stateless function components in JSX too
 * @param {{a: string, b: number}} test - Some param
 */
var sfc = (test) => <div>{test.a.charAt(0)}</div>;

/**
 * A parameter can be a class constructor, using Closure syntax.
 *
 * @param {{new(...args: any[]): object}} C - The class to register
 */
function registerClass(C) {}

/**
 * @param {...string} p1 - A 'rest' arg (array) of strings. (treated as 'any')
 */
function fn10(p1){}

/**
 * @param {...string} p1 - A 'rest' arg (array) of strings. (treated as 'any')
 */
function fn9(p1) {
  return p1.join();
}
```

### 已知的模式不受支持

引用值空间中的对象，因为类型不起作用，除非对象也创建类型，如构造函数。

```ts
function aNormalFunction() {

}
/**
 * @type {aNormalFunction}
 */
var wrong;
/**
 * Use 'typeof' instead:
 * @type {typeof aNormalFunction}
 */
var right;
```

对象文字类型中的属性类型的Postfix等于未指定可选属性：

```ts
/**
 * @type {{ a: string, b: number= }}
 */
var wrong;
/**
 * Use postfix question on the property name instead:
 * @type {{ a: string, b?: number }}
 */
var right;
```

如果启用了strictNullChecks，则可空类型仅具有意义：

```ts
/**
 * @type {?number}
 * With strictNullChecks: true -- number | null
 * With strictNullChecks: off  -- number
 */
var nullable;
```

非可空类型没有任何意义，并且被视为原始类型：

```ts
/**
 * @type {!number}
 * Just has type number
 */
var normal;
```

与JSDoc的类型系统不同，Typescript只允许您将类型标记为包含null或不包含null。 没有明确的非可空性 - 如果启用了strictNullChecks，则number不可为空。 如果它关闭，则number可以为空。
