---
title: "TypeScript基础入门 - 接口 - 继承接口"
date: "2025-07-08 16:00:54"
slug: "typescript-ji-chu-ru-men-jie-kou-ji-cheng-jie-kou"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-接口-继承接口/"
  - "/2025/07/08/TypeScript基础入门-接口-继承接口.html"
  - "/TypeScript基础入门-接口-继承接口/"
  - "/TypeScript基础入门-接口-继承接口.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-ji-cheng-jie-kou/"
  - "/2025/07/08/typescript-ji-chu-ru-men-jie-kou-ji-cheng-jie-kou.html"
  - "/typescript-ji-chu-ru-men-jie-kou-ji-cheng-jie-kou.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.13
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

### **继承接口**

和类一样，接口也可以相互继承。 这让我们能够从一个接口里复制成员到另一个接口里，可以更灵活地将接口分割到可重用的模块里。如下实例演示

```ts
interface Shape {
    color: string;
}

interface Square extends Shape {
    sideLength: number;
}

let square = <Square> {};
square.color = 'red'
square.sideLength = 10;
```

一个接口可以继承多个接口，创建出多个接口的合成接口。如下实例演示

```ts
interface Shape {
    color: string;
}

interface PenStroke {
    penWidth: number;
}

interface Square extends Shape, PenStroke {
    sideLength: number;
}

let square = <Square> {};
square.color = 'red'
square.sideLength = 10;
square.penWidth = 10;
```

### **混合类型**

先前我们提过，接口能够描述JavaScript里丰富的类型。 因为JavaScript其动态灵活的特点，有时你会希望一个对象可以同时具有上面提到的多种类型。一个例子就是，一个对象可以同时做为函数和对象使用，并带有额外的属性。

```ts
interface Counter {
    (start: number): string
    interval: number;
    reset(): void;
}

function getCounter(): Counter {
    let counter = <Counter>function(start: number) {};
    counter.interval = 10;
    counter.reset = function() {}
    return counter;
}

let counter = getCounter()
counter(10);
counter.reset();
counter.interval = 10.0
```

在使用JavaScript第三方库的时候，你可能需要像上面那样去完整地定义类型。

### **接口继承类**

当接口继承了一个类类型时，它会继承类的成员但不包括其实现。 就好像接口声明了所有类中存在的成员，但并没有提供具体实现一样。 接口同样会继承到类的private和protected成员。 这意味着当你创建了一个接口继承了一个拥有私有或受保护的成员的类时，这个接口类型只能被这个类或其子类所实现（implement）。当你有一个庞大的继承结构时这很有用，但要指出的是你的代码只在子类拥有特定属性时起作用。 这个子类除了继承至基类外与基类没有任何关系。 例：

```ts
class Control {
    private state: any;
}

interface SelectableControl extends Control {
    select(): void;
}

class Button extends Control implements SelectableControl {
    select() {}
}

class TextBox extends Control {

}

class Image implements SelectableControl {
    select() {}
}
```

运行后会爆出如下异常

```bash
⨯ Unable to compile TypeScript:
src/interface_8.ts(54,7): error TS2300: Duplicate identifier 'Image'.
src/interface_8.ts(54,7): error TS2420: Class 'Image' incorrectly implements interface 'SelectableControl'.
  Property 'state' is missing in type 'Image'.
```

在上面的例子里，SelectableControl包含了Control的所有成员，包括私有成员state。 因为 state是私有成员，所以只能够是Control的子类们才能实现SelectableControl接口。 因为只有 Control的子类才能够拥有一个声明于Control的私有成员state，这对私有成员的兼容性是必需的。

在Control类内部，是允许通过SelectableControl的实例来访问私有成员state的。 实际上， SelectableControl接口和拥有select方法的Control类是一样的。 Button和TextBox类是SelectableControl的子类（因为它们都继承自Control并有select方法），但Image和Location类并不是这样的。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.14
```
