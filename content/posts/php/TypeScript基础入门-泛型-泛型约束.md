---
title: "TypeScript基础入门 - 泛型 - 泛型约束"
date: "2025-07-09 09:59:28"
slug: "typescript-ji-chu-ru-men-fan-xing-fan-xing-yue-shu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-泛型-泛型约束/"
  - "/2025/07/09/TypeScript基础入门-泛型-泛型约束.html"
  - "/TypeScript基础入门-泛型-泛型约束/"
  - "/TypeScript基础入门-泛型-泛型约束.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-fan-xing-yue-shu/"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-fan-xing-yue-shu.html"
  - "/typescript-ji-chu-ru-men-fan-xing-fan-xing-yue-shu.html"
---
*项目实践仓库*

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.4
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

### 泛型约束

我之前分享的一个例子中，有时候想操作某类型的一组值，并且知道这组值具有什么样的属性。在loggingIdentity例子中，我们想访问arg的length属性，但是编译器并不能证明每种类型都有length属性，所以就报错了。

```ts
function loggingIdentity<T>(arg: T): T {
    console.log(arg.length);  // Error: T doesn't have .length
    return arg;
}
```

相比于操作any所有类型，我们想要限制函数去处理任意带有.length属性的所有类型。 只要传入的类型有这个属性，我们就允许，就是说至少包含这一属性。 为此，我们需要列出对于T的约束要求。为此，我们定义一个接口来描述约束条件。 创建一个包含 .length属性的接口，使用这个接口和extends关键字来实现约束：

```ts
interface LengthDefine {
    length: number;
}

function loggingIdentity<T extends LengthDefine>(arg: T): T {
    console.log(arg.length);

    return arg;
}
```

现在这个泛型函数被定义了约束，因此它不再是适用于任意类型：

```ts
loggingIdentity(3);
```

运行后会遇到如下错误提示

```bash
⨯ Unable to compile TypeScript:
src/generics_5.ts(11,17): error TS2345: Argument of type '3' is not assignable to parameter of type 'LengthDefine'.
```

我们需要传入符合约束类型的值，必须包含必须的属性：

```ts
loggingIdentity({length: 10, value:3});
```

运行后会得到如下结果

```bash
$ npx ts-node src/generics_5.ts
10
```

### 在泛型约束中使用类型参数

我们可以声明一个类型参数，且它被另一个类型参数所约束。 比如，现在我们想要用属性名从对象里获取这个属性。 并且我们想要确保这个属性存在于对象 obj上，因此我们需要在这两个类型之间使用约束。

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K) {
    return obj[key]
}

let x = {a:1, b:2, c:3, d:4};
getProperty(x, "a"); // 正常
getProperty(x, "m"); // 异常
```

运行后得到如下错误信息

```bash
$ npx ts-node src/generics_5.ts
⨯ Unable to compile TypeScript:
src/generics_5.ts(21,16): error TS2345: Argument of type '"m"' is not assignable to parameter of type '"a" | "b" | "c" | "d"'.
```

### 在泛型里使用类类型

在TypeScript使用泛型创建工厂函数时，需要引用构造函数的类类型。比如，

```ts
function create<T> (c: {new(): T;}): T {
    return new c();
}
```

一个更高级的例子，使用原型属性推断并约束构造函数与类实例的关系。

```ts
class Keeper1 {
    hasMask: boolean;
}

class Keeper2 {
    nameTag: string;
}

class Keeper3 {
    numLength: number;
}

class ChildrenKeeper1 extends Keeper3 {
    keeper: Keeper1;
}

class ChildrenKeeper2 extends Keeper3 {
    keeper: Keeper2;
}

function createInstance<A extends Keeper3> (c: new() => A): A {
    return new c();
}

console.log(createInstance(ChildrenKeeper1));
console.log(createInstance(ChildrenKeeper2));
```

运行后得到如下输出

```bash
$ npx ts-node src/generics_5.ts
ChildrenKeeper1 {}
ChildrenKeeper2 {}
```

感觉没在实际应用中使用，很鸡肋呀

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.5
```
