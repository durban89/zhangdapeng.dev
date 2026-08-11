---
title: "TypeScript基础入门之Javascript文件类型检查(二)"
date: "2025-07-10 10:56:26"
slug: "typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(二)/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(二).html"
  - "/TypeScript基础入门之Javascript文件类型检查(二)/"
  - "/TypeScript基础入门之Javascript文件类型检查(二).html"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-二/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-二.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-er/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-er.html"
  - "/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-er.html"
---
继续上篇文章【[TypeScript基础入门之Javascript文件类型检查(一)](https://www.gowhich.com/blog/959)】

**对象文字是开放式的**

在.ts文件中，初始化变量声明的对象文字将其类型赋予声明。不能添加未在原始文本中指定的新成员。此规则在.js文件中放宽;对象文字具有开放式类型（索引签名），允许添加和查找最初未定义的属性。例如：

```ts
var obj = { a: 1 };
obj.b = 2;  // Allowed
```

对象文字的行为就像它们具有索引签名[x：string]：任何允许它们被视为开放映射而不是封闭对象的任何东西。

与其他特殊的JS检查行为一样，可以通过为变量指定JSDoc类型来更改此行为。例如：

```ts
/** @type {{a: number}} */
var obj = { a: 1 };
obj.b = 2;  // Error, type {a: number} does not have property b
```

null，undefined和empty数组初始值设定项的类型为any或any[]

使用null或undefined初始化的任何变量，参数或属性都将具有类型any，即使打开了严格的空检查。使用[]初始化的任何变量，参数或属性都将具有类型any[]，即使打开了严格的空检查。唯一的例外是具有如上所述的多个初始值设定项的属性。

```ts
function Foo(i = null) {
    if (!i) i = 1;
    var j = undefined;
    j = 2;
    this.l = [];
}
var foo = new Foo();
foo.l.push(foo.i);
foo.l.push("end");
```

**功能参数默认是可选的**

由于无法在ES2015之前的Javascript中指定参数的可选性，因此.js文件中的所有函数参数都被视为可选参数。允许使用参数少于声明的参数数量的调用。

重要的是要注意，调用具有太多参数的函数是错误的。

例如：

```ts
function bar(a, b) {
    console.log(a + " " + b);
}

bar(1);       // OK, second argument considered optional
bar(1, 2);
bar(1, 2, 3); // Error, too many arguments
```

JSDoc注释函数被排除在此规则之外。使用JSDoc可选参数语法来表示可选性。例如：

```ts
/**
 * @param {string} [somebody] - Somebody's name.
 */
function sayHello(somebody) {
    if (!somebody) {
        somebody = 'John Doe';
    }
    console.log('Hello ' + somebody);
}

sayHello();
```

**由arguments推断出的var-args参数声明**

其主体具有对参数引用的引用的函数被隐式地认为具有var-arg参数(即（...arg: any[]) => any)。使用JSDoc var-arg语法指定参数的类型。

```ts
/** @param {...number} args */
function sum(/* numbers */) {
    var total = 0
    for (var i = 0; i < arguments.length; i++) {
      total += arguments[i]
    }
    return total
}
```

**未指定的类型参数默认为any**

由于在Javascript中没有用于指定泛型类型参数的自然语法，因此未指定的类型参数默认为any。

*在extends子句中：*

例如，React.Component被定义为具有两个类型参数，Props和State。在.js文件中，没有合法的方法在extends子句中指定它们。默认情况下，类型参数将是any：

```ts
import { Component } from "react";

class MyComponent extends Component {
    render() {
        this.props.b; // Allowed, since this.props is of type any
    }
}
```

使用JSDoc @augments明确指定类型。例如：

```ts
import { Component } from "react";

/**
 * @augments {Component<{a: number}, State>}
 */
class MyComponent extends Component {
    render() {
        this.props.b; // Error: b does not exist on {a:number}
    }
}
```

*在JSDoc引用中*

JSDoc中的未指定类型参数默认为any：

```ts
/** @type{Array} */
var x = [];

x.push(1);        // OK
x.push("string"); // OK, x is of type Array<any>

/** @type{Array.<number>} */
var y = [];

y.push(1);        // OK
y.push("string"); // Error, string is not assignable to number
```

*在函数调用中*

对泛型函数的调用使用参数来推断类型参数。有时这个过程无法推断任何类型，主要是因为缺乏推理源;在这些情况下，类型参数将默认为any。例如：

```ts
var p = new Promise((resolve, reject) => { reject() });

p; // Promise<any>;
```

未完待续...
