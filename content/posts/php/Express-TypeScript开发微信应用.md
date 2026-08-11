---
title: "Express + TypeScript开发微信应用"
date: "2025-07-10 10:23:27"
slug: "express-typescript-kai-fa-wei-xin-ying-yong"
categories: ["技术"]
tags: ["TypeScript", "ExpressJS"]
aliases:
  - "/2025/07/10/Express-+-TypeScript开发微信应用/"
  - "/2025/07/10/Express-+-TypeScript开发微信应用.html"
  - "/Express-+-TypeScript开发微信应用/"
  - "/Express-+-TypeScript开发微信应用.html"
  - "/2025/07/10/Express-TypeScript开发微信应用/"
  - "/2025/07/10/Express-TypeScript开发微信应用.html"
  - "/2025/07/10/express-typescript-kai-fa-wei-xin-ying-yong/"
  - "/2025/07/10/express-typescript-kai-fa-wei-xin-ying-yong.html"
  - "/express-typescript-kai-fa-wei-xin-ying-yong.html"
---
在进行微信开发之前，首先需要注册一个微信公众号或者是订阅号，这个是最基本的操作，没有这一步，后面的的步伐很难走。  
注册完微信之后，获取appId和appSecret，有了这两个就可以了

## 第一步、创建项目

```bash
$ mkdir ts_node_wx
$ cd ts_node_wx && npm init 
```

## 第二步、安装依赖库

安装需要的packages（express, ejs, request以及sha1）

```bash
npm install --save express ejs request sha1
```

安装TypeScript以及之前安装的packages的类型定义。

```bash
npm install --save-dev typescript @types/node @types/express @types/request @types/sha1
```

由于暂时DefinitelyTyped中并没有JSSDK相关的类型定义文件(.d.ts)，请将types文件夹（包含类型定义文件wechat.d.ts）复制到根目录（ts\_node\_wx）中以便TypeScript获取JSSDK的类型定义。

## 第三步、配置TypeScript

在ts\_node\_wx根目录下添加TypeScript配置文件tsconfig.json

```json
{
    "compilerOptions": {
        "target": "es6",
        /* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', or 'ESNEXT'. */
        "module": "commonjs",
        /* Specify module code generation: 'commonjs', 'amd', 'system', 'umd' or 'es2015'. */
        "moduleResolution": "node" /* Specify module resolution strategy: 'node' (Node.js) or 'classic' (TypeScript pre-1.6). */
    }
}
```

可以根据项目的需求自行添加其他编译选项，比如strict。

## 第四步、核心逻辑讲解

1、获取token

```ts
private getWXToken(): Promise<WXToken> {
  return new Promise((resolve, reject) => {
    request.get(`https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=${config.appId}&secret=${config.appSecret}`, (err, res, body) => {
      if (err) {
        return reject(err);
      }

      const token = JSON.parse(body).access_token || '';
      return resolve(new WXToken(token));
    });
  });
}
```

2、获取ticket

```ts
private getWXTicket(token: string): Promise<WXTicket> {
  return new Promise((resolve, reject) => {
    request.get(`https://api.weixin.qq.com/cgi-bin/ticket/getticket?access_token=${token}&type=jsapi`, (err, res, body) => {
      if (err) {
        return reject(err);
      }

      const ticket = JSON.parse(body).ticket || '';
      return resolve(new WXTicket(ticket));
    })
  });
}
```

3、签名并将数据传递到前端

```ts
const url = req.protocol + '://' + req.get('host') + req.originalUrl;

const tokenRes = await this.getWXToken();
const token = tokenRes.token || '';
const ticketRes = await this.getWXTicket(token);
const ticket = ticketRes.ticket || '';
const timestamp = `${parseInt(new Date().getTime() / 1000 + '', 10)}`;

const params = 'jsapi_ticket=' + ticket + '&noncestr=' + config.nonceStr + '&timestamp=' + timestamp + '&url=' + url;
const signature = sha1(params).toString();

let options: Object = {
  title: 'Home | TS Blog',
  message: 'Welcome to the TS Blog',
  appId: config.appId,
  timestamp,
  nonceStr: config.nonceStr,
  signature,
};

this.render(req, res, "index", options);
```

4、前端代码调用

```html
<html>
  <head>
    <title><%= title %></title>
  </head>
  <body>
    <h1><%= message %></h1>
  </body>
  <script type="text/javascript" src="//res.wx.qq.com/open/js/jweixin-1.0.0.js"></script>
  <script type="text/javascript">
      wx.config({
          debug: false,
          appId: '<%= appId %>',
          timestamp: '<%= timestamp %>',
          nonceStr: '<%= nonceStr %>',
          signature: '<%= signature %>',
          jsApiList: [
              'checkJsApi',
              'onMenuShareTimeline',
              'onMenuShareAppMessage',
              'onMenuShareQQ',
              'onMenuShareWeibo',
              'onMenuShareQZone',
              'hideMenuItems',
              'showMenuItems',
              'hideAllNonBaseMenuItem',
              'showAllNonBaseMenuItem',
              'translateVoice',
              'startRecord',
              'stopRecord',
              'onVoiceRecordEnd',
              'playVoice',
              'onVoicePlayEnd',
              'pauseVoice',
              'stopVoice',
              'uploadVoice',
              'downloadVoice',
              'chooseImage',
              'previewImage',
              'uploadImage',
              'downloadImage',
              'getNetworkType',
              'openLocation',
              'getLocation',
              'hideOptionMenu',
              'showOptionMenu',
              'closeWindow',
              'scanQRCode',
              'chooseWXPay',
              'openProductSpecificView',
              'addCard',
              'chooseCard',
              'openCard'
          ]
      });
  </script>
  <script type="text/javascript" src="/js/main.js"></script>
</html>
```

/js/main.js中的内容如下

```js
wx.ready(() => {
  // open specifc location on map
  wx.openLocation({
    latitude: 0,
    longitude: 0,
    name: '千灯裕花园二期',
    address: '江苏省苏州市昆山市千灯镇千灯裕花园二期',
    scale: 1,
    infoUrl: ''
  });
})
```

## 第四步、编译并运行项目

```bash
$ npm run grunt
$ npm run start 或者 npx pm2 start ecosystem.config.js
```

走到第四步的时候，有些人看了这篇博文可能会晕，觉得为什么到这一步就完事了。这里我说明下，这里我主要是说如何用TypeScript写一个微信端的应用，怎么去调用微信相关SDK的逻辑，如果需要一个完整的应用的话可能需要花费更多的时间，有需要的同学可以下面留言，我根据需要的人数来做在此分享吧。

当然这个应用也是可以使用的，后面更重要的一步是在项目运行起来后，我们通过nginx做代理转发，将应用绑定到一个域名上面，这个通过域名访问就能够访问到我们的项目，然后项目就能正常的运行起来了。我这边贴一下我这边的整体的代码，地址如下  
**https://github.com/durban89/ts\_node\_wx**

可以把代码下载后，修改下config文件里面的appId和appSecret之后再部署编译运行。

运行后效果如下

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1539008092/gowhich/14_1_1.jpg)
