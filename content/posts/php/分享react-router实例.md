---
title: "分享react-router实例"
date: "2025-07-02 16:01:10"
slug: "fen-xiang-react-router-shi-li"
categories: ["技术"]
tags: ["ReactJS", "React-Router"]
aliases:
  - "/2025/07/02/分享react-router实例/"
  - "/2025/07/02/分享react-router实例.html"
  - "/分享react-router实例/"
  - "/分享react-router实例.html"
  - "/2025/07/02/fen-xiang-react-router-shi-li/"
  - "/2025/07/02/fen-xiang-react-router-shi-li.html"
  - "/fen-xiang-react-router-shi-li.html"
---
终于搞了一个大大的router：

```jsx
ReactDOM.render((
  <Router history={browserHistory}>
    <Route path='/' component={PanelContainer} onEnter={Public.reactCheckLogin}>
      <IndexRoute component={DiagramListShow} />
      <Route path='panel/dataShow' component={DiagramListShow}/>
      <Route path='panel/diagramShow' component={DiagramShow}>
        <IndexRoute component={ApiDiagram}/>
        <Route path='apisum' component={ApiDiagram}/>
        <Route path='opensum' component={ OpenSum }/>
        <Route path='dayregister' component={ DayRegister }/>
        <Route path='activitysum' component={ ActivitySum }/>
        <Route path='recordsum' component={ RecordSum }/>
        <Route path='startsum' component={ StartSum }/>
        <Route path='downloadsum' component={ DownloadSum }/>
        <Route path='recordmoney' component={ RecordMoney }/>
        <Route path='recordnotice' component={ RecordNotice }/>
        <Route path='recordmulticurrency' component={ RecordMultiCurrency }/>
        <Route path='financeClickSum' component={ FinanceClickSum }/>
        <Route path='*' component={NoMatch}/>
      </Route>
    </Route>
    <Route path='/user' component={Container} onEnter={Public.reactCheckLogin}>
      <Route path='userinfo' component={UserInfo}/>
    </Route>
    <Route path='/manager' component={Container} onEnter={Public.reactCheckLogin}>
      <Route path='taskManage' component={TaskManage}/>
      <Route path='sqlManage' component={SqlManage}/>
      <Route path='oauthManage' component={oauthManage} />
    </Route>
    <Route path='/operation' component={Container} onEnter={Public.reactCheckLogin}>
      <Route path='typeinfo' component={Typeinfo}/>
      <Route path='listinfo' component={Listinfo}/>
      <Route path='financeNotice' component={FinanceNotice}/>
    </Route>
    <Route path='/panel/login' component={LoginRender} />
  </Router>
), document.getElementById('main-content'));
```

整理完后，感觉整个网站清晰多了.

这里有几个两点，一点是终于有办法可以判断进入某个路由的时候是否登录了。第二个两点是，之前的版本是在url后面添加hash，看起来很乱，这个版本的更新，从url上你完全看不出这个是用hash实现的。


