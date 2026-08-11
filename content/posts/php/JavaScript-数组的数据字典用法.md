---
title: "JavaScript 数组的数据字典用法"
date: "2025-06-19 13:54:55"
slug: "javascript-shu-zu-de-shu-ju-zi-dian-yong-fa"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/19/JavaScript-数组的数据字典用法/"
  - "/2025/06/19/JavaScript-数组的数据字典用法.html"
  - "/JavaScript-数组的数据字典用法/"
  - "/JavaScript-数组的数据字典用法.html"
  - "/2025/06/19/javascript-shu-zu-de-shu-ju-zi-dian-yong-fa/"
  - "/2025/06/19/javascript-shu-zu-de-shu-ju-zi-dian-yong-fa.html"
  - "/javascript-shu-zu-de-shu-ju-zi-dian-yong-fa.html"
---
javascript 中的数组 可以当做数据字典用，还可以当栈用，等很多用法。普通的数组用法只是数据字典用法的一个特例。

比如：arr[1]="gao";

只是key是int类型，value是字符串类型。其实数组的key和value都是object类型。相当于c# 中的hashtable.

```javascript
<script>
var dict=new Array;
dict["省"]="山东";
dict["市"]="济南";
dict["县"]="市中心";
alert(dict["省"]); 
for(var k in dict)
{
    alert(k);  //结果是key的值，也就是  "省"，"市"，"县"
}
for(var k in dict)
{
    alert(dict[k]);  //结果是value的值，也就是  "山东"，"济南"，"市中心"
}
</script>
```

复制到自己的html页面去吧，运行一下，效果不是吹的，呵呵
