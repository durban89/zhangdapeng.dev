---
title: "展示一个Reflux的实例【虽然用的人比较少】"
date: "2025-07-01 15:03:45"
slug: "zhan-shi-yi-ge-reflux-de-shi-li-sui-ran-yong-de-ren-bi-jiao-shao"
categories: ["技术"]
tags: ["Reflux", "ReactJS"]
aliases:
  - "/2025/07/01/展示一个Reflux的实例【虽然用的人比较少】/"
  - "/2025/07/01/展示一个Reflux的实例【虽然用的人比较少】.html"
  - "/展示一个Reflux的实例【虽然用的人比较少】/"
  - "/展示一个Reflux的实例【虽然用的人比较少】.html"
  - "/2025/07/01/展示一个Reflux的实例-虽然用的人比较少/"
  - "/2025/07/01/展示一个Reflux的实例-虽然用的人比较少.html"
  - "/2025/07/01/zhan-shi-yi-ge-reflux-de-shi-li-sui-ran-yong-de-ren-bi-jiao-shao/"
  - "/2025/07/01/zhan-shi-yi-ge-reflux-de-shi-li-sui-ran-yong-de-ren-bi-jiao-shao.html"
  - "/zhan-shi-yi-ge-reflux-de-shi-li-sui-ran-yong-de-ren-bi-jiao-shao.html"
---
Reflux是根据React的flux创建的单向数据流类库。

Reflux的单向数据流模式主要由actions和stores组成。例如，当组件list新增item时，会调用actions的某个方法（如addItem(data)）,并将新的数据当参数传递进去，通过事件机制，数据会传递到stroes中，stores可以向服务器发起请求，并更新数据数据库。数据更新成功后，还是通过事件机制传递的组件list当中，并更新ui。整个过程的对接是通过事件驱动的。

这里记录一个比较实用的实例；具体的想看详情的可以去‘http://segmentfault.com/a/1190000002793786#articleHeader24’这里仔细研读。

```jsx
var TodoActions = Reflux.createActions([
    'getAll',
    'addItem',
    'deleteItem',
    'updateItem'
]);
var TodoStore = Reflux.createStore({
    items: [1, 2, 3],
    listenables: [TodoActions],
    onGetAll: function () {
        $.get('/all', function (data) {
            this.items = data;
            this.trigger(this.items);
        }.bind(this));
    },
    onAddItem: function (model) {
        $.post('/add', model, function (data) {
            this.items.unshift(data);
            this.trigger(this.items);
        }.bind(this));
    },
    onDeleteItem: function (model, index) {
        $.post('/delete', model, function (data) {
            this.items.splice(index, 1);
            this.trigger(this.items);
        }.bind(this));
    },
    onUpdateItem: function (model, index) {
        $.post('/update', model, function (data) {
            this.items[index] = data;
            this.trigger(this.items);
        }.bind(this));
    }
});
var TodoComponent = React.createClass({
    mixins: [Reflux.connect(TodoStore, 'list')],
    getInitialState: function () {
        return {list: []};
    },
    componentDidMount: function () {
        TodoActions.getAll();
    },   
    render: function () {
        return (
            <div>
                {this.state.list.map(function(item){
                    return <TodoItem data={item}/>
                })}
            </div>
        )
    }
});
var TodoItem = React.createClass({
    componentDidMount: function () {
        TodoActions.getAll();
    },
    handleAdd: function (model) {
        TodoActions.addItem(model);
    },
    handleDelete: function (model,index) {
        TodoActions.deleteItem(model,index);
    },
    handleUpdate: function (model) {
        TodoActions.updateItem(model);
    },
    render: function () {
        var item=this.props.data;
        return (
            <div>
                <p>{item.name}</p>
                <p>{item.email}</p>
                <p>/*操作按钮*/</p>
            </div>
        )
    }
});
React.render(<TodoComponent />, document.getElementById('container'));
```


