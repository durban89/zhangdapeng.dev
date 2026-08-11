---
title: "Webpack4+React16+ReactRouter4+Redux整合开发 - react-hot-loader"
date: "2025-07-04 14:27:34"
slug: "webpack4react16reactrouter4redux-zheng-he-kai-fa-react-hot-loader"
categories: ["技术"]
tags: ["Webpack", "ReactJS", "React-Router", "Redux"]
aliases:
  - "/2025/07/04/Webpack4+React16+ReactRouter4+Redux整合开发-react-hot-loader/"
  - "/2025/07/04/Webpack4+React16+ReactRouter4+Redux整合开发-react-hot-loader.html"
  - "/Webpack4+React16+ReactRouter4+Redux整合开发-react-hot-loader/"
  - "/Webpack4+React16+ReactRouter4+Redux整合开发-react-hot-loader.html"
  - "/2025/07/04/Webpack4-React16-ReactRouter4-Redux整合开发-react-hot-loader/"
  - "/2025/07/04/Webpack4-React16-ReactRouter4-Redux整合开发-react-hot-loader.html"
  - "/2025/07/04/webpack4react16reactrouter4redux-zheng-he-kai-fa-react-hot-loader/"
  - "/2025/07/04/webpack4react16reactrouter4redux-zheng-he-kai-fa-react-hot-loader.html"
  - "/webpack4react16reactrouter4redux-zheng-he-kai-fa-react-hot-loader.html"
---
继续上篇文章【[Webpack4+React16+ReactRouter4+Redux整合开发](https://www.gowhich.com/blog/827)】继续分享，这里我们针对细节的部分做下优化，主要是能更加高效的提升我们的开发效率

1、clone 实例代码并将代码运行起来

```bash
git clone https://github.com/durban89/webpack4-react16-reactrouter-demo.git react-hot-loader-demo && cd react-hot-loader-demo
```

```bash
npm install
```

2、运行项目

```bash
npm start
```

3、修改webpack.config.js

修改webpack-dev-server的配置，添加

```bash
hot: true
```

结果如下

```js
devServer: {
    hot: true,
    contentBase: path.join(__dirname, 'dist'),
    compress: true,
    port: 8083,
    historyApiFallback: {
        rewrites: [{
            from: /^\/$/,
            to: './index.html',
        },
        ],
    },
},
```

修改entry

```js
entry: {
  app: [
    'webpack/hot/only-dev-server', // 这里新加
    'react-hot-loader/patch', // 这里新加
    './src/index.jsx',
  ],
},
```

修改module中rule部分

```js
{
  test: /\.(js|jsx)$/,
  loader: [
    'babel-loader',
    'react-hot-loader/webpack',
  ],
  exclude: [
    path.resolve(__dirname, 'node_modules'),
  ],
  options: {
    plugins: ['transform-async-to-generator', 'transform-strict-mode', 'transform-object-assign', 'transform-decorators-legacy'],
    presets: ['es2015', 'react', 'stage-0'],
  },
}
```

修改src/index.jsx  
将原来的

```jsx
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

替换为

```jsx
const render = () => {
  ReactDOM.render(
    (
      <AppContainer>
        <Provider store={store}>
          <App history={history} />
        </Provider>
      </AppContainer>
    ),
    document.getElementById('root'),
  );
};

render();

if (module.hot) {
  module.hot.addStatusHandler((status) => {
    console.log('status = ', status);
  });

  module.hot.accept('./App', () => {
    // 这里是当前版本很重要的环节，不然的话react-hot-reload不起作用
    require('./App').default;
    render();
  });

  module.hot.accept('./reducers', () => {
    store.replaceReducer(connectRouter(history)(rootReducer));
    render();
  });
}
```

添加src/App.jsx

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import { ConnectedRouter } from 'connected-react-router';
import routes from './routes';

const App = ({ history }) => (
  <ConnectedRouter history={history}>
    {routes}
  </ConnectedRouter>
);

App.propTypes = {
  history: PropTypes.objectOf(PropTypes.any).isRequired,
};

export default App;
```

最后一个package.json中start命令修改

```json
"start": "npx webpack-dev-server --open --hot"
```

最后重启项目

```bash
npm start
```

试着改改UI，会有神奇的效果

实践环境具体版本以项目的package.json为准

> os: mac  
> node: v8.9.4

项目地址  
https://github.com/durban89/webpack4-react16-reactrouter-demo.git  
TAG: v_1.0.2
