---
title: "TypeScript基础入门之高级类型的可null类型"
date: "2025-07-09 10:42:15"
slug: "typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ke-null-lei-xing"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之高级类型的可null类型/"
  - "/2025/07/09/TypeScript基础入门之高级类型的可null类型.html"
  - "/TypeScript基础入门之高级类型的可null类型/"
  - "/TypeScript基础入门之高级类型的可null类型.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ke-null-lei-xing/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ke-null-lei-xing.html"
  - "/typescript-ji-chu-ru-men-zhi-gao-ji-lei-xing-de-ke-null-lei-xing.html"
---
## 高级类型

### 可null类型（Nullable Types）

TypeScript具有两种特殊的类型，null和undefined，它们分别具有值null和undefined。 默认情况下，类型检查器认为null与undefined可以赋值给任何类型。  
null与undefined是所有其它类型的一个有效值。 这也意味着，你阻止不了将它们赋值给其它类型，就算是你想要阻止这种情况也不行。  
null的发明者，Tony Hoare，称它为价值亿万美金的错误。

`--strictNullChecks`标记可以解决此错误：当你声明一个变量时，它不会自动地包含null或undefined。  
你可以使用联合类型明确的包含它们，如下

```ts
let s = "foo";
s = null; // 错误, 'null'不能赋值给'string'
let sn: string | null = "bar";
sn = null; // 可以

sn = undefined; // error, 'undefined'不能赋值给'string | null'
```

注意，按照JavaScript的语义，TypeScript会把null和undefined区别对待。   
`string | null`，`string | undefined`和 `string | undefined | null`是不同的类型。

### 可选参数和可选属性

使用了 `--strictNullChecks`，可选参数会被自动地加上`| undefined`:

```ts
function f(x: number, y?: number) {
    return x + (y || 0);
}
f(1, 2);
f(1);
f(1, undefined);
f(1, null); // error, 'null' is not assignable to 'number | undefined'
```

可选属性也会有同样的处理：

```ts
class C {
    a: number;
    b?: number;
}
let c = new C();
c.a = 12;
c.a = undefined; // error, 'undefined' is not assignable to 'number'
c.b = 13;
c.b = undefined; // ok
c.b = null; // error, 'null' is not assignable to 'number | undefined'
```

### 类型保护和类型断言

由于可以为null的类型是通过联合类型实现，那么你需要使用类型保护来去除 null。 幸运地是这与在JavaScript里写的代码一致：

```ts
function f(sn: string | null): string {
    if (sn == null) {
        return "default";
    } else {
        return sn;
    }
}
```

这里很明显地去除了null，你也可以使用||运算符：

```ts
function f(sn: string | null): string {
    return sn || "default";
}
```

如果编译器不能够去除null或undefined，你可以使用类型断言手动去除。 语法是添加!后缀：`identifier!`从identifier的类型里去除了null和undefined：

先看第一个失败的例子

```ts
function broken(name: string | null): string {
  function postfix(epithet: string) {
    return name.charAt(0) + '.  the ' + epithet; // error, 'name' is possibly null
  }
  name = name || "Bob";
  return postfix("great");
}
```

在看下第二个成功的例子

```ts
function fixed(name: string | null): string {
  function postfix(epithet: string) {
    return name!.charAt(0) + '.  the ' + epithet; // ok
  }
  name = name || "Bob";
  return postfix("great");
}
```

上面的例子使用了嵌套函数，因为编译器无法去除嵌套函数的null（除非是立即调用的函数表达式）。 因为它无法跟踪所有对嵌套函数的调用，尤其是你将内层函数做为外层函数的返回值。 如果无法知道函数在哪里被调用，就无法知道调用时name的类型。
