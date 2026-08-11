---
title: "TypeScript基础入门之JSX(一)"
date: "2025-07-10 10:23:53"
slug: "typescript-ji-chu-ru-men-zhi-jsx-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之JSX(一)/"
  - "/2025/07/10/TypeScript基础入门之JSX(一).html"
  - "/TypeScript基础入门之JSX(一)/"
  - "/TypeScript基础入门之JSX(一).html"
  - "/2025/07/10/TypeScript基础入门之JSX-一/"
  - "/2025/07/10/TypeScript基础入门之JSX-一.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-jsx-yi/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-jsx-yi.html"
  - "/typescript-ji-chu-ru-men-zhi-jsx-yi.html"
---
### 介绍

JSX是一种可嵌入的类似XML的语法。 它旨在转换为有效的JavaScript，尽管该转换的语义是特定于实现的。 JSX在React框架中越来越受欢迎，但此后也看到了其他实现。 TypeScript支持嵌入，类型检查和直接编译JSX到JavaScript。

### 基本用法

要使用JSX，您必须做两件事。 1. 使用.tsx扩展名命名您的文件 2. 启用jsx选项

TypeScript附带三种JSX模式：preserve, react 和 react-native。 这些模式仅影响编译阶段 - 类型检查不受影响。 preserve模式将保持JSX作为输出的一部分，以便由另一个变换步骤（例如Babel）进一步编译。 此外，输出将具有.jsx文件扩展名。 react模式将编译React.createElement，在使用之前不需要经过JSX转换，输出将具有.js文件扩展名。 react-native模式相当于保留，因为它保留了所有JSX，但输出将具有.js文件扩展名。

| Mode | Input | Output | Output File Extension |
| --- | --- | --- | --- |
| preserve |  |  | .jsx |
| react |  | React.createElement(“div”) | .js |
| react-native |  |  | .js |

您可以使用–jsx命令行标志或tsconfig.json文件中的相应选项指定此模式。

> 注意：标识符React是硬编码的，因此必须使用大写的R使React可用

### as 操作符

回想一下如何写一个类型断言：

```ts
var foo = <foo>bar;
```

声明变量bar的类型为foo。 由于TypeScript还对类型断言使用尖括号，因此将其与JSX的语法结合会引入某些解析困难。 因此，TypeScript不允许.tsx文件中的尖括号类型断言。

由于上述语法不能在.tsx文件中使用，因此应使用备用类型断言运算符：as。 可以使用as运算符轻松重写该示例。

```ts
var foo = bar as foo;
```

as运算符在.ts和.tsx文件中均可用，并且行为与尖括号类型断言样式相同。

### 类型检查

为了理解使用JSX进行类型检查，您必须首先了解内部元素和基于值的元素之间的区别。 给定JSX表达式，expr可以引用环境固有的东西（例如DOM环境中的div或span）或者您创建的自定义组件。 这有两个重要原因：

1. 对于React，内部元素以字符串形式发出(React.createElement(“div”))，而您创建的组件则不是(React.createElement(MyComponent))。
2. 应该以不同的方式查找在JSX元素中传递的属性的类型。内在元素属性本质上应该是已知的，而组件可能想要指定它们自己的属性集。

TypeScript使用与React相同的约定来区分它们。内部元素始终以小写字母开头，而基于值的元素始终以大写字母开头。

**内在元素** 在特殊接口JSX.IntrinsicElements上查找内部元素。 默认情况下，如果未指定此接口，则会执行任何操作，并且不会对内部元素进行类型检查。 但是，如果存在此接口，则将内部元素的名称作为JSX.IntrinsicElements接口上的属性进行查找。 例如：

```ts
declare namespace JSX {
    interface IntrinsicElements {
        foo: any
    }
}

<foo />; // ok
<bar />; // error
```

在上面的示例中，将正常工作，但将导致错误，因为它尚未在JSX.IntrinsicElements上指定。

注意：您还可以在JSX.IntrinsicElements上指定catch-all字符串索引器，如下所示：

```ts
declare namespace JSX {
   interface IntrinsicElements {
       [elemName: string]: any;
   }
}
```

**基于值的要素**

基于值的元素只需通过范围内的标识符进行查找。

```ts
import MyComponent from "./myComponent";

<MyComponent />; // ok
<SomeOtherComponent />; // error
```

有两种方法可以定义基于值的元素：

1. 无状态功能组件（SFC）
2. 类组件

因为这两种类型的基于值的元素在JSX表达式中无法区分，所以首先TS尝试使用重载解析将表达式解析为无状态功能组件。 如果该过程成功，则TS完成将表达式解析为其声明。 如果该值无法解析为SFC，则TS将尝试将其解析为类组件。 如果失败，TS将报告错误。

*无状态功能组件*

顾名思义，该组件被定义为JavaScript函数，其第一个参数是props对象。 TS强制其返回类型必须可分配给JSX.Element。

```ts
interface FooProp {
  name: string;
  X: number;
  Y: number;
}

declare function AnotherComponent(prop: {name: string});
function ComponentFoo(prop: FooProp) {
  return <AnotherComponent name={prop.name} />;
}

const Button = (prop: {value: string}, context: { color: string }) => <button>
```

因为SFC只是一个JavaScript函数，所以这里也可以使用函数重载：

```ts
interface ClickableProps {
  children: JSX.Element[] | JSX.Element
}

interface HomeProps extends ClickableProps {
  home: JSX.Element;
}

interface SideProps extends ClickableProps {
  side: JSX.Element | string;
}

function MainButton(prop: HomeProps): JSX.Element;
function MainButton(prop: SideProps): JSX.Element {
  ...
}
```

*类组件*

可以定义类组件的类型。 但是，要这样做，最好理解两个新术语：元素类类型和元素实例类型。

给定，元素类类型是Expr的类型。 因此，在上面的示例中，如果MyComponent是ES6类，则类类型将是该类的构造函数和静态。 如果MyComponent是工厂函数，则类类型将是该函数。

一旦建立了类类型，实例类型就由类类型构造的返回类型或调用签名（无论哪个存在）的并集决定。 同样，在ES6类的情况下，实例类型将是该类的实例的类型，并且在工厂函数的情况下，它将是从函数返回的值的类型。

```ts
class MyComponent {
  render() {}
}

// use a construct signature
var myComponent = new MyComponent();

// element class type => MyComponent
// element instance type => { render: () => void }

function MyFactoryFunction() {
  return {
    render: () => {
    }
  }
}

// use a call signature
var myComponent = MyFactoryFunction();

// element class type => FactoryFunction
// element instance type => { render: () => void }
```

元素实例类型很有趣，因为它必须可以赋值给JSX.ElementClass，否则会导致错误。 默认情况下，JSX.ElementClass是{}，但可以对其进行扩充，以将JSX的使用仅限于那些符合正确接口的类型。

```ts
declare namespace JSX {
  interface ElementClass {
    render: any;
  }
}

class MyComponent {
  render() {}
}
function MyFactoryFunction() {
  return { render: () => {} }
}

<MyComponent />; // ok
<MyFactoryFunction />; // ok

class NotAValidComponent {}
function NotAValidFactoryFunction() {
  return {};
}

<NotAValidComponent />; // error
<NotAValidFactoryFunction />; // error
```
