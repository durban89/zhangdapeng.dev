---
title: "TypeScript基础入门之Javascript文件类型检查(四)"
date: "2025-07-10 10:56:37"
slug: "typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-si"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(四)/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查(四).html"
  - "/TypeScript基础入门之Javascript文件类型检查(四)/"
  - "/TypeScript基础入门之Javascript文件类型检查(四).html"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-四/"
  - "/2025/07/10/TypeScript基础入门之Javascript文件类型检查-四.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-si/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-si.html"
  - "/typescript-ji-chu-ru-men-zhi-javascript-wen-jian-lei-xing-jian-cha-si.html"
---
继续上篇文章【[TypeScript基础入门之Javascript文件类型检查(三)](https://www.gowhich.com/blog/961)】

**@param 和 @returns**

@param使用与@type相同的类型语法，但添加了参数名称。 通过用方括号括起名称，也可以声明该参数是可选的：

```ts
// Parameters may be declared in a variety of syntactic forms
/**
 * @param {string}  p1 - A string param.
 * @param {string=} p2 - An optional param (Closure syntax)
 * @param {string} [p3] - Another optional param (JSDoc syntax).
 * @param {string} [p4="test"] - An optional param with a default value
 * @return {string} This is the result
 */
function stringsStringStrings(p1, p2, p3, p4){
  // TODO
}
```

同样，对于函数的返回类型：

```ts
/**
 * @return {PromiseLike<string>}
 */
function ps(){}

/**
 * @returns {{ a: string, b: number }} - May use '@returns' as well as '@return'
 */
function ab(){}
```

**@typedef, @callback, 和 @param**

@typedef可用于定义复杂类型。 类似的语法适用于@param。

```ts
/**
 * @typedef {Object} SpecialType - creates a new type named 'SpecialType'
 * @property {string} prop1 - a string property of SpecialType
 * @property {number} prop2 - a number property of SpecialType
 * @property {number=} prop3 - an optional number property of SpecialType
 * @prop {number} [prop4] - an optional number property of SpecialType
 * @prop {number} [prop5=42] - an optional number property of SpecialType with default
 */
/** @type {SpecialType} */
var specialTypeObject;
```

您可以在第一行使用对象或对象。

```ts
/**
 * @typedef {object} SpecialType1 - creates a new type named 'SpecialType'
 * @property {string} prop1 - a string property of SpecialType
 * @property {number} prop2 - a number property of SpecialType
 * @property {number=} prop3 - an optional number property of SpecialType
 */
/** @type {SpecialType1} */
var specialTypeObject1;
```

@param允许一次性类型规范使用类似的语法。 请注意，嵌套属性名称必须以参数名称为前缀：

```ts
/**
 * @param {Object} options - The shape is the same as SpecialType above
 * @param {string} options.prop1
 * @param {number} options.prop2
 * @param {number=} options.prop3
 * @param {number} [options.prop4]
 * @param {number} [options.prop5=42]
 */
function special(options) {
  return (options.prop4 || 1001) + options.prop5;
}
```

@callback类似于@typedef，但它指定了一个函数类型而不是一个对象类型：

```ts
/**
 * @callback Predicate
 * @param {string} data
 * @param {number} [index]
 * @returns {boolean}
 */
/** @type {Predicate} */
const ok = s => !(s.length % 2);
```

当然，任何这些类型都可以在单行@typedef中使用Typescript语法声明：

```ts
/** @typedef {{ prop1: string, prop2: string, prop3?: number }} SpecialType */
/** @typedef {(data: string, index?: number) => boolean} Predicate */
```

**@template**

您可以使用@template标记声明泛型类型：

```ts
/**
 * @template T
 * @param {T} p1 - A generic parameter that flows through to the return type
 * @return {T}
 */
function id(x){ return x }
```

使用逗号或多个标签声明多个类型参数：

```ts
/**
 * @template T,U,V
 * @template W,X
 */
```

您还可以在类型参数名称之前指定类型约束。 只限列表中的第一个类型参数：

```ts
/**
 * @template {string} K - K must be a string or string literal
 * @template {{ serious(): string }} Seriousalizable - must have a serious method
 * @param {K} key
 * @param {Seriousalizable} object
 */
function seriousalize(key, object) {
  // ????
}
```

未完待续...
