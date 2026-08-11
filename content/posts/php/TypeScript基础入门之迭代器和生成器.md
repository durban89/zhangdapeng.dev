---
title: "TypeScript基础入门之迭代器和生成器"
date: "2025-07-09 10:43:01"
slug: "typescript-ji-chu-ru-men-zhi-die-dai-qi-he-sheng-cheng-qi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之迭代器和生成器/"
  - "/2025/07/09/TypeScript基础入门之迭代器和生成器.html"
  - "/TypeScript基础入门之迭代器和生成器/"
  - "/TypeScript基础入门之迭代器和生成器.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-die-dai-qi-he-sheng-cheng-qi/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-die-dai-qi-he-sheng-cheng-qi.html"
  - "/typescript-ji-chu-ru-men-zhi-die-dai-qi-he-sheng-cheng-qi.html"
---
## 迭代性

如果对象具有Symbol.iterator属性的实现，则该对象被视为可迭代。  
一些内置类型，如Array，Map，Set，String，Int32Array，Uint32Array等，已经实现了Symbol.iterator属性。  
对象上的Symbol.iterator函数负责返回值列表以进行迭代。

### for..of语句

`for..of`循环遍历可迭代对象，调用对象上的Symbol.iterator属性。下面是一个简单的for..of循环数组：

```ts
let someArray = [1, "string", false];

for (let entry of someArray) {
    console.log(entry); // 1, "string", false
}
```

### for..of vs. for..in语句

`for..of`和`for..in`语句都遍历列表;迭代的值是不同的，for..in返回正在迭代的对象上的键列表，而for..of返回正在迭代的对象的数值属性的值列表。下面展示一个对比的例子：

```ts
let list = [4, 5, 6];

for (let i in list) {
   console.log(i); // "0", "1", "2",
}

for (let i of list) {
   console.log(i); // "4", "5", "6"
}
```

另一个区别是`for..in`可以操作任何物体;它用作检查此对象的属性的方法。另一方面，`for..of`主要关注可迭代对象的值。Map和Set等内置对象实现了Symbol.iterator属性，允许访问存储的值。如下实例演示

```ts
let pets = new Set(["Cat", "Dog", "Hamster"]);
pets["species"] = "mammals";

for (let pet in pets) {
   console.log(pet); // "species"
}

for (let pet of pets) {
    console.log(pet); // "Cat", "Dog", "Hamster"
}
```

上面这段代码我在运行的时候是报错了的，不知道是不是官方哪里弄错了，也可能是需要做另外一些配置。如果您也遇到了跟我一样的错误，请留言指导

## 生成器

***目标为 ES5 和 ES3***

在针对ES5或ES3时，只允许在Array类型的值上使用迭代器。在非数组值上使用for循环是错误的，即使这些非数组值实现了Symbol.iterator属性也是如此。编译器将为`for..of`循环生成一个简单的for循环，例如：

```ts
let numbers = [1, 2, 3];
for (let num of numbers) {
    console.log(num);
}
```

编译后生成的代码如下

```ts
var numbers = [1, 2, 3];
for (var _i = 0; _i < numbers.length; _i++) {
    var num = numbers[_i];
    console.log(num);
}
```

在针对ECMAScipt 2015兼容引擎时，编译器将生成for..of循环以定位引擎中的内置迭代器实现。
