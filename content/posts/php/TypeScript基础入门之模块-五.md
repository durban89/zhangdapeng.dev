---
title: "TypeScript基础入门之模块(五)"
date: "2025-07-09 10:43:18"
slug: "typescript-ji-chu-ru-men-zhi-mo-kuai-wu"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之模块(五)/"
  - "/2025/07/09/TypeScript基础入门之模块(五).html"
  - "/TypeScript基础入门之模块(五)/"
  - "/TypeScript基础入门之模块(五).html"
  - "/2025/07/09/TypeScript基础入门之模块-五/"
  - "/2025/07/09/TypeScript基础入门之模块-五.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-wu/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-wu.html"
  - "/typescript-ji-chu-ru-men-zhi-mo-kuai-wu.html"
---
## 构建模块的指南

### 导出尽可能接近顶级

使用您导出的东西时，模块的消费者应尽可能少地摩擦。  
添加太多级别的嵌套往往很麻烦，因此请仔细考虑如何构建事物。

从模块导出命名空间是添加太多嵌套层的示例。  
虽然名称空间有时会有用，但在使用模块时会增加额外的间接级别。  
这很快就会成为用户的痛点，而且通常是不必要的。

导出类上的静态方法也有类似的问题 - 类本身会添加一层嵌套。  
除非以明显有用的方式增加表达性或意图，否则请考虑简单地导出辅助函数。

如果您只导出单个类或函数，请使用export default

正如"顶级附近的出口"减少了模块消费者的摩擦，引入默认导出也是如此。  
如果模块的主要用途是容纳一个特定的导出，那么您应该考虑将其导出为默认导出。  
这使导入和实际使用导入更容易一些。  
例如：

MyClass.ts

```ts
export default class SomeType {
  constructor() { ... }
}
```

MyFunc.ts

```ts
export default function getThing() { return "thing"; }
```

Consumer.ts

```ts
import t from "./MyClass";
import f from "./MyFunc";
let x = new t();
console.log(f());
```

这对消费者来说是最佳的。  
他们可以根据需要命名您的类型（在这种情况下为t），并且不必进行任何过多的点击来查找对象。  
如果您要导出多个对象，请将它们全部放在顶层

MyThings.ts

```ts
export class SomeType { /* ... */ }
export function someFunc() { /* ... */ }
```

相反，导入时：  
明确列出导入的名称  
Consumer.ts

```ts
import { SomeType, someFunc } from "./MyThings";
let x = new SomeType();
let y = someFunc();
```

如果要导入大量内容，请使用命名空间导入模式

MyLargeModule.ts

```ts
export class Dog { ... }
export class Cat { ... }
export class Tree { ... }
export class Flower { ... }
```

Consumer.ts

```ts
import * as myLargeModule from "./MyLargeModule.ts";
let x = new myLargeModule.Dog();
```

### 重新导出扩展延伸

通常，您需要扩展模块的功能。  
一个常见的JS模式是使用扩展来扩充原始对象，类似于JQuery扩展的工作方式。  
正如我们之前提到的，模块不像全局命名空间对象那样合并。  
建议的解决方案是不改变原始对象，而是导出提供新功能的新实体。  
考虑模块Calculator.ts中定义的简单计算器实现。  
该模块还导出一个辅助函数，通过传递输入字符串列表并在结尾写入结果来测试计算器功能。

```ts
export class Calculator {
    private current = 0;
    private memory = 0;
    private operator: string;

    protected processDigit(digit: string, currentValue: number) {
        if (digit >= "0" && digit <= "9") {
            return currentValue * 10 + (digit.charCodeAt(0) - "0".charCodeAt(0));
        }
    }

    protected processOperator(operator: string) {
        if (["+", "-", "*", "/"].indexOf(operator) >= 0) {
            return operator;
        }
    }

    protected evaluateOperator(operator: string, left: number, right: number): number {
        switch (this.operator) {
            case "+": return left + right;
            case "-": return left - right;
            case "*": return left * right;
            case "/": return left / right;
        }
    }

    private evaluate() {
        if (this.operator) {
            this.memory = this.evaluateOperator(this.operator, this.memory, this.current);
        }
        else {
            this.memory = this.current;
        }
        this.current = 0;
    }

    public handleChar(char: string) {
        if (char === "=") {
            this.evaluate();
            return;
        }
        else {
            let value = this.processDigit(char, this.current);
            if (value !== undefined) {
                this.current = value;
                return;
            }
            else {
                let value = this.processOperator(char);
                if (value !== undefined) {
                    this.evaluate();
                    this.operator = value;
                    return;
                }
            }
        }
        throw new Error(`Unsupported input: '${char}'`);
    }

    public getResult() {
        return this.memory;
    }
}

export function test(c: Calculator, input: string) {
    for (let i = 0; i < input.length; i++) {
        c.handleChar(input[i]);
    }

    console.log(`result of '${input}' is '${c.getResult()}'`);
}
```

这是使用暴露测试功能的计算器的简单测试。

```ts
import { Calculator, test } from "./Calculator";

let c = new Calculator();
test(c, "1+2*33/11="); // prints 9
```

现在扩展这个以添加对10以外基数的输入的支持，让我们创建ProgrammerCalculator.tsProgrammerCalculator.ts

```ts
import { Calculator } from "./Calculator";

class ProgrammerCalculator extends Calculator {
    static digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"];

    constructor(public base: number) {
        super();
        const maxBase = ProgrammerCalculator.digits.length;
        if (base <= 0 || base > maxBase) {
            throw new Error(`base has to be within 0 to ${maxBase} inclusive.`);
        }
    }

    protected processDigit(digit: string, currentValue: number) {
        if (ProgrammerCalculator.digits.indexOf(digit) >= 0) {
            return currentValue * this.base + ProgrammerCalculator.digits.indexOf(digit);
        }
    }
}

// Export the new extended calculator as Calculator
export { ProgrammerCalculator as Calculator };

// Also, export the helper function
export { test } from "./Calculator";
```

新模块ProgrammerCalculator导出类似于原始Calculator模块的API形状，但不会扩充原始模块中的任何对象。  
这是我们的ProgrammerCalculator类的测试：TestProgrammerCalculator.ts

```ts
import { Calculator, test } from "./ProgrammerCalculator";

let c = new Calculator(2);
test(c, "001+010="); // prints 3
```

### 不要在模块中使用名称空间

首次迁移到基于模块的组织时，常见的趋势是将导出包装在额外的命名空间层中。  
模块有自己的范围，只有模块外部才能看到导出的声明。  
考虑到这一点，在使用模块时，命名空间提供的值很小（如果有的话）。

在组织方面，命名空间可以方便地将全局范围内与逻辑相关的对象和类型组合在一起。  
例如，在C＃中，您将在System.Collections中找到所有集合类型。  
通过将我们的类型组织成分层命名空间，我们为这些类型的用户提供了良好的“发现”体验。  
另一方面，模块必然存在于文件系统中。  
我们必须通过路径和文件名来解决它们，因此我们可以使用逻辑组织方案。  
我们可以在 /collections/generic/文件夹中包含一个列表模块。

命名空间对于避免在全局范围内命名冲突很重要。  
例如，您可能拥有My.Application.Customer.AddForm和My.Application.Order.AddForm - 两个具有相同名称但具有不同名称空间的类型。  
然而，这不是模块的问题。  
在一个模块中，没有合理的理由让两个具有相同名称的对象。  
从消费方面来看，任何给定模块的消费者都会选择他们用来引用模块的名称，因此不可能发生意外命名冲突。

> 有关模块和命名空间的更多讨论，请参阅命名空间和模块。

以下所有内容都是模块结构的红色标志。如果其中任何一个适用于您的文件，请仔细检查您是否尝试命名外部模块：

1. 一个文件，其唯一的顶级声明是导出命名空间Foo {...}（删除Foo并将所有内容"向上移动"一个级别）  
2. 具有单个导出类或导出功能的文件（请考虑使用导出默认值）  
3. 具有相同```export namespace Foo {```的多个文件在顶层(不要认为这些将组合成一个Foo！)
