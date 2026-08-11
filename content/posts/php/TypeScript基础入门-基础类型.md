---
title: "TypeScript基础入门 - 基础类型"
date: "2025-07-08 15:16:32"
slug: "typescript-ji-chu-ru-men-ji-chu-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/08/TypeScript基础入门-基础类型/"
  - "/2025/07/08/TypeScript基础入门-基础类型.html"
  - "/TypeScript基础入门-基础类型/"
  - "/TypeScript基础入门-基础类型.html"
  - "/2025/07/08/typescript-ji-chu-ru-men-ji-chu-lei-xing/"
  - "/2025/07/08/typescript-ji-chu-ru-men-ji-chu-lei-xing.html"
  - "/typescript-ji-chu-ru-men-ji-chu-lei-xing.html"
---
项目实践仓库

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.2
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

### **基础类型简介**

TypeScript支持与JavaScript几乎相同的数据类型，包括：数字，字符串，结构体，布尔值等。此外还提供了实用的枚举类型方便我们使用。

### **布尔值**

最基本的数据类型就是简单的true/false值，在JavaScript和TypeScript里叫做boolean（其它语言中也一样）。

```ts
// 布尔值
let isDone: boolean = false;
console.log('isDone = ', isDone);
```

运行后结果如下

```bash
isDone =  false
```

### **数字**

和JavaScript一样，TypeScript里的所有数字都是浮点数。 这些浮点数的类型是 number。 除了支持十进制和十六进制字面量，TypeScript还支持ECMAScript 2015中引入的二进制和八进制字面量。

```ts
// 数字
let number1: number = 6;
let number2: number = 0xf00d;
let number3: number = 0b1010;
let number4: number = 0o744;

console.log('number1 = ', number1);
console.log('number2 = ', number2);
console.log('number3 = ', number3);
console.log('number4 = ', number4);
```

运行后结果如下

```bash
number1 =  6
number2 =  61453
number3 =  10
number4 =  484
```

### **字符串**

JavaScript程序的另一项基本操作是处理网页或服务器端的文本数据。 像其它语言里一样，我们使用 string表示文本数据类型。 和JavaScript一样，可以使用双引号（"）或单引号（'）表示字符串。

```ts
let title: string = "gowhich"
console.log('title = ', title);
```

运行后结果如下

```bash
title =  gowhich
```

你还可以使用模版字符串，它可以定义多行文本和内嵌表达式。 这种字符串是被反引号包围（`），并且以${ expr }这种形式嵌入表达式

```ts
let firstName: string = "Durban";
let age: number = 42
let sentence: string = `==
Hello, 大家好，我是${firstName}

下个月我就${age}岁大了。
`;
console.log(sentence);
```

运行后结果如下

```bash
==
Hello, 大家好，我是Durban

下个月我就42岁大了。
```

### **数组**

TypeScript像JavaScript一样可以操作数组元素。 有两种方式可以定义数组。 第一种，可以在元素类型后面接上 []，表示由此类型元素组成的一个数组：

```ts
let list1: number[] = [1,2,3];
```

运行后结果如下

```bash
[ 1, 2, 3 ]
```

第二种方式是使用数组泛型，Array<元素类型>：

```ts
let list2: Array<number> = [1,2,3];
```

运行后结果如下

```bash
[ 1, 2, 3 ]
```

### **元组 Tuple**

元组类型允许表示一个已知元素数量和类型的数组，各元素的类型不必相同。 比如，你可以定义一对值分别为 string和number类型的元组。

```ts
// 声明元组类型
let x: [string, number]
// 正确的初始化x
x = ["durban", 42]
// 错误的初始化
// x = [42， "durban"]
console.log('x = ', x);
```

运行后结果如下

```bash
x =  [ 'durban', 42 ]
```

当访问一个已知索引的元素，会得到正确的类型：

```ts
console.log(x[0].substr(1));
// console.log(x[1].substr(1)); // number 没有substr
```

当访问一个越界的元素，会使用联合类型替代：

```ts
x[3] = "world"
console.log(x[5])
console.log('x = ', x);
// x[6] = true // Error, 布尔不是(string | number)类型
```

运行后的结果如下

```bash
undefined
x =  [ 'durban', 42, <1 empty item>, 'world' ]
```

联合类型是高级主题，我们会在以后的分享中介绍。

### **枚举**

enum类型是对JavaScript标准数据类型的一个补充。 像C#等其它语言一样，使用枚举类型可以为一组数值赋予友好的名字。

```ts
enum Color {Red, Green, Blue}
let c: Color = Color.Green;
console.log('c = ', c)
```

运行后结果如下

```bash
c =  1
```

默认情况下，从0开始为元素编号。 你也可以手动的指定成员的数值。 例如，我们将上面的例子改成从 1开始编号：

```ts
enum Color {Red = 1, Green, Blue}
let c: Color = Color.Green;
console.log('c = ', c)
```

运行后结果如下

```bash
c =  2
```

或者，全部都采用手动赋值：

```ts
enum Color {Red = 1, Green = 4, Blue = 8}
let c: Color = Color.Green;
console.log('c = ', c)
```

运行后结果如下

```bash
c =  4
```

枚举类型提供的一个便利是你可以由枚举的值得到它的名字。 例如，我们知道数值为2，但是不确定它映射到Color里的哪个名字，我们可以查找相应的名字：

```ts
enum Color {Red = 1, Green = 4, Blue = 8}
let c: string = Color[4];
console.log('c = ', c)
```

运行后结果如下

```bash
c =  Green
```

### **Any**

有时候，我们会想要为那些在编程阶段还不清楚类型的变量指定一个类型。 这些值可能来自于动态的内容，比如来自用户输入或第三方代码库。 这种情况下，我们不希望类型检查器对这些值进行检查而是直接让它们通过编译阶段的检查。 那么我们可以使用 any类型来标记这些变量：

```ts
let notSure: any = 4
notSure = false
notSure = "A string"
```

在对现有代码进行改写的时候，any类型是十分有用的，它允许你在编译时可选择地包含或移除类型检查。 你可能认为 Object有相似的作用，就像它在其它语言中那样。 但是 Object类型的变量只是允许你给它赋任意值 - 但是却不能够在它上面调用任意的方法，即便它真的有这些方法：

```ts
let notSure: any = 4;
notSure.ifItExists(); // okay, ifItExists might exist at runtime
notSure.toFixed(); // okay, toFixed exists (but the compiler doesn't check)

let prettySure: Object = 4;
prettySure.toFixed(); // Error: Property 'toFixed' doesn't exist on type 'Object'.
```

当你只知道一部分数据的类型时，any类型也是有用的。 比如，你有一个数组，它包含了不同的类型的数据：

```ts
let list: any[] = [1, true, 'durban'];
console.log(list[1])
list[1] = 100;
console.log(list[1])
```

运行后结果如下

```bash
true
100
```

### **Void**

某种程度上来说，void类型像是与any类型相反，它表示没有任何类型。 当一个函数没有返回值时，你通常会见到其返回值类型是 void：

```ts
function noReturn(params:string): void {
    alert("HaHa");
}
```

声明一个void类型的变量没有什么大用，因为你只能为它赋予undefined和null：

```ts
let unusable: void = undefined;
console.log('unusable = ', unusable);
```

运行后结果如下

```bash
unusable =  undefined
```

### **Null 和 Undefined**

TypeScript里，undefined和null两者各自有自己的类型分别叫做undefined和null。 和void相似，它们的本身的类型用处不是很大：

```ts
let u: undefined = undefined
let n: null = null
n = undefined
u = null
```

默认情况下null和undefined是所有类型的子类型。 就是说你可以把 null和undefined赋值给number类型的变量。

然而，当你指定了--strictNullChecks标记，null和undefined只能赋值给void和它们各自。 这能避免 很多常见的问题。 也许在某处你想传入一个 string或null或undefined，你可以使用联合类型string | null | undefined。

> 注意：我们鼓励尽可能地使用--strictNullChecks，但在本手册里我们假设这个标记是关闭的。

### **Never**

never类型表示的是那些永不存在的值的类型。 例如， never类型是那些总是会抛出异常或根本就不会有返回值的函数表达式或箭头函数表达式的返回值类型； 变量也可能是 never类型，当它们被永不为真的类型保护所约束时。

never类型是任何类型的子类型，也可以赋值给任何类型；然而，没有类型是never的子类型或可以赋值给never类型（除了never本身之外）。 即使 any也不可以赋值给never。下面是一些返回never类型的函数:

```ts
// 返回never的函数必须存在无法达到的终点
function error(message:string): never {
    throw new Error(message);
}

// 推断的返回值类型为never
function Failed() {
    return error("Fauled");
}
// 返回never的函数必须存在无法达到的终点
function infiniteLoop(): never {
    while (true) {

    }
}
```

### **Object**

object是表示非基本类型的类型, 例如除了number, string, boolean, symbol, null, or undefined之外的类型  
使用object类型，像Object.create等APIs。如下代码

```ts
declare function create(o: object | null) :void ;
create({ prop: 0 })
create(null)
// create(42) // 会报错
// create("string") // 会报错
// create(false) // 会报错
// create(undefined) // 会报错
```

### **类型断言**

有时候你会遇到这样的情况，你会比TypeScript更了解某个值的详细信息。 通常这会发生在你清楚地知道一个实体具有比它现有类型更确切的类型。

通过类型断言这种方式可以告诉编译器，“相信我，我知道自己在干什么”。 类型断言好比其它语言里的类型转换，但是不进行特殊的数据检查和解构。 它没有运行时的影响，只是在编译阶段起作用。 TypeScript会假设你，程序员，已经进行了必须的检查。  
类型断言有两种形式。 其一是“尖括号”语法：

```ts
let someValue: any = "this is a string";

let strLength: number = (<string>someValue).length;
```

另一个为as语法：

```ts
let someValue: any = "this is a string";

let strLength: number = (someValue as string).length;
```

两种形式是等价的。 至于使用哪个大多数情况下是凭个人喜好；然而，当你在TypeScript里使用JSX时，只有 as语法断言是被允许的。

### **关于let**

你可能已经注意到了，我们使用let关键字来代替大家所熟悉的JavaScript关键字var。 let关键字是JavaScript的一个新概念，TypeScript实现了它。 我们会在以后详细介绍它，很多常见的问题都可以通过使用 let来解决，所以尽可能地使用let来代替var吧。

这里有个知识点要注意下  
就是对需要编译的文件进行处理的逻辑

```ts
"include": [
    "src/**/*.ts"
],
```

可以做模糊的匹配然后将匹配的文件进行编译

```ts
"files": [
    "src/main.ts"
],
```

是做具体的文件匹配，同时指定要输出的目录  
在compilerOptions配置中加入

```ts
"outDir": "./dist",
```

本次实例分享结束实践项目地址

```bash
https://github.com/durban89/typescript_demo.git
tag: 1.0.3
```
