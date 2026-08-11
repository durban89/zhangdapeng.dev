---
title: "如何创建高质量的TypeScript声明文件(七) - 该做什么和不该做什么"
date: "2025-07-10 10:57:09"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-qi-gai-zuo-shen-me-he-bu-gai-zuo-shen-me"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(七)-该做什么和不该做什么/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(七)-该做什么和不该做什么.html"
  - "/如何创建高质量的TypeScript声明文件(七)-该做什么和不该做什么/"
  - "/如何创建高质量的TypeScript声明文件(七)-该做什么和不该做什么.html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-七-该做什么和不该做什么/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-七-该做什么和不该做什么.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-qi-gai-zuo-shen-me-he/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-qi-gai-zuo-shen-m.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-qi-gai-zuo-shen-me-he-bu-gai.html"
---
### 该做什么和不该做什么

一般类型

**数字，字符串，布尔值和对象**

不要使用Number，String，Boolean或Object类型。 这些类型指的是在JavaScript代码中几乎从不正确使用的非原始盒装对象。

```ts
/* WRONG */
function reverse(s: String): String;
```

请使用类型number，string和boolean。

```ts
/* OK */
function reverse(s: string): string;
```

而不是Object，使用非基本对象类型（在TypeScript 2.2中添加）。

**泛型**

不要使用不使用其类型参数的泛型类型。在TypeScript FAQ页面中查看更多详细信息。

### 回调类型

**返回回调类型**

不要将返回类型any用于其值将被忽略的回调：

```ts
/* WRONG */
function fn(x: () => any) {
    x();
}
```

对于其值将被忽略的回调，请使用返回类型void：

```ts
/* OK */
function fn(x: () => void) {
    x();
}
```

原因：使用void更安全，因为它可以防止您以未经检查的方式意外使用x的返回值：

```ts
function fn(x: () => void) {
    var k = x(); // oops! meant to do something else
    k.doSomething(); // error, but would be OK if the return type had been 'any'
}
```

**回调中的可选参数**

除非你真的是这样说，否则不要在回调中使用可选参数：

```ts
/* WRONG */
interface Fetcher {
    getObject(done: (data: any, elapsedTime?: number) => void): void;
}
```

这具有非常具体的含义：完成的回调可以使用1个参数调用，也可以使用2个参数调用。作者可能打算说回调可能不关心elapsedTime参数，但是没有必要使参数可选来完成这一点 - 提供一个接受较少参数的回调总是合法的。

写回调参数是非可选的：

```ts
/* OK */
interface Fetcher {
    getObject(done: (data: any, elapsedTime: number) => void): void;
}
```

**重载和回调**

不要编写仅在回调函数参数上不同的单独重载：

```ts
/* WRONG */
declare function beforeAll(action: () => void, timeout?: number): void;
declare function beforeAll(action: (done: DoneFn) => void, timeout?: number): void;
```

应该只使用最大参数个数写一个重载：

```ts
/* OK */
declare function beforeAll(action: (done: DoneFn) => void, timeout?: number): void;
```

原因：忽略参数的回调总是合法的，因此不需要更短的过载。首先提供较短的回调允许传入错误输入的函数，因为它们匹配第一个重载。

### 函数重载

**顺序**

不要在更具体的重载之前放置更多的一般重载：

```ts
/* WRONG */
declare function fn(x: any): any;
declare function fn(x: HTMLElement): number;
declare function fn(x: HTMLDivElement): string;

var myElem: HTMLDivElement;
var x = fn(myElem); // x: any, wat?
```

通过在更具体的签名之后放置更一般的签名来对重载进行排序：

```ts
/* OK */
declare function fn(x: HTMLDivElement): string;
declare function fn(x: HTMLElement): number;
declare function fn(x: any): any;

var myElem: HTMLDivElement;
var x = fn(myElem); // x: string, :)
```

原因：TypeScript在解析函数调用时选择第一个匹配的重载。当较早的重载比较晚的重载“更一般”时，后一个重载是有效隐藏的，不能被调用。

**使用可选参数**

不要写几个仅在尾随参数上有所不同的重载：

```ts
/* WRONG */
interface Example {
    diff(one: string): number;
    diff(one: string, two: string): number;
    diff(one: string, two: string, three: boolean): number;
}
```

尽可能使用可选参数：

```ts
/* OK */
interface Example {
    diff(one: string, two?: string, three?: boolean): number;
}
```

请注意，只有当所有重载具有相同的返回类型时，才会发生此折叠。

原因：这有两个重要原因。

TypeScript通过查看是否可以使用源的参数调用目标的任何签名来解析签名兼容性，并允许使用无关的参数。例如，只有在使用可选参数正确编写签名时，此代码才会公开错误：

```ts
function fn(x: (a: string, b: number, c: number) => void) { }
var x: Example;
// When written with overloads, OK -- used first overload
// When written with optionals, correctly an error
fn(x.diff);
```

第二个原因是消费者使用TypeScript的“严格空检查”功能。由于未指定的参数在JavaScript中显示为未定义，因此将显式的undefined传递给带有可选参数的函数通常很好。例如，在严格的空值下，此代码应该是正常的：

**使用联合类型**

不要只在一个参数位置写入因类型不同的重载：

```ts
/* WRONG */
interface Moment {
    utcOffset(): number;
    utcOffset(b: number): Moment;
    utcOffset(b: string): Moment;
}
```

尽可能使用联合类型：

```ts
/* OK */
interface Moment {
    utcOffset(): number;
    utcOffset(b: number|string): Moment;
}
```

请注意，我们在这里没有使b可选，因为签名的返回类型不同。

原因：这对于将“值”传递给函数的人来说非常重要：

```ts
function fn(x: string): void;
function fn(x: number): void;
function fn(x: number|string) {
    // When written with separate overloads, incorrectly an error
    // When written with union types, correctly OK
    return moment().utcOffset(x);
}
```
