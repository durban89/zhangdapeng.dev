---
title: "TypeScript基础入门 - 变量声明(一)"
date: "2025-07-08 15:16:35"
slug: "typescript-ji-chu-ru-men-bian-liang-sheng-ming-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-变量声明(一)/"
  - "/2025/07/08/TypeScript基础入门-变量声明(一).html"
  - "/TypeScript基础入门-变量声明(一)/"
  - "/TypeScript基础入门-变量声明(一).html"
  - "/2025/07/08/TypeScript基础入门-变量声明-一/"
  - "/2025/07/08/TypeScript基础入门-变量声明-一.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-bian-liang-sheng-ming-yi/"
  - "/2025/07/08/typescript-ji-chu-ru-men-bian-liang-sheng-ming-yi.html"
  - "/typescript-ji-chu-ru-men-bian-liang-sheng-ming-yi.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.3
```

为了保证后面的学习演示需要安装下ts-node，这样后面的每个操作都能直接运行看到输出的结果。

```bash
npm install -D ts-node
```

后面自己在练习的时候可以这样使用

```bash
npx ts-node src/learn_basic_types.ts
```

```bash
npx ts-node 脚本路径
```

### **变量声明**

let和const是JavaScript里相对较新的变量声明方式。 像我们之前提到过的， let在很多方面与var是相似的，但是可以帮助大家避免在JavaScript里常见一些问题。 const是对let的一个增强，它能阻止对一个变量再次赋值。

因为TypeScript是JavaScript的超集，所以它本身就支持let和const。 下面我们会详细说明这些新的声明方式以及为什么推荐使用它们来代替 var。

如果你之前使用JavaScript时没有特别在意，那么这节内容会唤起你的回忆。 如果你已经对 var声明的怪异之处了如指掌，那么可以了解加深下记忆。

### **var 声明**

一直以来我们都是通过var关键字定义JavaScript变量。

```ts
var a = 10;
```

大家都能理解，这里定义了一个名为a值为10的变量。我们也可以在函数内部定义变量：

```ts
function f() {
    var message = "Hello, world!";

    return message;
}
```

并且我们也可以在其它函数内部访问相同的变量。

```ts
function f() {
    var a = 10;
    return function g() {
        var b = a + 1;
        return b;
    }
}

var g = f();
console.log(g());
```

运行后得到的结果如下

```bash
11
```

上面的例子里，g可以获取到f函数里定义的a变量。 每当 g被调用时，它都可以访问到f里的a变量。 即使当 g在f已经执行完后才被调用，它仍然可以访问及修改a。

```ts
function f() {
    var a = 1;

    a = 2;
    var b = g();
    a = 3;

    return b;

    function g() {
        return a;
    }
}

console.log(f());
```

运行后得到的结果如下

```bash
2
```

### **作用域规则**

对于熟悉其它语言的人来说，var声明有些奇怪的作用域规则。 看下面的例子：

```ts
function f(shouldInitialize: boolean) {
    if (shouldInitialize) {
        var x = 10;
    }

    return x;
}

console.log(f(true));
console.log(f(false));
```

运行后得到的结果如下

```bash
10
undefined
```

有些读者可能要多看几遍这个例子。 变量 x是定义在\*if语句里面\*，但是我们却可以在语句的外面访问它。 这是因为 var声明可以在包含它的函数，模块，命名空间或全局作用域内部任何位置被访问，包含它的代码块对此没有什么影响。 有些人称此为 \*var作用域或函数作用域\*。 函数参数也使用函数作用域。这些作用域规则可能会引发一些错误。 其中之一就是，多次声明同一个变量并不会报错：

```ts
function sumMatrix(matrix: number[][]) {
    var sum = 0;
    for (var i = 0; i < matrix.length; i++) {
        var currentRow = matrix[i];
        for (var i = 0; i < currentRow.length; i++) {
            sum += currentRow[i];
        }
    }

    return sum;
}
```

这里很容易看出一些问题，里层的for循环会覆盖变量i，因为所有i都引用相同的函数作用域内的变量。 有经验的开发者们很清楚，这些问题可能在代码审查时漏掉，引发无穷的麻烦。

### **捕获变量怪异之处**

下面的代码会返回什么：

```ts
for (var i = 0; i < 10; i++) {
    setTimeout(function() { console.log(i); }, 100 * i);
}
```

介绍一下，setTimeout会在若干毫秒的延时后执行一个函数（等待其它代码执行完毕）。

好吧，看一下结果：

```bash
10
10
10
10
10
10
10
10
10
10
```

很多JavaScript程序员对这种行为已经很熟悉了。 大多数人期望输出结果是这样：

```bash
0
1
2
3
4
5
6
7
8
9
```

还记得我们上面提到的捕获变量吗？

我们传给setTimeout的每一个函数表达式实际上都引用了相同作用域里的同一个i。

让我们花点时间思考一下这是为什么。 setTimeout在若干毫秒后执行一个函数，并且是在for循环结束后。 for循环结束后，i的值为10。 所以当函数被调用的时候，它会打印出 10！

一个通常的解决方法是使用立即执行的函数表达式（IIFE）来捕获每次迭代时i的值：

```ts
for (var i = 0; i < 10; i++) {
    (function (i) {
        setTimeout(function () { console.log(i); }, 100 * i);
    })(i);
}
```

运行后的结果如下

```bash
0
1
2
3
4
5
6
7
8
9
```

这种奇怪的形式我们已经司空见惯了。 参数 i会覆盖for循环里的i，但是因为我们起了同样的名字，所以我们不用怎么改for循环体里的代码。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.4
```
