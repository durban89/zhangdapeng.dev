---
title: "axios的post请求变成options请求的坑"
date: "2025-07-14 14:45:00"
slug: "axios-de-post-qing-qiu-bian-cheng-options-qing-qiu-de-keng"
categories: ["技术"]
tags: ["Axios"]
aliases:
  - "/2025/07/14/axios的post请求变成options请求的坑/"
  - "/2025/07/14/axios的post请求变成options请求的坑.html"
  - "/axios的post请求变成options请求的坑/"
  - "/axios的post请求变成options请求的坑.html"
  - "/2025/07/14/axios-de-post-qing-qiu-bian-cheng-options-qing-qiu-de-keng/"
  - "/2025/07/14/axios-de-post-qing-qiu-bian-cheng-options-qing-qiu-de-keng.html"
  - "/axios-de-post-qing-qiu-bian-cheng-options-qing-qiu-de-keng.html"
---
不知道其他的类似axios库有没有这个情况，我用的也少，基本很少用，不过其他的库也确实遇到的比较少，这里遇到这个问题记录下解决办法

如果你的代码是下面这个情况

```javascript
var data = {
  'id': 1,
  'name': 'minmin',
  'age': 23
}

axios({
  method: 'POST',
  url: 'http://xx.xxx.xxx',
  data: data,
}).then(function(res){
  console.log(res);
}).catch(function(err){
  console.log(err);
});
```

请换成如下的情况

```javascript
var data = new URLSearchParams();
data.append('id', '1');
data.append('name', 'minmin');
data.append('age', '23')

axios({
  method: 'POST',
  url: 'http://xx.xxx.xxx',
  data: data,
}).then(function(res){
  console.log(res);
}).catch(function(err){
  console.log(err);
});
```
