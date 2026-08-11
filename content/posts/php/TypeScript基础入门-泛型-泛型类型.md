---
title: "TypeScript基础入门 - 泛型 - 泛型类型"
date: "2025-07-09 09:59:03"
slug: "typescript-ji-chu-ru-men-fan-xing-fan-xing-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-泛型-泛型类型/"
  - "/2025/07/09/TypeScript基础入门-泛型-泛型类型.html"
  - "/TypeScript基础入门-泛型-泛型类型/"
  - "/TypeScript基础入门-泛型-泛型类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-fan-xing-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-fan-xing-lei-xing.html"
  - "/typescript-ji-chu-ru-men-fan-xing-fan-xing-lei-xing.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.2
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## 泛型

### 泛型类型

上一篇文章的分享，我们创建了identity通用函数，可以适用于不同的类型。 在这次分享中分享一下函数本身的类型，以及如何创建泛型接口。泛型函数的类型与非泛型函数的类型没什么不同，只是有一个类型参数在最前面，像函数声明一样，如下

```ts
function identity<T> (arg: T) : T {
    return arg;
}

let otherIdentity: <T> (arg: T) => T = identity;
```

我们也可以使用不同的泛型参数名，只要在数量上和使用方式上能对应上就可以，如下

```ts
function identity<T> (arg: T) : T {
    return arg;
}

let other1Identity: <U> (arg: U) => U = identity;
```

我们还可以使用带有调用签名的对象字面量来定义泛型函数，如下

```ts
function identity<T> (arg: T) : T {
    return arg;
}

let other2Identity: { <U>(arg: U): U } = identity;
```

这引导我们去写第一个泛型接口了。 我们把上面例子里的对象字面量拿出来做为一个接口，如下

```ts
function identity<T> (arg: T) : T {
    return arg;
}

interface GenerateIdentityFunc {
    <U> (arg: U): U;
}

let other3Identity: GenerateIdentityFunc = identity;
```

一个相似的例子，我们可能想把泛型参数当作整个接口的一个参数。 这样我们就能清楚的知道使用的具体是哪个泛型类型（比如： `Dictionary<string>`而不只是Dictionary）。 这样接口里的其它成员也能知道这个参数的类型了。

```ts
function identity<T> (arg: T) : T {
    return arg;
}

interface GenerateIdentityFunc1<U> {
    (arg: U): U
}

let other4Identity: GenerateIdentityFunc1<number> = identity;
```

注意，我们的示例做了少许改动。 不再描述泛型函数，而是把非泛型函数签名作为泛型类型一部分。 当我们使用 GenerateIdentityFunc1的时候，还得传入一个类型参数来指定泛型类型（这里是：`number`），锁定了之后代码里使用的类型。 对于描述哪部分类型属于泛型部分来说，理解何时把参数放在调用签名里和何时放在接口上是很有帮助的。

除了泛型接口，我们还可以创建泛型类。 注意，无法创建泛型枚举和泛型命名空间。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.3
```
