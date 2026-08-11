---
title: "TypeScript基础入门之高级类型的类型保护与区分类型"
date: "2025-07-09 10:00:21"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bao-hu-yu-qu-fen-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的类型保护与区分类型/"
  - "/2025/07/09/TypeScript基础入门之高级类型的类型保护与区分类型.html"
  - "/TypeScript基础入门之高级类型的类型保护与区分类型/"
  - "/TypeScript基础入门之高级类型的类型保护与区分类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bao-hu-yu-qu-fen-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bao-hu-yu-qu-fen-lei-xing.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-lei-xing-bao-hu-yu-qu-fen-lei-xing.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.3
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

继续分享高级类型相关的基础知识，有人说我是抄官网的，我想说，有多少人把官网的例子从头看了一边然后又照着抄了一遍，虽然效率很慢，但是我在这个过程中能够知道官网写例子跟说的话是否都是正确的，需要自己去验证下，我们就是因为太多的照猫画虎、依葫芦画瓢导致我们今天技术上没有太多的成就，我希望大家在学习技术的时候，能够踏踏实实的学习一下，知识学到了是你自己的，尤其是写代码，不要让别人觉得今天的程序员没有价值。  
打个比方，有人觉得写代码实现功能就可以了，但是我想说，这个是作为一个非技术公司的结果，希望大家去技术型公司，不然老板今天让你改明天让你改，改到最后，你都不知道自己在做神马，而且你写的代码给谁看？写的东西就是垃圾，不说写的多漂亮，至少我们可以对得起自己的花的时间，不要觉得去网上找个例子就抄抄，写写东西就很牛了，其实里面的东西差的不只是表面，这个年代，该让自己沉淀一下了，别太浮躁，现在不是战争年代，我们要有更高的追求。废话不多说继续基础分享。

## 高级类型

## 类型保护与区分类型（Type Guards and Differentiating Types）

从上一篇文章【[TypeScript基础入门之高级类型的交叉类型和联合类型](https://www.gowhich.com/blog/918)】的分享中我们可以了解到，联合类型适合于那些值可以为不同类型的情况。 但当我们想确切地了解是否为某个类型时怎么办？ JavaScript里常用来区分2个可能值的方法是检查成员是否存在。 如上一篇文章文章【[TypeScript基础入门之高级类型的交叉类型和联合类型](https://www.gowhich.com/blog/918)】中之前提及的，我们只能访问联合类型中共同拥有的成员。如下实例，访问任何一个非公有成员，程序编译的时候都会报错

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
if (type.func1) {
    type.func1(); // 报错
} else if (type.func3) {
    type.func3(); // 报错
}
```

编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_2.ts
src/advanced_types_2.ts:45:10 - error TS2551: Property 'func1' does not exist on type 'Type1Class | Type2Class'. Did you mean 'func2'?
  Property 'func1' does not exist on type 'Type2Class'.

45 if (type.func1) {
            ~~~~~

src/advanced_types_2.ts:46:10 - error TS2551: Property 'func1' does not exist on type 'Type1Class | Type2Class'. Did you mean 'func2'?
  Property 'func1' does not exist on type 'Type2Class'.

46     type.func1(); // 报错
            ~~~~~

src/advanced_types_2.ts:47:17 - error TS2551: Property 'func3' does not exist on type 'Type1Class | Type2Class'. Did you mean 'func2'?
  Property 'func3' does not exist on type 'Type1Class'.

47 } else if (type.func3) {
                   ~~~~~

src/advanced_types_2.ts:48:10 - error TS2551: Property 'func3' does not exist on type 'Type1Class | Type2Class'. Did you mean 'func2'?
  Property 'func3' does not exist on type 'Type1Class'.

48     type.func3(); // 报错
```

为了让这段代码工作，我们要使用类型断言，如下：

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
if ((<Type1Class>type).func1) {
    (<Type1Class>type).func1();
} else if ((<Type2Class>type).func3) {
    (<Type2Class>type).func3();
}
```

编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_2.ts && node ./src/advanced_types_2.js
func2 run
func1 run  
```

### 用户自定义的类型保护

这里可以注意到我们不得不多次使用类型断言。 假若我们一旦检查过类型，就能在之后的每个分支里清楚地知道let type = getSomeType('1')的类型的话就好了。

TypeScript里的 类型保护机制让它成为了现实。 类型保护就是一些表达式，它们会在运行时检查以确保在某个作用域里的类型。 要定义一个类型保护，我们只要简单地定义一个函数，它的返回值是一个"类型谓词"，如下实例

```ts
function isType1(type: Type1Class | Type2Class): type is Type1Class {
    return (<Type1Class>type).func1 !== undefined;
}
```

在这个例子里，"type is Type1Class"就是类型谓词。 谓词为 parameterName is Type这种形式， parameterName必须是来自于当前函数签名里的一个参数名。

每当使用一些变量调用isType1时，如果原始类型兼容，TypeScript会将该变量缩小到该特定类型。如下

```ts
if(isType1(type)) {
    type.func1()
} else {
    type.func3();
}
```

注意意TypeScript不仅知道在if分支里Type是Type1Class类型；它还清楚在else分支里，一定不是Type1Class类型，一定是Type2Class类型。

### typeof类型保护

我以上篇文章[TypeScript基础入门之高级类型的交叉类型和联合类型]的padLeft代码的代码为例，看看如何使用联合类型来改写padLeft。 可以像下面这样利用类型断言来写：

```ts
function isNumber(x: any): x is number {
    return typeof x === "number";
}

function isString(x: any): x is string {
    return typeof x === "string";
}

function padLeft(value: string, padding: string | number) {
    if (isString(padding)) {
        return padding + value;
    }

    if (isNumber(padding)) {
        return Array(padding + 1).join(' ') + value;
    }

    throw new Error(`Excepted string or number, got ${padding}`);
}

console.log("|" + padLeft("string", 4) + "|");
console.log("|" + padLeft("string", "a") + "|");
```

编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_2.ts && node ./src/advanced_types_2.js
|    string|
|astring|    
```

然而，必须要定义一个函数来判断类型是否是原始类型，这太痛苦了。 幸运的是，现在我们不必将typeof x === "number"抽象成一个函数，因为TypeScript可以将它识别为一个类型保护。 也就是说我们可以直接在代码里检查类型了。代码和上篇文章是一样的，省去了定义函数的痛苦。

```ts
function padLeft(value: string, padding: string | number) {
    if (typeof padding === 'string') {
        return padding + value;
    }

    if (typeof padding === 'number') {
        return Array(padding + 1).join(' ') + value;
    }

    throw new Error(`Excepted string or number, got ${padding}`);
}
```

这些 **\*\*typeof类型保护\*\*** 只有两种形式能被识别：`typeof v === "typename"`和`typeof v !== "typename"`， "typename"必须是"number"，"string"，"boolean"或"symbol"。 但是TypeScript并不会阻止你与其它字符串比较，语言不会把那些表达式识别为类型保护。

### instanceof类型保护

instanceof类型保护是通过构造函数来细化类型的一种方式。 比如，我们借鉴一下之前字符串填充的例子：

```ts
interface PadInterface {
    getPadString(): string;
}

class SpacePad implements PadInterface {
    constructor(private num: number){}
    getPadString(): string {
        return Array(this.num + 1).join(' ');
    }
}

class StringPad implements PadInterface {
    constructor(private string: string) { }
    getPadString(): string {
        return this.string;
    }
}

function getRandomPad() {
    return Math.random() < 0.5 ? 
    new SpacePad(5) :
    new StringPad(" ");
}

let pad: PadInterface = getRandomPad();
if (pad instanceof SpacePad) {
    console.log("|" + pad.getPadString() + "string|")
}

if (pad instanceof StringPad) {
    console.log("|" + pad + "string|")
}
```

第一次编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_2.ts && node ./src/advanced_types_2.js
|     string|
```

第二次编译并运行后得到如下结果

```bash
$ tsc ./src/advanced_types_2.ts && node ./src/advanced_types_2.js
| string|
```

instanceof的右侧要求是一个构造函数，TypeScript将细化为：

* 此构造函数的prototype属性的类型，如果它的类型不为any的话
* 构造签名所返回的类型的联合

以此顺序。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.4
```
