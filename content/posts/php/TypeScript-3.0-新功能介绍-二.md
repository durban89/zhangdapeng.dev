---
title: "TypeScript 3.0 新功能介绍（二）"
date: "2025-07-09 09:59:53"
slug: "typescript-30-xin-gong-neng-jie-shao-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript-3.0-新功能介绍（二）/"
  - "/2025/07/09/TypeScript-3.0-新功能介绍（二）.html"
  - "/TypeScript-3.0-新功能介绍（二）/"
  - "/TypeScript-3.0-新功能介绍（二）.html"
  - "/2025/07/09/TypeScript-3.0-新功能介绍-二/"
  - "/2025/07/09/TypeScript-3.0-新功能介绍-二.html"
  - "/2025/07/09/typescript-30-xin-gong-neng-jie-shao-er/"
  - "/2025/07/09/typescript-30-xin-gong-neng-jie-shao-er.html"
  - "/typescript-30-xin-gong-neng-jie-shao-er.html"
---
TypeScript 3.0 新功能介绍（二）

## **New unknown top type**

TypeScript 3.0引入了一种新的顶级类型unknown。  
unknown是任何类型安全的对应物。  
任何东西都可以分配给unknown，但是unknown的东西除了本身以及任何没有类型断言或基于控制流的缩小之外的任何东西都不能分配。  
同样，如果没有先断言或缩小到更具体的类型，则不允许对unknown操作进行操作。具体看下官方给的例子

```ts
// In an intersection everything absorbs unknown

type T00 = unknown & null;  // null
type T01 = unknown & undefined;  // undefined
type T02 = unknown & null & undefined;  // null & undefined (which becomes never)
type T03 = unknown & string;  // string
type T04 = unknown & string[];  // string[]
type T05 = unknown & unknown;  // unknown
type T06 = unknown & any;  // any

// In a union an unknown absorbs everything

type T10 = unknown | null;  // unknown
type T11 = unknown | undefined;  // unknown
type T12 = unknown | null | undefined;  // unknown
type T13 = unknown | string;  // unknown
type T14 = unknown | string[];  // unknown
type T15 = unknown | unknown;  // unknown
type T16 = unknown | any;  // any

// Type variable and unknown in union and intersection

type T20<T> = T & {};  // T & {}
type T21<T> = T | {};  // T | {}
type T22<T> = T & unknown;  // T
type T23<T> = T | unknown;  // unknown

// unknown in conditional types

type T30<T> = unknown extends T ? true : false;  // Deferred
type T31<T> = T extends unknown ? true : false;  // Deferred (so it distributes)
type T32<T> = never extends T ? true : false;  // true
type T33<T> = T extends never ? true : false;  // Deferred

// keyof unknown

type T40 = keyof any;  // string | number | symbol
type T41 = keyof unknown;  // never

// Only equality operators are allowed with unknown

function f10(x: unknown) {
    x == 5;
    x !== 10;
    x >= 0;  // Error
    x + 1;  // Error
    x * 2;  // Error
    -x;  // Error
    +x;  // Error
}

// No property accesses, element accesses, or function calls

function f11(x: unknown) {
    x.foo;  // Error
    x[5];  // Error
    x();  // Error
    new x();  // Error
}

// typeof, instanceof, and user defined type predicates

declare function isFunction(x: unknown): x is Function;

function f20(x: unknown) {
    if (typeof x === "string" || typeof x === "number") {
        x;  // string | number
    }
    if (x instanceof Error) {
        x;  // Error
    }
    if (isFunction(x)) {
        x;  // Function
    }
}

// Homomorphic mapped type over unknown

type T50<T> = { [P in keyof T]: number };
type T51 = T50<any>;  // { [x: string]: number }
type T52 = T50<unknown>;  // {}

// Anything is assignable to unknown

function f21<T>(pAny: any, pNever: never, pT: T) {
    let x: unknown;
    x = 123;
    x = "hello";
    x = [1, 2, 3];
    x = new Error();
    x = x;
    x = pAny;
    x = pNever;
    x = pT;
}

// unknown assignable only to itself and any

function f22(x: unknown) {
    let v1: any = x;
    let v2: unknown = x;
    let v3: object = x;  // Error
    let v4: string = x;  // Error
    let v5: string[] = x;  // Error
    let v6: {} = x;  // Error
    let v7: {} | null | undefined = x;  // Error
}

// Type parameter 'T extends unknown' not related to object

function f23<T extends unknown>(x: T) {
    let y: object = x;  // Error
}

// Anything but primitive assignable to { [x: string]: unknown }

function f24(x: { [x: string]: unknown }) {
    x = {};
    x = { a: 5 };
    x = [1, 2, 3];
    x = 123;  // Error
}

// Locals of type unknown always considered initialized

function f25() {
    let x: unknown;
    let y = x;
}

// Spread of unknown causes result to be unknown

function f26(x: {}, y: unknown, z: any) {
    let o1 = { a: 42, ...x };  // { a: number }
    let o2 = { a: 42, ...x, ...y };  // unknown
    let o3 = { a: 42, ...x, ...y, ...z };  // any
}

// Functions with unknown return type don't need return expressions

function f27(): unknown {
}

// Rest type cannot be created from unknown

function f28(x: unknown) {
    let { ...a } = x;  // Error
}

// Class properties of type unknown don't need definite assignment

class C1 {
    a: string;  // Error
    b: unknown;
    c: any;
}
```

## 在JSX中支持 defaultProps

TypeScript 2.9及更早版本没有利用JSX组件中的React defaultProps声明。  
用户通常必须声明属性可选并在render中使用非null断言，或者在导出之前使用type-assertions来修复组件的类型。  
TypeScript 3.0添加支持JSX名称空间中名为LibraryManagedAttributes的新类型别名。  
在用于检查以其为目标的JSX表达式之前，此助手类型定义组件的Props类型的转换;  
从而允许自定义，例如：如何处理提供的道具和推断道具之间的冲突，如何映射推理，如何处理选项，以及如何组合来自不同地方的推理。  
简而言之，我们可以使用这种通用类型来模拟React的特定行为，例如defaultProps，以及某种程度上propTypes。

```ts
export interface Props {
    name: string;
}

export class Greet extends React.Component<Props> {
    render() {
        const { name } = this.props;
        return <div>Hello ${name.toUpperCase()}!</div>;
    }
    static defaultProps = { name: "world"};
}

// Type-checks! No type assertions needed!
let el = <Greet />
```

```bash
**注意事项**
```

### defaultProps上的显式类型

默认ed属性是从defaultProps属性类型推断出来的。  
如果添加了显式类型注释，例如  
`static defaultProps：Partial <Props>;`  
编译器将无法识别哪些属性具有默认值（因为defaultProps的类型包括Props的所有属性）。  
使用`static defaultProps：Pick <Props，"name">;`  
相反，作为显式类型注释，或者不像上面的示例中那样添加类型注释。  
对于无状态功能组件（SFC），请使用ES2015 SFC的默认初始化程序：

```ts
function Greet({ name = "world" }: Props) {
    return <div>Hello ${name.toUpperCase()}!</div>;
}
```

### 对@types/React的更改

仍然需要在@types/React中将LibraryManagedAttributes定义添加到JSX名称空间的相应更改。  
请记住，有一些限制。

## /// <reference lib="..." />引用指令

TypeScript添加了一个新的三斜杠引用指令(`/// <reference lib="..." />`)，允许文件显式包含现有的内置lib文件。  
内置的lib文件以与tsconfig.json中的"lib"编译器选项相同的方式引用（例如，使用lib ="es2015"而不是lib ="lib.es2015.d.ts"等）。  
对于在内置类型上进行中继的声明文件作者，例如  
建议使用DOM API或内置的JS运行时构造函数（如Symbol或Iterable，三斜杠引用lib指令）。  
以前这些.d.ts文件必须添加此类型的前向/重复声明。

将`/// <reference lib="es2017.string" />`用于编译中的一个文件相当于使用--lib es2017.string进行编译。

```ts
/// <reference lib="es2017.string" />

"foo".padStart(4);
```

介绍就这些，如果有不对或者想看具体详情请到官网查看 http://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-0.html
