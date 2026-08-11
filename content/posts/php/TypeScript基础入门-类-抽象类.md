---
title: "TypeScript基础入门 - 类 - 抽象类"
date: "2025-07-08 16:01:24"
slug: "typescript-ji-chu-ru-men-lei-chou-xiang-lei"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-类-抽象类/"
  - "/2025/07/08/TypeScript基础入门-类-抽象类.html"
  - "/TypeScript基础入门-类-抽象类/"
  - "/TypeScript基础入门-类-抽象类.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-chou-xiang-lei/"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-chou-xiang-lei.html"
  - "/typescript-ji-chu-ru-men-lei-chou-xiang-lei.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.4
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

### **抽象类**

抽象类做为其它派生类的基类使用。 它们一般不会直接被实例化。 不同于接口，抽象类可以包含成员的实现细节。 abstract关键字是用于定义抽象类和在抽象类内部定义抽象方法。具体例子如下

```ts
abstract class Animal {
    abstract makeSount(): void;    move(): void {
        console.log('我在移动');
    }
}
```

抽象类中的抽象方法不包含具体实现并且必须在派生类中实现。 抽象方法的语法与接口方法相似。 两者都是定义方法签名但不包含方法体。 然而，抽象方法必须包含 abstract关键字并且可以包含访问修饰符。具体示例如下

```ts
abstract class Department {
    constructor(public name: string) {

    }

    printName(): void {
        console.log("部门名称:" + this.name);
    }

    abstract printMeeting(): void; // 必须在派生类中实现   
}

class AccountingDepartment extends Department {
    constructor() {
        super("会计和审计"); // 在派生类中必须调用super()
    }

    printMeeting(): void {
        console.log('会计部每个星期一上午10点开会');
    }

    generateReports(): void {
        console.log('生成会议报告');
    }
}

let department: Department; // 允许创建一个对抽象类型的引用

// department = new Department(); // 不能创建一个抽象类的实例
department = new AccountingDepartment(); //  允许对一个抽象子类进行实例化和赋值
department.printName();
department.printMeeting();
// department.generateReports(); //  此方法不能调用，因为在声明的抽象类中不存在
```

运行后的结果如下

```bash
$ npx ts-node src/classes_6.ts
部门名称:会计和审计
会计部每个星期一上午10点开会
```

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.5
```
