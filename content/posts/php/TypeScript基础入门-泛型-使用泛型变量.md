---
title: "TypeScript基础入门 - 泛型 - 使用泛型变量"
date: "2025-07-09 09:58:53"
slug: "typescript-ji-chu-ru-men-fan-xing-shi-yong-fan-xing-bian-liang"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-泛型-使用泛型变量/"
  - "/2025/07/09/TypeScript基础入门-泛型-使用泛型变量.html"
  - "/TypeScript基础入门-泛型-使用泛型变量/"
  - "/TypeScript基础入门-泛型-使用泛型变量.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-shi-yong-fan-xing-bian-liang/"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-shi-yong-fan-xing-bian-liang.html"
  - "/typescript-ji-chu-ru-men-fan-xing-shi-yong-fan-xing-bian-liang.html"
---
*项目实践仓库*

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.1
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

### 使用泛型变量

使用泛型创建像上篇分享提到的identity这样的泛型函数时，编译器要求你在函数体必须正确的使用这个通用的类型。 换句话说，你必须把这些参数当做是任意或所有类型。

看下之前identity例子：

```ts
function identity<T>(arg: T): T {
    return arg
}
```

如果我们想同时打印出arg的长度。 我们很可能会这样做：

```ts
function loggingIdentity<T>(arg: T): T {
    // console.log(arg.length); // no length property
    return arg
}
```

如果这么做，编译器会报错说我们使用了arg的.length属性，但是没有地方指明arg具有这个属性。 记住，这些类型变量代表的是任意类型，所以使用这个函数的人可能传入的是个数字，而数字是没有 .length属性的。

现在假设我们想操作T类型的数组而不直接是T。由于我们操作的是数组，所以.length属性是应该存在的。 我们可以像创建其它数组一样创建这个数组：

```ts
function loggingIdentity<T>(arg: T[]): T[] {
    console.log(arg.length);
    return arg;
}
```

使用过其它语言的话，你可能对这种语法已经很熟悉了。 在下一次的分享，会介绍如何创建自定义泛型像 Array<T>一样。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.2
```
