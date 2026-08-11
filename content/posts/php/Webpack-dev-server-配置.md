---
title: "Webpack-dev-server 配置"
date: "2025-07-01 15:24:59"
slug: "webpack-dev-server-pei-zhi"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/01/Webpack-dev-server-配置/"
  - "/2025/07/01/Webpack-dev-server-配置.html"
  - "/Webpack-dev-server-配置/"
  - "/Webpack-dev-server-配置.html"
  - "/2025/07/01/webpack-dev-server-pei-zhi/"
  - "/2025/07/01/webpack-dev-server-pei-zhi.html"
  - "/webpack-dev-server-pei-zhi.html"
---
1，安装需要的包

```bash
npm install --save-dev webpack webpack-dev-server
```

2，配置添加

```js
output: {
  filename: 'bundle.js', //this is the default name, so you can skip it
  //at this directory our bundle file will be available
  //make sure port 8090 is used when launching webpack-dev-server
  publicPath: 'http://localhost:8090/assets' //重点在这里
},
```

3，安装 http-server

```bash
npm install --save-dev http-server
```

4，页面添加启动脚本

```html
<!DOCTYPE html>
<html>
<head>
    <title>Basic Property Grid</title>
    <!-- include react -->
    <script src="./node_modules/react/dist/react-with-addons.js"></script>
</head>
<body>
    <div id="content">
        <!-- this is where the root react component will get rendered -->
    </div>
    <!-- include the webpack-dev-server script so our scripts get reloaded when we make a change -->
    <!-- we'll run the webpack dev server on port 8090, so make sure it is correct -->
    <script src="http://localhost:8090/webpack-dev-server.js"></script>
    <!-- include the bundle that contains all our scripts, produced by webpack -->
    <!-- the bundle is served by the webpack-dev-server, so serve it also from localhost:8090 -->
    <script type="text/javascript" src="http://localhost:8090/assets/bundle.js"></script>
</body>
</html>
```


