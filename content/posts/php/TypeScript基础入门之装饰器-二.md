---
title: "TypeScript基础入门之装饰器(二)"
date: "2025-07-10 10:24:07"
slug: "typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之装饰器(二)/"
  - "/2025/07/10/TypeScript基础入门之装饰器(二).html"
  - "/TypeScript基础入门之装饰器(二)/"
  - "/TypeScript基础入门之装饰器(二).html"
  - "/2025/07/10/TypeScript基础入门之装饰器-二/"
  - "/2025/07/10/TypeScript基础入门之装饰器-二.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-er/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-er.html"
  - "/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-er.html"
---
### 装饰器求值

如何应用装饰器应用于类内的各种声明的顺序：

1. 对每个实例成员应用参数装饰器，后跟Method，Accessor或Property Decorators。  
2. 对每个静态成员应用参数装饰器，后跟Method，Accessor或Property Decorators。  
3. 参数装饰器应用于构造函数。  
4. 类装饰器适用于该类。

### 类装饰器

类装饰器在类声明之前声明。  
类装饰器应用于类的构造函数，可用于观察，修改或替换类定义。  
类装饰器不能在声明文件中使用，也不能在任何其他环境上下文中使用（例如在声明类上）。

类装饰器的表达式将在运行时作为函数调用，装饰类的构造函数作为其唯一参数。

如果类装饰器返回一个值，它将使用提供的构造函数替换类声明。

>注意: 如果您选择返回新的构造函数，则必须注意维护原始原型。在运行时应用装饰器的逻辑不会为您执行此操作。

以下是应用于Greeter类的类装饰器（@sealed）的示例：

```ts
@sealed
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        return "Hello, " + this.greeting;
    }
}
```

我们可以使用以下函数声明定义@sealed装饰器：

```ts
function sealed(constructor: Function) {
    Object.seal(constructor);
    Object.seal(constructor.prototype);
}
```

当执行@sealed时，它将密封构造函数及其原型。

接下来，我们有一个如何覆盖构造函数的示例。

```ts
function classDecorator<T extends {new(...args:any[]):{}}>(constructor:T) {
    return class extends constructor {
        newProperty = "new property";
        hello = "override";
    }
}

@classDecorator
class Greeter {
    property = "property";
    hello: string;
    constructor(m: string) {
        this.hello = m;
    }
}

console.log(new Greeter("world"));
```

### 方法装饰器

方法装饰器在方法声明之前声明。  
装饰器应用于方法的属性描述符，可用于观察，修改或替换方法定义。  
方法装饰器不能用于声明文件，重载或任何其他环境上下文（例如声明类）中。

方法装饰器的表达式将在运行时作为函数调用，具有以下三个参数：

1. 静态成员的类的构造函数，或实例成员的类的原型。  
2. 会员的名字。  
3. 会员的属性描述

> 注意: 如果脚本目标小于ES5，则属性描述符将不确定。

如果方法装饰器返回一个值，它将用作方法的属性描述符。

> 注意: 如果脚本目标小于ES5，则忽略返回值。

以下是应用于Greeter类上的方法的方法装饰器（@enumerable）的示例：

```ts
class Greeter {
    greeting: string;
    constructor(message: string) {
        this.greeting = message;
    }

    @enumerable(false)
    greet() {
        return "Hello, " + this.greeting;
    }
}
```

我们可以使用以下函数声明定义@enumerable装饰器：

```ts
function enumerable(value: boolean) {
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        descriptor.enumerable = value;
    };
}
```

这里的@enumerable(false)装饰器是一个装饰工厂。  
当调用@enumerable(false)装饰器时，它会修改属性描述符的可枚举属性。

未完待续...
