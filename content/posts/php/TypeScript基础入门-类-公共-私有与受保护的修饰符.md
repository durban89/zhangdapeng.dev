---
title: "TypeScript基础入门 - 类 - 公共、私有与受保护的修饰符"
date: "2025-07-08 16:01:12"
slug: "typescript-ji-chu-ru-men-lei-gong-gong-si-you-yu-shou-bao-hu-de-xiu-shi-fu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-类-公共、私有与受保护的修饰符/"
  - "/2025/07/08/TypeScript基础入门-类-公共、私有与受保护的修饰符.html"
  - "/TypeScript基础入门-类-公共、私有与受保护的修饰符/"
  - "/TypeScript基础入门-类-公共、私有与受保护的修饰符.html"
  - "/2025/07/08/TypeScript基础入门-类-公共-私有与受保护的修饰符/"
  - "/2025/07/08/TypeScript基础入门-类-公共-私有与受保护的修饰符.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-gong-gong-si-you-yu-shou-bao-hu-de-xiu-shi-fu/"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-gong-gong-si-you-yu-shou-bao-hu-de-xiu-shi-fu.html"
  - "/typescript-ji-chu-ru-men-lei-gong-gong-si-you-yu-shou-bao-hu-de-xiu-shi-fu.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.1
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

### **公共，私有与受保护的修饰符**

### **默认为 public**

在上篇文章【[TypeScript基础入门 - 类 - 继承](https://www.gowhich.com/blog/884)】的例子里，我们可以自由的访问程序里定义的成员。 如果你对其它语言中的类比较了解，就会注意到我们在之前的代码里并没有使用 public来做修饰；例如，C#要求必须明确地使用 public指定成员是可见的。 在TypeScript里，成员都默认为public。你也可以明确的将一个成员标记成public。 我们可以用下面的方式来实现一个Animal类：

```ts
class Animal {
    public name: string;
    public constructor(theColor: string) {
        this.name = theColor;
    }

    public move(distanceMeter: number = 0) {
        console.log(`${this.name} moved ${distanceMeter}m`);
    }
}
```

### **理解 private**

当成员被标记成 private时，它就不能在声明它的类的外部访问。比如：

```ts
class Animal {
    private name: string;
    public constructor(theName: string) {
        this.name = theName;
    }

    public move(distanceMeter: number = 0) {
        console.log(`${this.name} moved ${distanceMeter}m`);
    }
}

new Animal('small cat').name;
```

运行后得到如下结果

```bash
$ npx ts-node src/classes_3.ts
⨯ Unable to compile TypeScript:
src/classes_3.ts(12,25): error TS2341: Property 'name' is private and only accessible within class 'Animal'.
```

TypeScript使用的是结构性类型系统。 当我们比较两种不同的类型时，并不在乎它们从何处而来，如果所有成员的类型都是兼容的，我们就认为它们的类型是兼容的。

然而，当我们比较带有 private或 protected成员的类型的时候，情况就不同了。 如果其中一个类型里包含一个 private成员，那么只有当另外一个类型中也存在这样一个 private成员， 并且它们都是来自同一处声明时，我们才认为这两个类型是兼容的。 对于 protected成员也使用这个规则。下面来看一个例子，更好地说明了这一点：

```ts
class Animal {
    private name: string;
    public constructor(theName: string) {
        this.name = theName;
    }

    public move(distanceMeter: number = 0) {
        console.log(`${this.name} moved ${distanceMeter}m`);
    }
}

class Dog extends Animal {
    constructor(name: string) {
        super(name);
    }
}

class Person {
    private name: string;

    public constructor(theName: string) {
        this.name = theName;
    }

    public move(distanceMeter: number = 0) {
        console.log(`${this.name} moved ${distanceMeter}m`);
    }
}

let animal = new Animal('animal');
let dog = new Dog('dog');
let person = new Person('person');

animal = dog
animal = person;
```

运行后得到如下结果

```bash
$ npx ts-node src/classes_3.ts
⨯ Unable to compile TypeScript:
src/classes_3.ts(35,1): error TS2322: Type 'Person' is not assignable to type 'Animal'.
  Types have separate declarations of a private property 'name'.
```

这个例子中有Animal和Dog两个类， Dog是 Animal类的子类。还有一个Person类，其类型看上去与Animal是相同的。 我们创建了几个这些类的实例，并相互赋值来看看会发生什么。因为Animal和Dog共享了来自Animal里的私有成员定义private name: string，因此它们是兼容的。 然而 Person却不是这样。当把Person赋值给Animal的时候，得到一个错误，说它们的类型不兼容。尽管Person里也有一个私有成员name，但它明显不是Animal里面定义的那个。

### **理解 protected**

protected修饰符与 private修饰符的行为很相似，但有一点不同， protected成员在派生类中仍然可以访问。例如：

```ts
class Person {
    protected name: string;
    constructor(name: string) {
        this.name = name;
    }
}

class Employee extends Person {
    private department: string;

    constructor(name: string, department: string) {
        super(name);
        this.department = department;
    }

    getWorkInfo() {
        return `我叫${this.name}，我工作在${this.department}`;
    }
}

let aEmployee = new Employee('durban', '华盛顿');
console.log(aEmployee.getWorkInfo());
console.log(aEmployee.name);
```

运行后得到的结果如下

```bash
$ npx ts-node src/classes_3.ts
⨯ Unable to compile TypeScript:
src/classes_3.ts(23,23): error TS2445: Property 'name' is protected and only accessible within class 'Person' and its subclasses.
```

注意，我们不能在 Person类外使用 name，但是我们仍然可以通过 Employee类的实例方法访问，因为 Employee是由 Person派生而来的。构造函数也可以被标记成 protected。 这意味着这个类不能在包含它的类外被实例化，但是能被继承。比如:

```ts
class Person {
    protected name: string;
    protected constructor(name: string) {
        this.name = name;
    }
}

class Employee extends Person {
    private department: string;

    constructor(name: string, department: string) {
        super(name);
        this.department = department;
    }

    getWorkInfo() {
        return `我叫${this.name}，我工作在${this.department}`;
    }
}

let aEmployee = new Employee('durban', '华盛顿');
let aPerson = new Person('Sakuro');
```

运行后得到如下错误

```bash
$ npx ts-node src/classes_3.ts
⨯ Unable to compile TypeScript:
src/classes_3.ts(22,15): error TS2674: Constructor of class 'Person' is protected and only accessible within the class declaration.
```

### **readonly修饰符**

你可以使用 readonly关键字将属性设置为只读的。 只读属性必须在声明时或构造函数里被初始化。如下:

```ts
class Person {
    readonly name: string;
    constructor(name: string) {
        this.name = name;
    }
}

const aPerson = new Person('Xiaowang');
aPerson.name = 'Xiaoli';
```

运行后得到如下

```bash
$ npx ts-node src/classes_3.ts
⨯ Unable to compile TypeScript:
src/classes_3.ts(9,9): error TS2540: Cannot assign to 'name' because it is a constant or a read-only property.
```

### **参数属性**

在上面的例子中，我们不得不定义一个受保护的成员 name和一个构造函数参数 theName在 Person类里，并且立刻给 name和 theName赋值。 这种情况经常会遇到。 参数属性可以方便地让我们在一个地方定义并初始化一个成员。 下面的例子是对之前 Animal类的修改版，使用了参数属性：

```ts
class Animal {
    public constructor(private name: string) { }

    public move(distanceMeter: number = 0) {
        console.log(`${this.name} moved ${distanceMeter}m`);
    }
}
```

注意看我们是如何舍弃了 theName，仅在构造函数里使用 private name: string参数来创建和初始化 name成员。 我们把声明和赋值合并至一处。

参数属性通过给构造函数参数添加一个访问限定符来声明。 使用 private限定一个参数属性会声明并初始化一个私有成员；对于 public和 protected来说也是一样。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.2
```
