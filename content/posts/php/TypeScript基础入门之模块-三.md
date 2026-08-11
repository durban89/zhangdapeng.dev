---
title: "TypeScript基础入门之模块(三)"
date: "2025-07-09 10:43:12"
slug: "typescript-ji-chu-ru-men-zhi-mo-kuai-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之模块(三)/"
  - "/2025/07/09/TypeScript基础入门之模块(三).html"
  - "/TypeScript基础入门之模块(三)/"
  - "/TypeScript基础入门之模块(三).html"
  - "/2025/07/09/TypeScript基础入门之模块-三/"
  - "/2025/07/09/TypeScript基础入门之模块-三.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-san/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-san.html"
  - "/typescript-ji-chu-ru-men-zhi-mo-kuai-san.html"
---
## 可选模块加载和其他高级加载方案

在某些情况下，您可能只想在某些条件下加载模块。在TypeScript中，我们可以使用下面显示的模式来实现此模式和其他高级加载方案，以直接调用模块加载器而不会丢失类型安全性。

编译器检测是否生成的JavaScript中使用了每个模块。如果模块标识符仅用作类型注释的一部分而从不用作表达式，则不会为该模块生成require调用。这种未使用的引用的省略是一种良好的性能优化，并且还允许可选地加载这些模块。

该模式的核心思想是`import id = require("...")`语句使我们能够访问模块公开的类型。  
模块加载器是动态调用的(通过require)，如下面的if块所示。  
这利用了参考省略优化，因此模块仅在需要时加载。  
为了使这个模式起作用，重要的是通过导入定义的符号仅用于类型位置(即从不在将被生成到JavaScript中的位置)。  
为了保持类型安全，我们可以使用typeof关键字。  
typeof关键字在类型位置使用时会生成值的类型，在本例中为模块的类型。

**\*\*示例：Node.js里的动态模块加载\*\***

```ts
declare function require(moduleName: string): any;

import { ZipCodeValidator as Zip } from "./ZipCodeValidator";

if (needZipValidation) {
    let ZipCodeValidator: typeof Zip = require("./ZipCodeValidator");
    let validator = new ZipCodeValidator();
    if (validator.isAcceptable("...")) { /* ... */ }
}
```

**\*\*示例：require.js里的动态模块加载\*\***

```ts
declare function require(moduleNames: string[], onLoad: (...args: any[]) => void): void;

import * as Zip from "./ZipCodeValidator";

if (needZipValidation) {
    require(["./ZipCodeValidator"], (ZipCodeValidator: typeof Zip) => {
        let validator = new ZipCodeValidator.ZipCodeValidator();
        if (validator.isAcceptable("...")) { /* ... */ }
    });
}
```

**\*\*示例：System.js里的动态模块加载\*\***

```ts
declare const System: any;

import { ZipCodeValidator as Zip } from "./ZipCodeValidator";

if (needZipValidation) {
    System.import("./ZipCodeValidator").then((ZipCodeValidator: typeof Zip) => {
        var x = new ZipCodeValidator();
        if (x.isAcceptable("...")) { /* ... */ }
    });
}
```
