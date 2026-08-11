---
title: "VS Code开发Flutter App - 添加有状态小部件篇"
date: "2025-08-01 10:31:52"
slug: "vs-code-kai-fa-flutter-app-tian-jia-you-zhuang-tai-xiao-bu-jian-pian"
categories: ["技术"]
tags: ["Flutter"]
aliases:
  - "/2025/08/01/VS-Code开发Flutter-App-添加有状态小部件篇/"
  - "/2025/08/01/VS-Code开发Flutter-App-添加有状态小部件篇.html"
  - "/VS-Code开发Flutter-App-添加有状态小部件篇/"
  - "/VS-Code开发Flutter-App-添加有状态小部件篇.html"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-tian-jia-you-zhuang-tai-xiao-bu-jian-pian/"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-tian-jia-you-zhuang-tai-xiao-bu-jian-pian.html"
  - "/vs-code-kai-fa-flutter-app-tian-jia-you-zhuang-tai-xiao-bu-jian-pian.html"
---
无状态小部件是不可变的，这意味着它们的属性不能改变 - 所有值都是最终的。

有状态窗口小部件维护可能在窗口小部件生命周期内发生更改的状态。  
实现有状态窗口小部件至少需要两个类：  
1) 一个StatefulWidget类，它创建一个2)State类的实例。  
`StatefulWidget`类本身是不可变的，但State类在窗口小部件的生命周期内持久存在。

在此步骤中，将添加一个有状态窗口小部件`RandomWords`，它创建其State类，RandomWordsState。然后，我们将使用`RandomWords`作为现有MyApp无状态组件

### 创建一个最小的状态类。

将以下内容添加到main.dart的底部：

```dart
class RandomWordsState extends State<RandomWords> {

}
```

注意声明`State<RandomWords>`。  
这表明我们正在使用专门用于RandomWords的通用State类。  
应用程序的大多数逻辑和状态都驻留在这里 - 它维护RandomWords小部件的状态。  
当用户通过切换图标从列表中添加或删除它们时，此类保存生成的单词对，这些单词对随着用户滚动而无限增长，并且最喜欢的单词对（在第2部分中）。

`RandomWordsState`依赖于RandomWords类。接下来会添加它。

### 将有状态的`RandomWords`小部件添加到main.dart。除了创建State类之外，RandomWords小部件几乎没有其他功能：

```dart
class RandomWords extends StatefulWidget {
  @override
  RandomWordsState createState() => new RandomWordsState();
}
```

添加状态类后，IDE会抱怨该类缺少构建方法。  
接下来，将添加一个基本构建方法，通过将单词生成代码从MyApp移动到RandomWordsState来生成单词对。

### 将build()方法添加到RandomWordsState：

```dart
class RandomWordsState extends State<RandomWords> {
  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random();
    return Text(wordPair.asCamelCase);
  }
}
```

### 从MyApp中删除单词生成代码：

删除MyApp中的如下代码

```dart
final wordPair = WordPair.random();
```

同时将如下代码

```dart
child: Text(wordPair.asCamelCase),
```

替换为

```dart
child: RandomWords(),
```

### 重启应用。

应用程序应该像以前一样运行，每次热重新加载或保存应用程序时都会显示一个单词配对。

**\*\*Tips\*\***  
如果您在热重新加载时看到以下警告，请考虑重新启动应用程序：

```bash
Reloading…
Some program elements were changed during reload but did not run when the view was reassembled; you may need to restart the app (by pressing “R”) for the changes to have an effect.
```

这可能是误报，但重新启动可确保您的更改反映在应用程序的UI中。
