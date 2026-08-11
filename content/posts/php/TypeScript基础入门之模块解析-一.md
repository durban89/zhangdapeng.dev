---
title: "TypeScript基础入门之模块解析(一)"
date: "2025-07-10 10:23:24"
slug: "typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之模块解析(一)/"
  - "/2025/07/10/TypeScript基础入门之模块解析(一).html"
  - "/TypeScript基础入门之模块解析(一)/"
  - "/TypeScript基础入门之模块解析(一).html"
  - "/2025/07/10/TypeScript基础入门之模块解析-一/"
  - "/2025/07/10/TypeScript基础入门之模块解析-一.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-yi/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-yi.html"
  - "/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-yi.html"
---
## 模块解析

> 本节假设有关模块的一些基本知识。有关更多信息，请参阅模块文档。

模块解析是编译器用来确定导入所引用内容的过程。  
考虑一个导入语句，如`import { a } from "moduleA";`  
为了检查a的任何使用，编译器需要确切地知道它代表什么，并且需要检查它的定义moduleA。

此时，编译器将询问"moduleA的类型是什么？“虽然这听起来很简单，但是moduleA可以在您自己的.ts/.tsx文件中定义，或者在您的代码所依赖的.d.ts中定义。

首先，编译器将尝试查找表示导入模块的文件。  
为此，编译器遵循两种不同策略之一：Classic或Node。  
这些策略告诉编译器在哪里寻找moduleA。

如果这不起作用并且模块名称是非相对的（并且在"moduleA"的情况下，则是），则编译器将尝试查找环境模块声明。  
接下来我们将介绍非相对进口。

最后，如果编译器无法解析模块，它将记录错误。  
在这种情况下，错误就像`error TS2307: Cannot find module 'moduleA'`

### 相对与非相对模块导入

根据模块引用是相对引用还是非相对引用，模块导入的解析方式不同。

相对导入是以/、./或../开头的导入。  
一些例子包括：

* import Entry from "./components/Entry";
* import { DefaultHeaders } from "../constants/http";
* import "/mod";

任何其他import都被视为非亲属。  
一些例子包括：

* import \* as $ from "jquery";
* import { Component } from "@angular/core";

相对导入是相对于导入文件解析的，无法解析为环境模块声明。  
您应该为自己的模块使用相对导入，这些模块可以保证在运行时保持其相对位置。

可以相对于baseUrl或通过路径映射解析非相对导入，我们将在下面介绍。  
他们还可以解析为环境模块声明。  
导入任何外部依赖项时，请使用非相对路径。

### 模块解决策略

有两种可能的模块解析策略：Node和Classic。  
您可以使用--moduleResolution标志指定模块解析策略。  
如果未指定，则默认为Classic for `--module AMD | System | ES2015`或其他Node。

### *Classic 策略*

这曾经是TypeScript的默认解析策略。  
如今，这种策略主要用于向后兼容。

将相对于导入文件解析相对导入。  
因此，从源文件/root/src/folder/A.ts中的`import { b } from "./moduleB"`将导致以下查找：

* /root/src/folder/moduleB.ts
* /root/src/folder/moduleB.d.ts

但是，对于非相对模块导入，编译器会从包含导入文件的目录开始遍历目录树，尝试查找匹配的定义文件。

例如：

在源文件/root/src/folder/A.ts中对moduleB进行非相对导入(例如`import { b } from "moduleB")`将导致尝试以下位置来定位"moduleB"：

* /root/src/folder/moduleB.ts
* /root/src/folder/moduleB.d.ts
* /root/src/moduleB.ts
* /root/src/moduleB.d.ts
* /root/moduleB.ts
* /root/moduleB.d.ts
* /moduleB.ts
* /moduleB.d.ts

### *Node 策略*

他的解析策略试图在运行时模仿Node.js模块解析机制。Node.js模块文档中概述了完整的Node.js解析算法。

**Node.js如何解析模块**

要了解TS编译器将遵循的步骤，重要的是要阐明Node.js模块。  
传统上，Node.js中的导入是通过调用名为require的函数来执行的。  
Node.js采取的行为将根据require是否给定相对路径或非相对路径而有所不同。

相对路径相当简单。  
例如，让我们考虑位于`/root/src/moduleA.js`的文件，其中包含import `var x = require("./ moduleB");`  
Node.js按以下顺序解析导入：

1. 询问名为`/root/src/moduleB.js`的文件（如果存在）。  
2. 询问文件夹`/root/src/moduleB`是否包含名为package.json的文件，该文件指定了"main"模块。在我们的示例中，如果Node.js找到包含`{"main": "lib/mainModule.js"}`的文件`/root/src/moduleB/package.json`，那么Node.js将引用`/root/src/moduleB/lib/mainModule.js`。  
3. 询问文件夹/root/src/moduleB是否包含名为index.js的文件。该文件被隐含地视为该文件夹的"main"模块。

您可以在Node.js文档中了解有关文件模块和文件夹模块的更多信息。

但是，非相对模块名称的解析以不同方式执行。  
Node将在名为node\_modules的特殊文件夹中查找模块。  
node\_modules文件夹可以与当前文件位于同一级别，或者在目录链中位于更高级别。  
Node将走向目录链，查看每个node\_modules，直到找到您尝试加载的模块。

按照上面的示例，考虑是否`/root/src/moduleA.js`使用非相对路径并且导入`var x = require("moduleB");`然后，Node会尝试将moduleB解析到每个位置，直到一个工作。

* /root/src/node\_modules/moduleB.js
* /root/src/node\_modules/moduleB/package.json (if it specifies a "main" property)
* /root/src/node\_modules/moduleB/index.js
* /root/node\_modules/moduleB.js
* /root/node\_modules/moduleB/package.json (if it specifies a "main" property)
* /root/node\_modules/moduleB/index.js
* /node\_modules/moduleB.js
* /node\_modules/moduleB/package.json (if it specifies a "main" property)
* /node\_modules/moduleB/index.js

请注意，Node.js在步骤(4)和(7)中跳过了一个目录。

您可以在Node.js文档中阅读有关从node\_modules加载模块的过程的更多信息。

**TypeScript如何解析模块**

TypeScript将模仿Node.js运行时解析策略，以便在编译时定位模块的定义文件。  
为此，TypeScript通过Node的解析逻辑覆盖TypeScript源文件扩展名(.ts、.tsx和.d.ts)。  
TypeScript还将使用package.json中名为"types"的字段来镜像"main"的目的 - 编译器将使用它来查找要查询的"main"定义文件。

例如，`/root/src/moduleA.ts`中的`import { b } from "./moduleB"`等导入语句将导致尝试以下位置来定位"./moduleB"：

* /root/src/moduleB.ts
* /root/src/moduleB.tsx
* /root/src/moduleB.d.ts
* /root/src/moduleB/package.json (if it specifies a "types" property)
* /root/src/moduleB/index.ts
* /root/src/moduleB/index.tsx
* /root/src/moduleB/index.d.ts

回想一下，Node.js查找名为moduleB.js的文件，然后查找适用的package.json，然后查找index.js。

类似地，非相对导入将遵循Node.js解析逻辑，首先查找文件，然后查找适用的文件夹。  
因此，从源文件`/root/src/moduleA.ts`中的`import { b } from "moduleB"`将导致以下查找：

* /root/src/node\_modules/moduleB.ts
* /root/src/node\_modules/moduleB.tsx
* /root/src/node\_modules/moduleB.d.ts
* /root/src/node\_modules/moduleB/package.json (if it specifies a "types" property)
* /root/src/node\_modules/moduleB/index.ts
* /root/src/node\_modules/moduleB/index.tsx
* /root/src/node\_modules/moduleB/index.d.ts
* /root/node\_modules/moduleB.ts
* /root/node\_modules/moduleB.tsx
* /root/node\_modules/moduleB.d.ts
* /root/node\_modules/moduleB/package.json (if it specifies a "types" property)
* /root/node\_modules/moduleB/index.ts
* /root/node\_modules/moduleB/index.tsx
* /root/node\_modules/moduleB/index.d.ts
* /node\_modules/moduleB.ts
* /node\_modules/moduleB.tsx
* /node\_modules/moduleB.d.ts
* /node\_modules/moduleB/package.json (if it specifies a "types" property)
* /node\_modules/moduleB/index.ts
* /node\_modules/moduleB/index.tsx
* /node\_modules/moduleB/index.d.ts

不要被这里的步骤数吓倒 - TypeScript仍然只在步骤(8)和(15)两次跳过目录。  
这实际上并不比Node.js本身正在做的复杂。

**附加模块分辨率标志**

项目源布局有时与输出的布局不匹配。  
通常，一组构建步骤会导致生成最终输出。  
这些包括将.ts文件编译为.js，以及将不同源位置的依赖项复制到单个输出位置。  
最终结果是运行时的模块可能具有与包含其定义的源文件不同的名称。  
或者，在编译时，最终输出中的模块路径可能与其对应的源文件路径不匹配。

TypeScript编译器具有一组附加标志，用于通知编译器预期发生在源上的转换以生成最终输出。

重要的是要注意编译器不会执行任何这些转换;  
它只是使用这些信息来指导将模块导入解析到其定义文件的过程。

未完待续...
