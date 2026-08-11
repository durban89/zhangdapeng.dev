---
title: "TypeScript基础入门 - 变量声明(三)"
date: "2025-07-08 15:16:51"
slug: "typescript-ji-chu-ru-men-bian-liang-sheng-ming-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-变量声明(三)/"
  - "/2025/07/08/TypeScript基础入门-变量声明(三).html"
  - "/TypeScript基础入门-变量声明(三)/"
  - "/TypeScript基础入门-变量声明(三).html"
  - "/2025/07/08/TypeScript基础入门-变量声明-三/"
  - "/2025/07/08/TypeScript基础入门-变量声明-三.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-bian-liang-sheng-ming-san/"
  - "/2025/07/08/typescript-ji-chu-ru-men-bian-liang-sheng-ming-san.html"
  - "/typescript-ji-chu-ru-men-bian-liang-sheng-ming-san.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.5
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

## **变量声明 - 解构**

Another TypeScript已经可以解析其它 ECMAScript 2015 特性了。 完整列表请参见 [the article on the Mozilla Developer Network](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring_assignment)。 这里将给出一个简短的概述。

### **解构数组**

最简单的解构莫过于数组的解构赋值了：

```ts
let input = [1, 2];
let [first, second] = input;
console.log(first);
console.log(second);
```

运行后将得到如下输出

```bash
1
2
```

这创建了2个命名变量 first 和 second。 相当于使用了索引，但更为方便：

```ts
first = input[0];
second = input[1];

console.log(first);
console.log(second);
```

运行后将得到如下输出

```bash
1
2
```

解构作用于已声明的变量会更好：

```ts
[first, second] = [second, first];
```

运行后将得到如下输出

```bash
2
1
```

作用于函数参数：

```ts
function f6([first, second]: [number, number]) {
    console.log(first);
    console.log(second);
}
f6([1,2]);
```

运行后将得到如下输出

```bash
1
2
```

你可以在数组里使用...语法创建剩余变量：

```ts
let [one, ...rest] = [1, 2, 3, 4];
console.log(one);
console.log(rest);
```

运行后将得到如下输出

```bash
1
[ 2, 3, 4 ]
```

当然，由于是JavaScript, 你可以忽略你不关心的尾随元素：

```ts
let [number_one] = [1, 2, 3, 4];
console.log(number_one);
```

运行后将得到如下输出

```bash
1
```

或其它元素：

```ts
let [, second, , fourth] = [1, 2, 3, 4];
```

### **对象解构**

对象也可以进行解构：

```ts
let o = {
    a: "foo",
    b: 12,
    c: "bar"
};
let { a, b } = o;
console.log(a, b);
```

运行后将得到如下输出

```bash
foo 12
```

这通过 o.a and o.b 创建了 a 和 b 。 注意，如果你不需要 c 你可以忽略它。

就像数组解构，你可以用没有声明的赋值：

```ts
({ a, b } = { a: "baz", b: 101 });
console.log(a, b);
```

运行后将得到如下输出

```bash
baz 101
```

注意，我们需要用括号将它括起来，因为Javascript通常会将以 { 起始的语句解析为一个块。

你可以在对象里使用...语法创建剩余变量：

```ts
let { x, ...passthrough } = m;
let total = passthrough.y + passthrough.z.length;
console.log(x, total, passthrough)
```

运行后将得到如下输出

```bash
a 13 { y: 12, z: 'b' }
```

### **属性重命名**

你也可以给属性以不同的名字：

```ts
let { a: newName1, b: newName2 } = o;
```

这里的语法开始变得混乱。 你可以将 a: newName1 读做 "a 作为 newName1"。 方向是从左到右，好像你写成了以下样子：

```ts
let newName1 = o.a;
let newName2 = o.b;
```

令人困惑的是，这里的冒号不是指示类型的。 如果你想指定它的类型， 仍然需要在其后写上完整的模式。

```ts
let {a, b}: {a: string, b: number} = o;
```

### **默认值**

默认值可以让你在属性为 undefined 时使用缺省值：

```ts
function keepWholeObject(wholeObject: { a: string, b?: number }) {
    let { a, b = 1001 } = wholeObject;
}
```

现在，即使 b 为 undefined ， keepWholeObject 函数的变量 wholeObject 的属性 a 和 b 都会有值。

### **函数声明**

解构也能用于函数声明。 看以下简单的情况：

```ts
type C = { a: string, b?: number }
function f7({ a, b }: C): void {
    // ...
}
```

但是，通常情况下更多的是指定默认值，解构默认值有些棘手。 首先，你需要在默认值之前设置其格式。

```ts
function f8({ a, b } = { a: "hello", b: 0 }): void {
    // ...
    console.log(a, b);
}
f8();
```

运行后将得到如下输出

```bash
hello 0
```

上面的代码是一个类型推断的例子

其次，你需要知道在解构属性上给予一个默认或可选的属性用来替换主初始化列表。 要知道 C 的定义有一个 b 可选属性：

```ts
function f({ a, b = 0 } = { a: "" }): void {
    // ...
}
f({ a: "yes" }); // 正常, 默认 b = 0
f(); // 正常, 默认传参 {a: ""}, 默认 b = 0
f({}); // 报错, 如果只传递一个参数的话'a'是必须的传递的
```

要小心使用解构。 从前面的例子可以看出，就算是最简单的解构表达式也是难以理解的。 尤其当存在深层嵌套解构的时候，就算这时没有堆叠在一起的重命名，默认值和类型注解，也是令人难以理解的。 解构表达式要尽量保持小而简单。 你自己也可以直接使用解构将会生成的赋值表达式。

### **展开**

展开操作符正与解构相反。 它允许你将一个数组展开为另一个数组，或将一个对象展开为另一个对象。 例如：

```ts
let a_one = [1, 2];
let a_two = [3, 4];
let bothPlus = [0, ...a_one, ...a_two, 5];
console.log(bothPlus);
```

运行后将得到如下输出

```bash
[ 0, 1, 2, 3, 4, 5 ]
```

这会令bothPlus的值为[0, 1, 2, 3, 4, 5]。 展开操作创建了 first和second的一份浅拷贝。 它们不会被展开操作所改变。

你还可以展开对象：

```ts
let defaults = { food: "spicy", price: "$$", ambiance: "noisy" };
let search = { ...defaults, food: "rich" };
console.log(search)
```

运行后将得到如下输出

```bash
{ food: 'rich', price: '$$', ambiance: 'noisy' }
```

search的值为{ food: "rich", price: "$$", ambiance: "noisy" }。 对象的展开比数组的展开要复杂的多。 像数组展开一样，它是从左至右进行处理，但结果仍为对象。这就意味着出现在展开对象后面的属性会覆盖前面的属性。 因此，如果我们修改上面的例子，在结尾处进行展开的话：

那么，defaults里的food属性会重写food: "rich"，在这里这并不是我们想要的结果。

对象展开还有其它一些意想不到的限制。 首先，它仅包含对象 自身的可枚举属性。 大体上是说当你展开一个对象实例时，你会丢失其方法：

```ts
class C {
  p = 12;
  m() {
  }
}
let c = new C();
let clone = { ...c };
clone.p; // 正常调用
clone.m(); // 调用失败
```

其次，TypeScript编译器不允许展开泛型函数上的类型参数。 这个特性会在TypeScript的未来版本中考虑实现。

本实例结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.6
```
