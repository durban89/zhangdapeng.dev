---
title: "Webpack4+React16+ReactRouter4+Redux整合开发"
date: "2025-07-04 14:27:31"
slug: "webpack4react16reactrouter4redux-zheng-he-kai-fa"
categories: ["技术"]
tags: ["Webpack", "ReactJS", "React-Router", "Redux"]
aliases:
  - "/2025/07/04/Webpack4+React16+ReactRouter4+Redux整合开发/"
  - "/2025/07/04/Webpack4+React16+ReactRouter4+Redux整合开发.html"
  - "/Webpack4+React16+ReactRouter4+Redux整合开发/"
  - "/Webpack4+React16+ReactRouter4+Redux整合开发.html"
  - "/2025/07/04/Webpack4-React16-ReactRouter4-Redux整合开发/"
  - "/2025/07/04/Webpack4-React16-ReactRouter4-Redux整合开发.html"
  - "/2025/07/04/webpack4react16reactrouter4redux-zheng-he-kai-fa/"
  - "/2025/07/04/webpack4react16reactrouter4redux-zheng-he-kai-fa.html"
  - "/webpack4react16reactrouter4redux-zheng-he-kai-fa.html"
---
续接上文【[Webpack4+React16+ReactRouter4整合开发](https://www.gowhich.com/blog/826)】

拉取github代码  
https://github.com/durban89/webpack4-react16-reactrouter-demo.git

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git webpack4-react16-reactrouter-redux
cd webpack4-react16-reactrouter-redux
npm install 
npm start
```

如果没有异常就可以正常写代码了

首先看下react-router-redux，从react-router官网的redux介绍部分可以看出写的是React Router Redux，但是点击后会告诉你Deprecated。我的天！废弃了，好吧，然后下面告诉你connected-react-router  
我的天，又造了一个轮子，看来要重头学起了，没关系，咱们就是不怕折腾，人活着就是折腾嘛。  
我们链接到connected-react-router，各种的炫耀夸，太多了，各种优点，我们还是来点实际的，操作开始

```bash
npm install redux react-redux history react-hot-loader connected-react-router --save
```

**如何使用**  
修改src/index.jsx

1、第一步  
添加第一部分 - 导入使用的库函数

```js
import { AppContainer } from 'react-hot-loader';
import { createBrowserHistory } from 'history';
import { applyMiddleware, compose, createStore } from 'redux';
import { Provider } from 'react-redux';
import { connectRouter, ConnectedRouter, routerMiddleware } from 'connected-react-router';
```

添加第二部分 - 需要自己去定义

```js
import rootReducer from './reducers'; // 这里的文件是新加的 - 具体是如何创建的可以看下项目代码
import routes from './routes'; // 这里的文件是新加的 - 具体是如何创建的可以看下项目代码
```

添加第三部分 - 配置redux相关的逻辑

```js
const history = createBrowserHistory();
const initialState = {};
const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  connectRouter(history)(rootReducer),
  initialState,
  composeEnhancer(applyMiddleware(routerMiddleware(history))),
);
```

添加第四部分 - 整合react-router

```js
ReactDOM.render(
  (
    <AppContainer>
      <Provider store={store}>
        <ConnectedRouter history={history}>
          {routes}
        </ConnectedRouter>
      </Provider>
    </AppContainer>
  ),
  document.getElementById('root'),
);
```

最终src/index.jsx内容如下

```js
import React from 'react';
import { AppContainer } from 'react-hot-loader';
import { createBrowserHistory } from 'history';
import { applyMiddleware, compose, createStore } from 'redux';
import { Provider } from 'react-redux';
import { connectRouter, ConnectedRouter, routerMiddleware } from 'connected-react-router';
import ReactDOM from 'react-dom';
import rootReducer from './reducers';
import routes from './routes';

const history = createBrowserHistory();
const initialState = {};
const composeEnhancer = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const store = createStore(
  connectRouter(history)(rootReducer),
  initialState,
  composeEnhancer(applyMiddleware(routerMiddleware(history))),
);

ReactDOM.render(
  (
    <AppContainer>
      <Provider store={store}>
        <ConnectedRouter history={history}>
          {routes}
        </ConnectedRouter>
      </Provider>
    </AppContainer>
  ),
  document.getElementById('root'),
);
```

src/routes.jsx 主要配置路由跟组件的关系 -> 上面这行import routes from './routes';代码

```js
import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link as ALink,
} from 'react-router-dom';

import AppComponent from './components/AppComponent';
import HomeComponent from './components/HomeComponent';
import AboutComponent from './components/AboutComponent';
import TopicsComponent from './components/TopicsComponent';

const routes = (
  <div>
    <Router>
      <AppComponent>
        <ul>
          <li><ALink to="/">首页</ALink></li>
          <li><ALink to="/about">关于</ALink></li>
          <li><ALink to="/topics">论题</ALink></li>
        </ul>
        <hr />

        <Route exact path="/" component={HomeComponent} />
        <Route path="/about" component={AboutComponent} />
        <Route path="/topics" component={TopicsComponent} />
      </AppComponent>
    </Router>
  </div>
);

export default routes;
```

2、第二步  
配置好了，就要开始使用了  
1】、创建reducers  
src/reducers/counter.js

```js
const counterReducer = (state = 0, action) => {
  switch (action.type) {
    case 'INCREMENT':
      return state + 1;
    case 'DECREMENT':
      return state - 1;
    default:
      return state;
  }
};

export default counterReducer;
```

2】、将counter.js加入到主reducers里面

```js
src/reducers/index.js // 这里的文件就是对应这段代码 import rootReducer from './reducers';
import { combineReducers } from 'redux';
import counterReducer from './counter';

export default combineReducers({
  count: counterReducer,
});
```

3】、创建actions

```js src/actions/counter.js

export const increment = () => ({
  type: 'INCREMENT',
});

export const decrement = () => ({
  type: 'DECREMENT',
});
```

4】、添加一个组件src/components/CounterComponent.jsx

```js
import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { connect } from 'react-redux';
import { counter } from 'Actions';

const {
  increment, decrement,
} = counter;

class CounterComponent extends Component {
  constructor(props, context) {
    super(props, context);

    this.state = {};
  }

  render() {
    const {
      count,
    } = this.props;

    return (
      <div>
        <p>数值: {count}</p>
        <button onClick={this.props.doIncrement}>+</button>
        <button onClick={this.props.doDecrement}>-</button>
      </div>
    );
  }
}

CounterComponent.propTypes = {
  count: PropTypes.number,
  doIncrement: PropTypes.func.isRequired,
  doDecrement: PropTypes.func.isRequired,
};

CounterComponent.defaultProps = {
  count: 0,
};

const mapStateToProps = state => ({
  count: state.count,
});

const mapDispatchToProps = dispatch => ({
  doIncrement: () => dispatch(increment()),
  doDecrement: () => dispatch(decrement()),
});

export default connect(mapStateToProps, mapDispatchToProps)(CounterComponent);
```

5】、将组件加到路由里面

src/routes.js

```js
import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link as ALink,
} from 'react-router-dom';

import AppComponent from './components/AppComponent';
import HomeComponent from './components/HomeComponent';
import AboutComponent from './components/AboutComponent';
import TopicsComponent from './components/TopicsComponent';
import CounterComponent from './components/CounterComponent';

const routes = (
  <div>
    <Router>
      <AppComponent>
        <ul>
          <li><ALink to="/">首页</ALink></li>
          <li><ALink to="/about">关于</ALink></li>
          <li><ALink to="/topics">论题</ALink></li>
          <li><ALink to="/counter">计数器</ALink></li>
        </ul>
        <hr />

        <Route exact path="/" component={HomeComponent} />
        <Route path="/about" component={AboutComponent} />
        <Route path="/topics" component={TopicsComponent} />
        <Route path="/counter" component={CounterComponent} />
      </AppComponent>
    </Router>
  </div>
);

export default routes;
```

6】、为了引入方便再加一个src/actions/index.js

```js
import counter from './counter';

const actions = {
  counter,
};

export default actions;
export { counter };
```

到这里基本上就完工了，应该可以在页面看到计数器，并进行操作了

```js
import { counter } from 'Actions';
```

这里是比较特殊的  
这个要归功于webpack

```js
resolve: {
    extensions: ['.js', '.jsx'], // 这里是必须要加的，不然默认的值加载['.js','.json']为后缀的文件
    alias: {
        Actions: path.resolve(__dirname, 'src/actions'),
    },
},
```

这里我们加了这个配置，于是在引入的时候就会正常引入需要的代码了。

好了，整个配置就完成了，项目我已经上传到github了，需要的同学可以自行去下载查看

实例项目地址:

https://github.com/durban89/webpack4-react16-reactrouter-demo.git  
tag: v_1.0.1
