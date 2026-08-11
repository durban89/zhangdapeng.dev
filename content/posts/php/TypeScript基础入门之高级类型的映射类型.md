---
title: "TypeScript基础入门之高级类型的映射类型"
date: "2025-07-09 10:42:50"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ying-she-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的映射类型/"
  - "/2025/07/09/TypeScript基础入门之高级类型的映射类型.html"
  - "/TypeScript基础入门之高级类型的映射类型/"
  - "/TypeScript基础入门之高级类型的映射类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ying-she-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ying-she-lei-xing.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ying-she-lei-xing.html"
---
## 高级类型

### 映射类型

一个常见的任务是将一个已知的类型每个属性都变为可选的：

```ts
interface PersonPartial {
    name?: string;
    age?: number;
}
```

或者我们想要一个只读版本：

```ts
interface PersonReadonly {
    readonly name: string;
    readonly age: number;
}
```

这在JavaScript里经常出现，TypeScript提供了从旧类型中创建新类型的一种方式 — 映射类型。 在映射类型里，新类型以相同的形式去转换旧类型里每个属性。 例如，你可以令每个属性成为 readonly类型或可选的。 下面是一些例子：

```ts
type Readonly<T> = {
    readonly [P in keyof T]: T[P];
}
type Partial<T> = {
    [P in keyof T]?: T[P];
}
```

像下面这样使用：

```ts
type PersonPartial = Partial<Person>;
type ReadonlyPerson = Readonly<Person>;
```

下面来看看最简单的映射类型和它的组成部分：

```ts
type Keys = 'option1' | 'option2';
type Flags = { [K in Keys]: boolean };
```

它的语法与索引签名的语法类型，内部使用了 for .. in。 具有三个部分：

1. 类型变量 K，它会依次绑定到每个属性。  
2. 字符串字面量联合的 Keys，它包含了要迭代的属性名的集合。  
3. 属性的结果类型。  
在这个简单的例子里， Keys是硬编码的的属性名列表并且属性类型永远是boolean，因此这个映射类型等同于：

```ts
type Flags = {
    option1: boolean;
    option2: boolean;
}
```

在真正的应用里，可能不同于上面的 Readonly或 Partial。 它们会基于一些已存在的类型，且按照一定的方式转换字段。 这就是 keyof和索引访问类型要做的事情：

```ts
type NullablePerson = { [P in keyof Person]: Person[P] | null }
type PartialPerson = { [P in keyof Person]?: Person[P] }
```

但它更有用的地方是可以有一些通用版本。

```ts
type Nullable<T> = { [P in keyof T]: T[P] | null }
type Partial<T> = { [P in keyof T]?: T[P] }
```

在这些例子里，属性列表是 keyof T且结果类型是 T[P]的变体。 这是使用通用映射类型的一个好模版。 因为这类转换是 同态的，映射只作用于 T的属性而没有其它的。 编译器知道在添加任何新属性之前可以拷贝所有存在的属性修饰符。 例如，假设 Person.name是只读的，那么 Partial<Person>.name也将是只读的且为可选的。

下面是另一个例子， T[P]被包装在 Proxy<T>类里：

```ts
type Proxy<T> = {
    get(): T;
    set(value: T): void;
}
type Proxify<T> = {
    [P in keyof T]: Proxy<T[P]>;
}
function proxify<T>(o: T): Proxify<T> {
   // ... wrap proxies ...
}
let proxyProps = proxify(props);
```

注意 Readonly<T>和 Partial<T>用处不小，因此它们与 Pick和 Record一同被包含进了TypeScript的标准库里：

```ts
type Pick<T, K extends keyof T> = {
    [P in K]: T[P];
}
type Record<K extends string, T> = {
    [P in K]: T;
}
```

Readonly， Partial和 Pick是同态的，但 Record不是。 因为 Record并不需要输入类型来拷贝属性，所以它不属于同态：

```ts
type ThreeStringProps = Record<'prop1' | 'prop2' | 'prop3', string>
```

非同态类型本质上会创建新的属性，因此它们不会从它处拷贝属性修饰符。

### *由映射类型进行推断*

现在你了解了如何包装一个类型的属性，那么接下来就是如何拆包。 其实这也非常容易：

```ts
function unproxify<T>(t: Proxify<T>): T {
    let result = {} as T;
    for (const k in t) {
        result[k] = t[k].get();
    }
    return result;
}

let originalProps = unproxify(proxyProps);
```

注意这个拆包推断只适用于同态的映射类型。 如果映射类型不是同态的，那么需要给拆包函数一个明确的类型参数。
