---
title: "ReactJS 实现代码高亮"
date: "2025-07-02 15:40:51"
slug: "reactjs-shi-xian-dai-ma-gao-liang"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/02/ReactJS-实现代码高亮/"
  - "/2025/07/02/ReactJS-实现代码高亮.html"
  - "/ReactJS-实现代码高亮/"
  - "/ReactJS-实现代码高亮.html"
  - "/2025/07/02/reactjs-shi-xian-dai-ma-gao-liang/"
  - "/2025/07/02/reactjs-shi-xian-dai-ma-gao-liang.html"
  - "/reactjs-shi-xian-dai-ma-gao-liang.html"
---
使用插件google的prettify和jquery的format 完成了一套很完美的代码高亮显示，还能自动格式化。

先说jquery.format的接入【我这里开发是用的webpack】

在引入文件中使用reqiure方法，把jquery.format加入到js代码中。

```js
require('./jquery.format.js');
```

jquery.format.js 这个文件我放在了与引入文件同级的目录下

就可以样就可以了。

在说引入prettify到react中，这个当然是在html页面中进行的了，所以在html中引入

```html
<script src="https://cdn.bootcss.com/prettify/r298/prettify.min.js?skin=sunburst"></script>
<script src="https://cdn.bootcss.com/prettify/r298/lang-sql.min.js?skin=sunburst"></script>
```

就这样就可以了。

然后把我们需要的高亮代码的css也加入进来吧

```css
pre .str, code .str { color: #65B042; } /* string  - green */
pre .kwd, code .kwd { color: #E28964; } /* keyword - dark pink */
pre .com, code .com { color: #AEAEAE; font-style: italic; } /* comment - gray */
pre .typ, code .typ { color: #89bdff; } /* type - light blue */
pre .lit, code .lit { color: #3387CC; } /* literal - blue */
pre .pun, code .pun { color: #fff; } /* punctuation - white */
pre .pln, code .pln { color: #fff; } /* plaintext - white */
pre .tag, code .tag { color: #89bdff; } /* html/xml tag    - light blue */
pre .atn, code .atn { color: #bdb76b; } /* html/xml attribute name  - khaki */
pre .atv, code .atv { color: #65B042; } /* html/xml attribute value - green */
pre .dec, code .dec { color: #3387CC; } /* decimal - blue */
pre.prettyprint, code.prettyprint {
  background-color: #000;
  -moz-border-radius: 8px;
  -webkit-border-radius: 8px;
  -o-border-radius: 8px;
  -ms-border-radius: 8px;
  -khtml-border-radius: 8px;
  border-radius: 8px;
}
pre.prettyprint {
  width: 95%;
  margin: 0.2em auto;
  padding: 1em;
  white-space: pre-wrap;
}
/* Specify class=linenums on a pre to get line numbering */
ol.linenums { margin-top: 0; margin-bottom: 0; color: #AEAEAE; } /* IE indents via margin-left */
li.L0,li.L1,li.L2,li.L3,li.L5,li.L6,li.L7,li.L8 { list-style-type: none }
/* Alternate shading for lines */
li.L1,li.L3,li.L5,li.L7,li.L9 { }
@media print {
  pre .str, code .str { color: #060; }
  pre .kwd, code .kwd { color: #006; font-weight: bold; }
  pre .com, code .com { color: #600; font-style: italic; }
  pre .typ, code .typ { color: #404; font-weight: bold; }
  pre .lit, code .lit { color: #044; }
  pre .pun, code .pun { color: #440; }
  pre .pln, code .pln { color: #000; }
  pre .tag, code .tag { color: #006; font-weight: bold; }
  pre .atn, code .atn { color: #404; }
  pre .atv, code .atv { color: #060; }
}
```

最后看下react里面是如何操作的

在render方法里面操作，稍微有点基础知识的肯定都知道的。

```jsx
  render:function(){
    if(this.props.data.length > 0){
      return (
        <table className="table table-striped table-bordered table-hover table-responsive">
          <thead>
          <colgroup>
            <col width="5%"></col>
            <col></col>
            <col width="20%"></col>
            <col width="20%"></col>
            <col width="10%"></col>
          </colgroup>
          <tr>
            <th>ID号</th>
            <th>SQL Template</th>
            <th>参数</th>
            <th>备注</th>
            <th>创建日期</th>
          </tr>
          </thead>
          <tbody id="itemContainer">
          {this.props.data.map(function(i){
            let ctime = moment.unix(i.ctime).format('YYYY-MM-DD');
            let template = $.format(i.template, {'method':'sql'});
            let config = $.format(i.config, {'method':'json'});
            return (
              <tr key={i.autokid}>
                <td>{i.autokid}</td>
                <td style={{'wordWrap':'break-word','wordBreak':'break-all','verticalAlign':'top'}} >
                  <pre className="prettyprint">
                    <code className="language-sql">{template}</code>
                  </pre>
                </td>
                <td style={{'verticalAlign':'top'}}>
                  <pre className="prettyprint">
                    <code className="language-js">{config}</code>
                  </pre>
                </td>
                <td style={{'verticalAlign':'top'}}>{i.comment} bezhu de qing</td>
                <td style={{'verticalAlign':'top'}}>{ctime}</td>
              </tr>
            );
          })}
          </tbody>
        </table>
      );
    }else{
      return <Loading type='spinning-bubbles' color='#e3e3e3'/>;
    }
  }
```

最后为了是的pretty的效果产生我们还要进行一个启动的操作

```jsx
componentDidMount(){
  prettyPrint();
},
componentDidUpdate(){
  prettyPrint();
},
```

可以了，就是这样的。


