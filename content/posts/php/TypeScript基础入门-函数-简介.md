---
title: "TypeScript基础入门 - 函数 - 简介"
date: "2025-07-08 16:01:35"
slug: "typescript-ji-chu-ru-men-han-shu-jian-jie"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-函数-简介/"
  - "/2025/07/08/TypeScript基础入门-函数-简介.html"
  - "/TypeScript基础入门-函数-简介/"
  - "/TypeScript基础入门-函数-简介.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-jian-jie/"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-jian-jie.html"
  - "/typescript-ji-chu-ru-men-han-shu-jian-jie.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.6
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## **函数**

### **介绍**

函数是JavaScript应用程序的基础。 它帮助你实现抽象层，模拟类，信息隐藏和模块。 在TypeScript里，虽然已经支持类，命名空间和模块，但函数仍然是主要的定义 行为的地方。 TypeScript为JavaScript函数添加了额外的功能，让我们可以更容易地使用。说实话我都不想看这块的东西，函数嘛是个写程序的都会写，但是为了追求整体及探索新的知识，没准有意外发现，还是要学习下。

### **函数**

和JavaScript一样，TypeScript函数可以创建有名字的函数和匿名函数。 你可以随意选择适合应用程序的方式，不论是定义一系列API函数还是只使用一次的函数。通过下面的例子可以迅速回想起这两种JavaScript中的函数：

```ts
function add(x, y) {
    return x + y
}

let addFunc = function(x, y) { return x + y }
```

在JavaScript里，函数可以使用函数体外部的变量。 当函数这么做时，我们说它‘捕获’了这些变量。   
至于为什么可以这样做以及其中的利弊超出了本文的范围，但是深刻理解这个机制对学习JavaScript和TypeScript会很有帮助。

```ts
let z = 10;
function addTo(x, y) {
    return x + y + z;
}
```

### **函数类型**

**为函数定义类型**  
让我们为上面那个函数添加类型

```ts
function add(x: number, y:number): number {
    return x + y;
}

let addFunc = function (x: number, y: number): number { return x + y }
```

我们可以给每个参数添加类型之后再为函数本身添加返回值类型。 TypeScript能够根据返回语句自动推断出返回值类型，因此我们通常省略它。

**书写完整函数类型**

现在我们已经为函数指定了类型，下面让我们写出函数的完整类型。

```ts
let addFunc: (x: number, y:number) => number = function(x: number, y: number): number { return x + y }
```

函数类型包含两部分：参数类型和返回值类型。 当写出完整函数类型的时候，这两部分都是需要的。 我们以参数列表的形式写出参数类型，为每个参数指定一个名字和类型。 这个名字只是为了增加可读性。 我们也可以这么写

```ts
let addFunc: (baseValue: number, increment: number) => number = function (x: number, y: number): number { return x + y }
```

只要参数类型是匹配的，那么就认为它是有效的函数类型，而不在乎参数名是否正确。

第二部分是返回值类型。 对于返回值，我们在函数和返回值类型之前使用( =>)符号，使之清晰明了。 如之前提到的，返回值类型是函数类型的必要部分，如果函数没有返回任何值，你也必须指定返回值类型为 void而不能留空。

函数的类型只是由参数类型和返回值组成的。 函数中使用的捕获变量不会体现在类型里。 实际上，这些变量是函数的隐藏状态并不是组成API的一部分。

### **推断类型**

尝试这个例子的时候，你会发现如果你在赋值语句的一边指定了类型但是另一边没有类型的话，TypeScript编译器会自动识别出类型：

```ts
let addFunc = function(x: number, y: number): number { return x + y }
```

```ts
let addFunc: (baseValue: number, increment: number) => number = function(x, y) { return  x + y }
```

这叫做“按上下文归类”，是类型推论的一种。 它帮助我们更好地为程序指定类型。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.0
```
