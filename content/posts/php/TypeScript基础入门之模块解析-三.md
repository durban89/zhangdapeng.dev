---
title: "TypeScript基础入门之模块解析(三)"
date: "2025-07-10 10:23:37"
slug: "typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-san"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之模块解析(三)/"
  - "/2025/07/10/TypeScript基础入门之模块解析(三).html"
  - "/TypeScript基础入门之模块解析(三)/"
  - "/TypeScript基础入门之模块解析(三).html"
  - "/2025/07/10/TypeScript基础入门之模块解析-三/"
  - "/2025/07/10/TypeScript基础入门之模块解析-三.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-san/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-san.html"
  - "/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-san.html"
---
继续上文[[TypeScript基础入门之模块解析(二)](https://www.gowhich.com/blog/946)]

## 跟踪模块解析

如前所述，编译器可以在解析模块时访问当前文件夹之外的文件。  
在诊断模块未解析的原因或解析为错误定义时，这可能很难。  
使用--traceResolution启用编译器模块分辨率跟踪可以深入了解模块解析过程中发生的情况。

假设我们有一个使用typescript模块的示例应用程序。  
app.ts有一个导入，比如import \* as ts from "typescript"。

```bash
│   tsconfig.json
├───node_modules
│   └───typescript
│       └───lib
│               typescript.d.ts
└───src
    └───app.ts
```

### 使用--traceResolution调用编译器

```bash
tsc --traceResolution
```

输出结果如下：

```bash
======== Resolving module 'typescript' from 'src/app.ts'. ========
Module resolution kind is not specified, using 'NodeJs'.
Loading module 'typescript' from 'node_modules' folder.
File 'src/node_modules/typescript.ts' does not exist.
File 'src/node_modules/typescript.tsx' does not exist.
File 'src/node_modules/typescript.d.ts' does not exist.
File 'src/node_modules/typescript/package.json' does not exist.
File 'node_modules/typescript.ts' does not exist.
File 'node_modules/typescript.tsx' does not exist.
File 'node_modules/typescript.d.ts' does not exist.
Found 'package.json' at 'node_modules/typescript/package.json'.
'package.json' has 'types' field './lib/typescript.d.ts' that references 'node_modules/typescript/lib/typescript.d.ts'.
File 'node_modules/typescript/lib/typescript.d.ts' exist - use it as a module resolution result.
======== Module name 'typescript' was successfully resolved to 'node_modules/typescript/lib/typescript.d.ts'. ========
```

值得关注的事情

1. 导入的名称和位置

```bash
======== Resolving module 'typescript' from 'src/app.ts'. ========
```

2. 编译器遵循的策略

```bash
Module resolution kind is not specified, using 'NodeJs'.
```

3. 从npm包加载类型

```bash
'package.json' has 'types' field './lib/typescript.d.ts' that references 'node_modules/typescript/lib/typescript.d.ts'.
```

4. 最后结果

```bash
======== Module name ‘typescript’ was successfully resolved to ‘node_modules/typescript/lib/typescript.d.ts’. ========
```

### 使用--noResolve

通常，编译器将在启动编译过程之前尝试解析所有模块导入。  
每次成功解析导入到文件时，该文件都会添加到编译器稍后将处理的文件集中。

--noResolve编译器选项指示编译器不要将任何文件"add"到未在命令行上传递的编译中。  
它仍将尝试将模块解析为文件，但如果未指定该文件，则不会包含该文件。

例如:

app.ts

```ts
import * as A from "moduleA" // OK, 'moduleA' passed on the command-line
import * as B from "moduleB" // Error TS2307: Cannot find module 'moduleB'.
```

```bash
tsc app.ts moduleA.ts --noResolve
```

使用--noResolve编译app.ts应该导致：  
1. 正确查找在命令行上传递的moduleA。  
2. 找不到未通过的moduleB时出错。

### 常见问题

为什么排除列表中的模块仍然被编译器拾取？

tsconfig.json将文件夹转换为"project"。如果不指定任何"exclude"或"files"条目，则包含tsconfig.json及其所有子目录的文件夹中的所有文件都包含在编译中。  
如果要排除某些文件使用"exclude"，如果您希望指定所有文件而不是让编译器查找它们，请使用"files"。

那是tsconfig.json自动包含。  
这并没有嵌入上面讨论的模块解析。  
如果编译器将文件标识为模块导入的目标，则无论它是否在前面的步骤中被排除，它都将包含在编译中。

因此，要从编译中排除文件，您需要将其和所有具有import或`/// <reference path ="..."/>`指令的文件排除在外。
