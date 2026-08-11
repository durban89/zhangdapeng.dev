---
title: "TypeScript项目引用(project references)"
date: "2025-07-09 10:42:53"
slug: "typescript-xiang-mu-yin-yong-project-references"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/09/TypeScript项目引用(project-references)/"
  - "/2025/07/09/TypeScript项目引用(project-references).html"
  - "/TypeScript项目引用(project-references)/"
  - "/TypeScript项目引用(project-references).html"
  - "/2025/07/09/TypeScript项目引用-project-references/"
  - "/2025/07/09/TypeScript项目引用-project-references.html"
  - "/2025/07/09/typescript-xiang-mu-yin-yong-project-references/"
  - "/2025/07/09/typescript-xiang-mu-yin-yong-project-references.html"
  - "/typescript-xiang-mu-yin-yong-project-references.html"
---
## TypeScript新特性之项目引用(project references)

项目引用是TypeScript 3.0中的一项新功能，允许您将TypeScript程序构建为更小的部分。

通过这样做，您可以大大缩短构建时间，实现组件之间的逻辑分离，并以新的更好的方式组织代码。

我们还为tsc引入了一种新模式，即--build标志，它与项目引用协同工作，以实现更快的TypeScript构建。

## 示例项目

让我们看一个相当正常的程序，看看项目引用如何帮助我们更好地组织它。  
想象一下，你有一个项目有两个模块，转换器和单元，以及每个模块的相应测试文件：

```bash
/src/converter.ts
/src/units.ts
/test/converter-tests.ts
/test/units-tests.ts
/tsconfig.json
```

测试文件导入实现文件并进行一些测试：

```ts
// converter-tests.ts
import * as converter from "../converter";

assert.areEqual(converter.celsiusToFahrenheit(0), 32);
```

以前，如果您使用单个tsconfig文件，则此结构很难处理：

1. 实现文件可以导入测试文件  
2. 在输出文件夹名称中没有出现src的情况下，无法同时构建test和src，这可能是您不想要的  
3. 仅更改实现文件中的内部结构需要再次检查测试，即使这不会导致新的错误  
4. 仅更改测试需要再次对实现进行检查，即使没有任何改变

您可以使用多个tsconfig文件来解决其中的一些问题，但会出现新的问题：

1. 没有内置的最新检查，因此您最终总是运行两次tsc  
2. 两次调用tsc会导致更多的启动时间开销  
3. tsc -w无法一次在多个配置文件上运行

项目引用(project references)可以解决所有这些问题等等。

## 什么是项目引用(project references)?

tsconfig.json文件有一个新的顶级属性"references"。  
它是一个对象数组，指定要引用的项目：

```json
{
    "compilerOptions": {
        // The usual
    },
    "references": [
        { "path": "../src" }
    ]
}
```

每个引用的path属性可以指向包含tsconfig.json文件的目录，也可以指向配置文件本身(可以具有任何名称)。  
当您引用项目时，会发生新的事情：

1. 从引用的项目导入模块将改为加载其输出声明文件（.d.ts）  
2. 如果引用的项目生成outFile，则输出文件.d.ts文件的声明将在此项目中可见  
3. 如果需要，构建模式(下面会提到)将自动构建引用的项目

通过分成多个项目，您可以大大提高类型检查和编译的速度，减少使用编辑器时的内存使用量，并改进程序逻辑分组的实施。

### composite

引用的项目必须启用新的composite设置。  
需要此设置以确保TypeScript可以快速确定在何处查找引用项目的输出。  
启用composite标志会改变一些事情：

1. rootDir设置（如果未显式设置）默认为包含tsconfig文件的目录  
2. 所有实现文件必须由include模式匹配或在files数组中列出。如果违反此约束，tsc将通知您未指定哪些文件  
3. declaration必须打开

### declarationMaps

我们还增加了对declaration source maps的支持。如果启用--declarationMap，您将能够使用编辑器功能，如"转到定义"和重命名，以在支持的编辑器中跨项目边界透明地导航和编辑代码。

### 以outFile为前缀

您还可以使用引用中的prepend选项启用前置依赖项的输出：

```json
"references": [
   { "path": "../utils", "prepend": true }
]
```

预先设置项目将包括项目的输出高于当前项目的输出。  
这适用于.js文件和.d.ts文件，源代码映射文件也将正确发出。

tsc只会使用磁盘上的现有文件来执行此过程，因此可以创建一个项目，其中无法生成正确的输出文件，因为某些项目的输出将在结果文件中出现多次。  
例如：

```bash
   A
  ^ ^
 /   \
B     C
 ^   ^
  \ /
   D
```

在这种情况下，重要的是不要在每个参考文献中添加前缀，因为在D的输出中最终会得到两个A副本 - 这可能会导致意外结果。

## 项目引用的注意事项

项目引用有一些您应该注意的权衡。

因为依赖项目使用从其依赖项构建的.d.ts文件，所以您必须在克隆之后签入某些构建输出或构建项目，然后才能在编辑器中导航项目而不会看到虚假错误。  
我们正在开发一个能够缓解这种情况的幕后.d.ts生成过程，但是现在我们建议告知开发人员他们应该在克隆之后构建它们。

此外，为了保持与现有构建工作流的兼容性，除非使用--build开关调用，否则tsc不会自动构建依赖项。  
让我们了解更多关于--build的信息。

## TypeScript的构建模式

期待已久的功能是TypeScript项目的智能增量构建。  
在3.0中，您可以将-build标志与tsc一起使用。  
这实际上是tsc的新入口点，其行为更像构建协调器而不是简单的编译器。

运行`tsc --build`(简称tsc -b)将执行以下操作：

1. 查找所有引用的项目  
2. 检测它们是否是最新的  
3. 按正确的顺序构建过时的项目

您可以为tsc -b提供多个配置文件路径(例如tsc -b src test)。  
就像tsc -p一样，如果命名为tsconfig.json，则不需要指定配置文件名本身。

```bash
> tsc -b                                # 在当前目录中构建tsconfig.json
> tsc -b src                            # 构建src/tsconfig.json
> tsc -b foo/release.tsconfig.json bar  # 构建foo/release.tsconfig.json和构建bar/tsconfig.json
```

不要担心您在命令行上传递的排过序的文件 - 如果需要，tsc将重新排序它们，以便始终首先构建依赖项。  
还有一些特定于tsc -b的标志：

> --verbose: 打印详细日志记录以解释正在发生的事情（可能与任何其他标志组合）  
> --dry: 显示将要完成的但实际上不构建任何内容  
> --clean: 删除指定项目的输出（可以与--dry结合使用）  
> --force: 就好像所有项目都已过时一样  
> --watch: 监视模式（除了--verbose外，不得与任何标志组合使用）

## 注意事项

通常，除非出现noEmitOnError，否则tsc将在出现语法或类型错误时生成输出（.js和.d.ts）。  
在增量构建系统中执行此操作将非常糟糕 - 如果您的一个过时的依赖项出现新错误，您只能看到它一次，因为后续构建将跳过构建现在最新的项目。  
因此，tsc -b实际上就像为所有项目启用noEmitOnError一样。  
如果您检查任何构建输出(.js，.d.ts，.d.ts.map等)，您可能需要在某些源控制操作之后运行--force构建，具体取决于源控制工具是否保留  
本地副本和远程副本之间的时间映射。

## MSBuild

如果您有msbuild项目，则可以通过添加如下代码到您的proj文件来启用构建模式

```ts
<TypeScriptBuildMode>true</TypeScriptBuildMode>
```

这将启用自动增量构建和清洁。

请注意，与tsconfig.json/-p一样，不会遵循现有的TypeScript项目属性 - 应使用tsconfig文件管理所有设置。

一些团队已经设置了基于msbuild的工作流，其中tsconfig文件与他们配对的托管项目具有相同的隐式图表排序。  
如果您的解决方案是这样的，您可以继续使用msbuild和tsc -p以及项目引用;  
这些是完全可互操作的。

## 指导(Guidance)

### 整体结构

使用更多tsconfig.json文件，您通常需要使用配置文件继承来集中您的常用编译器选项。  
这样，您可以在一个文件中更改设置，而不必编辑多个文件。

另一个好的做法是拥有一个"解决方案"tsconfig.json文件，该文件只引用了所有leaf-node项目。  
这提供了一个简单的切入点;  
例如，在TypeScript repo中，我们只运行tsc -b src来构建所有端点，因为我们列出了src/tsconfig.json中的所有子项目。请注意，从3.0开始，如果在tsconfig.json中至少有一个reference将不会针对空的files数组报错

您可以在TypeScript存储库中看到这些模式 - `src/tsconfig_base.json`，`src/tsconfig.json`和`src/tsc/tsconfig.json`作为关键示例。

### *构建相关模块*

通常，使用相关模块transition a repo并不需要太多。  
只需将tsconfig.json文件放在给定父文件夹的每个子目录中，并添加对这些配置文件的引用以匹配程序的预期分层。  
您需要将outDir设置为输出文件夹的显式子文件夹，或将rootDir设置为所有项目文件夹的公共根目录。

### *构建outFiles*

使用outFile进行编译的布局更灵活，因为相对路径无关紧要。  
要记住的一件事是，您通常希望在"最后"项目之前不使用前置 - 这将改善构建时间并减少任何给定构建中所需的I/O量。  
TypeScript repo本身就是一个很好的参考 - 我们有一些"库"项目和一些"端点"项目;  
"端点"项目尽可能小，只吸引他们需要的库。

原文地址：  
http://www.typescriptlang.org/docs/handbook/project-references.html
