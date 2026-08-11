---
title: "TypeScript基础入门 - 类 - 继承"
date: "2025-07-08 16:01:08"
slug: "typescript-ji-chu-ru-men-lei-ji-cheng"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-类-继承/"
  - "/2025/07/08/TypeScript基础入门-类-继承.html"
  - "/TypeScript基础入门-类-继承/"
  - "/TypeScript基础入门-类-继承.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-ji-cheng/"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-ji-cheng.html"
  - "/typescript-ji-chu-ru-men-lei-ji-cheng.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.0
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

### **继承**

在TypeScript里，我们可以使用常用的面向对象模式。 基于类的程序设计中一种最基本的模式是允许使用继承来扩展现有的类。看下面的例子：

```ts
class Animal {
    move(distanceMeter: number = 0) {
        console.log(`Animal moved ${distanceMeter}m`);
    }
}

class Dog extends Animal {
    bark() {
        console.log('Woof........!');
    }
}

const dog = new Dog();
dog.bark();
dog.move(3);
dog.bark();
```

运行后得到如下结果

```bash
$ npx ts-node src/classes_2.ts
Woof........!
Animal moved 3m
Woof........!
```

这个例子展示了最基本的继承：类从基类中继承了属性和方法。这里，Dog是一个派生类，它派生自Animal基类，通过extends关键字。派生类通常被称作 子类，基类通常被称作超类。

因为Dog继承了Animal的功能，因此我们可以创建一个Dog的实例，它能够 bark()和move()。下面我们来看个更加复杂的例子。

```ts
class Animal {
    name: string;
    constructor(theName: string) {
        this.name = theName;
    }

    move(distanceMeter: number = 0) {
        console.log(`${this.name} moved ${distanceMeter}m`);
    }
}

class Snake extends Animal {
    constructor(name: string) {
        super(name);
    }

    move(distanceMeter: number = 5) {
        console.log('滑动的声音......');
        super.move(distanceMeter);
    }
}

class Horse extends Animal {
    constructor(name: string) {
        super(name);
    }

    move(distanceMeter: number = 45) {
        console.log('跑动的声音......');
        super.move(distanceMeter);
    }
}

const snake = new Snake('small snake');
const horse: Animal = new Horse('small horse');

snake.move();
horse.move(152);
```

运行后得到如下结果

```bash
$ npx ts-node src/classes_2.ts
滑动的声音......
small snake moved 5m
跑动的声音......
small horse moved 152m
```

这个例子展示了一些上篇文章【[TypeScript基础入门 - 类 - 简介](https://www.gowhich.com/blog/883)】没有提到的特性。 这一次，我们使用extends关键字创建了 Animal的两个子类：Horse和 Snake。

与前一个例子的不同点是，派生类包含了一个构造函数，它必须调用super()，它会执行基类的构造函数。 而且，在构造函数里访问this的属性之前，我们一定要调用 super()。 这个是TypeScript强制执行的一条重要规则。

这个例子演示了如何在子类里可以重写父类的方法。Snake类和 Horse类都创建了move方法，它们重写了从Animal继承来的move方法，使得 move方法根据不同的类而具有不同的功能。注意，即使horse被声明为Animal类型，但因为它的值是Horse，调用tom.move(152)时，它会调用Horse里重写的方法。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.1
```
