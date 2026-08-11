---
title: "React Native 之 列表【ListView 添加 点击列表跳转到指定视图】"
date: "2025-07-02 16:01:00"
slug: "react-native-zhi-lie-biao-listview-tian-jia-dian-ji-lie-biao-tiao-zhuan-dao-zhi-ding-shi-tu"
categories: ["技术"]
tags: ["React-Native"]
aliases:
  - "/2025/07/02/React-Native-之-列表【ListView-添加-点击列表跳转到指定视图】/"
  - "/2025/07/02/React-Native-之-列表【ListView-添加-点击列表跳转到指定视图】.html"
  - "/React-Native-之-列表【ListView-添加-点击列表跳转到指定视图】/"
  - "/React-Native-之-列表【ListView-添加-点击列表跳转到指定视图】.html"
  - "/2025/07/02/React-Native-之-列表-ListView-添加-点击列表跳转到指定视图/"
  - "/2025/07/02/React-Native-之-列表-ListView-添加-点击列表跳转到指定视图.html"
  - "/2025/07/02/react-native-zhi-lie-biao-listview-tian-jia-dian-ji-lie-biao-tiao-zhuan-dao-zhi-ding-sh/"
  - "/2025/07/02/react-native-zhi-lie-biao-listview-tian-jia-dian-ji-lie-biao-tiao-zhuan-dao-zhi-din.html"
  - "/react-native-zhi-lie-biao-listview-tian-jia-dian-ji-lie-biao-tiao-zhuan-dao-zhi-ding-shi-tu.html"
---
上一篇文章中我们了解了一下，简单的添加列表，但是列表添加了，点击列表没有什么反应啊，这不就没啥作用了，这里记录下如何实现点击的效果。

React Native中有个组件叫做TouchableHighlight，一看这名字就知道干啥的了，然后我们在这上面加一个touch的事件。

这里我把上一节的renderMovie的方法代码列到这里：

```jsx
renderMovie:function(movie){
    return (
      <TouchableHighlight onPress={() => this._pressRow(movie.id)}>
        <View style={styles.container} key={movie.id}>
          <Image
            source={{uri:movie.posters.thumbnail}}
            style={styles.thumbnail} />
          <View style={styles.rightContainer}>
            <Text style={styles.title} numberOfLines={1}>
              {movie.title}
            </Text>
            <Text style={styles.year}>
              {movie.year}
            </Text>
          </View>
          <View style={styles.separator}></View>
        </View>
      </TouchableHighlight>
    );
  },
```

然后我们给这个onPress添加一个指定的事件函数

```jsx
_pressRow:function(rowID: number){
    this.props.navigator.push({
      title:'详情',
      component:MovieView
    })
  }
```

这里的组件MovieView,我加在了另外一个文件里面，代码如下：【自己可以进行引入】

```jsx
'use strict';

var React = require('react-native');

var {
  StyleSheet,
  Text,
  View
} = React;

var MovieView = React.createClass({
  render:function(){
    return (
      <View style={styles.container}>
        <Text>Movie View</Text>
      </View>
    );
  }
});

var styles = StyleSheet.create({
  container:{
    flex:1,
    backgroundColor:'#fff'
  }
});

module.exports = MovieView;
```

好了，运行吧，可以跳转了，还是蛮简单的。

添加了这些，还有个问题，就是要如何才能修改按下去时背景色的颜色，其实只要加入这行代码就好了：

`underlayColor='rgba(24,36,35,0.1)'`

最终我的renderMovie代码就成了如下的样子：

```jsx
renderMovie:function(movie){
    return (
      <TouchableHighlight underlayColor='rgba(24,36,35,0.1)' onPress={() => this._pressRow(movie.id)}>
        <View style={styles.container} key={movie.id}>
          <Image
            source={{uri:movie.posters.thumbnail}}
            style={styles.thumbnail} />
          <View style={styles.rightContainer}>
            <Text style={styles.title} numberOfLines={1}>
              {movie.title}
            </Text>
            <Text style={styles.year}>
              {movie.year}
            </Text>
          </View>
          <View style={styles.separator}></View>
        </View>
      </TouchableHighlight>
    );
  },
```


