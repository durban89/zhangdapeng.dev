---
title: "UEditor 使用表格功能报错"
date: "2025-06-27 14:15:00"
slug: "ueditor-shi-yong-biao-ge-gong-neng-bao-cuo"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/27/UEditor-使用表格功能报错/"
  - "/2025/06/27/UEditor-使用表格功能报错.html"
  - "/UEditor-使用表格功能报错/"
  - "/UEditor-使用表格功能报错.html"
  - "/2025/06/27/ueditor-shi-yong-biao-ge-gong-neng-bao-cuo/"
  - "/2025/06/27/ueditor-shi-yong-biao-ge-gong-neng-bao-cuo.html"
  - "/ueditor-shi-yong-biao-ge-gong-neng-bao-cuo.html"
---
UEditor使用表格功能报错:错误如下

> Uncaught TypeMismatchError: Failed to execute ‘removeAttributeNode’ on ‘Element’: The 1st argument provided is either null, or an invalid Attr object.

解决办法如下：

找到如下代码：

```js
switch (ci) {
  
    case 'className':
  
        node[ci] = '';
  
        break;
  
    case 'style':
  
        node.style.cssText = '';
  
        !browser.ie && node.removeAttributeNode(node.getAttributeNode('style'))
  
}
```

将其修改为如下：

```js
switch (ci) {
  
    case 'className':
  
        node[ci] = '';
  
        break;
  
    case 'style':
  
        node.style.cssText = '';
          
        if (node.getAttributeNode('style') !== null) { // 加判断
  
            !browser.ie && node.removeAttributeNode(node.getAttributeNode('style'))
  
        }
  
}
```

如果是压缩文件的话如下：

将如下

```js
switch(d){
    case "className":
        a[d]="";
        break;
    case "style":
        a.style.cssText="", !m.ie && a.removeAttributeNode(a.getAttributeNode("style"))
}
```

改为

```js
switch(d){
    case "className":
        a[d]="";
        break;
    case "style":
        a.style.cssText="";
        if(a.getAttributeNode("style")!==null){
            !m.ie&&a.removeAttributeNode(a.getAttributeNode("style"))
        }
}
```


