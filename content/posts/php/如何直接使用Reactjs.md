---
title: "如何直接使用Reactjs"
date: "2025-07-10 10:58:10"
slug: "ru-he-zhi-jie-shi-yong-reactjs"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/10/如何直接使用Reactjs/"
  - "/2025/07/10/如何直接使用Reactjs.html"
  - "/如何直接使用Reactjs/"
  - "/如何直接使用Reactjs.html"
  - "/2025/07/10/ru-he-zhi-jie-shi-yong-reactjs/"
  - "/2025/07/10/ru-he-zhi-jie-shi-yong-reactjs.html"
  - "/ru-he-zhi-jie-shi-yong-reactjs.html"
---
这里说的直接使用Reactjs，指的是不使用任何打包工具，直接在代码中引入，这种方式类似于在html页面中直接引入javascript脚本文件，不过现在的前端开发基本也不建议使用类似的这种方式，而是喜欢建改代码工程化，包括一些打包发布之类的。比如使用webpack等类似的打包工具，可以包括压缩、分包各种优化放在里面。直接引入的方式就是我们自己写的代码，直接上线使用了，不包括什么压缩、分包之类的，所以我也不推荐直接引入的方式，除非引入的是打包好的，并进行了优化的，方便前端进行加载。

## Reactjs安装

```html
<script src="/static/js/@babel/[email protected]/babel.min.js"></script>
<script src="/static/js/[email protected]/umd/react.production.min.js" crossorigin></script>
<script src="/static/js/[email protected]/umd/react-dom.production.min.js" crossorigin></script>
```

这里使用了babel是为了对jsx语法进行转义，将react语法转义为es5通用语法。同时也可以将一些es6语法进行部分转义，为什么说是部分，因为在遇到async/await的时候，并没有进行转义，这个问题有待解决。我试过绑定plugins的方式，但是结果都不是很理想。

## Fetch Api安装

```html
<script src="/static/js/3.0.0/fetch.umd.js" crossorigin></script>
```

这里添加这个fetch的api，主要是为了替换类似jquery值之类的ajax，当然你也可以使用。不过需要谨慎“异步”的逻辑

## 添加jsx代码

```html
<script type="text/babel">

// store
const Store = React.createContext();

function StoreProvider(props) {
  const [state, dispatch] = React.useReducer(reducer, initialState);
  const value = { state, dispatch };
  return <Store.Provider value={value}>{props.children}</Store.Provider>
}

// reducer
const initialState = {
  renderData: {!! json_encode($renderData) !!}, // server端直接进渲染的变量
};

function reducer (state, action) {
  switch(action.type) {
    case 'FETCH_DATA':
      return { ...state, films: action.payload };
    default:
      return state;
  }
}

// view
function MainContainer () {
  const {state, dispatch} = React.useContext(Store);

  const checkPoint = (data) => {
    return fetch('/xxx/xxx/xxx', {
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: "same-origin",
      method: 'POST',
    });
  }

  const exchangeHandle = (id) => {
    checkPoint({id:id}).then(data => {
      data.json().then(o => {
        console.log(o);

        if (!o.success) {
          throw new Error(o.message);
        }

        window.location.href = '/xxx/xxx/xxx/'+id;
      }).catch(e => {
        console.log(e);
        toast({
          'message': e.message
        });
      });
    }).catch(e => {
      console.log(e);
      toast({
        'message': '网络异常'
      });
    });
  }

  const pointHandle = () => {
    window.location.href = '/xxx/xxx/xxx';
  }

  const ruleLinkHandle = () => {
    window.location.href = state.renderData.ruleLink;
  }

  React.useEffect(() => {
    // 页面加载后的逻辑

  });

  console.log(state);

  let levelComponent = (<span></span>);
  if (state.renderData.level == 1) {
    levelComponent = (<img src='/images/xxx/xxx/lv1.png' className='level-logo' />);
  } else if (state.renderData.level == 2) {
    levelComponent = (<img src='/images/xxx/xxx/lv2.png' className='level-logo' />);
  }

  return (
    <React.Fragment>
      <div className='main-container'>
        <div className="bg-container">
          <img src="/images/xxx/xxx/bg.png" className="bg-img"/>
        </div>
        <div className="content-1-container">
          <span className="level-container">
            {levelComponent}
          </span>
          <span className="point-container" onClick={ruleLinkHandle}>等级与积分说明<img src='/images/xxx/xxx/help_icon.png' className='rule-img' /></span>
        </div>
        <div className="content-2-container">
          <span className="point-2-container">{state.renderData.point}</span>
        </div>
        <div className="content-3-container">
          <span className="point-3-container" onClick={pointHandle}>我的积分 <img src='/images/xxx/xxx/point-arrow.png' /></span>
        </div>
        <div className="line-container"></div>
        <div className="goods-container">
          <div className="goods-title">积分商城</div>
          <div className="goods-item">
          {
            state.renderData.goods_item.map((v, k) => {
              return (
                <div className="goods-row" key={v.goods_id}>
                  <div className="goods-content-container">
                    <div className="img"><img src={v.icon} className='img-1' /></div>
                    <div className="title">{v.name}</div>
                    <div className="price">
                      <span>{v.point}积分</span><span className="money">￥{v.original_price}</span>
                    </div>
                    <div className="btn">
                      <span className="btn-ele" onClick={() => exchangeHandle(v.goods_id)}>立即兑换</span>
                    </div>
                  </div>
                </div>
              );
            })
          }
          </div>
        </div>
      </div>
    </React.Fragment>
  )
}

const domContainer = document.querySelector('#root');

ReactDOM.render(
  <StoreProvider>
    <MainContainer />
  </StoreProvider>,
  domContainer
);
</script>
```

演示的代码稍微有点多，不过确实是使用了本人在开发的项目中的代码，并没有做太多删减，当然这里也只是做了一个例子，这个代码并不能直接copy后直接使用的。

另外，你也许会觉得这个代码放到一个文件中会比较好，是的，那么在说下引入的方式，比如我在实际项目中使用了tost，那我自己就写了一个toast，但是这个toast是在所有页面展示的时候都能统一样式，所以需要抽出来放到一个文件，然后可以在任意页面调用，于是这个文件可以这样引用，

```html
<script type="text/babel" src="/js/xxx/xxx/toast.jsx"></script>
```

这个文件的代码大致如下

```jsx
// store
const Store = React.createContext();

function StoreProvider(props) {
  const [state, dispatch] = React.useReducer(reducer, initialState);
  const value = { state, dispatch };
  return <Store.Provider value={value}>{props.children}</Store.Provider>
}

// reducer
const initialState = {
  show: true
};

function reducer (state, action) {
  switch(action.type) {
    case 'FETCH_DATA':
      return { ...state, films: action.payload };
    default:
      return state;
  }
}

function Toast(props) {
  return (
    <React.Fragment>
      <div className='toast-container'>
        <div className='toast-text'>
          <img src="/images/xxx/xxx/emijo_icon_1.png" />
          <p>{props.message}</p>
        </div>
      </div>
    </React.Fragment>
  );
}

const toastContainer = [];

function toast(properties) {
  const { ...props } = properties || {};

  const divEle = document.createElement('div');

  if (toastContainer.length > 0) {
    return false;
  }
  const t = setTimeout(() => {
    document.body.removeChild(divEle);

    clearTimeout(t);
    toastContainer.pop();
  }, props.timeout || 2000);

  document.body.appendChild(divEle);
  toastContainer.push(1);

  ReactDOM.render(<StoreProvider><Toast {...props} /></StoreProvider>, divEle);
}
```

在其他页面中可以直接调用方法`toast({message: '我是一个提示'})`。

之所以记录这个Reactjs如何在不安装打包工具的情况下直接使用，是因为安装一个打包工具在取做配置然后在开发还是蛮麻烦的，但是要开发的功能其实并没有多么复杂。可以临时这样用一下。实际上在使用的过程中，如果遇到太复杂的功能建议不这样用，因为babel将jsx语法进行转义的时候，是要花费时间的。
