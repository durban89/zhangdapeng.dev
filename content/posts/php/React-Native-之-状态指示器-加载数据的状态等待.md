---
title: "React Native 之 状态指示器【加载数据的状态等待】"
date: "2025-07-02 16:01:03"
slug: "react-native-zhi-zhuang-tai-zhi-shi-qi-jia-zai-shu-ju-de-zhuang-tai-deng-dai"
categories: ["技术"]
tags: ["React-Native"]
aliases:
  - "/2025/07/02/React-Native-之-状态指示器【加载数据的状态等待】/"
  - "/2025/07/02/React-Native-之-状态指示器【加载数据的状态等待】.html"
  - "/React-Native-之-状态指示器【加载数据的状态等待】/"
  - "/React-Native-之-状态指示器【加载数据的状态等待】.html"
  - "/2025/07/02/React-Native-之-状态指示器-加载数据的状态等待/"
  - "/2025/07/02/React-Native-之-状态指示器-加载数据的状态等待.html"
  - "/2025/07/02/react-native-zhi-zhuang-tai-zhi-shi-qi-jia-zai-shu-ju-de-zhuang-tai-deng-dai/"
  - "/2025/07/02/react-native-zhi-zhuang-tai-zhi-shi-qi-jia-zai-shu-ju-de-zhuang-tai-deng-dai.html"
  - "/react-native-zhi-zhuang-tai-zhi-shi-qi-jia-zai-shu-ju-de-zhuang-tai-deng-dai.html"
---
结合上几篇博文,今天学习下，如果来优化一下我们的状态指示器。

前面几篇文章，在renderLoadingView方法中，直接使用了一个View，然后加了一个简单的字符串进行提示，看起来还是简陋的很。

修改之后，这个方法的代码如下：

```jsx
renderLoadingView:function(){
  return (
    <LoadingView />    
  );
},
```

这个LoadingView方法，是根据官方教程进行改写的，其中有个小提示，里面用到了react-timer-mixin这个库，还是提交安装比较好，不然后面还要安装之后再重新启动。

重要的问题就上面这些了，下面把LoadingView整个代码贴到下面:

```jsx
'use strict';

var React = require('react-native');

var {
  ActivityIndicatorIOS,
  StyleSheet,
  View
} = React;

var TimerMixin = require('react-timer-mixin');

var LoadingView = React.createClass({
  mixins:[TimerMixin],
  getInitialState:function(){
    return {
      animating:true
    }
  },
  setToggleTimeout:function(){
    this.setTimeout(
      () => {
        this.setState({animating:!this.state.animating});
        this.setToggleTimeout();
      },
      1200
    );
  },
  componentDidMount:function(){
    this.setToggleTimeout();
  },
  render:function(){
    return (
      <View>
        <ActivityIndicatorIOS 
            animating={this.state.animating} 
            style={[styles.centering, {height:80}]} 
            size="large" />
      </View>
    );
  }
});

var styles = StyleSheet.create({
  centering: {
    alignItems: 'center',
    justifyContent: 'center',
    marginTop:65
  }
});

module.exports = LoadingView;
```

好了，样式啥的我都调整好了，你就贴进去，在根据自己的需求修改下吧。


