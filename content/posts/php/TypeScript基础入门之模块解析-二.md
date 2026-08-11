---
title: "TypeScript基础入门之模块解析(二)"
date: "2025-07-10 10:23:31"
slug: "typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-er"
categories: ["技术"]
tags: ["TypeScript"]
aliases:
  - "/2025/07/10/TypeScript基础入门之模块解析(二)/"
  - "/2025/07/10/TypeScript基础入门之模块解析(二).html"
  - "/TypeScript基础入门之模块解析(二)/"
  - "/TypeScript基础入门之模块解析(二).html"
  - "/2025/07/10/TypeScript基础入门之模块解析-二/"
  - "/2025/07/10/TypeScript基础入门之模块解析-二.html"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-er/"
  - "/2025/07/10/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-er.html"
  - "/typescript-ji-chu-ru-men-zhi-mo-kuai-jie-xi-er.html"
---
继续上文[[TypeScript基础入门之模块解析(一)](https://www.gowhich.com/blog/944)]

## 模块解析

### Base URL

使用baseUrl是使用AMD模块加载器的应用程序中的常见做法，其中模块在运行时"deployed"到单个文件夹。  
这些模块的源代码可以存在于不同的目录中，但构建脚本会将它们放在一起。

设置baseUrl通知编译器在哪里可以找到模块。  
假定所有具有非相对名称的模块导入都相对于baseUrl

baseUrl的值确定为：

1) baseUrl命令行参数的值（如果给定的路径是相对的，则根据当前目录计算）  
2) 'tsconfig.json'中baseUrl属性的值（如果给定的路径是相对的，则根据'tsconfig.json'的位置计算）

请注意，设置baseUrl不会影响相对模块导入，因为它们始终相对于导入文件进行解析。  
您可以在RequireJS和SystemJS文档中找到有关baseUrl的更多文档。

### 路径映射(Path mapping)

有时模块不直接位于baseUrl下。  
例如，对模块"jquery"的导入将在运行时转换为"node\_modules/jquery/dist/jquery.slim.min.js"。  
加载程序使用映射配置在运行时将模块名称映射到文件，请参阅RequireJs文档和SystemJS文档

TypeScript编译器支持使用tsconfig.json文件中的"paths"属性声明此类映射。  
以下是如何为jquery指定"paths"属性的示例。

```json
{
  "compilerOptions": {
    "baseUrl": ".", // This must be specified if "paths" is.
    "paths": {
      "jquery": ["node_modules/jquery/dist/jquery"] // This mapping is relative to "baseUrl"
    }
  }
}
```

请注意，相对于"baseUrl"解析"paths"。  
当将"baseUrl"设置为"."之外的另一个值，即tsconfig.json的目录时，必须相应地更改映射。  
比如说，你在上面的例子中设置了"baseUrl": "./src"，然后jquery应该映射到"../node\_modules/jquery/dist/jquery"

使用"paths"还允许更复杂的映射，包括多个后退位置。  
考虑一个项目配置，其中只有一些模块在一个位置可用，其余模块在另一个位置。  
构建步骤将它们放在一个地方。  
项目布局可能如下所示：

```bash
projectRoot
├── folder1
│   ├── file1.ts (imports 'folder1/file2' and 'folder2/file3')
│   └── file2.ts
├── generated
│   ├── folder1
│   └── folder2
│       └── file3.ts
└── tsconfig.json
```

相应的tsconfig.json如下所示：

```json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "*": [
        "*",
        "generated/*"
      ]
    }
  }
}
```

这告诉编译器任何与模式"\*"（即所有值）匹配的模块导入，以查看两个位置：

1) "\*"表示同名不变，因此map `<moduleName> => <baseUrl>/<moduleName>`  
2) "generated/\*"表示带有附加前缀"generated"的模块名称，因此map `<moduleName> => <baseUrl>/generated/<moduleName>`

遵循此逻辑，编译器将尝试解析这两个导入：

1) import 'folder1/file2'  
   1. 模式'\*'匹配，通配符捕获整个模块名称  
   2. 尝试列表中的第一个替换：'\*' -> folder1/file2  
   3. 替换结果是非相对名称 - 将其与`baseUrl -> projectRoot/folder1/file2.ts`结合使用。  
   4. 文件已存在。完成。

2) import 'folder2/file3'  
   1. 模式'\*'匹配，通配符捕获整个模块名称  
   2. 尝试列表中的第一个替换：'\*' -> folder2/file3  
   3. 替换结果是非相对名称 - 将其与`baseUrl -> projectRoot/folder2/file3.ts`结合使用。  
   4. 文件不存在，移动到第二个替换  
   5. 第二次替换'generated/\*' -> generated/folder2/file3  
   6. 替换结果是非相对名称 - 将它与baseUrl -> projectRoot/generated/folder2/file3.ts结合使用  
   7. 文件已存在。完成。

### 使用rootDirs的虚拟目录

有时，编译时来自多个目录的项目源都被组合在一起以生成单个输出目录。  
这可以看作是一组源目录创建一个"虚拟"目录。

使用'rootDirs'，您可以通知编译器构成此"虚拟"目录的根;  
因此编译器可以解析这些"虚拟"目录中的相关模块导入，就像在一个目录中合并在一起一样。

例如，考虑这个项目结构：

```bash
src
└── views
     └── view1.ts (imports './template1')
     └── view2.ts

generated
└── templates
    └── views
        └── template1.ts (imports './view2')
```

src/views中的文件是某些UI控件的用户代码。  
生成/模板中的文件是由模板生成器自动生成的UI模板绑定代码，作为构建的一部分。  
构建步骤会将/src/views和/generated/templates/views中的文件复制到输出中的同一目录。  
在运行时，视图可以期望其模板存在于其旁边，因此应使用相对名称"./template"将其导入。

要指定与编译器的此关系，请使用"rootDirs"。  
"rootDirs"指定一个根列表，其内容应在运行时合并。  
因此，按照我们的示例，tsconfig.json文件应如下所示：

```json
{
  "compilerOptions": {
    "rootDirs": [
      "src/views",
      "generated/templates/views"
    ]
  }
}
```

每次编译器在其中一个rootDirs的子文件夹中看到相对模块导入时，它将尝试在rootDirs的每个条目中查找此导入。

rootDirs的灵活性不仅限于指定逻辑合并的物理源目录列表。  
所提供的阵列可以包括任意数量的ad hoc，任意目录名，而不管它们是否存在。  
这允许编译器以类型安全的方式捕获复杂的捆绑和运行时功能，例如条件包含和项目特定的加载器插件。

考虑一种国际化场景，其中构建工具通过插入特殊路径令牌（例如＃{locale}）自动生成特定于语言环境的包，作为相对模块路径的一部分，例如./#{locale}/messages。  
在此假设设置中，该工具枚举支持的语言环境，将抽象的路径映射到./zh/messages,./de/messages等。

假设每个模块都导出一个字符串数组。  
例如./zh/messages可能包含：

```ts
export default [
    "您好吗",
    "很高兴认识你"
];
```

通过利用rootDirs，我们可以通知编译器这个映射，从而允许它安全地解析./#{locale}/messages，即使该目录永远不存在。  
例如，使用以下tsconfig.json配置：

```json
{
  "compilerOptions": {
    "rootDirs": [
      "src/zh",
      "src/de",
      "src/#{locale}"
    ]
  }
}
```

编译器现在将解析来自'./#{locale}/messages'的导入消息，以便从工具中导入来自'./zh/messages'的消息，允许以区域设置无关的方式进行开发，而不会影响设计时支持。

未完待续...
