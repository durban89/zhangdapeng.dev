---
title: "TypeScript基础入门 - 类 - 高级技巧"
date: "2025-07-08 16:01:28"
slug: "typescript-ji-chu-ru-men-lei-gao-ji-ji-qiao"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-类-高级技巧/"
  - "/2025/07/08/TypeScript基础入门-类-高级技巧.html"
  - "/TypeScript基础入门-类-高级技巧/"
  - "/TypeScript基础入门-类-高级技巧.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-gao-ji-ji-qiao/"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-gao-ji-ji-qiao.html"
  - "/typescript-ji-chu-ru-men-lei-gao-ji-ji-qiao.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.5
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

# **类**

## **高级技巧**

### **构造函数**

当你在TypeScript里声明了一个类的时候，实际上同时声明了很多东西。 首先就是类的 实例的类型。

```ts
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }

    greet() {
        return "Hello, " + this.greeting;
    }
}

let greeter: Greeter;
greeter = new Greeter('Gowhich');
console.log(greeter.greet());
```

运行后得到如下结果

```bash
$ npx ts-node src/classes_7.ts
Hello, Gowhich
```

这里，我们写了 let greeter: Greeter，意思是 Greeter类的实例的类型是 Greeter。 这对于用过其它面向对象语言的程序员来讲已经是老习惯了。

我们也创建了一个叫做 构造函数的值。 这个函数会在我们使用 new创建类实例的时候被调用。 下面我们来看看，上面的代码被编译成JavaScript后是什么样子的，如下所示

```ts
var Greeter = /** @class */ (function () {
    function Greeter(message) {
        this.greeting = message;
    }
    Greeter.prototype.greet = function () {
        return "Hello, " + this.greeting;
    };
    return Greeter;
}());
var greeter;
greeter = new Greeter('Gowhich');
console.log(greeter.greet());
```

上面的代码里， var Greeter将被赋值为构造函数。 当我们调用 new并执行了这个函数后，便会得到一个类的实例。 这个构造函数也包含了类的所有静态属性。 换个角度说，我们可以认为类具有 实例部分与 静态部分这两个部分。让我们稍微改写一下这个例子，看看它们之间的区别：

```ts
class Greeter {
    static standardGreeting: string = 'Hello, World';
    greeting: string;
    greet() {
        if (this.greeting) {
            return "Hello, "+this.greeting;
        } else {
            return Greeter.standardGreeting;
        }
    }
}

let greeter1: Greeter;
greeter1 = new Greeter();
console.log(greeter1.greet());

let greeterMaker: typeof Greeter = Greeter;
greeterMaker.standardGreeting = 'Hello, other';

let greeter2: Greeter = new greeterMaker();
console.log(greeter2.greet());
```

运行后得到的结果如下

```bash
$ npx ts-node src/classes_7.ts
Hello, World
Hello, other
```

这个例子里， greeter1与之前看到的一样。 我们实例化 Greeter类，并使用这个对象。 与我们之前看到的一样。

再之后，我们直接使用类。 我们创建了一个叫做 greeterMaker的变量。 这个变量保存了这个类或者说保存了类构造函数。 然后我们使用 typeof Greeter，意思是取Greeter类的类型，而不是实例的类型。 或者更确切的说，"告诉我 Greeter标识符的类型"，也就是构造函数的类型。 这个类型包含了类的所有静态成员和构造函数。 之后，就和前面一样，我们在 greeterMaker上使用 new，创建 Greeter的实例。

### **把类当做接口使用**

类定义会创建两个东西：类的实例类型和一个构造函数。 因为类可以创建出类型，所以你能够在允许使用接口的地方使用类。

```ts
class Point {
    x: number;
    y: number;
}

interface Point3D extends Point {
    z: number;
}

let point3d: Point3D = {
    x: 1,
    y: 2,
    z: 3,
}

console.log('point3d = ', point3d);
```

运行后得到的结果如下

```bash
$ npx ts-node src/classes_7.ts
point3d =  { x: 1, y: 2, z: 3 }
```

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.6
```
