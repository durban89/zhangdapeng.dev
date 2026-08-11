---
title: "TypeScript基础入门 - 类 - 存取器"
date: "2025-07-08 16:01:18"
slug: "typescript-ji-chu-ru-men-lei-cun-qu-qi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-类-存取器/"
  - "/2025/07/08/TypeScript基础入门-类-存取器.html"
  - "/TypeScript基础入门-类-存取器/"
  - "/TypeScript基础入门-类-存取器.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-cun-qu-qi/"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-cun-qu-qi.html"
  - "/typescript-ji-chu-ru-men-lei-cun-qu-qi.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.2
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

### **存取器**

TypeScript支持通过getters/setters来截取对对象成员的访问。 它能帮助你有效的控制对对象成员的访问。下面来看如何把一个简单的类改写成使用 get和 set。 首先，我们从一个没有使用存取器的例子开始

```ts
class Employee {
    fullName: string    
}

let employee = new Employee();
employee.fullName = "durban zhang";

if (employee.fullName) {
    console.log(employee.fullName);
}
```

运行后结果如下

```bash
$ npx ts-node src/classes_4.ts
durban zhang
```

我们可以随意的设置 fullName，这是非常方便的，但是这也可能会带来麻烦。

下面这个版本里，我们先检查用户密码是否正确，然后再允许其修改员工信息。 我们把对 fullName的直接访问改成了可以检查密码的 set方法。 我们也加了一个 get方法，让上面的例子仍然可以工作。

```ts
let passcode = 'pass';
class Employee {
    private _fullName: string;

    get fullName(): string {
        return this._fullName;
    }

    set fullName(name: string) {
        if (passcode && passcode === 'pass') {
            this._fullName = name;
        } else {
            console.log('授权失败');
        }
    }
}

let employee = new Employee();
employee.fullName = "durban zhang";

if (employee.fullName) {
    console.log(employee.fullName);
}
```

运行后结果如下

```bash
$ npx ts-node src/classes_4.ts
durban zhang
```

可以修改一下密码，来验证一下存取器是否是工作的。当密码不对时，会提示我们没有权限去修改员工。

对于存取器有下面几点需要注意的：

首先，存取器要求你将编译器设置为输出ECMAScript 5或更高。 不支持降级到ECMAScript 3。 其次，只带有 get不带有 set的存取器自动被推断为 readonly。 这在从代码生成 .d.ts文件时是有帮助的，因为利用这个属性的用户会看到不允许够改变它的值。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.3
```
