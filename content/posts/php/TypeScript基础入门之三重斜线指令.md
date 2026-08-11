---
title: "TypeScript基础入门之三重斜线指令"
date: "2025-07-10 10:24:14"
slug: "typescript-ji-chu-ru-men-zhi-san-chong-xie-xian-zhi-ling"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之三重斜线指令/"
  - "/2025/07/10/TypeScript基础入门之三重斜线指令.html"
  - "/TypeScript基础入门之三重斜线指令/"
  - "/TypeScript基础入门之三重斜线指令.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-san-chong-xie-xian-zhi-ling/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-san-chong-xie-xian-zhi-ling.html"
  - "/typescript-ji-chu-ru-men-zhi-san-chong-xie-xian-zhi-ling.html"
---
三斜杠指令是包含单个XML标记的单行注释。 注释的内容用作编译器指令。

三斜杠指令仅在其包含文件的顶部有效。 三重斜杠指令只能在单行或多行注释之前，包括其他三重斜杠指令。 如果在声明或声明之后遇到它们，则将它们视为常规单行注释，并且没有特殊含义。

**`/// <reference path ="..."/>`**

`/// <reference path ="..."/>`指令是该组中最常见的。 它充当文件之间的依赖声明。

三斜杠引用指示编译器在编译过程中包含其他文件。

它们还可以作为在使用–out或–outFile时对输出进行排序的方法。 在预处理传递之后，文件以与输入相同的顺序发送到输出文件位置。

该过程从一组根文件开始; 这些是在命令行或tsconfig.json文件的”files”列表中指定的文件名。 这些根文件按照指定的顺序进行预处理。 在将文件添加到列表之前，将处理其中的所有三重斜杠引用，并包括其目标。 三重斜杠引用按照它们在文件中看到的顺序以深度优先方式解析。

如果无根则，则相对于包含文件解析三斜杠参考路径。

*错误*

引用不存在的文件是错误的。 如果文件具有对自身的三斜杠引用，则会出错。

*使用–noResolve*

如果指定了编译器标志–noResolve，则忽略三次斜杠引用; 它们既不会导致添加新文件，也不会更改所提供文件的顺序。

***/// <reference types="..." />***

类似于`/// <reference path ="..."/>`指令，该指令用作依赖声明; 但是，`/// <references types ="..."/>`指令声明了对包的依赖性。

解析这些包名称的过程类似于在import语句中解析模块名称的过程。 考虑三重斜杠引用类型指令的简单方法是作为声明包的导入。

例如，在声明文件中包含`/// <references types ="node"/>`声明此文件使用在[types/node](https://github.com/types/node)/index.d.ts中声明的名称; 因此，此包需要与声明文件一起包含在编译中。

只有在手动创建d.ts文件时才使用这些指令。

对于编译期间生成的声明文件，编译器会自动为您添加`/// <references types ="..."/>`; 当且仅当生成的文件使用引用包中的任何声明时，才会添加生成的声明文件中的`/// <reference types ="..."/>`。

***/// <reference lib="..." />***

该指令允许文件显式包含现有的内置lib文件。

内置的lib文件以与tsconfig.json中的”lib”编译器选项相同的方式引用（例如，使用lib=”es2015”而不是lib=”lib.es2015.d.ts”等）。

对于在内置类型上进行中继的声明文件作者，例如 建议使用DOM API或内置的JS运行时构造函数（如Symbol或Iterable，三斜杠引用lib指令）。 以前这些.d.ts文件必须添加此类型的前向/重复声明。

例如，将`/// <reference lib="es2017.string"/>`添加到编译中的一个文件等效于使用–lib es2017.string进行编译。

```javascript
/// <reference lib="es2017.string" />

"foo".padStart(4);
```

***/// <reference no-default-lib="true"/>***

该指令将文件标记为默认库。 您将在lib.d.ts及其不同变体的顶部看到此注释。

该指令指示编译器不在编译中包含默认库（即lib.d.ts）。 这里的影响类似于在命令行上传递–noLib。

另请注意，在传递–skipDefaultLibCheck时，编译器将仅跳过使用`/// <reference no-default-lib ="true"/>`检查文件。

***/// <amd-module />***

默认情况下，AMD模块是匿名生成的。 当使用其他工具处理结果模块（例如捆绑器（例如r.js））时，这会导致问题。

amd-module指令允许将可选模块名称传递给编译器：

amdModule.ts

```javascript
///<amd-module name="NamedModule"/>
export class C {
}
```

将导致将名称NamedModule分配给模块作为调用AMD定义的一部分：

amdModule.js

```javascript
define("NamedModule", ["require", "exports"], function (require, exports) {
    var C = (function () {
        function C() {
        }
        return C;
    })();
    exports.C = C;
});
```

***/// <amd-dependency />***

> 注意：此指令已被弃用。使用import”moduleName”;而是声明。

`/// <amd-dependency path ="x"/>`通知编译器需要在结果模块的require调用中注入的非TS模块依赖项。

amd-dependency指令也可以有一个可选的name属性; 这允许传递amd依赖的可选名称：

```javascript
/// <amd-dependency path="legacy/moduleA" name="moduleA"/>
declare var moduleA:MyType
moduleA.callStuff()
```

生成的JS代码：

```javascript
define(["require", "exports", "legacy/moduleA"], function (require, exports, moduleA) {
    moduleA.callStuff()
});
```
