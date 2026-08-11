---
title: "抛弃Redux，迎接React的hooks和context（二）"
date: "2025-07-10 10:57:55"
slug: "pao-qi-redux-ying-jie-react-de-hooks-he-context-er"
categories: ["技术"]
tags: ["RequireJS"]
aliases:
  - "/2025/07/10/抛弃Redux，迎接React的hooks和context（二）/"
  - "/2025/07/10/抛弃Redux，迎接React的hooks和context（二）.html"
  - "/抛弃Redux，迎接React的hooks和context（二）/"
  - "/抛弃Redux，迎接React的hooks和context（二）.html"
  - "/2025/07/10/抛弃Redux-迎接React的hooks和context-二/"
  - "/2025/07/10/抛弃Redux-迎接React的hooks和context-二.html"
  - "/2025/07/10/pao-qi-redux-ying-jie-react-de-hooks-he-context-er/"
  - "/2025/07/10/pao-qi-redux-ying-jie-react-de-hooks-he-context-er.html"
  - "/pao-qi-redux-ying-jie-react-de-hooks-he-context-er.html"
---
继续【[抛弃Redux，迎接React的hooks和context（一）](http://localhost:6419/)】文章继续介绍一些新的东西

如果你还不知道什么情况的话，建议回到前面的文章看下，做下热身了解。

## 样式

前面的文章我们没有做关于样式太多的操作，这里我们简单的加一些样式，使得我们的应用能够更加具有导航性

* 添加下面的样式到文件index.css

```css
.episode-layout {
  display: flex;
  flex-wrap: wrap;
  min-width: 100vh;
}

.episode-box {
  padding: 0.5rem;
}

.header {
  align-items: center;  
  background: white;
  border-bottom: 1px solid black;
  display: flex;
  justify-content: space-between;
  padding: .5rem;
  position: sticky;
  top: 0;
}
.header * {
  margin: 0;
}
```

* 在index.js文件中StoreProvider下面加入下面的代码

```js
import './index.css';
```

* 在App.jsx文件中，给`<section>`标签添加className属性，让className等于**film-layout**
* 在`<section>`标签中的`state.films.map`里面的`<section>`添加className，让className等于**film-box**
* 将最后的那个`</div>`，在`</React.Fragment>`标签上面的，移到`<p>`标签下面。
* 最后给`<div>`标签添加属性className，让className等于**header**

最后App.jsx的代码如下

```jsx
import React from 'react';
import { Store } from './Store';

function App() {
  const { state, dispatch } = React.useContext(Store);

  const fetchDataAction = async () => {
    const data = await fetch('https://api.tvmaze.com/singlesearch/shows?q=rick-&-morty&embed=episodes');

    const dataJson = await data.json();

    return dispatch({
      type: 'FETCH_DATA',
      payload: dataJson._embedded.episodes
    });
  }

  React.useEffect(() => {
    state.films.length === 0 && fetchDataAction();
  });

  return (
    <React.Fragment>
      {console.log(state)}
      <div className="header">
        <h1>Example</h1>
        <p>Favourite</p>
      </div>
      <section className="film-layout">
        {
          state.films.map(f => {
            return (
              <section key={f.id} className="film-box">
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
    </React.Fragment>
  );
}

export default App;
```

让我们再次运行`npm start`，如果已经启动则不需要这个操作，会自动刷新

[![react context and hooks](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560852738/gowhich/gw_183_1.gif)](https://camo.githubusercontent.com/fccdf08e079944b0be3c1989d444459d386988cf/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303835323733382f676f77686963682f67775f3138335f312e676966)

## 添加功能

* 仍然是在App.jsx文件中，在包含Season和Number的`</div>`标签下面添加下面的代码

```jsx
<button type='button' onClick={() => toggleCreatorAction(f)}>ADD</button>
```

* 在**fetchDataAction**函数下面添加**toggleCreatorAction**函数，其代码如下

```jsx
const toggleCreatorAction = film => {
  dispatch({
    type: 'CREATOR_ADD',
    payload: film
  })
}
```

正如这里面写的，**toggleCreatorAction**函数返回一个dispatch，这个dispatch发送一个creator对象到store，你也许已经猜到了这个函数的功能。

* 打开**Store.js**，在**reducer**人中添加下面这个case在**default**上面

```jsx
case 'CREATOR_ADD':
  return {
    ...state,
    creators: [...state.creators, action.payload]
  }
```

当点击按钮ADD的时候，*CREATOR\_ADD*的case会更新creators数组，并将新的creator对象添加到creators中

* 打开浏览器查看开发者工具，然后点击ADD按钮将会看到creators更新变化的情况

[![react context and hooks](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560852788/gowhich/gw_183_2.gif)](https://camo.githubusercontent.com/be215dffbc984332bb213b481d2f3b58707e539f/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303835323738382f676f77686963682f67775f3138335f322e676966)

## 删除功能

* 修改**toggleCreatorAction**函数修改后代码如下

```jsx
const toggleCreatorAction = film => {
  const filmInCreator = state.creators.includes(film)

  let dispatchObj =  {
    type: 'CREATOR_ADD',
    payload: film,
  }

  if (filmInCreator) {
    const filmWithoutCreator = state.creators.filter(creator => creator.id !== film.id)

    dispatchObj = {
      type: 'CREATOR_DEL',
      payload: filmWithoutCreator,
    }
  }

  return dispatch(dispatchObj)
}
```

filmInCreator用来检查creators中是否已经存在film，如果存在的话则进行删除操作，filmWithoutCreator用来移除存在的film，然后用新的filmWithoutCreator来更新creators数组。

* 在Store.js中的reducer中添加一个新的case，代码如下

```jsx
case 'CREATOR_DEL':
  return {
    ...state,
    creators: action.payload
  }
```

上面的功能完成后，该有的功能都差不多了，但是为了向用户展示，正在发生的事情，我们需要再做一些事情

* 修改App.jsx，修改header部分，修改后的代码如下

```jsx
<header>
  <div className="header">
    <h1>Example</h1>
    <p>Favourite</p>
  </div>
  <div>
    Creator(s) {state.creators.length}
  </div>
</header>
```

* 修改组件，用下面的代码替换掉*ADD*

```jsx
{state.creators.find(creator => creator.id === f.id) ? 'DEL' : 'ADD'}
```

这段代码使用了 [array.find](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/find) 方法，为了检查film对象的id是否存在于creators数组中，如果存在，则显示*DEL*

* 小样式的修改，在`<div>{f.name}</div>`下面的`<section>`，给`<section>`标签添加一个style，代码如下

```jsx
style={{ display: 'flex', justifyContent: 'space-between' }}
```

希望一切顺利，你有代码在浏览器中类似如下。

[![react context and hooks](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560852825/gowhich/gw_183_3.gif)](https://camo.githubusercontent.com/792eb5dea55bec274f5eb5730763e9eec17adfdf/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303835323832352f676f77686963682f67775f3138335f332e676966)

## 分隔代码

前面做了一些基本逻辑上的实现操作，下面做一些关于代码拆分的操作

* 创建一个新的文件，叫做FlimList.jsx，其代码如下

```jsx
import React from 'react';

export default function FilmList(props) {
  const { films, toggleCreatorAction, creators } = props;
}
```

你可能已经明白我们要做的事情了

* 在App.jsx文件中，复制`state.films.map`的代码，然后粘贴到***creators***文件中。
* 在**FilmList.jsx**中将`state.films.map`替换为`return films.map`
* 将`state.creators.find`替换为`creators.find`

所有步骤做完后，**FilmList.jsx**文件中的代码看起来如下

```jsx
import React from 'react';

export default function FilmList(props) {
  const { films, toggleCreatorAction, creators } = props;

  return films.map(f => {
    return (
      <section key={f.id} className="film-box">
        <img
          src={f.image ? f.image.medium : ''}
          alt={`Year and Date ${f.name}`}
        />
        <div>
          {f.name}
        </div>
        <section style={{ display: 'flex', justifyContent: 'space-between' }}>
          <div>
            Season: {f.season} Number: {f.number}
          </div>
          <button type='button' onClick={() => toggleCreatorAction(f)}>
            {creators.find(creator => creator.id === f.id) ? 'DEL' : 'ADD'}
          </button>
        </section>
      </section>
    )
  })
}
```

## suspense 和 lazy

* 在App.jsx文件中加入下面的代码

```jsx
const FilmList = React.lazy(() => import('./FilmList'));
```

* 在`<React.Suspense>`嵌套标签`<React.Fragment>`
* `<React.Suspense>`标签应该有下面这个属性

```jsx
**fallback**={<div>Loading...</div>}
```

* 移除`<section className="film-layout">...</section>`部分的代码，并用`<FilmList {...props} />`替换
* 添加下面的代码在返回组件的上面

```jsx
const props = {
  films: state.films,
  toggleCreatorAction,
  creators: state.creators,
};
```

以上所有操作做完之后，保存代码并刷新浏览器应该会正常工作，并且在打开的时候会有一个'Loading...'状态

[![react context and hooks](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1560852849/gowhich/gw_183_4.gif)](https://camo.githubusercontent.com/029743b6ce005a8d93e82b3c8bf80bd6b6097e57/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f6479356476637563312f696d6167652f75706c6f61642f76313536303835323834392f676f77686963682f67775f3138335f342e676966)

参考自:<https://medium.com/octopus-labs-london/replacing-redux-with-react-hooks-and-context-part-2-838fd20e6739>
