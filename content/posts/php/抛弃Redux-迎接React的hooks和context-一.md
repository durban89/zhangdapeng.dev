---
title: "抛弃Redux，迎接React的hooks和context（一）"
date: "2025-07-10 10:57:52"
slug: "pao-qi-redux-ying-jie-react-de-hooks-he-context-yi"
categories: ["技术"]
tags: ["RequireJS"]
aliases:
  - "/2025/07/10/抛弃Redux，迎接React的hooks和context（一）/"
  - "/2025/07/10/抛弃Redux，迎接React的hooks和context（一）.html"
  - "/抛弃Redux，迎接React的hooks和context（一）/"
  - "/抛弃Redux，迎接React的hooks和context（一）.html"
  - "/2025/07/10/抛弃Redux-迎接React的hooks和context-一/"
  - "/2025/07/10/抛弃Redux-迎接React的hooks和context-一.html"
  - "/2025/07/10/pao-qi-redux-ying-jie-react-de-hooks-he-context-yi/"
  - "/2025/07/10/pao-qi-redux-ying-jie-react-de-hooks-he-context-yi.html"
  - "/pao-qi-redux-ying-jie-react-de-hooks-he-context-yi.html"
---
如果你使用React很长时间，Redux应该听说过。Redux是非常酷的，它是一种获取单独组件来改变和从主应用程序store中提取数据的方法，但是它不是非常容易入手的，尤其是新手。

有很多概念性的东西，比如`reducers`, `actions`, `action creators`，并且有一些方法，比如`mapDispatchToProps`和`mapStateToProps`，以及需要根据常规原因创建的一堆文件和文件夹。为了分享和改编数据需要做大量的工作。

随着Context API和hooks的引入，我们可以在我们的React应用程序中重新创建Redux，而无需实际安装redux和react-redux，本篇文章将演示下如何操作。

## 配置

前提确保已经安装Nodejs(我使用的版本是v10.15.0)，然后使用`create-react-app`初始化一个app:

```bash
npx create-react-app no-redux-app
```

这个根据具体网络情况需要花一些时间，确实真的要好长时间

一旦初始化结束后，在no-redux-app这个目录下通过使用命令`npm start`来启动项目，会自动打开浏览器，并且会看到类如下图的页面

[![React hooks context](https://cdn-images-1.medium.com/max/1600/1*iHxFtQPjIY8sYaNYvbG0ZQ.png)](https://camo.githubusercontent.com/4448c3224bc9b532246d663375afc10ce7080e0a/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313630302f312a694878467451506a4959387359614e59766247305a512e706e67)

* `ctrl + c`停止运行
* 打开```package.json````文件，查看react和react-dom的版本号，如果是在16.7.0以上则可以使用hooks，如果不是请运行下面命令安装最新版本

```bash
$ npm i [email protected] [email protected]
```

* 为了保证下面的操作清晰，我们把src下面除了App.js、index.js和index.css文件的其他文件
* 修改index.js文件

```js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App.jsx';
import { StoreProvider } from "./Store";

ReactDOM.render(
  <StoreProvider>
    < App / >
  </StoreProvider>
  , document.getElementById('root'));
```

* 将App.js重命名为App.jsx，并用下面的代码替换

```js
import React from 'react';

function App() {
  return (
    <React.Fragment>
      <div>
        <h1>Example</h1>
        <p>Favourite</p>
      </div>
    </React.Fragment>
  );
}

export default App;
```

## Redux概念

根据它的文档介绍，Redux能够概括为三个基本概念：**stores**，**actions**和**reducers**

[![redux概念或者redx流程](https://cdn-images-1.medium.com/max/1600/1*OLdS7KqIA_4f1RHu0-YtsQ.jpeg)](https://camo.githubusercontent.com/ea28b35fd541912ff0299c8fe57c8bcf6976671f/68747470733a2f2f63646e2d696d616765732d312e6d656469756d2e636f6d2f6d61782f313630302f312a4f4c6453374b7149415f346631524875302d597473512e6a706567)

1. **action**只有一个事情就是触发`state`的改变，它通常返回一个带有**type**和**payload**的对象

```js
function actionFunc(dispatch) {
  return dispatch({type: 'COMPLETE_TODO', payload: 1}) 
}
```

这里的dispatch参数告诉操作该对象需要影响的store是什么，因为应用程序可以有多个reducers。这将在以后有意义。

1. **reducer**指定store将受操作影响的部分。因为redux存储是不可变的，所以reducer返回一个替换当前store的新store。Reducers通常写为switch语句。

```js
function visibilityFilter(state, action) {
  switch (action.type) {
    case 'SET_VISIBILITY_FILTER':
      return action.payload;
    default:
      return state;
  }
}
```

1. **store**将所有应用程序数据保存在对象树中。Redux有一个store，但[Facebook的Flux](https://facebook.github.io/flux/)等其他state管理器可以拥有多个store。

```js
{
  visibilityFilter: 'SHOW_ALL',
  todos: [
    text: 'Consider using Redux',
    completed: true,
  ]
}
```

1. 应用程序中任何组件的组件都可以访问**store**，并可以通过触发**action**来更改**store**。

下面用React自带的hooks和context实现下这个概念

## 创建Store

* 在src目录下面创建一个Store.js文件

在这里，我们将使用react context来创建一个父组件，该组件将为其子组件访问它所拥有的数据。这里暂时不深入研究context，但基本上是有provider - consumer关系。**provider**拥有所有数据，**consumer**使用它（有意义）。

* 添加下面的代码到Store.js文件中

```js
import React from "react";

export const Store = React.createContext();

const initialState = {};

function reducer () {}

export function StoreProvider(props) {}
```

第3行创建了一个子组件将订阅的context对象。暂时跳过初始化state对象和reducer函数，先看下**StoreProvider**

* 添加下面的代码到**StoreProvider**中

```js
export function StoreProvider(props) {
  return <Store.Provider value='data from store'>{props.children}</Store.Provider>
}
```

* 现在修改index.js文件并且从./Store导入StoreProvider

```bash
import { StoreProvider } from './Store';
```

* 将组件放入到中，添加完的代码看起来类似如下

```js
ReactDOM.render(
  <StoreProvider>
    <App />
  </StoreProvider>,
  document.getElementById('root')
);
```

* 在App.jsx中导入Store，代码如下

```js
import { Store } from './Store';
```

* 在App函数中加入如下代码

```js
const store = React.useContext(Store);
```

这里使用了第一个hooks，就是useContext。这将使组件可以访问context提供程序的value属性中的数据。

* 在`<React.Fragment>`里面第一行添加`{console.log(store)}`
* 启动程序打开浏览器，在开发工具控制台中将会看到```data from store````

[![hooks和context](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560505341/gowhich/gw_182_1.png)](https://camo.githubusercontent.com/6e814b92316e83010ede3d4c94f448c434e755c9/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303530353334312f676f77686963682f67775f3138325f312e706e67)

如果你没有看到，请确认下你的代码是否跟我的一致

* 文件结构

[![hooks和context](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560505587/gowhich/gw_182_2.png)](https://camo.githubusercontent.com/72a115fc4135fd059700101cb99c38a1f55a6188/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303530353538372f676f77686963682f67775f3138325f322e706e67)

* 代码结构

```js
// index.js

import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { StoreProvider } from './Store';

ReactDOM.render(
  <StoreProvider>
    <App />
  </StoreProvider>,
  document.getElementById('root')
);
```

// Store.js

```js
import React from 'react';

export const Store = React.createContext();

const initialState = {};

function reducer() {}

export function StoreProvider(props) {
  return <Store.Provider value='data from store'>{props.children}</Store.Provider>;
}
```

// App.jsx

```jsx
import React from 'react';
import { Store } from './Store';

export default function App() {
  const store = React.useContext(Store);

  return (
    <React.Fragment>
      {console.log(store)}
      <div>
        <h1>Example</h1>
        <p>Favourite</p>
      </div>
    </React.Fragment>
  );
}
```

## 创建Reducer

如果看到这里的话，说明前面的实现是你已动手实现了下，并且是没有问题的。下面继续更新代码

* Store.js文件中，在initialState中加入下面的代码

```js
const initialState = {
  films: [],
  favourites: [],
};
```

这是我们的初始**store**在添加任何新数据之前的样子。

* 修改reducer函数看起来像这样

```js
function reducer (state, action) {
  switch(action.type) {
    case 'FETCH_DATA':
      return { ...state, films: action.payload };
    default:
      return state;
  }
}
```

前面看到的reducer函数有两个参数，state - 运行时store中的数据，以及action - 返回的action对象。目前，我们的reducer有一个case 'FETCH\_DATA'，它将用传回的数据替换我们的films数组。如果调用了无效操作，则需要使用**default**关键字返回状态。

* 在StoreProvider函数中，添加下面的代码

```js
const [state, dispatch] = React.useReducer(reducer, initialState);
const value = { state, dispatch };
```

这里遇到了第二个hook，就是[useReducer](https://reactjs.org/docs/hooks-reference.html#usereducer)。它需要两个参数**reducer**和**initialState**。它返回一个数组，里面分别是state - store里面的数据和dispatch - 我们如何向reducer发送动作（反过来改变我们的state）。我希望这是有意义的。

然后，我们将新状态转换为对象，并将其分配给名为value的变量。基本上价值是相同的

```js
const value = {
  state: state,
  dispatch: dispatch
}
```

但是可以在Javascript ES6及更高版本中编写更短的内容。

* 在Store.Provider中用下面的代码替换`value='data from store'`

```js
value={value}
```

现在我们可以将state和dispatch传递给子组件。

* 修改App.jsx文件，将`const store = React.useContext(Store)`替换为`const { state, dispatch } = React.useContext(Store);`

现在更新控制台日志中的store以查看状态并查看控制台。

[![hooks和context](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560507182/gowhich/gw_182_3.png)](https://camo.githubusercontent.com/34cce5a2d723a2b6c110b3962a7b38a5ae2b6414/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303530373138322f676f77686963682f67775f3138325f332e706e67)

你应该看到它从Store.jsx中提取我们的initialState数据。现在让我们来处理一些数据。

## 创建Action

我们的redux概念的最后一块。

* 修改App.jsx文件，再返回组件之前添加一个匿名函数，叫fetchDataAction

```js
const fetchDataAction = async () => {}
```

我们将使用[fetch api](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)使用async/await从[tvmaze](https://www.tvmaze.com/)api获取数据。

* 添加新代码到我们的新fetchDataAction函数中

```js
const fetchDataAction = async () => {
  const data = await fetch('https://api.tvmaze.com/singlesearch/shows?q=rick-&-morty&embed=episodes');

  const dataJson = await data.json();

  return dispatch({
    type: 'FETCH_DATA',
    payload: dataJson._embedded.episodes
  });
}
```

我建议您在浏览器中访问api url并查看数据。episodes列表在\_embedded之下。

我们返回dispatch方法，其type和payload的对象作为属性，以便我们的reducer将知道要执行的是什么情况。

我们希望每次页面加载时都运行**fetchDataAction**，所以让我们将它放在返回组件的上方的[useEffect](https://reactjs.org/docs/hooks-effect.html) hook中。

```js
React.useEffect(() => {
  state.films.length === 0 && fetchDataAction();
});
```

上面的代码类似于componentDidMount。基本上应用程序加载，如果state.episodes为空（默认情况下），则运行fetchDataAction。

保存并刷新页面。查看开发工具控制台，您应该看到一些数据。

[![hooks和context](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560507846/gowhich/gw_182_4.png)](https://camo.githubusercontent.com/0faa58e8e8e3aee0067edd24fa6b72fbc43f4145/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303530373834362f676f77686963682f67775f3138325f342e706e67)

简而言之，这就是redux模式。某些情况触发了一个动作（在我们的例子中它是一个页面加载），动作在reducer中运行一个case，它反过来更新了store。现在让我们使用这些数据。

* 修改App.jsx，在`<p>Favourite</p>`下面加入如下代码

```jsx
<section>
          {
            state.films.map(f => {
              return (
                <section key={f.id}>
                  <img
                    src={f.image ? f.image.medium : ''} 
                    alt={`Year and Date ${f.name}`}
                  />
                  <div>
                    {f.name}
                  </div>
                  <section>
                    <div>
                      Season: {f.season} Number: {f.number}
                    </div>
                  </section>
                </section>
              )
            })
          }
        </section>
```

这段代码基本上遍历我们的剧集数组中的对象（在用api填充数据之后），并用这些数据填充dom。随意添加或删除您选择的数据点。

[![hooks和context](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560508362/gowhich/QQ20190614-182830-HD-1.gif)](https://camo.githubusercontent.com/44ae199708dd38fec19cc149c362f555150ddd0f/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303530383336322f676f77686963682f515132303139303631342d3138323833302d48442d312e676966)

参考自:<https://medium.com/octopus-labs-london/replacing-redux-with-react-hooks-and-context-part-1-11b72ffdb533>
