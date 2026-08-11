---
title: "TypeScript基础入门 - 函数 - 剩余参数"
date: "2025-07-08 16:01:42"
slug: "typescript-ji-chu-ru-men-han-shu-sheng-yu-can-shu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-函数-剩余参数/"
  - "/2025/07/08/TypeScript基础入门-函数-剩余参数.html"
  - "/TypeScript基础入门-函数-剩余参数/"
  - "/TypeScript基础入门-函数-剩余参数.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-sheng-yu-can-shu/"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-sheng-yu-can-shu.html"
  - "/typescript-ji-chu-ru-men-han-shu-sheng-yu-can-shu.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.1
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

### **剩余参数**

必要参数，默认参数和可选参数有个共同点：它们表示某一个参数。 有时，你想同时操作多个参数，或者你并不知道会有多少参数传递进来。 在JavaScript里，你可以使用 arguments来访问所有传入的参数。在TypeScript里，你可以把所有参数收集到一个变量里：

```ts
function buildName(firstName: string, ...restOfName: string[]) {
    return firstName + " " + restOfName.join(" ")
}

let aName = buildName("Lili", "John", "David", "Durban");
console.log(aName);
```

运行后得到的结果如下

```bash
$ npx ts-node src/function_3.ts
Lili John David Durban
```

剩余参数会被当做个数不限的可选参数。 可以一个都没有，同样也可以有任意个。 编译器创建参数数组，名字是你在省略号（...）后面给定的名字，你可以在函数体内使用这个数组。这个省略号也会在带有剩余参数的函数类型定义上使用到：

```ts
function buildName(firstName: string, ...restOfName: string[]) {
    return firstName + " " + restOfName.join(" ");
}

let buildNameFunc: (fname: string, ...rest: string[]) => string = buildName;

console.log(buildNameFunc("John", "Julia", "July"));
```

运行后得到的结果如下

```bash
$ npx ts-node src/function_3.ts
Lili John David Durban
```

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.2
```
