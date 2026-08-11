---
title: "ReactJS 0.14 mocha组件单元测试（二）"
date: "2025-07-02 16:01:18"
slug: "reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-er"
categories: ["技术"]
tags: ["ReactJS", "Mocha"]
aliases:
  - "/2025/07/02/ReactJS-0.14-mocha组件单元测试（二）/"
  - "/2025/07/02/ReactJS-0.14-mocha组件单元测试（二）.html"
  - "/ReactJS-0.14-mocha组件单元测试（二）/"
  - "/ReactJS-0.14-mocha组件单元测试（二）.html"
  - "/2025/07/02/ReactJS-0-14-mocha组件单元测试-二/"
  - "/2025/07/02/ReactJS-0-14-mocha组件单元测试-二.html"
  - "/2025/07/02/reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-er/"
  - "/2025/07/02/reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-er.html"
  - "/reactjs-014-mocha-zu-jian-dan-yuan-ce-shi-er.html"
---
使用react的情况下，一般也会用到redux，那么对于这种在react中使用redux的情况，写测试的时候就不能只用之前的文章里面介绍的方式写了。

来看下组件例子

```jsx
import React, { Component, findDOMNode } from 'react'
import { connect } from 'react-redux'
import { increase, decrease, fetchItems } from '../../actions/counter'

class Home extends Component {

  render() {
    const {
      item,
      number,
      isFetching,
      increase,
      decrease,
      fetchItems
    } = this.props;

    return (
      <div className='container'>
        <div className='row'>
          Some state changes:
          {number}
          <p>Item Length : {item.length}</p>
          <p>Request Item State:{!isFetching ? '已完成' : '获取中'}</p>
        </div>
        <div className='btn-group'>
          <button className='btn btn-primary btn-xs' 
                  onClick={() => increase(1)}>Increase</button>
          <button className='btn btn-primary btn-xs' 
                  onClick={() => decrease(1)}>Decrease</button>
          <button className='btn btn-primary btn-xs' 
                  onClick={() => fetchItems(item)}>FetchItems</button>
        </div>
      </div>
    )
  }

  componentDidMount() {
    // const { item, fetchItems } = this.props;
    // fetchItems(item)
  }

  componentDidUpdate() {
    console.log('did update');
  }
}

export default connect(
  state => {
    const { counter } = state;
    return {
      number: counter.number,
      item: counter.item || [],
      isFetching: counter.isFetching || false
    }
  }, {
    increase,
    decrease,
    fetchItems
  }
)(Home)
```

这里涉及到了actions，那么代码如下：

```jsx
import {
  INCREASE,
  DECREASE,
  REQUEST_DATA,
  FETCH_DATA,
  RECEIVE_DATA,
  ERROR_DATA
} from '../constants';

import Utils from 'utils';
import $ from 'jquery';

const token = Utils.get_token();

require('babel-polyfill');

export function increase(n) {
  return {
    type: INCREASE,
    amount: n
  }
}

export function decrease(n) {
  return {
    type: DECREASE,
    amount: n
  }
}

export function fetchData(item) {
  return dispatch => {
    return new Promise((resolve, reject) => {
      let sql = `SELECT * FROM qeeniao.user limit 0,10`;
      $.ajax({
        url: '/proxy/admin/query',
        dataType: 'json',
        type: 'post',
        data: {
          access_token: token,
          sql: sql
        },
        beforeSend: () => {
          resolve(dispatch(requestData(item)));
        },
        success: (data) => {
          resolve(dispatch(receiveData(item, data)));
        },
        error: (error) => {
          console.log(error.message);
          reject(dispatch(errorData(item, error)));
        }
      })
    });

  }
}

function errorData(item, error) {
  return {
    type: ERROR_DATA,
    item: item || [],
    error: error
  }
}

function requestData(item) {
  return {
    type: REQUEST_DATA,
    item: item || []
  }
}

function receiveData(item, data) {
  return {
    type: RECEIVE_DATA,
    item: (item || []).concat(data),
    data: data
  }
}

export function fetchItems(item = []) {
  return (dispatch, getState) => {
    return dispatch(fetchData(item))
  }
}
```

这里又涉及到了contants，代码如下

```jsx
export const INCREASE = 'INCREASE'
export const DECREASE = 'DECREASE'
export const FETCH_DATA = 'FETCH_DATA';
export const RECEIVE_DATA = 'RECEIVE_DATA';
export const REQUEST_DATA = 'REQUEST_DATA';
export const ERROR_DATA = 'ERROR_DATA';
```

到这里基本上一个简单的例子就出来了。让我们写个测试吧。

```jsx
import React from 'react';
import expect from 'expect';
import { counter } from '../../app/js/reducers';
import TestUtils from 'react-addons-test-utils';
import Home from '../../app/js/components/test/Home';
import { Provider } from 'react-redux';
import { createStore, combineReducers } from 'redux';

const reducer = combineReducers({
  counter
})

const configureStore = (initialState) => {
  const store = createStore(reducer, initialState);
  return store;
}


describe('Home components', () => {
  before('render and locate element ', function(){
    const store = configureStore({});
    const renderedComponent = TestUtils.renderIntoDocument(
      <Provider store={store}>
        <Home />
      </Provider>
    );

    const container = TestUtils.findRenderedDOMComponentWithClass(
      renderedComponent,
      'container'
    );

    const row = TestUtils.findRenderedDOMComponentWithClass(
      renderedComponent,
      'row'
    );

    const btnGroup = TestUtils.findRenderedDOMComponentWithClass(
      renderedComponent,
      'btn-group'
    )

    this.container = container;
    this.row = row;
    this.btnGroup = btnGroup;
  });

  it('container should exist', function(){
    expect(this.container).toExist();
  });

  it('container class name should be container', function(){
    expect(this.container.getAttribute('class')).toBe('container');
  });

  it('row should exist', function() {
    expect(this.row).toExist();
  });

  it('row class name should be row', function() {
    expect(this.row.getAttribute('class')).toBe('row');
  });

  it('btnGroup should exist', function(){
    expect(this.btnGroup).toExist();
  })

  it('btnGroup class name should be btn-group', function() {
    expect(this.btnGroup.getAttribute('class')).toBe('btn-group');
  });

})
```

我去，又牵扯到了reducers了，代码如下：

这里说下，我是把reducer做了一个目录的方式来调用。

reducers

--couner.js

--index.js

index.js的代码如下：

```jsx
import counter from './counter'

export {
  counter
} ;
```

counter.js的代码如下：

```jsx
import {
  INCREASE,
  DECREASE,
  REQUEST_DATA,
  FETCH_DATA,
  RECEIVE_DATA,
  ERROR_DATA
} from '../constants';

const initialState = {
  number: 1
}

export default function counter(state = initialState, action) {
  switch (action.type) {
    case INCREASE:
      return {
        number: state.number + action.amount,
        item: state.item || []
      }
      break;
    case DECREASE:
      return {
        number: state.number - action.amount,
        item: state.item || []
      }
      break;
    case REQUEST_DATA:
      return {
        number: state.number,
        isFetching: true,
        item: action.item || []
      }
      break;
    case FETCH_DATA:
      return {
        number: state.number,
        isFetching: true,
        item: action.item || []
      }
      break;
    case ERROR_DATA:
      return {
        number: state.number,
        isFetching: false,
        item: action.item || [],
        error: action.error
      }
      break;
    case RECEIVE_DATA:
      return {
        number: state.number,
        isFetching: false,
        item: action.item || [],
        data: action.data
      }
      break;
    default:
      return state;
  }
}
```

好了，到这里，相关的一些配置可以在浏览下这篇文章：[React 0.14 mocha组件单元测试（一）](http://gowhich.com/blog/734)。


