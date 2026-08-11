---
title: "react-router 之 routerWillLeave 实现 自定义Dialog"
date: "2025-07-03 11:59:44"
slug: "react-router-zhi-routerwillleave-shi-xian-zi-ding-yi-dialog"
categories: ["技术"]
tags: ["React-Router"]
aliases:
  - "/2025/07/03/react-router-之-routerWillLeave-实现-自定义Dialog/"
  - "/2025/07/03/react-router-之-routerWillLeave-实现-自定义Dialog.html"
  - "/react-router-之-routerWillLeave-实现-自定义Dialog/"
  - "/react-router-之-routerWillLeave-实现-自定义Dialog.html"
  - "/2025/07/03/React-Router-之-routerWillLeave-实现-自定义Dialog/"
  - "/2025/07/03/React-Router-之-routerWillLeave-实现-自定义Dialog.html"
  - "/2025/07/03/react-router-zhi-routerwillleave-shi-xian-zi-ding-yi-dialog/"
  - "/2025/07/03/react-router-zhi-routerwillleave-shi-xian-zi-ding-yi-dialog.html"
  - "/react-router-zhi-routerwillleave-shi-xian-zi-ding-yi-dialog.html"
---
react-router 可以在 react中起到路由的作用，同时也有一个routerWillLeave，这个函数帮助我们再处理路由的时候，离开某个路由要做的某个判断起到了很好的作用，但是version 2 才有这个功能，这里记录下如何自定自己弹出框。

由于react-router自带的功能不是很好，需要我们自己处理一下，于是google参考了stackoverflow上的一篇文章，先建立一个函数

```jsx
function setAsyncRouteLeaveHook(router, route, hook) {
  let withinHook = false
  let finalResult = undefined
  let finalResultSet = false
  router.setRouteLeaveHook(route, nextLocation => {
    withinHook = true
    if (!finalResultSet) {
      hook(nextLocation).then(result => {
        finalResult = result
        finalResultSet = true
        if (!withinHook && nextLocation) {
          router.replace(nextLocation)
        }
      })
    }
    let result = finalResultSet ? finalResult : false
    withinHook = false
    finalResult = undefined
    finalResultSet = false
    return result
  })
}
```

原来的push，我这里改成了replace，为了适合我自己的逻辑。

然后添加一下routerWillLeave的逻辑

```jsx
routerWillLeave(nextLocation) {
    //获取红包相关的信息
    
    return new Promise((resolve, reject) => {
      Popbox.pop({
        text: '你离使用红包只差一步之遥，确定放弃吗？',
        confirmBtnText: '继续绑卡',
        cancelBtnText: '放弃',
        cancelFunc: () => {
          resolve(true);
        },
      });
    })

    return false;
  }
```

这里是需要返回一个Promise的，所以自己的代码记得处理一下。

最后我们跟根据自己的逻辑来设置一下这个Hook。

我这里是放在了componentDidMount中做的处理

```jsx
componentDidMount() {
    const { type } = this.props.params;
      
    if(type){
      setAsyncRouteLeaveHook(this.context.router, this.props.route, this.routerWillLeave);
    }
  }
```

好了，希望能帮到不了解英文的你，或者是找不到资料的你。


