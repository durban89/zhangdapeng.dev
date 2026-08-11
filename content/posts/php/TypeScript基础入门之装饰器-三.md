---
title: "TypeScript基础入门之装饰器(三)"
date: "2025-07-10 10:24:09"
slug: "typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之装饰器(三)/"
  - "/2025/07/10/TypeScript基础入门之装饰器(三).html"
  - "/TypeScript基础入门之装饰器(三)/"
  - "/TypeScript基础入门之装饰器(三).html"
  - "/2025/07/10/TypeScript基础入门之装饰器-三/"
  - "/2025/07/10/TypeScript基础入门之装饰器-三.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-san/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-san.html"
  - "/typescript-ji-chu-ru-men-zhi-zhuang-shi-qi-san.html"
---
继续上篇文章[[TypeScript基础入门之装饰器(二)](https://www.gowhich.com/blog/955)]

### 访问器装饰器

Accessor Decorator在访问器声明之前声明。 访问器装饰器应用于访问器的属性描述符，可用于观察，修改或替换访问者的定义。 访问器装饰器不能在声明文件中使用，也不能在任何其他环境上下文中使用（例如在声明类中）。

> 注意: TypeScript不允许为单个成员装饰get和set访问器。相反，该成员的所有装饰器必须应用于按文档顺序指定的第一个访问器。这是因为装饰器适用于属性描述符，它结合了get和set访问器，而不是单独的每个声明。

访问器装饰器的表达式将在运行时作为函数调用，具有以下三个参数：

1. 静态成员的类的构造函数，或实例成员的类的原型。
2. 成员的名字。
3. 会员的财产描述。

> 注意: 如果脚本目标小于ES5，则属性描述符将不确定。

如果访问器装饰器返回一个值，它将用作该成员的属性描述符。

> 注意: 如果脚本目标小于ES5，则忽略返回值。

以下是应用于Point类成员的访问器装饰器([@configurable](https://github.com/configurable))的示例：

```ts
class Point {
    private _x: number;
    private _y: number;
    constructor(x: number, y: number) {
        this._x = x;
        this._y = y;
    }

    @configurable(false)
    get x() { return this._x; }

    @configurable(false)
    get y() { return this._y; }
}
```

我们可以使用以下函数声明定义@configurable装饰器：

```ts
function configurable(value: boolean) {
    return function (target: any, propertyKey: string, descriptor: PropertyDescriptor) {
        descriptor.configurable = value;
    };
}
```

### 属性装饰器

Property Decorator在属性声明之前声明。 属性修饰器不能在声明文件中使用，也不能在任何其他环境上下文中使用（例如在声明类中）。

属性装饰器的表达式将在运行时作为函数调用，具有以下两个参数：

1. 静态成员的类的构造函数，或实例成员的类的原型。
2. 成员的名字。

> 注意: 由于在TypeScript中如何初始化属性装饰器，因此不提供属性描述符作为属性装饰器的参数。这是因为在定义原型的成员时，当前没有机制来描述实例属性，也无法观察或修改属性的初始化程序。返回值也会被忽略。因此，属性装饰器只能用于观察已为类声明特定名称的属性。

我们可以使用此信息来记录有关属性的元数据，如以下示例所示：

```ts
class Greeter {
    @format("Hello, %s")
    greeting: string;

    constructor(message: string) {
        this.greeting = message;
    }
    greet() {
        let formatString = getFormat(this, "greeting");
        return formatString.replace("%s", this.greeting);
    }
}
```

然后我们可以使用以下函数声明定义@format装饰器和getFormat函数：

```javascript
import "reflect-metadata";

const formatMetadataKey = Symbol("format");

function format(formatString: string) {
    return Reflect.metadata(formatMetadataKey, formatString);
}

function getFormat(target: any, propertyKey: string) {
    return Reflect.getMetadata(formatMetadataKey, target, propertyKey);
}
```

这里的[@format](https://github.com/format)("Hello，％s")装饰器是一个装饰工厂。 当调用[@format](https://github.com/format)("Hello，％s")时，它会使用reflect-metadata库中的Reflect.metadata函数为该属性添加元数据条目。 调用getFormat时，它会读取格式的元数据值。

注意此示例需要reflect-metadata库。 有关reflect-metadata库的更多信息，请参阅元数据。

### 参数装饰器

参数装饰器在参数声明之前声明。 参数装饰器应用于类构造函数或方法声明的函数。 参数装饰器不能用于声明文件，重载或任何其他环境上下文（例如声明类中）。

参数装饰器的表达式将在运行时作为函数调用，具有以下三个参数：

1. 静态成员的类的构造函数，或实例成员的类的原型。
2. 成员的名字。
3. 函数参数列表中参数的序数索引。

> 注意: 参数装饰器只能用于观察已在方法上声明参数。

将忽略参数装饰器的返回值。

以下是应用于Greeter类成员参数的参数装饰器([@required](https://github.com/required))的示例：

```ts
class Greeter {
    greeting: string;

    constructor(message: string) {
        this.greeting = message;
    }

    @validate
    greet(@required name: string) {
        return "Hello " + name + ", " + this.greeting;
    }
}
```

然后我们可以使用以下函数声明定义@required和@validate装饰器：

```ts
import "reflect-metadata";

const requiredMetadataKey = Symbol("required");

function required(target: Object, propertyKey: string | symbol, parameterIndex: number) {
    let existingRequiredParameters: number[] = Reflect.getOwnMetadata(requiredMetadataKey, target, propertyKey) || [];
    existingRequiredParameters.push(parameterIndex);
    Reflect.defineMetadata(requiredMetadataKey, existingRequiredParameters, target, propertyKey);
}

function validate(target: any, propertyName: string, descriptor: TypedPropertyDescriptor<Function>) {
    let method = descriptor.value;
    descriptor.value = function () {
        let requiredParameters: number[] = Reflect.getOwnMetadata(requiredMetadataKey, target, propertyName);
        if (requiredParameters) {
            for (let parameterIndex of requiredParameters) {
                if (parameterIndex >= arguments.length || arguments[parameterIndex] === undefined) {
                    throw new Error("Missing required argument.");
                }
            }
        }

        return method.apply(this, arguments);
    }
}
```

@required装饰器添加一个元数据条目，根据需要标记参数。 然后，@validate装饰器将现有的greet方法包装在一个函数中，该函数在调用原始方法之前验证参数。

> 注意: 此示例需要reflect-metadata库。有关reflect-metadata库的更多信息，请参阅元数据。

### 元数据

一些示例使用reflect-metadata库，它为实验元数据API添加了polyfill。 该库尚未成为ECMAScript（JavaScript）标准的一部分。 但是，一旦装饰器被正式采用为ECMAScript标准的一部分，这些扩展将被提议采用。

您可以通过npm安装此库：

```bash
npm i reflect-metadata --save
```

TypeScript包含实验支持，用于为具有装饰器的声明发出某些类型的元数据。 要启用此实验性支持，必须在命令行或tsconfig.json中设置emitDecoratorMetadata编译器选

*命令行：*

```bash
tsc --target ES5 --experimentalDecorators --emitDecoratorMetadata
```

tsconfig.json:

```json
{
    "compilerOptions": {
        "target": "ES5",
        "experimentalDecorators": true,
        "emitDecoratorMetadata": true
    }
}
```

启用后，只要导入了reflect-metadata库，就会在运行时公开其他设计时类型信息。

我们可以在以下示例中看到这一点：

```ts
import "reflect-metadata";

class Point {
    x: number;
    y: number;
}

class Line {
    private _p0: Point;
    private _p1: Point;

    @validate
    set p0(value: Point) { this._p0 = value; }
    get p0() { return this._p0; }

    @validate
    set p1(value: Point) { this._p1 = value; }
    get p1() { return this._p1; }
}

function validate<T>(target: any, propertyKey: string, descriptor: TypedPropertyDescriptor<T>) {
    let set = descriptor.set;
    descriptor.set = function (value: T) {
        let type = Reflect.getMetadata("design:type", target, propertyKey);
        if (!(value instanceof type)) {
            throw new TypeError("Invalid type.");
        }
        set(value);
    }
}
```

TypeScript编译器将使用@ Reflect.metadata装饰器注入设计时类型信息。 你可以认为它相当于以下TypeScript：

```ts
class Line {
    private _p0: Point;
    private _p1: Point;

    @validate
    @Reflect.metadata("design:type", Point)
    set p0(value: Point) { this._p0 = value; }
    get p0() { return this._p0; }

    @validate
    @Reflect.metadata("design:type", Point)
    set p1(value: Point) { this._p1 = value; }
    get p1() { return this._p1; }
}
```

> 注意: 装饰器元数据是一个实验性功能，可能会在将来的版本中引入重大更改。
