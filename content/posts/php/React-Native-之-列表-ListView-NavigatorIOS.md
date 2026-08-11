---
title: "React Native 之 列表【ListView，NavigatorIOS】"
date: "2025-07-02 16:00:52"
slug: "react-native-zhi-lie-biao-listview-navigatorios"
categories: ["技术"]
tags: ["React-Native"]
aliases:
  - "/2025/07/02/React-Native-之-列表【ListView，NavigatorIOS】/"
  - "/2025/07/02/React-Native-之-列表【ListView，NavigatorIOS】.html"
  - "/React-Native-之-列表【ListView，NavigatorIOS】/"
  - "/React-Native-之-列表【ListView，NavigatorIOS】.html"
  - "/2025/07/02/React-Native-之-列表-ListView-NavigatorIOS/"
  - "/2025/07/02/React-Native-之-列表-ListView-NavigatorIOS.html"
  - "/2025/07/02/react-native-zhi-lie-biao-listview-navigatorios/"
  - "/2025/07/02/react-native-zhi-lie-biao-listview-navigatorios.html"
  - "/react-native-zhi-lie-biao-listview-navigatorios.html"
---
React-Native最近看了下他的ListView组件，记录下自己实现的小小功能：

一个简单的列表都没啥特别的了，这里添加一个导航。

首先使用NavigatorIOS组件，给我们的首页添加一个导航

```jsx
var WalkerfreeProject = React.createClass({
  render:function(){
    return (
      <NavigatorIOS
        style={styles.container}
        initialRoute={{
          'title':'Welcome',
          'component': Movies,
        }} />
    );
  }
});
```

如果只是就这么几行代码，还是有问题的，需要加一下样式

```jsx
var styles = StyleSheet.create({
  container: {
    flex: 1,
  }
});
```

最后组件注册

```jsx
AppRegistry.registerComponent('WalkerfreeProject', () => WalkerfreeProject);
```

***Movies***这个就是一个ListView的组件。

```jsx
var React = require('react-native');

var {
  AppRegistry,
  Image,
  ListView,
  StyleSheet,
  Text,
  View,
  NavigatorIOS,
  ScrollView,
  Navigator
} = React;

var REQUEST_URL = 'https://raw.githubusercontent.com/facebook/react-native/master/docs/MoviesExample.json';

var Movies = React.createClass({
  getInitialState:function(){
    return {
      dataSource:new ListView.DataSource({
        rowHasChanged:(row1, row2) => row1 != row2
      }),
      loaded:false
    }
  },
  componentDidMount:function(){
    this.fetchData();
  },
  fetchData:function(){
    fetch(REQUEST_URL)
    .then((response) => response.json())
    .then((responseData) => {
      this.setState({
        dataSource:this.state.dataSource.cloneWithRows(responseData.movies),
        loaded:true
      });
    })
    .done()
  },
  renderLoadingView:function(){
    return (
      <View style={styles.container}>
        <Text>
          Loading Views
        </Text>
      </View>
    );
  },
  renderMovie:function(movie){
    return (
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
    );
  },
  render: function() {
    if(!this.state.loaded){
      return this.renderLoadingView();
    }

    return (
      <ListView
        dataSource={this.state.dataSource}
        renderRow={this.renderMovie}
        style={styles.listView} />
    );
  }
});

var styles = StyleSheet.create({
  separator: {
    height: 1,
    backgroundColor: '#CCCCCC',
  },
  listView:{
    marginTop:65,
  },
  container: {
    flex: 1,
  },
  thumbnail: {
    width: 53,
    height: 81,
  },
  rightContainer:{
    flex:1,
    position:'absolute',
    top:0,
    left:55
  },
  title:{
    fontSize:20,
    marginBottom:8,
    textAlign:'left',
    width:260
  },
  year:{
    textAlign:'center'
  }
});

module.exports = Movies;
```

整个代码就贴到这里了，没有啥需要说明的。这个官网也是有的，只是注意一下这里的样式就好了。当然在index.ios.js的里面要引入

```jsx
var Movies = require('./App/Movies');
```

这个我是他Movies添加到了App这个目录里了，所以需要自己引入一下。其实也还是蛮简单的，因为就是一个简单的例子而已

