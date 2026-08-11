---
title: "TypeScript基础入门 - 变量声明(二)"
date: "2025-07-08 15:16:48"
slug: "typescript-ji-chu-ru-men-bian-liang-sheng-ming-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-变量声明(二)/"
  - "/2025/07/08/TypeScript基础入门-变量声明(二).html"
  - "/TypeScript基础入门-变量声明(二)/"
  - "/TypeScript基础入门-变量声明(二).html"
  - "/2025/07/08/TypeScript基础入门-变量声明-二/"
  - "/2025/07/08/TypeScript基础入门-变量声明-二.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-bian-liang-sheng-ming-er/"
  - "/2025/07/08/typescript-ji-chu-ru-men-bian-liang-sheng-ming-er.html"
  - "/typescript-ji-chu-ru-men-bian-liang-sheng-ming-er.html"
---
*项目实践仓库*

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.4
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

## **变量声明**

### **let 声明**

现在你已经知道了var存在一些问题，这恰好说明了为什么用let语句来声明变量。 除了名字不同外， let与var的写法一致。

主要的区别不在语法上，而是语义，我们接下来会深入研究。

### **块作用域**

当用let声明一个变量，它使用的是词法作用域或块作用域。 不同于使用 var声明的变量那样可以在包含它们的函数外访问，块作用域变量在包含它们的块或for循环之外是不能访问的。

```ts
function f(input: boolean) {
    let a = 100;

    if (input) {
        // Still okay to reference 'a'
        let b = a + 1;
        return b;
    }

    // Error: 'b' doesn't exist here
    return b;
}
console.log(f3(true));
console.log(f3(false));
```

运行后结果类似如下

```bash
101
/Users/durban/nodejs/typescript_demo/dist/variable_declarations.js:58
    return b;
    ^

ReferenceError: b is not defined
    at f3 (/Users/durban/nodejs/typescript_demo/dist/variable_declarations.js:58:5)
    at Object.<anonymous> (/Users/durban/nodejs/typescript_demo/dist/variable_declarations.js:61:13)
    at Module._compile (module.js:652:30)
    at Object.Module._extensions..js (module.js:663:10)
    at Module.load (module.js:565:32)
    at tryModuleLoad (module.js:505:12)
    at Function.Module._load (module.js:497:3)
    at Function.Module.runMain (module.js:693:10)
    at startup (bootstrap_node.js:191:16)
    at bootstrap_node.js:612:3
```

这里我们定义了2个变量a和b。 a的作用域是f函数体内，而b的作用域是if语句块里。

在catch语句里声明的变量也具有同样的作用域规则。

```ts
try {
    throw "oh no!";
}
catch (e) {
    console.log("Oh well.");
}

// Error: 'e' doesn't exist here
console.log(e);
```

运行后结果如下

```bash
Oh well.
/Users/durban/nodejs/typescript_demo/dist/variable_declarations.js:69
console.log(e);
            ^

ReferenceError: e is not defined
    at Object.<anonymous> (/Users/durban/nodejs/typescript_demo/dist/variable_declarations.js:69:13)
    at Module._compile (module.js:652:30)
    at Object.Module._extensions..js (module.js:663:10)
    at Module.load (module.js:565:32)
    at tryModuleLoad (module.js:505:12)
    at Function.Module._load (module.js:497:3)
    at Function.Module.runMain (module.js:693:10)
    at startup (bootstrap_node.js:191:16)
    at bootstrap_node.js:612:3
```

拥有块级作用域的变量的另一个特点是，它们不能在被声明之前读或写。 虽然这些变量始终“存在”于它们的作用域里，但在直到声明它的代码之前的区域都属于 暂时性死区。 它只是用来说明我们不能在 let语句之前访问它们，幸运的是TypeScript可以告诉我们这些信息。

```ts
a++; // illegal to use 'a' before it's declared;
let a;
```

注意一点，我们仍然可以在一个拥有块作用域变量被声明前获取它。 只是我们不能在变量声明前去调用那个函数。 如果生成代码目标为ES2015，现代的运行时会抛出一个错误；然而，现今TypeScript是不会报错的。

```ts
function foo() {
    // okay to capture 'a'
    return a;
}

// 不能在'a'被声明前调用'foo'
// 运行时应该抛出错误
foo();

let a;
```

关于暂时性死区的更多信息，查看这里[Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let#Temporal_dead_zone_and_errors_with_let).

### **重定义及屏蔽**

我们提过使用var声明时，它不在乎你声明多少次；你只会得到1个。示例如下

```ts
function f(x) {
    var x;
    var x;

    if (true) {
        var x;
    }
}
```

在上面的例子里，所有x的声明实际上都引用一个相同的x，并且这是完全有效的代码。 这经常会成为bug的来源。 好的是， let声明就不会这么宽松了。示例如下

```ts
let x = 10;
let x = 20; // 错误，不能在1个作用域里多次声明`x`
```

并不是要求两个均是块级作用域的声明TypeScript才会给出一个错误的警告。

```ts
function f(x) {
    let x = 100; // error: interferes with parameter declaration
}

function g() {
    let x = 100;
    var x = 100; // error: can't have both declarations of 'x'
}
```

并不是说块级作用域变量不能用函数作用域变量来声明。 而是块级作用域变量需要在明显不同的块里声明。

```ts
function f(condition, x) {
    if (condition) {
        let x = 100;
        return x;
    }

    return x;
}

console.log("========f4=========\n");
console.log(f4(false, 0)); // returns 0
console.log(f4(true, 0));  // returns 100
```

运行后输出如下结果

```bash
========f4=========

0
100
```

在一个嵌套作用域里引入一个新名字的行为称做屏蔽。 它是一把双刃剑，它可能会不小心地引入新问题，同时也可能会解决一些错误。 例如，假设我们现在用 let重写之前的sumMatrix函数。

```ts
function sumMatrix2(matrix: number[][]) {
    let sum = 0;
    for (let i = 0; i < matrix.length; i++) {
        var currentRow = matrix[i];
        for (let i = 0; i < currentRow.length; i++) {
            sum += currentRow[i];
        }
    }

    return sum;
}

console.log("========== sumMatrix2 \n");
console.log(sumMatrix2([[1],[2]]))
```

运行后输出如下结果

```bash
========== sumMatrix2

3
```

这个版本的循环能得到正确的结果，因为内层循环的i可以屏蔽掉外层循环的i。

通常来讲应该避免使用屏蔽，因为我们需要写出清晰的代码。 同时也有些场景适合利用它，你需要好好打算一下。

### **块级作用域变量的获取**

在我们最初谈及获取用var声明的变量时，我们简略地探究了一下在获取到了变量之后它的行为是怎样的。 直观地讲，每次进入一个作用域时，它创建了一个变量的 环境。 就算作用域内代码已经执行完毕，这个环境与其捕获的变量依然存在。

```ts
function theCityThatAlwaysSleeps() {
    let getCity;

    if (true) {
        let city = "Seattle";
        getCity = function () {
            return city;
        }
    }

    return getCity();
}
console.log('====== theCityThatAlwaysSleeps ======');
console.log(theCityThatAlwaysSleeps());
```

运行后得到的结果如下

```bash
====== theCityThatAlwaysSleeps ======
Seattle
```

因为我们已经在city的环境里获取到了city，所以就算if语句执行结束后我们仍然可以访问它。

回想一下前面setTimeout的例子，我们最后需要使用立即执行的函数表达式来获取每次for循环迭代里的状态。 实际上，我们做的是为获取到的变量创建了一个新的变量环境。 这样做挺痛苦的，但是幸运的是，你不必在TypeScript里这样做了。

当let声明出现在循环体里时拥有完全不同的行为。 不仅是在循环里引入了一个新的变量环境，而是针对 每次迭代都会创建这样一个新作用域。 这就是我们在使用立即执行的函数表达式时做的事，所以在 setTimeout例子里我们仅使用let声明就可以了。

```ts
for (let i = 0; i < 10 ; i++) {
    setTimeout(function() {console.log(i); }, 100 * i);
}
```

会输出与预料一致的结果：

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

### **const 声明**

const 声明是声明变量的另一种方式。

```ts
const numLivesForCat = 9;
```

它们与let声明相似，但是就像它的名字所表达的，它们被赋值后不能再改变。 换句话说，它们拥有与 let相同的作用域规则，但是不能对它们重新赋值。这很好理解，它们引用的值是不可变的。

```ts
const numLivesForCat = 9;
const kitty = {
    name: "Aurora",
    numLives: numLivesForCat,
}

// Error
// kitty = {
//     name: "Danielle",
//     numLives: numLivesForCat
// };

// all "okay"
kitty.name = "Rory";
kitty.name = "Kitty";
kitty.name = "Cat";
kitty.numLives--;
```

除非你使用特殊的方法去避免，实际上const变量的内部状态是可修改的。 幸运的是，TypeScript允许你将对象的成员设置成只读的。

### **let vs. const**

现在我们有两种作用域相似的声明方式，我们自然会问到底应该使用哪个。 与大多数泛泛的问题一样，答案是：依情况而定。

使用最小特权原则，所有变量除了你计划去修改的都应该使用const。 基本原则就是如果一个变量不需要对它写入，那么其它使用这些代码的人也不能够写入它们，并且要思考为什么会需要对这些变量重新赋值。 使用 const也可以让我们更容易的推测数据的流动。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.5
```
