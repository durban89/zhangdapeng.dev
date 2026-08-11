---
title: "VS Code开发Flutter App - 配置篇"
date: "2025-08-01 10:31:43"
slug: "vs-code-kai-fa-flutter-app-pei-zhi-pian"
categories: ["技术"]
tags: ["Flutter"]
aliases:
  - "/2025/08/01/VS-Code开发Flutter-App-配置篇/"
  - "/2025/08/01/VS-Code开发Flutter-App-配置篇.html"
  - "/VS-Code开发Flutter-App-配置篇/"
  - "/VS-Code开发Flutter-App-配置篇.html"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-pei-zhi-pian/"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-pei-zhi-pian.html"
  - "/vs-code-kai-fa-flutter-app-pei-zhi-pian.html"
---
VS Code开发Flutter App - 配置篇

## 配置

**VS Code**  -  具有Flutter运行和调试支持的轻量级编辑器

### 安装 VS Code

[VS Code](https://code.visualstudio.com/), 下载最新稳定版本

### 安装Flutter插件

* 启动VS Code
* 调用 View>Command Palette
* 输入"install"，然后选择"Extensions：Install Extension"操作
* 在搜索框中输入flutter，在列表中选择"Flutter"，然后单击"Install"
* 选择"OK"以重新加载VS Code

### 使用Flutter Doctor验证您的设置

* 调用 View>Command Palette
* 输入"doctor"，然后选择"Flutter：Run Flutter Doctor"操作
* 查看"OUTPUT"窗口中的输出的信息，查看是否存在其他问题

做完以上几步，如果没有任何问题，就可以继续开发了，如果遇到问题，可以加群或者下面留言交流

## 创建一个新的 Flutter App

本次分享只是一个创建Flutter应用程序的分享。本次分享不需要具备太多技能，只要熟悉面向对象的代码和基本编程概念（如变量，循环和条件），下面的一些分享基本上你也可以完成。而且不需要以前有使用过Dart或移动编程的经验。

### 创建新应用

* 启动 VS Code
* 调用 View > Command Palette
* 输入 "flutter", 然后选择 "Flutter: New Project"操作
* 输入一个项目名称，例如"flutter\_myapp", 然后按回车键
* 为新项目目录创建或者选择一个父文件夹
* 等待项目创建完成main.dart文件会出现

**Tips** 这里我在创建的时候遇到一个问题，就是创建是失败了，原因是因为很多Flutter要求的没有正常处理完。主要是在执行"flutter doctor"的时候有一些提示没有解决完，所以建议大家在操作的时候，尽量将"flutter doctor"的提示处理完。

### 运行App

* 启动模拟器

运行之前先执行```open -a Simulator```启动一个模拟器，我是在mac下执行的，如果你是在linux或者window下执行，建议也提前启动一个模拟器。

* 调用 Debug > Start Debugging 或者按 F5
* 等待App运行 - Debug命令行窗口会被打印出进度
* 如果一切正常，应用程序构建完成后，将在设备上看到启动应用程序

---

![小绒毛的足迹](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1535554170/xiaorongmao/xrm_web_15_1.png)

### 尝试hot reload

Flutter提供快速开发周期和hot reload，能够重新加载实时运行的应用程序的代码，而无需重新启动或丢失应用程序状态。  
只需更改源代码，告诉IDE或命令行工具您要热重新加载，并查看模拟器，模拟器或设备中的更改。

* 打开lib/main.dart
* 修改字符串'You have pushed the button this many times:' 改为'You have clicked the button this many times:'

**Important**: 不要按停止按钮；让应用保持运行状态

* 保存更改: 调用 File > Save All, 或者点击R按钮来更新

你将立刻看到更新的字符串在运行的App上

这一点我非常喜欢，以前开发app，每次改完都要重新启动一次，而且android或者ios重新编译一次耗时很久，电脑性能不好的话，还真的就只能干等着。

### 更新lib/main.dart

删除lib/main.dart中的所有代码。替换为以下代码，在屏幕中央显示"Hello World"。

```dart
import 'package:flutter/material.dart';

void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Welcome to Flutter - Gowhich',
      home: Scaffold(
        appBar: AppBar(
          title: Text('Welcome to Flutter - Gowhich'),
        ),
        body: Center(
          child: Text("Holle Flutter - Gowhich")
        ),
      ),
    );
  }
}
```

![小绒毛的足迹](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1535554170/xiaorongmao/xrm_web_15_2.png)

**总结**

* 此示例创建一个Material应用程序。Material是一种视觉设计语言，是移动和Web上的标准语言。Flutter提供了丰富的Material小部件。
* main方法指定fat arrow(=>)表示法。对单行函数或方法使用(=>)表示法。
* 该应用程序扩展了StatelessWidget，使应用程序本身成为一个小部件。在Flutter中，几乎所有东西都是一个小部件，包括对齐，填充和布局。
* Material库中的"Scaffold"窗口小部件提供默认的应用栏、标题和包含主屏幕窗口小部件树的主体属性。小部件子树可能非常复杂。
* 小部件的主要工作是提供build()方法，该方法描述如何根据其他较低级别的小部件显示小部件。
* 此示例的正文包含一个包含Text子窗口小部件的Center窗口小部件。"Center"窗口小部件将其窗口小部件子树与屏幕中心对齐。

今天的分享就到这里。
