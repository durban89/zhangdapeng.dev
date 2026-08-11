---
title: "TypeScript基础入门 - 泛型 - 简介及使用"
date: "2025-07-09 09:58:48"
slug: "typescript-ji-chu-ru-men-fan-xing-jian-jie-ji-shi-yong"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-泛型-简介及使用/"
  - "/2025/07/09/TypeScript基础入门-泛型-简介及使用.html"
  - "/TypeScript基础入门-泛型-简介及使用/"
  - "/TypeScript基础入门-泛型-简介及使用.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-jian-jie-ji-shi-yong/"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-jian-jie-ji-shi-yong.html"
  - "/typescript-ji-chu-ru-men-fan-xing-jian-jie-ji-shi-yong.html"
---
*项目实践仓库*

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.6
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

### 简介

软件工程中，我们不仅要创建一致的定义良好的API，同时也要考虑可重用性。 组件不仅能够支持当前的数据类型，同时也能支持未来的数据类型，这在创建大型系统时为你提供了十分灵活的功能。

在像C#和Java这样的语言中，可以使用泛型来创建可重用的组件，一个组件可以支持多种类型的数据。 这样用户就可以以自己的数据类型来使用组件。

### 泛型的简单使用

下面来创建第一个使用泛型的例子：identity函数。 这个函数会返回任何传入它的值。 你可以把这个函数当成是 echo命令。

不用泛型的话，这个函数可能是下面这样：

```ts
function identity(arg: number): number {
    return arg;
}
```

或者

```ts
function identity(arg: any): any {
    return arg
}
```

使用any类型会导致这个函数可以接收任何类型的arg参数，这样就丢失了一些信息：传入的类型与返回的类型应该是相同的。如果我们传入一个数字，我们只知道任何类型的值都有可能被返回。

因此，我们需要一种方法使返回值的类型与传入参数的类型是相同的。 这里，我们使用了 "类型变量"，它是一种特殊的变量，只用于表示类型而不是值。

```ts
function identity<T>(arg: T): T {
    return arg;
}
```

我们给identity添加了类型变量T。 T帮助我们捕获用户传入的类型（比如：number），之后我们就可以使用这个类型。 之后我们再次使用了 T当做返回值类型。现在我们可以知道参数类型与返回值类型是相同的了。 这允许我们跟踪函数里使用的类型的信息。

我们把这个版本的identity函数叫做泛型，因为它可以适用于多个类型。 不同于使用 any，它不会丢失信息，像第一个例子那像保持准确性，传入数值类型并返回数值类型。我们定义了泛型函数后，可以用两种方法使用。 第一种是，传入所有的参数，包含类型参数，如下：

```ts
function identity<T>(arg: T): T {
    return arg;
}

let output = identity<string>("someString");
console.log(output);
console.log(typeof output);
```

运行后输出结果如下

```bash
$ npx ts-node src/generics_1.ts
someString
string
```

这里我们明确的指定了T是string类型，并做为一个参数传给函数，使用了<>括起来而不是()。第二种方法更普遍。利用了类型推论 -- 即编译器会根据传入的参数自动地帮助我们确定T的类型，如下

```ts
function identity<T>(arg: T): T {
    return arg;
}

let output = identity("other someString");
console.log(output);
console.log(typeof output);
```

运行后输出结果如下

```bash
$ npx ts-node src/generics_1.ts
someString
string
```

注意我们没必要使用尖括号（<>）来明确地传入类型；编译器可以查看`other someString`的值，然后把T设置为它的类型。 类型推论帮助我们保持代码精简和高可读性。如果编译器不能够自动地推断出类型的话，只能像上面那样明确的传入T的类型，在一些复杂的情况下，这是可能出现的。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.1
```
