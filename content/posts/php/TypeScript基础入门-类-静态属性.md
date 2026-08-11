---
title: "TypeScript基础入门 - 类 - 静态属性"
date: "2025-07-08 16:01:21"
slug: "typescript-ji-chu-ru-men-lei-jing-tai-shu-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-类-静态属性/"
  - "/2025/07/08/TypeScript基础入门-类-静态属性.html"
  - "/TypeScript基础入门-类-静态属性/"
  - "/TypeScript基础入门-类-静态属性.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-jing-tai-shu-xing/"
  - "/2025/07/08/typescript-ji-chu-ru-men-lei-jing-tai-shu-xing.html"
  - "/typescript-ji-chu-ru-men-lei-jing-tai-shu-xing.html"
---
### ***项目实践仓库***

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.3
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

### **静态属性**

到目前为止，只学习了类的实例成员，那些仅当类被实例化的时候才会被初始化的属性。 我们也可以创建类的静态成员，这些属性存在于类本身上面而不是类的实例上。 在这个例子里，我们使用 static定义 origin，因为它是所有网格都会用到的属性。 每个实例想要访问这个属性的时候，都要在 origin前面加上类名。 如同在实例属性上使用 this.前缀来访问属性一样，这里我们使用 Grid.来访问静态属性。

```ts
class Grid {
    constructor(public scale: number) { }

    static origin = {
        x:0,
        y:0,
    }

    calculateDistanceFromOrigin(point: {x: number, y: number}) {
        let xDist = point.x - Grid.origin.x;
        let yDist = point.y - Grid.origin.y;

        return Math.sqrt(xDist * xDist + yDist * yDist) / this.scale;
    }
}

let grid1 = new Grid(1.0)
let grid2 = new Grid(2.0)

console.log(grid1.calculateDistanceFromOrigin({x: 10, y: 10}));
console.log(grid2.calculateDistanceFromOrigin({ x: 10, y: 10 }));
```

运行后结果如下

```bash
14.142135623730951
7.0710678118654755
```

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.1.4
```
