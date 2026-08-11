---
title: "VS Code开发Flutter App - External Package篇"
date: "2025-08-01 10:31:46"
slug: "vs-code-kai-fa-flutter-app-external-package-pian"
categories: ["技术"]
tags: ["Flutter"]
aliases:
  - "/2025/08/01/VS-Code开发Flutter-App-External-Package篇/"
  - "/2025/08/01/VS-Code开发Flutter-App-External-Package篇.html"
  - "/VS-Code开发Flutter-App-External-Package篇/"
  - "/VS-Code开发Flutter-App-External-Package篇.html"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-external-package-pian/"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-external-package-pian.html"
  - "/vs-code-kai-fa-flutter-app-external-package-pian.html"
---
本次分享将使用名为english\_words的开源软件包，其中包含几千个最常用的英语单词和一些实用程序函数。可以在pub.dartlang.org上找到english\_words包以及许多其他开源软件包。

## 添加外部包

pubspec文件管理Flutter应用程序的资产和依赖项。  
打开VS Code，然后打开pubspec.yaml，在pubspec.yaml中，将english\_words(3.1.0或更高版本)添加到依赖项列表中。  
添加下面突出显示的行：

```yaml
dependencies:
  flutter:
    sdk: flutter

  cupertino_icons: ^0.1.0
  english_words: ^3.1.0 # 新加的一行
```

## 安装外部包

在VS Code中添加完此行后，会在输出窗口中看到如下输出，代表程序在更新并添加新的包

```bash
[flutter_myapp] flutter packages get
Running "flutter packages get" in flutter_myapp...
```

执行包也可以自动生成pubspec.lock文件，其中包含项目中所有包的列表及其版本号。

## 使用外部包

打开`lib/main.dart`文件, 导入新的包，代码如下:

```dart
import 'package:english_words/english_words.dart';
```

在您键入时，VS Code会为您提供导入库的建议。  
然后它将导入字符串呈灰色，让您知道导入的库未使用（到目前为止）。

## 修改代码

使用英语单词包生成文本而不是使用字符串"Hello World"。  
进行以下更改：

```dart
import 'package:flutter/material.dart';
import 'package:english_words/english_words.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random(); // 新加代码
    return MaterialApp(
      title: 'Welcome to Flutter - Gowhich',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Welcome to Flutter - Gowhich'),
        ),
        body: Center(
          child: Text(wordPair.asCamelCase), // 新加代码
        ),
      ),
    );
  }
}
```

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1535639188/xiaorongmao/xrm_web_16_1.png "" %}


如果应用程序正在运行，请使用hot reload功能更新正在运行的应用程序。  
每次进行hot reload操作或保存项目时，应该在正在运行的应用程序中看到一个随机选择的不同单词对。  
这是因为单词配对是在构建方法中生成的，该方法在每次MaterialApp需要渲染时运行，或者在Flutter Inspector中切换平台时运行。
