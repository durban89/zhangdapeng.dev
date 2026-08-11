---
title: "分享React表单提交获取值的方式"
date: "2025-07-01 15:04:08"
slug: "fen-xiang-react-biao-dan-ti-jiao-huo-qu-zhi-de-fang-shi"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/01/分享React表单提交获取值的方式/"
  - "/2025/07/01/分享React表单提交获取值的方式.html"
  - "/分享React表单提交获取值的方式/"
  - "/分享React表单提交获取值的方式.html"
  - "/2025/07/01/fen-xiang-react-biao-dan-ti-jiao-huo-qu-zhi-de-fang-shi/"
  - "/2025/07/01/fen-xiang-react-biao-dan-ti-jiao-huo-qu-zhi-de-fang-shi.html"
  - "/fen-xiang-react-biao-dan-ti-jiao-huo-qu-zhi-de-fang-shi.html"
---
很奇怪的，这个是要去自己发现的，我也是在摸索中发现的，其实React的使用，只有你发现了，才觉得好玩，最近的Reflux就是这样子的。

##表单提交部分

```jsx
handleSubmit:function(e){
  e.preventDefault();
  var params = {};
  var keys = React.findDOMNode(this.refs.keys).value.trim();
  var days = React.findDOMNode(this.refs.days).value.trim();
  var num = React.findDOMNode(this.refs.num).value.trim();
  var startDate = React.findDOMNode(this.refs.from_date).value.trim();
  var endDate = React.findDOMNode(this.refs.to_date).value.trim();
  //这部分是我自己发现的，哈哈
  var regStyle =  $('.regStyle')[0].value;
  var userTerminal =  $('.userTerminal')[0].value;
  params['keys'] = keys;
  params['regstyle'] = regStyle;
  params['terminal'] = userTerminal;
  params['days'] = days;
  params['num'] = num;
  params['startDate'] = startDate;
  params['endDate'] = endDate;
  this.props.searchHandle(keys,params);
  return false;
},
```

##Render部分

```jsx
render:function(){
  return (
    <form onSubmit={this.handleSubmit} className='form-inline'>
      <div className="row" style={{'marginBottom':'10px'}}>
        <div className="col-md-2">
          <select refs="type" className='form-control input type' data-style="btn-default" title='任务类型'>
            <option value=''>所有</option>
            <option value='exportUserData'>账单导出</option>
            <option value='repairDefaultData'>修复数据</option>
            <option value='updateUserExtendData'>用户数据统计</option>
            <option value='mockerImportMail'>模拟登录导入账单</option>
            <option value='protocolImportMail'>协议登录导入账单</option>
            <option value='mockerFundImport'>公积金查询账单</option>
            <option value='mockerCOImport'>话费查询账单</option>
            <option value='mockerOnlineShopImport'>网络平台导入账单</option>
            <option value='sendPassword'>发送密码</option>
          </select>
        </div>
        <div className="col-md-2">
          <select refs="status" className='form-control input status' data-style="btn-default" title='任务状态'>
            <option value=''>所有</option>
            <option value='200'>执行中</option>
            <option value='100'>等待执行</option>
            <option value='900'>执行成功</option>
          </select>
        </div>
        <div className="col-md-2">
          <input type='submit' className="btn btn-primary btn-block" value="搜索" />
        </div>
      </div>
    </form>
  );
}
```

如果这个时候你使用select的话，什么onChange会在某种情况是不好用的，我的这个就是针对这种情况的，

因为我还使用了selectpicker这个bootstrap插件库"bootstrap-select"，感兴趣的可以去看看


