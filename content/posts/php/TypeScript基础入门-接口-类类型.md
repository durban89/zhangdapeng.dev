---
title: "TypeScript基础入门 - 接口 - 类类型"
date: "2025-07-08 16:00:40"
slug: "typescript-ji-chu-ru-men-jie-kou-lei-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-接口-类类型/"
  - "/2025/07/08/TypeScript基础入门-接口-类类型.html"
  - "/TypeScript基础入门-接口-类类型/"
  - "/TypeScript基础入门-接口-类类型.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-lei-lei-xing/"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-lei-lei-xing.html"
  - "/typescript-ji-chu-ru-men-jie-kou-lei-lei-xing.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.12
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node src/learn_basic_types.ts
```

```bash
npx ts-node 脚本路径
```

## **接口**

TypeScript的核心原则之一是对值所具有的结构进行类型检查。 它有时被称做“鸭式辨型法”或“结构性子类型化”。 在TypeScript里，接口的作用就是为这些类型命名和为你的代码或第三方代码定义契约。

### **类类型**

### *实现接口*

与C#或Java里接口的基本作用一样，TypeScript也能够用它来明确的强制一个类去符合某种契约。如下实现

```ts
interface SomeClassInterface {
    property1: string;
}

class implementSomeInterface implements SomeClassInterface {
    property1: string;
    constructor(arg1: number, arg2: number) {}
}
```

你也可以在接口中描述一个方法，在类里实现它，如同下面的setProperty1方法一样：

```ts
interface SomeClassInterface {
    property1: string;
    // 设置property1
    setProperty1(p: string): any;
}

class implementSomeInterface implements SomeClassInterface {
    property1: string;
    constructor(arg1: number, arg2: number) {}
    setProperty1(p: string): any {
        this.property1 = p;
    }
}
```

接口描述了类的公共部分，而不是公共和私有两部分。 它不会帮你检查类是否具有某些私有成员。

### *类静态部分与实例部分的区别*

当你操作类和接口的时候，你要知道类是具有两个类型的：静态部分的类型和实例的类型。 你会注意到，当你用构造器签名去定义一个接口并试图定义一个类去实现这个接口时会得到一个错误：如下

```ts
interface SomeConstructor {
    new (arg1: string, arg2: string): any
}

class SomeClass implements SomeConstructor {
    property1: string;
    constructor(arg1: string, arg2: string) {}
}
```

运行后报错误如下

```bash
⨯ Unable to compile TypeScript:
src/interface_7.ts(20,7): error TS2420: Class 'SomeClass' incorrectly implements interface 'SomeConstructor'.
  Type 'SomeClass' provides no match for the signature 'new (arg1: string, arg2: string): any'.
```

这里因为当一个类实现了一个接口时，只对其实例部分进行类型检查。 constructor存在于类的静态部分，所以不在检查的范围内。因此，我们应该直接操作类的静态部分。 看下面的例子，我们定义了两个接口，SomeConstructor为构造函数所用和SomeClassInterface为实例方法所用。 为了方便我们定义一个构造函数createSomeFunc，它用传入的类型创建实例。

```ts
interface SomeClassInterface {
    property1: string;
    // 设置property1
    setProperty1(p: string): any;
    getProperty1(): string;
}

interface SomeConstructor {
    new(arg1: string, arg2: string): SomeClassInterface
}

function createSomeFunc(ctr: SomeConstructor, arg1: string, arg2: string): SomeClassInterface {
    return new ctr(arg1, arg2)
}

class ImplementSomeInterface1 implements SomeClassInterface {
    property1: string;
    property2: string;
    constructor(arg1: string, arg2: string) {
        this.property1 = arg1;
        this.property2 = arg2;
    }
    setProperty1(p: string): any {
        this.property1 = p;
    }

    getProperty1() {
        return this.property1 + ' = implementSomeInterface1';
    }
}

class ImplementSomeInterface2 implements SomeClassInterface {
    property1: string;
    property2: string;
    constructor(arg1: string, arg2: string) {
        this.property1 = arg1;
        this.property2 = arg2;
    }
    setProperty1(p: string): any {
        this.property1 = p;
    }

    getProperty1() {
        return this.property1 + ' = implementSomeInterface2';
    }
}

let instance1 = createSomeFunc(ImplementSomeInterface1, 'arg1', 'arg2');
let instance2 = createSomeFunc(ImplementSomeInterface2, 'arg1', 'arg2');
console.log(instance1.getProperty1());
console.log(instance2.getProperty1());
```

运行后得到的结果如下

```bash
arg1 = implementSomeInterface1
arg1 = implementSomeInterface2
```

因为createSomeFunc的第一个参数是SomeConstructor类型，在createSomeFunc(ImplementSomeInterface1, 'arg1', 'arg2')里，会检查ImplementSomeInterface1是否符合构造函数签名。

我觉得这里的话官方写的有点复杂了，为什么一定要使用一个构造函数接口呢，比如下面

```ts
let instance3 = new ImplementSomeInterface2('arg1','arg2')
console.log(instance3.getProperty1());
```

一样可以实现实例化，并且调用方法函数

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.13
```
