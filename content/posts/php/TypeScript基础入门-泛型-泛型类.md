---
title: "TypeScript基础入门 - 泛型 - 泛型类"
date: "2025-07-09 09:59:15"
slug: "typescript-ji-chu-ru-men-fan-xing-fan-xing-lei"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门-泛型-泛型类/"
  - "/2025/07/09/TypeScript基础入门-泛型-泛型类.html"
  - "/TypeScript基础入门-泛型-泛型类/"
  - "/TypeScript基础入门-泛型-泛型类.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-fan-xing-lei/"
  - "/2025/07/09/typescript-ji-chu-ru-men-fan-xing-fan-xing-lei.html"
  - "/typescript-ji-chu-ru-men-fan-xing-fan-xing-lei.html"
---
*项目实践仓库*

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.3
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node 脚本路径
```

## 泛型

### 泛型类

泛型类看上去与泛型接口差不多。 泛型类使用（<>）括起泛型类型，跟在类名后面。

```ts
class GenerateT<T> {
    zeroValue: T;
    add: (x: T, y: T) => T;
}

let generateT1 = new GenerateT<number>();
generateT1.zeroValue = 1
generateT1.add = (x, y) => { return x + y; }
```

GenerateNumber类的使用是十分直观的，并且你可能已经注意到了，没有什么去限制它只能使用number类型。 也可以使用字符串或其它更复杂的类型。

```ts
class GenerateT<T> {
    zeroValue: T;
    add: (x: T, y: T) => T;
}

let generateT2 = new GenerateT<string>();
generateT2.zeroValue = "";
generateT2.add = (x, y) => { return x + y; }

console.log(generateT2.add(generateT2.zeroValue, "test"));
```

与接口一样，直接把泛型类型放在类后面，可以帮助我们确认类的所有属性都在使用相同的类型。

我们在类那节说过，类有两部分：静态部分和实例部分。 泛型类指的是实例部分的类型，所以类的静态属性不能使用这个泛型类型。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.3.4
```
