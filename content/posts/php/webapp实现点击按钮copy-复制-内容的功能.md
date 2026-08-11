---
title: "webapp实现点击按钮copy（复制）内容的功能"
date: "2025-07-15 09:51:17"
slug: "webapp-shi-xian-dian-ji-an-niu-copy-fu-zhi-nei-rong-de-gong-neng"
categories: ["技术"]
tags: ["H5"]
aliases:
  - "/2025/07/15/webapp实现点击按钮copy（复制）内容的功能/"
  - "/2025/07/15/webapp实现点击按钮copy（复制）内容的功能.html"
  - "/webapp实现点击按钮copy（复制）内容的功能/"
  - "/webapp实现点击按钮copy（复制）内容的功能.html"
  - "/2025/07/15/webapp实现点击按钮copy-复制-内容的功能/"
  - "/2025/07/15/webapp实现点击按钮copy-复制-内容的功能.html"
  - "/2025/07/15/webapp-shi-xian-dian-ji-an-niu-copy-fu-zhi-nei-rong-de-gong-neng/"
  - "/2025/07/15/webapp-shi-xian-dian-ji-an-niu-copy-fu-zhi-nei-rong-de-gong-neng.html"
  - "/webapp-shi-xian-dian-ji-an-niu-copy-fu-zhi-nei-rong-de-gong-neng.html"
---
准备一个textarea(基于vuejs)

```html
<textarea v-model='videoUrl' id='copy' style="position:absolute;top:-99999999px"></textarea>
```

实现代码逻辑如下

```javascript
function copy() {
  if (navigator.userAgent.match(/(iPhone|iPod|iPad);?/i)) { //区分iPhone设备
    console.log('ios')

    window.getSelection().removeAllRanges(); //这段代码必须放在前面否则无效

    var copyNode = document.getElementById("copy"); //要复制文字的节点
    var editable = copyNode.contentEditable;
    var readOnly = copyNode.readOnly;
    copyNode.contentEditable = true;
    copyNode.readOnly = true;

    var range = document.createRange();
    // 选中需要复制的节点
    range.selectNodeContents(copyNode);

    // 执行选中元素
    var selection = window.getSelection();
    if (selection.rangeCount > 0) {
      selection.removeAllRanges();
    }

    selection.addRange(range);
    copyNode.setSelectionRange(0, 999999);
    copyNode.contentEditable = editable;
    copyNode.readOnly = readOnly;

    // 执行 copy 操作
    var successful = document.execCommand('copy');

    console.log('successful = ', successful);
    // alert(successful)
    if (successful) {
      layer.open({
        content: '复制成功^_^',
        btn: ['好的'],
        yes: function (index) {
          layer.closeAll();
        }
      })
    }
    // 移除选中的元素
    window.getSelection().removeAllRanges();
  } else {
    var text = document.getElementById("copy").value;
    const textarea = document.createElement("textarea");
    textarea.style.position = 'fixed';
    textarea.style.top = 0;
    textarea.style.left = 0;
    textarea.style.border = 'none';
    textarea.style.outline = 'none';
    textarea.style.resize = 'none';
    textarea.style.fontSize = '12pt';
    textarea.style.background = 'transparent';
    textarea.style.color = 'transparent';
    textarea.value = text; // 修改文本框的内容
    document.body.appendChild(textarea);
    textarea.select() // 选中文本
    try {
      const msg = document.execCommand('copy') ?
        'successful' : 'unsuccessful';
      // alert(msg)
      if (msg == 'successful') {
        layer.open({
          content: '复制成功^_^',
          btn: ['好的'],
          yes: function (index) {
            layer.closeAll();
          }
        })
      }
    } catch (err) { alert('unable to copy', err) }
    document.body.removeChild(textarea)
  }

}
```
