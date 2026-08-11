---
title: "TypeScript基础入门之JSX(二)"
date: "2025-07-10 10:23:58"
slug: "typescript-ji-chu-ru-men-zhi-jsx-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之JSX(二)/"
  - "/2025/07/10/TypeScript基础入门之JSX(二).html"
  - "/TypeScript基础入门之JSX(二)/"
  - "/TypeScript基础入门之JSX(二).html"
  - "/2025/07/10/TypeScript基础入门之JSX-二/"
  - "/2025/07/10/TypeScript基础入门之JSX-二.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-jsx-er/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-jsx-er.html"
  - "/typescript-ji-chu-ru-men-zhi-jsx-er.html"
---
### 属性类型检查

键入检查属性的第一步是确定元素属性类型。  
内在元素和基于价值的元素之间略有不同。

对于内部元素，它是JSX.IntrinsicElements上的属性类型

```ts
declare namespace JSX {
  interface IntrinsicElements {
    foo: { bar?: boolean }
  }
}

// element attributes type for 'foo' is '{bar?: boolean}'
<foo bar />;
```

对于基于价值的元素，它有点复杂。  
它由先前确定的元素实例类型上的属性类型确定。  
使用哪个属性由JSX.ElementAttributesProperty确定。  
它应该用单个属性声明。  
然后使用该属性的名称。  
从TypeScript 2.8开始，如果未提供JSX.ElementAttributesProperty，则将使用类元素的构造函数或SFC调用的第一个参数的类型。

```ts
declare namespace JSX {
  interface ElementAttributesProperty {
    props; // specify the property name to use
  }
}

class MyComponent {
  // specify the property on the element instance type
  props: {
    foo?: string;
  }
}

// element attributes type for 'MyComponent' is '{foo?: string}'
<MyComponent foo="bar" />
```

元素属性类型用于键入检查JSX中的属性。  
支持可选和必需的属性。

```ts
declare namespace JSX {
  interface IntrinsicElements {
    foo: { requiredProp: string; optionalProp?: number }
  }
}

<foo requiredProp="bar" />; // ok
<foo requiredProp="bar" optionalProp={0} />; // ok
<foo />; // error, requiredProp is missing
<foo requiredProp={0} />; // error, requiredProp should be a string
<foo requiredProp="bar" unknownProp />; // error, unknownProp does not exist
<foo requiredProp="bar" some-unknown-prop />; // ok, because 'some-unknown-prop' is not a valid identifier
```

> 注意：如果属性名称不是有效的JS标识符（如`data-*`属性），则如果在元素属性类型中找不到它，则不会将其视为错误。

此外，JSX.IntrinsicAttributes接口可用于指定JSX框架使用的额外属性，这些属性通常不被组件的props或参数使用 - 例如React中的键。  
进一步说，通用JSX.IntrinsicClassAttributes <T>类型也可用于为类组件（而不是SFC）指定相同类型的额外属性。  
在此类型中，泛型参数对应于类实例类型。  
在React中，这用于允许类型为Ref <T>的ref属性。  
一般来说，这些接口上的所有属性都应该是可选的，除非您打算让JSX框架的用户需要在每个标记上提供一些属性。  
扩展操作符也是有效的：

```jsx
var props = { requiredProp: "bar" };
<foo {...props} />; // ok

var badProps = {};
<foo {...badProps} />; // error
```

### 子类型检查

在TypeScript 2.3中，TS引入了子类型检查。  
children是元素属性类型中的特殊属性，其中子JSXExpressions被插入到属性中。  
类似于TS使用JSX.ElementAttributesProperty来确定props的名称，TS使用JSX.ElementChildrenAttribute来确定这些props中的子项名称。  
应使用单个属性声明JSX.ElementChildrenAttribute。

```ts
declare namespace JSX {
  interface ElementChildrenAttribute {
    children: {};  // specify children name to use
  }
}
```

```ts
<div>
  <h1>Hello</h1>
</div>;

<div>
  <h1>Hello</h1>
  World
</div>;

const CustomComp = (props) => <div>props.children</div>
<CustomComp>
  <div>Hello World</div>
  {"This is just a JS expression..." + 1000}
</CustomComp>
```

您可以像任何其他属性一样指定子类型。  
这将覆盖默认类型，例如React typings（如果您使用它们）。

```ts
interface PropsType {
  children: JSX.Element
  name: string
}

class Component extends React.Component<PropsType, {}> {
  render() {
    return (
      <h2>
        {this.props.children}
      </h2>
    )
  }
}

// OK
<Component>
  <h1>Hello World</h1>
</Component>

// Error: children is of type JSX.Element not array of JSX.Element
<Component>
  <h1>Hello World</h1>
  <h2>Hello World</h2>
</Component>

// Error: children is of type JSX.Element not array of JSX.Element or string.
<Component>
  <h1>Hello</h1>
  World
</Component>
```

### JSX结果类型

默认情况下，JSX表达式的结果键入为any。您可以通过指定JSX.Element接口来自定义类型。但是，无法从此接口检索有关JSX的元素，属性或子级的类型信息。这是一个黑盒子。

### 嵌入表达式

JSX允许您通过用大括号（{}）包围表达式来在标记之间嵌入表达式。

```jsx
var a = <div>
  {["foo", "bar"].map(i => <span>{i / 2}</span>)}
</div>
```

上面的代码将导致错误，因为您不能将字符串除以数字。  
使用preserve选项时，输出如下所示：

```jsx
var a = <div>
  {["foo", "bar"].map(function (i) { return <span>{i / 2}</span>; })}
</div>
```

### React整合

要将JSX与React一起使用，您应该使用React类型。  
这些类型适当地定义了JSX名称空间以与React一起使用。

```jsx
/// <reference path="react.d.ts" />

interface Props {
  foo: string;
}

class MyComponent extends React.Component<Props, {}> {
  render() {
    return <span>{this.props.foo}</span>
  }
}

<MyComponent foo="bar" />; // ok
<MyComponent foo={0} />; // error
```

### 工厂函数

jsx：react编译器选项使用的确切工厂函数是可配置的。  
可以使用jsxFactory命令行选项或内联@jsx注释编译指示来设置它以基于每个文件进行设置。  
例如，如果将jsxFactory设置为createElement，则<div />将作为createElement("div")而不是React.createElement("div")来编译。

注释pragma版本可以像这样使用（在TypeScript 2.8中）：

```jsx
import preact = require("preact");
/* @jsx preact.h */
const x = <div />;
```

编译为

```jsx
const preact = require("preact");
const x = preact.h("div", null);
```

选择的工厂也将影响JSX命名空间的查找位置(用于类型检查信息)，然后再回退到全局命名空间。  
如果工厂定义为React.createElement(默认值)，编译器将在检查全局JSX之前检查React.JSX。  
如果工厂定义为h，它将在全局JSX之前检查h.JSX。
