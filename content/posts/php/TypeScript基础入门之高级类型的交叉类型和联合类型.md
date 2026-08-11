---
title: "TypeScript基础入门之高级类型的交叉类型和联合类型"
date: "2025-07-09 10:00:16"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-jiao-cha-lei-xing-he-lian-he-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的交叉类型和联合类型/"
  - "/2025/07/09/TypeScript基础入门之高级类型的交叉类型和联合类型.html"
  - "/TypeScript基础入门之高级类型的交叉类型和联合类型/"
  - "/TypeScript基础入门之高级类型的交叉类型和联合类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-jiao-cha-lei-xing-he-lian-he-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-jiao-cha-lei-xing-he-lian-he-lei-xi.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-jiao-cha-lei-xing-he-lian-he-lei-xing.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.2
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## 高级类型

### 交叉类型(Intersection Types)

交叉类型是将多个类型合并为一个类型。 这让我们可以把现有的多种类型叠加到一起成为一种类型，它包含了所需的所有类型的特性。 例如， Person & Serializable & Loggable同时是 Person 和 Serializable 和 Loggable。 就是说这个类型的对象同时拥有了这三种类型的成员。您将主要看到用于mixins的交集类型和其他不适合经典面向对象模具的概念。（在JavaScript中有很多这些！）这是一个简单的例子，展示了如何创建mixin：

```ts
function extend<T, U>(first: T, second: U): T & U {
    let result = <T & U>{}

    for (let id in first) {
        (<any>result)[id] = (<any>first)[id];
    }

    for (let id in second) {
        if (!result.hasOwnProperty(id)) {
            (<any>result)[id] = (<any>second)[id];
        }
    }

    return result
} 

class AdvancedTypesClass {
    constructor(public name: string){}
}

interface LoggerInterface {
    log(): void;
}

class AdvancedTypesLoggerClass implements LoggerInterface {
    log(): void {
        console.log('console logging');
    }
}

var logger = new AdvancedTypesLoggerClass();

var extend1 = extend(new AdvancedTypesClass("string"), new AdvancedTypesLoggerClass());
var e = extend1.name;
console.log(e);
extend1.log();
```

编译运行，注意这里要编译运行，我使用ts-node已经不能运行成功了。可能是哪里配置的有问题，具体步骤如下。

```bash
tsc ./src/advanced_types_1.ts
$ node ./src/advanced_types_1.js
string
console logging
```

### 联合类型(Union Types)

联合类型与交叉类型很有关联，但是使用上却完全不同。 偶尔你会遇到这种情况，一个代码库希望传入 number或 string类型的参数。 例如下面的函数：

```ts
/**
 * 为给定的字符串左侧添加"padding"
 * 如果"padding"是一个字符串，则添加将字符串添加到给定字符串的左侧
 * 如果"padding"是一个数字，则添加padding个数量的空格到给定字符串的左侧
 */
function padLeft(value: string, padding: any) {
    if (typeof padding === 'string') {
        return padding + value;
    }

    if (typeof padding === 'number') {
        return Array(padding + 1).join(' ') + value;
    }

    throw new Error(`Excepted string or number, got ${padding}`);
}
console.log("|" + padLeft("string", 4) + "|");
console.log("|" + padLeft("string", "a") + "|");
```

编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_1.ts && node ./src/advanced_types_1.js
|    string|
|astring|
```

padLeft有一个问题，就是padding这个参数是一个any类型，那就意味着我们可以在传递参数的时候，参数的类型可以是number或者是string，而TypeScript将会正常解析，  
如果如下的方式调用，编译的时候是可以正常解析的，但是运行的时候回报错

```ts
padLeft("Hello world", true);
```

在传统的面向对象语言里，我们可能会将这两种类型抽象成有层级的类型。 这么做显然是非常清晰的，但同时也存在了过度设计。 padLeft原始版本的好处之一是允许我们传入原始类型。 这样做的话使用起来既简单又方便。 如果我们就是想使用已经存在的函数的话，这种新的方式就不适用了。除了any， 我们可以使用"联合类型"做为padding的参数，如下：

```ts
/**
 * 为给定的字符串左侧添加"padding"
 * 如果"padding"是一个字符串，则添加将字符串添加到给定字符串的左侧
 * 如果"padding"是一个数字，则添加padding个数量的空格到给定字符串的左侧
 */
function padLeft(value: string, padding: string | number) {
    if (typeof padding === 'string') {
        return padding + value;
    }

    if (typeof padding === 'number') {
        return Array(padding + 1).join(' ') + value;
    }

    throw new Error(`Excepted string or number, got ${padding}`);
}
console.log("|" + padLeft("string", 4) + "|");
console.log("|" + padLeft("string", "a") + "|");
console.log("|" + padLeft("string", true) + "|");
```

编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_1.ts && node ./src/advanced_types_1.js
src/advanced_types_1.ts:65:37 - error TS2345: Argument of type 'true' is not assignable to parameter of type 'string | number'.

65 console.log("|" + padLeft("string", true) + "|");
```

从实例演示可以看出，当传入一个boolean类型值的时候，在编辑的时候TypeScript就做出了判断，表示boolean类型的参数不被支持

联合类型表示一个值可以是几种类型之一。 我们用竖线(|)分隔每个类型，所以 number | string | boolean表示一个值可以是 number， string，或 boolean。

如果一个值是联合类型，我们只能访问此联合类型的所有类型里共有的成员，如下实例

```ts
interface Type1 {
    func1(): void;
    func2(): void;
}

interface Type2 {
    func3(): void;
    func2(): void;
}

class Type1Class implements Type1 {
    func1(): void {
        console.log('func1 run');
    }

    func2(): void {
        console.log('func2 run');
    }
}

class Type2Class implements Type2 {
    func3(): void {
        console.log('func1 run');
    }

    func2(): void {
        console.log('func2 run');
    }
}

function getSomeType(type: string): Type1Class | Type2Class {
    if (type === '1') {
        return new Type1Class();
    }

    if (type === '2') {
        return new Type2Class();
    }

    throw new Error(`Excepted Type1Class or Type2Class, got ${type}`);
}

let type = getSomeType('1');
type.func2();
type.func1(); // 报错
```

编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_1.ts
src/advanced_types_1.ts:111:6 - error TS2551: Property 'func1' does not exist on type 'Type1Class | Type2Class'. Did you mean 'func2'?
  Property 'func1' does not exist on type 'Type2Class'.

111 type.func1();
```

这里的联合类型可能有点复杂，但是你很容易就习惯了。 如果一个值的类型是 A | B，我们能够 确定的是它包含了 A 和 B中共有的成员。 这个例子里， Type1Class具有一个func1成员。 我们不能确定一个 Type1Class | Type2Class类型的变量是否有func1方法。 如果变量在运行时是Type1Class类型，那么调用type.func1()就出错了。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.3
```
