---
title: "ReactJS innerHtml 赋值操作"
date: "2025-07-02 16:00:30"
slug: "reactjs-innerhtml-fu-zhi-cao-zuo"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/02/ReactJS-innerHtml-赋值操作/"
  - "/2025/07/02/ReactJS-innerHtml-赋值操作.html"
  - "/ReactJS-innerHtml-赋值操作/"
  - "/ReactJS-innerHtml-赋值操作.html"
  - "/2025/07/02/reactjs-innerhtml-fu-zhi-cao-zuo/"
  - "/2025/07/02/reactjs-innerhtml-fu-zhi-cao-zuo.html"
  - "/reactjs-innerhtml-fu-zhi-cao-zuo.html"
---
使用react的时候，总有一些变量是html的字符串，但是我们却想要实现innerHtml的类似方法，直接用html进行渲染。

这里react提供了一个dangerouslySetInnerHTML方法，可以实现此赋值操作。具体详情可以自己去google一个下，关键字：'react dangerouslySetInnerHTML'.

下面是我为记录的一个示例，可以作为一个简单的demo了。

```jsx
const Login = React.createClass({
  getInitialState: function () {
    return {
      'error_state': false,
      'error_message': ''
    }
  },
  handleClick:function(){
    let error_message = '';
    error_message += '<li>错误信息一</li>';
    error_message += '<li>错误信息二</li>';
    error_message += '<li>错误信息三</li>';
    this.setState({
      'error_state': true,
      'error_message': error_message
    });
  },
  render:function(){
    let alert_class = this.state.error_state ? 'alert alert-danger' : 'aler hidden';
    return (
      <div>
        <button onClick={this.handleClick}>添加html</button>
        <div className={alert_class} dangerouslySetInnerHTML={{__html:this.state.error_message}} ></div>
      </div>
    );
  }
});
```


