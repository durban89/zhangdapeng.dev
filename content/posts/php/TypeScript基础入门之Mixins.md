---
title: "TypeScript基础入门之Mixins"
date: "2025-07-10 10:24:12"
slug: "typescript-ji-chu-ru-men-zhi-mixins"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之Mixins/"
  - "/2025/07/10/TypeScript基础入门之Mixins.html"
  - "/TypeScript基础入门之Mixins/"
  - "/TypeScript基础入门之Mixins.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mixins/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mixins.html"
  - "/typescript-ji-chu-ru-men-zhi-mixins.html"
---
### 介绍

与传统的OO层次结构一起，另一种从可重用组件构建类的流行方法是通过组合更简单的部分类来构建它们。  
您可能熟悉Scala等语言的mixin或traits的概念，并且该模式在JavaScript社区中也已经普及。

### Mixin示例

在下面的代码中，我们将展示如何在TypeScript中对mixin进行建模。  
在代码之后，我们将分解其工作原理。

```ts
// Disposable Mixin
class Disposable {
    isDisposed: boolean;
    dispose() {
        this.isDisposed = true;
    }

}

// Activatable Mixin
class Activatable {
    isActive: boolean;
    activate() {
        this.isActive = true;
    }
    deactivate() {
        this.isActive = false;
    }
}

class SmartObject implements Disposable, Activatable {
    constructor() {
        setInterval(() => console.log(this.isActive + " : " + this.isDisposed), 500);
    }

    interact() {
        this.activate();
    }

    // Disposable
    isDisposed: boolean = false;
    dispose: () => void;
    // Activatable
    isActive: boolean = false;
    activate: () => void;
    deactivate: () => void;
}
applyMixins(SmartObject, [Disposable, Activatable]);

let smartObj = new SmartObject();
setTimeout(() => smartObj.interact(), 1000);

////////////////////////////////////////
// In your runtime library somewhere
////////////////////////////////////////

function applyMixins(derivedCtor: any, baseCtors: any[]) {
    baseCtors.forEach(baseCtor => {
        Object.getOwnPropertyNames(baseCtor.prototype).forEach(name => {
            derivedCtor.prototype[name] = baseCtor.prototype[name];
        });
    });
}
```

### 理解示例

代码示例以两个类作为我们的mixins开始。  
您可以看到每个人都专注于特定的活动或能力。  
我们稍后将它们混合在一起，形成两种功能的新类。

```javascript
// Disposable Mixin
class Disposable {
    isDisposed: boolean;
    dispose() {
        this.isDisposed = true;
    }

}

// Activatable Mixin
class Activatable {
    isActive: boolean;
    activate() {
        this.isActive = true;
    }
    deactivate() {
        this.isActive = false;
    }
}
```

接下来，我们将创建将处理两个mixin组合的类。  
让我们更详细地看一下它是如何做到的：

```ts
class SmartObject implements Disposable, Activatable {
```

您可能在上面注意到的第一件事是，我们使用工具而不是使用扩展。  
这将类视为接口，并且仅使用Disposable和Activatable后面的类型而不是实现。  
这意味着我们必须在课堂上提供实现。  
除此之外，这正是我们想要通过使用mixins避免的。

为了满足这一要求，我们为来自mixin的成员创建了替身属性及其类型。  
这使编译器满足这些成员在运行时可用。  
这让我们仍然可以获得mixins的好处，尽管有一些簿记开销。

```ts
// Disposable
isDisposed: boolean = false;
dispose: () => void;
// Activatable
isActive: boolean = false;
activate: () => void;
deactivate: () => void;
```

最后，我们将mixin混合到类中，创建完整的实现。

```ts
applyMixins(SmartObject, [Disposable, Activatable]);
```

最后，我们创建了一个辅助函数，它将为我们进行混合。  
这将贯穿每个mixin的属性并将它们复制到mixins的目标，并使用它们的实现填充替代属性。

```ts
function applyMixins(derivedCtor: any, baseCtors: any[]) {
    baseCtors.forEach(baseCtor => {
        Object.getOwnPropertyNames(baseCtor.prototype).forEach(name => {
            derivedCtor.prototype[name] = baseCtor.prototype[name];
        });
    });
}
```
