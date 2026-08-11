---
title: "TypeScript基础入门之高级类型的索引类型(Index types)"
date: "2025-07-09 10:42:44"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-suo-yin-lei-xing-index-types"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的索引类型(Index-types)/"
  - "/2025/07/09/TypeScript基础入门之高级类型的索引类型(Index-types).html"
  - "/TypeScript基础入门之高级类型的索引类型(Index-types)/"
  - "/TypeScript基础入门之高级类型的索引类型(Index-types).html"
  - "/2025/07/09/TypeScript基础入门之高级类型的索引类型-Index-types/"
  - "/2025/07/09/TypeScript基础入门之高级类型的索引类型-Index-types.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-suo-yin-lei-xing-index-types/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-suo-yin-lei-xing-index-types.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-suo-yin-lei-xing-index-types.html"
---
## 高级类型

### 索引类型(Index types)

使用索引类型，编译器就能够检查使用了动态属性名的代码。 例如，一个常见的JavaScript模式是从对象中选取属性的子集。

```ts
function pluck(o, names) {
    return names.map(n => o[n]);
}
```

下面是如何在TypeScript里使用此函数，通过 索引类型查询和 索引访问操作符：

```ts
function pluck<T, K extends keyof T>(o:T, names: K[]): T[K][] {
  return names.map(n => o[n])
}

interface Interface1 {
  name: string;
  age: number;
}

let i: Interface1 = {
  name: "A",
  age: 1,
}

let pluckStr: string[] = pluck(i, ['name'])
console.log(pluckStr)
```

运行后输出如下

```bash
[ 'A' ]
```

编译器会检查 name是否真的是Interface1的一个属性。 本例还引入了几个新的类型操作符。 首先是 keyof T， 索引类型查询操作符。 对于任何类型 T， keyof T的结果为 T上已知的公共属性名的联合。 例如：

```ts
let someProps: keyof Interface1; // 'name' | 'age'
```

keyof Interface1是完全可以与'name'|'age'互相替换的。 不同的是如果你添加了其它的属性到Interface1，例如address: string，那么 keyof Interface1会自动变为'name'|'age'|'address'。 你可以在像pluck函数这类上下文里使用 keyof，因为在使用之前你并不清楚可能出现的属性名。 但编译器会检查你是否传入了正确的属性名给 pluck：

```ts
pluck(i, ['age', 'unknown']); // error, 'unknown' is not in 'name' | 'age'
```

第二个操作符是T[K]，索引访问操作符。 在这里，类型语法反映了表达式语法。 这意味着 i['name']具有类型Interface1['name'] — 在我们的例子里则为string类型。 然而，就像索引类型查询一样，你可以在普通的上下文里使用 T[K]，这正是它的强大所在。 你只要确保类型变量 K extends keyof T就可以了。 例如下面 getProperty函数的例子：

```ts
function getProperty<T, K extends keyof T>(o: T, name: K): T[K] {
    return o[name]; // o[name] is of type T[K]
}
```

getProperty里的 o: T和 name: K，意味着 o[name]: T[K]。 当你返回 T[K]的结果，编译器会实例化键的真实类型，因此 getProperty的返回值类型会随着你需要的属性改变。

```ts
let name: string = getProperty(i, 'name');
let age: number = getProperty(i, 'age');
let unknown = getProperty(i, 'unknown'); // error, 'unknown' is not in 'name' | 'age'
```

### *索引类型和字符串索引签名*

keyof和T[K]与字符串索引签名进行交互。如果你有一个带有字符串索引签名的类型，那么 keyof T会是 string。并且T[string]为索引签名的类型：

```ts
interface Map<T> {
    [key: string]: T;
}
let keys: keyof Map<number>; // string
let value: Map<number>['foo']; // number
```
