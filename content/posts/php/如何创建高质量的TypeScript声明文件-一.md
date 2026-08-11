---
title: "如何创建高质量的TypeScript声明文件(一)"
date: "2025-07-10 10:56:45"
slug: "ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-yi"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(一)/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件(一).html"
  - "/如何创建高质量的TypeScript声明文件(一)/"
  - "/如何创建高质量的TypeScript声明文件(一).html"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-一/"
  - "/2025/07/10/如何创建高质量的TypeScript声明文件-一.html"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-yi/"
  - "/2025/07/10/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-yi.html"
  - "/ru-he-chuang-jian-gao-zhi-liang-de-typescript-sheng-ming-wen-jian-yi.html"
---
### 库结构

“库结构”可帮助您了解常用库格式以及如何为每种格式编写正确的声明文件。 如果您正在编辑现有文件，则可能不需要阅读这篇文章。 新声明文件的作者必须阅读本篇文章以正确理解库的格式如何影响声明文件的写入。

**介绍**

从广义上讲，构造声明文件的方式取决于库的使用方式。 有许多方法可以在JavaScript中提供供消费的库，你需要编写你的声明文件来匹配它。 本篇文章介绍了如何识别公共库模式，以及如何编写与该模式对应的声明文件。

每种类型的主要库结构模式在“模板”部分中都有相应的文件。 您可以从这些模板开始，以帮助您更快地前进。

**识别各种库的类型**

首先，我们将回顾TypeScript声明文件可以表示的库类型。 我们将简要介绍如何使用各种库，如何编写，以及列出现实世界中的一些示例库。

识别库的结构是编写其声明文件的第一步。 我们将根据其用法和代码给出关于如何识别结构的提示。 根据图书馆的文档和组织，一个可能比另一个更容易。 我们建议您使用哪种方式更舒适。

*全局库*

全局库是可以从全局范围访问的库（即不使用任何形式的导入）。 许多库只是公开一个或多个全局变量以供使用。 例如，如果您使用的是jQuery，只需引用它就可以使用$变量：

您通常会在全局库的文档中看到如何在HTML脚本标记中使用库的指导：

```html
<script src="http://a.great.cdn.for/someLib.js"></script>
```

今天，大多数流行的全球可访问库实际上都是作为UMD库编写的（见下文）。 UMD库文档很难与全局库文档区分开来。 在编写全局声明文件之前，请确保该库实际上不是UMD。

*从代码中识别全局库*

全局库代码通常非常简单。 全局“Hello，world”库可能如下所示：

```ts
function createGreeting(s) {
    return "Hello, " + s;
}
```

或者像这样：

```ts
window.createGreeting = function(s) {
    return "Hello, " + s;
}
```

查看全局库的代码时，您通常会看到：

* 顶级var语句或函数声明
* window.someName的一个或多个赋值
* 存在DOM原语（如文档或窗口）的假设

你不会看到：

* 检查或使用模块加载器，如require或define
* CommonJS/Node.js样式导入形式var fs = require（"fs"）;
* 调用define(...)
* 描述如何require或import库的文档

*全局库的例子*

因为将全局库转换为UMD库通常很容易，所以很少有流行的库仍然以全局风格编写。 但是，小而且需要DOM（或没有依赖关系）的库可能仍然是全局的。

*全局库模板*

模板文件global.d.ts定义了一个示例库myLib。 请务必阅读"防止名称冲突"脚注。

未完待续...
