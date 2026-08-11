---
title: "React Pager分页实例"
date: "2025-06-30 12:01:03"
slug: "react-pager-fen-ye-shi-li"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/06/30/React-Pager分页实例/"
  - "/2025/06/30/React-Pager分页实例.html"
  - "/React-Pager分页实例/"
  - "/React-Pager分页实例.html"
  - "/2025/06/30/react-pager-fen-ye-shi-li/"
  - "/2025/06/30/react-pager-fen-ye-shi-li.html"
  - "/react-pager-fen-ye-shi-li.html"
---
React的分页实例来了！[适合与webpack组合使用，不太适合纯html页面调用，不过可以根据您自己的情况进行改写]

```js
define(function(require,exports,module){
   'use strict';
   
    var React = require('reactAddons');
   
    module.exports = React.createClass({
        clickHandler:function(e){
            e.preventDefault();
            this.props.listData(e.currentTarget.dataset.page);
        },
        render:function(){
            var cx = React.addons.classSet;
            var preClass = cx({
                'previous':true,
                'disabled':this.props.pre_stop == true
            });
            var nextClass = cx({
                'next':true,
                'disabled':this.props.next_stop == true
            });
   
            return (
                <nav>
                    <ul className="pager">
                        <li className={preClass}>
                            <a href="#" onClick={this.clickHandler} data-page={this.props.page-1}>
                                <span aria-hidden="true" >&larr;</span> Older
                            </a>
                        </li>
                        <li className={nextClass}>
                            <a href="#" onClick={this.clickHandler} data-page={this.props.page+1}>
                                Newer <span aria-hidden="true">&rarr;</span>
                            </a>
                        </li>
                    </ul>
                </nav>
            );
        }
    });
   
});
```

如何调用？

```js
const PagerTest = React.createClass(){
  getInitialState:function(){
    return {
      lostData: {
        lostUserItem: [],
        totalCount: 0,
        currentTotalCount: 0
      },
      pagesize: 20,
      page: 1,
      params: {}
    }
  },
  render:function(){
    let nextStop = false;
    let preStop = false;
    //this.state.lostData.lostUserItem 这个就是一个数据数组
    if (this.state.lostData.lostUserItem.length < this.state.pagesize) {
      nextStop = true;
    }

    if ((this.state.page - 1) <= 0) {
      preStop = true;
    }

    let pager_props = {
      page: this.state.page,
      pre_stop: preStop,
      next_stop: nextStop,
      listData: this.loadMorePage
    };
    return (
      <Pager {...pager_props}/>
    );
  }
}
```

