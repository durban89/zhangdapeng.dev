---
title: "TypeScript基础入门 - 类型兼容性 - 比较两个函数"
date: "2025-07-09 10:00:07"
slug: "typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-bi-jiao-liang-ge-han-shu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-类型兼容性-比较两个函数/"
  - "/2025/07/09/TypeScript基础入门-类型兼容性-比较两个函数.html"
  - "/TypeScript基础入门-类型兼容性-比较两个函数/"
  - "/TypeScript基础入门-类型兼容性-比较两个函数.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-bi-jiao-liang-ge-han-shu/"
  - "/2025/07/09/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-bi-jiao-liang-ge-han-shu.html"
  - "/typescript-ji-chu-ru-men-lei-xing-jian-rong-xing-bi-jiao-liang-ge-han-shu.html"
---
***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.9
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## 比较两个函数

相对来讲，在比较原始类型和对象类型的时候是比较容易理解的，问题是如何判断两个函数是兼容的。 下面我们从两个简单的函数入手，它们仅是参数列表略有不同：

```ts
let x = (a: number) => 0;
let y = (b: number, s: string) => 0;

y = x; // OK
x = y; // Error
```

要查看x是否能赋值给y，首先看它们的参数列表。 x的每个参数必须能在y里找到对应类型的参数。 注意的是参数的名字相同与否无所谓，只看它们的类型。 这里，x的每个参数在y中都能找到对应的参数，所以允许赋值。

第二个赋值错误，因为y有个必需的第二个参数，但是x并没有，所以不允许赋值。你可能会疑惑为什么允许忽略参数，像例子y = x中那样。 原因是忽略额外的参数在JavaScript里是很常见的。 例如， Array#forEach给回调函数传3个参数：数组元素，索引和整个数组。 尽管如此，传入一个只使用第一个参数的回调函数也是很有用的：

```ts
let items = [1, 2, 3];

// Don't force these extra arguments
items.forEach((item, index, array) => console.log(item));

// Should be OK!
items.forEach((item) => console.log(item));
```

下面来看看如何处理返回值类型，创建两个仅是返回值类型不同的函数：

```ts
let x = () => ({name: 'Alice'});
let y = () => ({name: 'Alice', location: 'Seattle'});

x = y; // OK
y = x; // Error 因为x()缺少一个location属性
```

类型系统强制源函数的返回值类型必须是目标函数返回值类型的子类型。

### 函数参数双向协变

当比较函数参数类型时，只有当源函数参数能够赋值给目标函数或者反过来时才能赋值成功。 这是不稳定的，因为调用者可能传入了一个具有更精确类型信息的函数，但是调用这个传入的函数的时候却使用了不是那么精确的类型信息。 实际上，这极少会发生错误，并且能够实现很多JavaScript里的常见模式。例如：

```ts
enum EventType {
    Mouse,
    Keyboard,
};

interface Event {
    timestamp: number;
}

interface MouseEvent extends Event {
    eventX: number;
    eventY: number;
}

interface KeyEvent extends Event {
    keyCode: number;
}

function listenEvent(eventType: EventType, handler: (n:Event) => void) {
    // other
}

listenEvent(EventType.Mouse, (e: MouseEvent)=>console.log(e.eventX+', '+e.eventY));

// 报类型异常
listenEvent(EventType.Mouse, (e: Event) => console.log(<MouseEvent>e.eventX + ', ' + <MouseEvent>e.eventY));

listenEvent(EventType.Mouse, <(e: Event) => void>((e: MouseEvent) => console.log(e.eventX + ', ' + e.eventY)))

// 报类型异常
listenEvent(EventType.Mouse, (e: number) => console.log(e))
```

运行后，详细的报错信息类似如下

```bash
$ npx ts-node src/type_compatibility_1.ts
⨯ Unable to compile TypeScript:
src/type_compatibility_1.ts(40,70): error TS2339: Property 'eventX' does not exist on type 'Event'.
src/type_compatibility_1.ts(40,100): error TS2339: Property 'eventY' does not exist on type 'Event'.
src/type_compatibility_1.ts(44,30): error TS2345: Argument of type '(e: number) => void' is not assignable to parameter of type '(n: Event) => void'.
  Types of parameters 'e' and 'n' are incompatible.
    Type 'Event' is not assignable to type 'number'.
```

### 可选参数及剩余参数

比较函数兼容性的时候，可选参数与必须参数是可互换的。 源类型上有额外的可选参数不是错误，目标类型的可选参数在源类型里没有对应的参数也不是错误。

当一个函数有剩余参数时，它被当做无限个可选参数。

这对于类型系统来说是不稳定的，但从运行时的角度来看，可选参数一般来说是不强制的，因为对于大多数函数来说相当于传递了一些undefinded。有一个好的例子，常见的函数接收一个回调函数并用对于程序员来说是可预知的参数但对类型系统来说是不确定的参数来调用，如下：

```ts
function invokeLater(args: any[], callback: (...args: any[]) => void) {
    // other
}

invokeLater([1, 2], (x, y) => console.log(x + ', ' + y));

invokeLater([1, 2], (x?, y?) => console.log(x + ', ' + y));
```

## 函数重载

对于有重载的函数，源函数的每个重载都要在目标函数上找到对应的函数签名。 这确保了目标函数可以在所有源函数可调用的地方调用。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.4.0
```
