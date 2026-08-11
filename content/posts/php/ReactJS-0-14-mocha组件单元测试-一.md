---
title: "ReactJS 0.14 mocha组件单元测试（一）"
date: "2025-07-02 16:01:14"
slug: "reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-yi"
categories: ["技术"]
tags: ["ReactJS", "Mocha"]
aliases:
  - "/2025/07/02/ReactJS-0.14-mocha组件单元测试（一）/"
  - "/2025/07/02/ReactJS-0.14-mocha组件单元测试（一）.html"
  - "/ReactJS-0.14-mocha组件单元测试（一）/"
  - "/ReactJS-0.14-mocha组件单元测试（一）.html"
  - "/2025/07/02/ReactJS-0-14-mocha组件单元测试-一/"
  - "/2025/07/02/ReactJS-0-14-mocha组件单元测试-一.html"
  - "/2025/07/02/reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-yi/"
  - "/2025/07/02/reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-yi.html"
  - "/reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-yi.html"
---
先来一个简单的小组件：

```jsx
import React, { Component } from 'react'


class Bar extends Component {
  render() {
    return (
      <div className='bar'>
        <h5>And I am Bar!</h5>
      </div>
    );
  }
}

export default Bar;
```

好了，到这里就足够了，来看看测试如何写：

```jsx
import React from 'react';
import expect from 'expect';
import TestUtils from 'react-addons-test-utils';
import Bar from '../../app/js/components/test/Bar';

describe('Bar components', () => {
  before('render and locate element ', function() {
    const renderedComponent = TestUtils.renderIntoDocument(
      <Bar/>
    );

    const bar = TestUtils.findRenderedDOMComponentWithClass(
      renderedComponent,
      'bar'
    );

    this.bar = bar;
  });

  it('bar should exist', function() {
    expect(this.bar).toExist();
  });

  it('bar should be closed', function() {
    expect(this.bar.getAttribute('class')).toBe('bar');
  });
})
```

在运行前，做个简单的配置：

package.json

在scripts中添加

```json
"test": "NODE_PATH=./app/js/lib ./node_modules/mocha/bin/mocha --compilers js:babel-register --recursive --require ./test/setup.js",
"test:watch": "npm test -- --watch"
```

添加`NODE_PATH`的原因是我要加载自己的lib库，不然在执行mocha的时候，会因为某些组建中调用了自己的库，而导致找不到对一个恩lib而报错。

这里还添加了一个setup.js,这个主要是为了解决类似window这类的问题，毕竟react渲染是需要dom的嘛。

setup.js代码如下：

```js
import { jsdom } from 'jsdom';

global.document = jsdom('<!doctype html><html><body></body></html>')
global.window = document.defaultView
global.navigator = global.window.navigator
```


