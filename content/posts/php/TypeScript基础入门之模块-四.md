---
title: "TypeScript基础入门之模块(四)"
date: "2025-07-09 10:43:14"
slug: "typescript-ji-chu-ru-men-zhi-mo-kuai-si"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript基础入门之模块(四)/"
  - "/2025/07/09/TypeScript基础入门之模块(四).html"
  - "/TypeScript基础入门之模块(四)/"
  - "/TypeScript基础入门之模块(四).html"
  - "/2025/07/09/TypeScript基础入门之模块-四/"
  - "/2025/07/09/TypeScript基础入门之模块-四.html"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-si/"
  - "/2025/07/09/typescript-ji-chu-ru-men-zhi-mo-kuai-si.html"
  - "/typescript-ji-chu-ru-men-zhi-mo-kuai-si.html"
---
## 使用其他JavaScript库

要描述不是用TypeScript编写的库的形状，我们需要声明库公开的API。  
我们称之为未定义实现"环境"的声明。  
通常，这些是在.d.ts文件中定义的。  
如果您熟悉C/C++，可以将它们视为.h文件。  
我们来看几个例子。

### 外部模块

在Node.js中，大多数任务是通过加载一个或多个模块来完成的。  
我们可以使用顶级导出声明在自己的.d.ts文件中定义每个模块，但将它们编写为一个较大的.d.ts文件会更方便。  
为此，我们使用类似于环境名称空间的构造，但我们使用模块关键字和模块的引用名称，以便稍后导入。  
例如：

node.d.ts (simplified excerpt)

```ts
declare module "url" {
  export interface Url {
    protocol?: string;
    hostname?: string;
    pathname?: string;
  }

  export function parse(urlStr: string, parseQueryString?, slashesDenoteHost?): Url;
}

declare module "path" {
  export function normalize(p: string): string;
  export function join(...paths: any[]): string;
  export var sep: string;
}
```

现在我们可以`/// <reference> node.d.ts`并且使用`import url = require("url");`或`import * as URL from "url"`加载模块。

```ts
/// <reference path="node.d.ts" />
import * as URL from "url";

let testUrl = URL.parse("https://www.gowhich.com");
```

### 外部模块简写

如果您不想在使用新模块之前花时间写出声明，则可以使用速记声明快速入门。  
declarations.d.ts

```ts
declare module "hot-new-module";
```

从速记模块导入的所有内容都将具有any类型

```ts
import x, {y} from "hot-new-module";
x(y);
```

### 通配符模块声明

某些模块加载器(如SystemJS和AMD)允许导入非JavaScript内容。  
这些通常使用前缀或后缀来指示特殊的加载语义。  
通配符模块声明可用于涵盖这些情况。

```ts
declare module "*!text" {
    const content: string;
    export default content;
}
// Some do it the other way around.
declare module "json!*" {
  const value: any;
  export default value;
}
```

现在您可以导入与"\*text"或"json\*"匹配的内容。

```ts
import fileContent from "./xyz.txt!text";
import data from "json!http://example.com/data.json";
console.log(data, fileContent);
```

### UMD模块

有些库设计用于许多模块加载器，或者没有模块加载（全局变量）。  
这些被称为UMD模块。  
可以通过导入或全局变量访问这些库。  
例如：

math-lib.d.ts

```ts
export function isPrime(x: number): boolean;
export as namespace mathLib;
```

然后，该库可用作模块中的导入：

```ts
import { isPrime } from "math-lib";
isPrime(2);
mathLib.isPrime(2); // ERROR: can't use the global definition from inside a module
```

它也可以用作全局变量，但仅限于脚本内部。（脚本是没有导入或导出的文件。）

```ts
mathLib.isPrime(2);
```
