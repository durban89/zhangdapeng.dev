---
title: "ReactJS 在  Browser 环境下是如何开发的"
date: "2025-07-03 11:08:00"
slug: "reactjs-zai-browser-huan-jing-xia-shi-ru-he-kai-fa-de"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/03/ReactJS-在-Browser-环境下是如何开发的/"
  - "/2025/07/03/ReactJS-在-Browser-环境下是如何开发的.html"
  - "/ReactJS-在-Browser-环境下是如何开发的/"
  - "/ReactJS-在-Browser-环境下是如何开发的.html"
  - "/2025/07/03/reactjs-zai-browser-huan-jing-xia-shi-ru-he-kai-fa-de/"
  - "/2025/07/03/reactjs-zai-browser-huan-jing-xia-shi-ru-he-kai-fa-de.html"
  - "/reactjs-zai-browser-huan-jing-xia-shi-ru-he-kai-fa-de.html"
---
以前使用reactjs做前端开发都是webpack打包然后在运行，这样的好处是，你开发的环境是一个纯碎在写nodejs的感觉，而且还能应用很多ES6的新特性，岂不快哉！

最近在做后端，也由于使用webpack时间长，一直没有找到很好的办法去解决，自动打包缓慢的问题，还有就是每次开发你都要去根据具体情况写要给跟webpack相关的config文件。

于是就试着用Browser的环境进行开发，结果今天尝试下后，果然还是很不错的。

首先引入react，我这里使用reflux，然后再引入reflux，再引入babel。

```html
<script src="/js/react.min.js" type="text/javascript" charset="utf-8"></script>
<script src="/js/react-dom.min.js" type="text/javascript" charset="utf-8"></script>
<script src="/js/reflux.min.js" type="text/javascript" charset="utf-8"></script>
<script src="https://cdn.bootcss.com/babel-standalone/6.10.3/babel.min.js"></script>
```

类似下面这样，跟使用jquery是一样的感觉。

接下来我们写一个简单的分页的组件。

```jsx
var Pagination = React.createClass({
  clickHandler: function (e) {
    e.preventDefault();
    if (e.currentTarget.dataset.handle == 'false') {
      this.props.listData(e.currentTarget.dataset.page);
    }
  },
  render: function () {
    let nextStop = false;
    let preStop = false;
    if (this.props.currentdata.length < this.props.pagesize) {
      nextStop = true;
    }

    if ((this.props.page - 1) <= 0) {
      preStop = true;
    }

    const preClass = preStop ? 'previous disabled' : 'previous';
    const nextClass = nextStop ? 'next disabled' : 'next';

    let pre_page = parseInt(this.props.page) - 1;
    let next_page = parseInt(this.props.page) + 1;

    return (
      <nav>
        <ul className="pager">
          <li className={preClass}>
            <a href="#" onClick={this.clickHandler} data-page={pre_page} data-handle={preStop}>
              上一页
            </a>
          </li>
          <li className={nextClass}>
            <a href="#" onClick={this.clickHandler} data-page={next_page} data-handle={nextStop}>
              下一页
            </a>
          </li>
        </ul>
      </nav>
    );
  }
});

Pagination.propTypes = {
  currentdata: React.PropTypes.array.isRequired,
  page: React.PropTypes.number.isRequired,
  pagesize: React.PropTypes.number.isRequired,
  listData: React.PropTypes.func.isRequired
};
```

就是这样，不需要其他的 export的东西，以为我们只要在页面中引入就可以了。

```html
<script src='/js/components/partial/Pagination.js' type="text/babel"></script>
```

就像上面这样就可以了。

下面我们调用一下：

```jsx
var pagerProps = {
    page: this.state.page,
    pagesize: this.state.pageSize,
    currentdata: this.state.recordItem,
    listData: this.loadMorePage
};
```

这里的loadMorePage是另外组件里面的一个方法，用来加载下一页数据的，page就是页数，pageSize就是每页的数量。

```jsx
loadMorePage:function(page){
    page = parseInt(page);
    this.setState({page: page});
    Action.getRecordItem(this.props.uid, page, this.state.pageSize);
},
```

就像上面这样子，加载一下数据就可以渲染到列表的组件里面去了。然后就是如何再其他组件里面调用了。

```jsx
<div className="col-md-12">
    <Pagination {...pagerProps}/>
</div>
```

pagerProp就是刚才上面的变量。这样就可以使用了。

总体感觉下来起始跟我之前的使用方法区别就是，不再需要去import和export了。

而且不需要去不断的打包了。不知道后面开发还会遇到啥其他问题，继续更新...


