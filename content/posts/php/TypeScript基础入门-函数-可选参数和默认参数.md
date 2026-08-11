---
title: "TypeScript基础入门 - 函数 - 可选参数和默认参数"
date: "2025-07-08 16:01:39"
slug: "typescript-ji-chu-ru-men-han-shu-ke-xuan-can-shu-he-mo-ren-can-shu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-函数-可选参数和默认参数/"
  - "/2025/07/08/TypeScript基础入门-函数-可选参数和默认参数.html"
  - "/TypeScript基础入门-函数-可选参数和默认参数/"
  - "/TypeScript基础入门-函数-可选参数和默认参数.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-ke-xuan-can-shu-he-mo-ren-can-shu/"
  - "/2025/07/08/typescript-ji-chu-ru-men-han-shu-ke-xuan-can-shu-he-mo-ren-can-shu.html"
  - "/typescript-ji-chu-ru-men-han-shu-ke-xuan-can-shu-he-mo-ren-can-shu.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.0
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

### 可选参数和默认参数

TypeScript里的每个函数参数都是必须的。 这不是指不能传递 null或undefined作为参数，而是说编译器检查用户是否为每个参数都传入了值。 编译器还会假设只有这些参数会被传递进函数。 简短地说，传递给一个函数的参数个数必须与函数期望的参数个数一致。如下实例演示

```ts
function buildName(firstName: string, lastName: string) {
    return firstName + ' ' + lastName
}

// 错误演示
buildName("firstName")
// 错误演示
buildName("firstName", "lastName", "lastName")
// 正确演示
buildName("firstName", "lastName")
```

JavaScript里，每个参数都是可选的，可传可不传。 没传参的时候，它的值就是undefined。 在TypeScript里我们可以在参数名旁使用 ?实现可选参数的功能。 比如，我们想让last name是可选的：

```ts
function buildName(firstName: string, lastName?: string) {
    return firstName + ' ' + lastName
}

// 错误演示
buildName("firstName", "lastName", "lastName")
// 正确演示
buildName("firstName")
// 正确演示
buildName("firstName", "lastName")
```

可选参数必须跟在必须参数后面。 如果上例我们想让first name是可选的，那么就必须调整它们的位置，把first name放在后面。在TypeScript里，我们也可以为参数提供一个默认值当用户没有传递这个参数或传递的值是undefined时。 它们叫做有默认初始化值的参数。 让我们修改上例，把last name的默认值设置为"Smith"。

```ts
function buildName(firstName: string, lastName="Smith") {
    return firstName + ' ' + lastName
}

// 正确演示
buildName("A")
// 正确演示
buildName("A", undefined)
// 错误演示
buildName("firstName", "lastName", "lastName")
// 正确演示
buildName("firstName", "lastName")
```

在所有必须参数后面的带默认初始化的参数都是可选的，与可选参数一样，在调用函数的时候可以省略。 也就是说可选参数与末尾的默认参数共享参数类型。

```ts
function buildName(firstName: string, lastName="Smith") {
    return firstName + ' ' + lastName
}
```

和

```ts
function buildName(firstName: string, lastName?: string) {
    return firstName + ' ' + lastName
}
```

共享同样的类型(firstName: string, lastName?: string) => string。 默认参数的默认值消失了，只保留了它是一个可选参数的信息。与普通可选参数不同的是，带默认值的参数不需要放在必须参数的后面。 如果带默认值的参数出现在必须参数前面，用户必须明确的传入 undefined值来获得默认值。 例如，我们重写最后一个例子，让 firstName是带默认值的参数：

```ts
function buildName(firstName="Durban", lastName: string) {
    return firstName + ' ' + lastName
}

// 错误演示
buildName("A")
// 正确演示
buildName(undefined,  "A")
// 错误演示
buildName("firstName", "lastName", "lastName")
// 正确演示
buildName("firstName", "lastName")
```

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.2.1
```
