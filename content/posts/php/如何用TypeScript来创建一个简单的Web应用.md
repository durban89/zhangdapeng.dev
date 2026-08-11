---
title: "如何用TypeScript来创建一个简单的Web应用"
date: "2025-07-08 15:16:00"
slug: "ru-he-yong-typescript-lai-chuang-jian-yi-ge-jian-dan-de-web-ying-yong"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/如何用TypeScript来创建一个简单的Web应用/"
  - "/2025/07/08/如何用TypeScript来创建一个简单的Web应用.html"
  - "/如何用TypeScript来创建一个简单的Web应用/"
  - "/如何用TypeScript来创建一个简单的Web应用.html"
  - "/2025/07/08/ru-he-yong-typescript-lai-chuang-jian-yi-ge-jian-dan-de-web-ying-yong/"
  - "/2025/07/08/ru-he-yong-typescript-lai-chuang-jian-yi-ge-jian-dan-de-web-ying-yong.html"
  - "/ru-he-yong-typescript-lai-chuang-jian-yi-ge-jian-dan-de-web-ying-yong.html"
---
### **安装TypeScript**

获取TypeScript工具的方式：  
   
通过npm（Node.js包管理器）

```bash
npm install -g typescript
```

### **构建你的第一个TypeScript文件**

创建项目文件夹

```bash
mkdir typescript_demo && cd typescript_demo
```

创建文件greeter.ts

```ts
touch greeter.ts
```

将下面的代码写入greeter.ts中

```ts
function greeter(person) {
    return "Hello, " + person;
}

let user = "Durban Zhang";

document.body.innerHTML = greeter(user);
```

### **编译代码**

这里使用.ts扩展名，但是这段代码仅仅是JavaScript而已。 你可以直接从现有的JavaScript应用里复制/粘贴这段代码。

在命令行上，运行TypeScript编译器：

```bash
tsc greeter.ts
```

输出结果为一个greeter.js文件，它包含了和输入文件中相同的JavsScript代码。 一切准备就绪，我们可以运行这个使用TypeScript写的JavaScript应用了！接下来让我们看看TypeScript工具带来的高级功能。 给 person函数的参数添加: string类型注解，如下：

```ts
function greeter(person:string) {
    return "Hello, " + person;
}

let user = "Durban Zhang";

document.body.innerHTML = greeter(user);
```

### **类型注解**

TypeScript里的类型注解是一种轻量级的为函数或变量添加约束的方式。 在这个例子里，我们希望 greeter函数接收一个字符串参数。 然后尝试把 greeter的调用改成传入一个数组：

```ts
function greeter(person:string) {
    return "Hello, " + person;
}

let user = "Durban Zhang";

document.body.innerHTML = greeter(user);
```

重新编译，你会看到如下产生 的一个错误。

```bash
greeter.ts:7:35 - error TS2345: Argument of type 'number[]' is not assignable to parameter of type 'string'.

7 document.body.innerHTML = greeter(user);
```

类似地，尝试删除greeter调用的所有参数。 TypeScript会告诉你使用了非期望个数的参数调用了这个函数。 在这两种情况中，TypeScript提供了静态的代码分析，它可以分析代码结构和提供的类型注解。

要注意的是尽管有错误，greeter.js文件还是被创建了。 就算你的代码里有错误，你仍然可以使用TypeScript。但在这种情况下，TypeScript会警告你代码可能不会按预期执行。

### **接口**

这里我们使用接口来描述一个拥有firstName和lastName字段的对象。 在TypeScript里，只在两个类型内部的结构兼容那么这两个类型就是兼容的。 这就允许我们在实现接口时候只要保证包含了接口要求的结构就可以，而不必明确地使用 implements语句。

```ts
interface Person {
    firstName: string;
    lastName: string;
}

function greeter(person: Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}

let user = { firstName: "Durban", lastName: "Zhang" };

document.body.innerHTML = greeter(user);
```

### **类**

最后，让我们使用类来改写这个例子。 TypeScript支持JavaScript的新特性，比如支持基于类的面向对象编程。

让我们创建一个Student类，它带有一个构造函数和一些公共字段。 注意类和接口可以一起共作，程序员可以自行决定抽象的级别。还要注意的是，在构造函数的参数上使用public等同于创建了同名的成员变量。

```ts
class Student {
    fullName:string;
    constructor (
        public firstName: string,
        public middleName: string,
        public lastName: string) {
        this.fullName = firstName + " " + middleName + " " + lastName;

    }

}

interface Person {
    firstName: string;
    lastName: string;
}

function greeter(person: Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}

let user = new Student("Durban", "M.", "Zhang");
document.body.innerHTML = greeter(user);
```

重新运行tsc greeter.ts，你会看到生成的JavaScript代码和原先的一样。 TypeScript里的类只是JavaScript里常用的基于原型面向对象编程的简写。

### **运行TypeScript Web应用**

创建greeter.html并在里面输入如下内容：

```html
<!DOCTYPE html>
<html>
    <head><title>TypeScript Greeter</title></head>
    <body>
        <script src="greeter.js"></script>
    </body>
</html>
```

### **实践项目地址**

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.0
```
