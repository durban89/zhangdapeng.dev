---
title: "VS Code开发Flutter App - 创建无限滚动ListView"
date: "2025-08-01 10:32:10"
slug: "vs-code-kai-fa-flutter-app-chuang-jian-wu-xian-gun-dong-listview"
categories: ["技术"]
tags: ["Flutter"]
aliases:
  - "/2025/08/01/VS-Code开发Flutter-App-创建无限滚动ListView/"
  - "/2025/08/01/VS-Code开发Flutter-App-创建无限滚动ListView.html"
  - "/VS-Code开发Flutter-App-创建无限滚动ListView/"
  - "/VS-Code开发Flutter-App-创建无限滚动ListView.html"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-chuang-jian-wu-xian-gun-dong-listview/"
  - "/2025/08/01/vs-code-kai-fa-flutter-app-chuang-jian-wu-xian-gun-dong-listview.html"
  - "/vs-code-kai-fa-flutter-app-chuang-jian-wu-xian-gun-dong-listview.html"
---
本次分享将展开RandomWordsState以生成并显示单词对的列表。当用户滚动时，ListView小部件中显示的列表会无限增长。ListView的构建器工厂构造函数允许您根据需要懒惰地构建列表视图。

## 第一步、将\_suggestions列表添加到RandomWordsState类以保存建议的单词对。另外，添加一个biggerFont变量来使字体更大。

**\*\*Tips\*\* 带有下划线前缀的标识符在Dart语言中会被强制进行隐私处理**。添加的代码如下

```dart
class RandomWordsState extends State<RandomWords> {
  final _suggestions = <WordPair>[]; // 新加

  final _biggerFont = const TextStyle(fontSize: 18.0); // 新加

  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random();
    return Text(wordPair.asCamelCase);
  }
}
```

下一步添加一个\_buildSuggestions()方法到RandomwordsState类中，这个方法创建ListView，用来显示建议单词对.

ListView类提供了一个构建器属性itemBuilder，它是一个工厂构建器和指定为匿名函数的回调函数。  
两个参数传递给函数 - BuildContext和行迭代器i。  
迭代器从0开始，每次调用函数时递增，对于每个建议的单词配对一次。  
此模型允许建议的列表在用户滚动时无限增长。

## 第二步、添加完整的\_buildSuggestions()方法到RandomwordsState类中

代码如下

```dart
class RandomWordsState extends State<RandomWords> {
  final _suggestions = <WordPair>[];
  final _biggerFont = const TextStyle(fontSize: 18.0);

  Widget _buildSuggestions() {
    return ListView.builder(
      padding: const EdgeInsets.all(16.0),
      itemBuilder: (context, i) {
        if (i.isOdd) return Divider();

        final index = i ~/ 2;

        if (index >= _suggestions.length) {
          _suggestions.addAll(generateWordPairs().take(10));
        }

        return _buildRow(_suggestions[index]);
      }
    );
  }

  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random();
    return Text(wordPair.asCamelCase);
  }
}
```

\_buildSuggestions()函数每个单词对调用一次\_buildRow()。此函数在ListTile中显示每个新对，可以在下一步中使行更具吸引力。

## 第三步、添加\_buildRow() 到RandomWordsState类中

完整代码如下

```dart
class RandomWordsState extends State<RandomWords> {
  final _suggestions = <WordPair>[];
  final _biggerFont = const TextStyle(fontSize: 18.0);

  Widget _buildSuggestions() {
    return ListView.builder(
      padding: const EdgeInsets.all(16.0),
      itemBuilder: (context, i) {
        if (i.isOdd) return Divider();

        final index = i ~/ 2;

        if (index >= _suggestions.length) {
          _suggestions.addAll(generateWordPairs().take(10));
        }

        return _buildRow(_suggestions[index]);
      }
    );
  }

  Widget _buildRow(WordPair wordPair) {
    return ListTile(
      title: Text(
        wordPair.asPascalCase,
        style: _biggerFont,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final wordPair = WordPair.random();
    return Text(wordPair.asCamelCase);
  }
}
```

## 第四步、更新RandomWordsState的构建方法以使用\_buildSuggestions()，而不是直接调用单词生成库。（脚手架实现了基本的Material Design视觉布局）

完整代码如下：

```dart
class RandomWordsState extends State<RandomWords> {
  final _suggestions = <WordPair>[];
  final _biggerFont = const TextStyle(fontSize: 18.0);

  Widget _buildSuggestions() {
    return ListView.builder(
      padding: const EdgeInsets.all(16.0),
      itemBuilder: (context, i) {
        if (i.isOdd) return Divider();

        final index = i ~/ 2;

        if (index >= _suggestions.length) {
          _suggestions.addAll(generateWordPairs().take(10));
        }

        return _buildRow(_suggestions[index]);
      }
    );
  }

  Widget _buildRow(WordPair wordPair) {
    return ListTile(
      title: Text(
        wordPair.asPascalCase,
        style: _biggerFont,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('启动一个生成器')
      ),
      body: _buildSuggestions(),
    );
  }
}
```

## 第五步、更新MyApp的构建方法，更改标题，并将home更改为RandomWords小部件

使用下面突出显示的构建方法替换原始方法：

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '启动一个生成器 - Gowhich',
      home: RandomWords(),
    );
  }
}
```

## 第六步、重启应用

无论你滚动多远，你都应该看到一个单词配对列表。如下图

{% img https://res.cloudinary.com/dy5dvcuc1/image/upload/v1536274634/xiaorongmao/xrm_web_23_1.png "" %}

