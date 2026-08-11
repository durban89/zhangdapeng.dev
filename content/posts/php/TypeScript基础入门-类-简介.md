---
title: "TypeScript基础入门 - 类 - 简介"
date: "2025-07-08 16:01:03"
slug: "typescript-ji-chu-ru-men-lei-jian-jie"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-类-简介/"
  - "/2025/07/08/TypeScript基础入门-类-简介.html"
  - "/TypeScript基础入门-类-简介/"
  - "/TypeScript基础入门-类-简介.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-jian-jie/"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-jian-jie.html"
  - "/typescript-ji-chu-ru-men-lei-jian-jie.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.14
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## **类**

### **介绍**

传统的JavaScript程序使用函数和基于原型的继承来创建可重用的组件，但对于熟悉使用面向对象方式的程序员来讲就有些棘手，因为他们用的是基于类的继承并且对象是由类构建出来的。 从ECMAScript 2015，也就是ECMAScript 6开始，JavaScript程序员将能够使用基于类的面向对象的方式。 使用TypeScript，我们允许开发者现在就使用这些特性，并且编译后的JavaScript可以在所有主流浏览器和平台上运行，而不需要等到下个JavaScript版本。

### **类的使用**

下面看一个使用类的例子：

```ts
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }

    greet() {
        return this.greeting;
    }
}

const greeter = new Greeter("Good Morning");
console.log(greeter.greet());
```

运行后得到如下结果

```bash
$ npx ts-node src/classes_1.ts
Good Morning
```

如果你使用过C#或Java，你会对这种语法非常熟悉。 我们声明一个 Greeter类。这个类有3个成员：一个叫做 greeting的属性，一个构造函数和一个 greet方法。

你会注意到，我们在引用任何一个类成员的时候都用了 this。 它表示我们访问的是类的成员。

最后一行，我们使用 new构造了 Greeter类的一个实例。 它会调用之前定义的构造函数，创建一个 Greeter类型的新对象，并执行构造函数初始化它。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.0
```
