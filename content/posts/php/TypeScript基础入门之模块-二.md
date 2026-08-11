---
title: "TypeScript基础入门之模块(二)"
date: "2025-07-09 10:43:08"
slug: "typescript-ji-chu-ru-men-zhi-mo-kuai-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之模块(二)/"
  - "/2025/07/09/TypeScript基础入门之模块(二).html"
  - "/TypeScript基础入门之模块(二)/"
  - "/TypeScript基础入门之模块(二).html"
  - "/2025/07/09/TypeScript基础入门之模块-二/"
  - "/2025/07/09/TypeScript基础入门之模块-二.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-er/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-er.html"
  - "/typescript-ji-chu-ru-men-zhi-mo-kuai-er.html"
---
## 生成模块代码

根据编译期间指定的模块目标，编译器将为Node.js（CommonJS），require.js（AMD），UMD，SystemJS或ECMAScript 2015本机模块（ES6）模块加载系统生成适当的代码。  
有关生成的代码中的define, require 和 register调用的更多信息，请参阅每个模块加载器的文档。

下面这个简单的示例展示了导入和导出期间使用的名称如何转换为模块加载代码。

SimpleModule.ts

```ts
import m = require("mod");
export let t = m.something + 1;
```

AMD/RequireJS SimpleModule.js

```js
define(["require", "exports", "./mod"], function (require, exports, mod_1) {
    exports.t = mod_1.something + 1;
});
```

CommonJS/Node SimpleModule.js

```ts
var mod_1 = require("./mod");
exports.t = mod_1.something + 1;
```

UMD SimpleModule.js

```js
(function (factory) {
    if (typeof module === "object" && typeof module.exports === "object") {
        var v = factory(require, exports); if (v !== undefined) module.exports = v;
    }
    else if (typeof define === "function" && define.amd) {
        define(["require", "exports", "./mod"], factory);
    }
})(function (require, exports) {
    var mod_1 = require("./mod");
    exports.t = mod_1.something + 1;
});
```

System SimpleModule.js

```js
System.register(["./mod"], function(exports_1) {
    var mod_1;
    var t;
    return {
        setters:[
            function (mod_1_1) {
                mod_1 = mod_1_1;
            }],
        execute: function() {
            exports_1("t", t = mod_1.something + 1);
        }
    }
});
```

Native ECMAScript 2015 modules SimpleModule.js

```js
import { something } from "./mod";
export var t = something + 1;
```

## 简单实例

下面，我们整合了前面【TypeScript基础入门之模块(一)】文章中使用的Validator实现，只导出每个模块的单个命名导出。

要编译，我们必须在命令行上指定模块目标。  
对于Node.js，使用--module commonjs;  
对于require.js，请使用--module amd。如下

```bash
tsc --module commonjs Test.ts
```

编译时，每个模块将成为一个单独的.js文件。  
与引用标记一样，编译器将遵循import语句来编译依赖文件。Validation.ts

```ts
export interface StringValidator {
  isAcceptable(s: string): boolean;
}
```

ZipCodeValidator.ts

```ts
import { StringValidator } from './Validation';

export const numberRegexp = /^[0-9]+$/;

export class ZipCodeValidator implements StringValidator {
  isAcceptable(s: string): boolean {
    return s.length === 5 && numberRegexp.test(s);
  }
}
```

LettersOnlyValidator.ts

```ts
import { StringValidator } from './Validation';

const letterRegexp = /^[A-Za-z]+/;

export class LettersOnlyValidator implements StringValidator {
  isAcceptable(s: string): boolean {
    return letterRegexp.test(s);
  }
}
```

Test.ts

```ts
import { StringValidator } from './Validation';
import { ZipCodeValidator } from './ZipCodeValidator';
import { LettersOnlyValidator } from './LettersOnlyValidator';

// 测试数据
let strings = ["Hello", "98052", "101"];
// 
let validators:{ [s: string]: StringValidator } = {};
validators["zip code validator"] = new ZipCodeValidator();
validators["letter validator"] = new LettersOnlyValidator();

strings.forEach((e) => {
  for (let name in validators) {
    console.log(`"${e}" - ${ validators[name].isAcceptable(e) ? "matches" : 'does not match'} ${name}`)
  }
});
```

编译后运行得到如下结果

```bash
"Hello" - does not match zip code validator
"Hello" - matches letter validator
"98052" - matches zip code validator
"98052" - does not match letter validator
"101" - does not match zip code validator
"101" - does not match letter validator
```
