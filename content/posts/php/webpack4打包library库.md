---
title: "webpack4打包library库"
date: "2025-07-04 14:27:13"
slug: "webpack4-da-bao-library-ku"
categories: ["技术"]
tags: ["Webpack"]
aliases:
  - "/2025/07/04/webpack4打包library库/"
  - "/2025/07/04/webpack4打包library库.html"
  - "/webpack4打包library库/"
  - "/webpack4打包library库.html"
  - "/2025/07/04/webpack4-da-bao-library-ku/"
  - "/2025/07/04/webpack4-da-bao-library-ku.html"
  - "/webpack4-da-bao-library-ku.html"
---
使用React做开发，经常会写一些符合自己项目需求的lib库，但是通常用的都是ES6的语法，没办法，谁叫我喜欢这中写代码的方式呢，但是其他同事不会写怎么办，但是又急于要一个跟我写的一模一样的UI，怎么办。我也没办法呀，于是网站找了一圈也只是具体的如何打包，但是具体到如何使用还是有很大的区别的，虽然我也找到了具体的解决办法，但是还是有区别于正常的调用方式  
希望懂的认识可以共同探讨

1、创建并初始化项目

```bash
mkdir webpack4-library && cd webpack4-library
npm init -y
npm install webpack webpack-cli eslint eslint-plugin-html eslint-plugin-react babel-eslint eslint-config-airbnb eslint-plugin-jsx-a11y eslint-plugin-import babel-loader babel-plugin-transform-object-assign babel-plugin-transform-decorators-legacy babel-preset-react babel-preset-stage-0 style-loader css-loader url-loader -D
```

创建webpack配置文件webpack.config.jswebpack.config.js

```js
/**
 * @author durban.zhang
 * @date 2018-05-31
 */

const path = require('path');
const webpack = require('webpack');
module.exports = {
  mode: 'production',
  devtool: 'source-map',
  entry: path.join(__dirname, 'src/index.js'),
  output: {
    filename: 'Popbox.min.js',
    library: 'Popbox',
    libraryTarget: 'umd',
    umdNamedDefine: true,
  },
  module: {
    rules: [{
      test: /\.(js|jsx)$/,
      loader: 'babel-loader',
      exclude: [
        path.resolve(__dirname, 'node_modules')
      ],
      options: {
        plugins: ['transform-async-to-generator', 'transform-strict-mode', 'transform-object-assign', 'transform-decorators-legacy'],
        presets: ['es2015', 'react', 'stage-0'],
      },
    },{
      test: /\.css$/,
      use: [
        'style-loader',
        'css-loader',
      ],
      exclude: [
        path.resolve(__dirname, 'node_modules')
      ],
    }]
  },
  plugins: [
    new webpack.ProvidePlugin({
      Promise: 'es6-promise',
    }),
    new webpack.DefinePlugin({
      'global.GENTLY': false,
      'process.env': {
        NODE_ENV: JSON.stringify('production'),
      },
    }),
    new webpack.optimize.OccurrenceOrderPlugin(),
  ],
};
```

src/index.js 这里js文件就是React项目里面的自己写的lib库，直接拿过来就好了。

```js
/**
 * @author durba.zhang xxx@xxx
 */
import './styles/index.css';

import tanchuangPng from './images/tanchuang.png';

class Box {
  constructor(options) {
    this.containerObj = $('.pop-container');
    this.options = Object.assign({}, {
      title: '提示',
      text: '',
    }, options);

    this.parent = $('<div class="pop-container"></div>');

    if (this.containerObj.length) {
      this.containerObj.remove();
    }
  }

  init() {
    const {
      middleBtnText,
    } = this.options;

    let {
      confirmBtnText,
      cancelBtnText,
    } = this.options;

    if (!confirmBtnText) {
      confirmBtnText = '确定';
    }

    if (!confirmBtnText) {
      cancelBtnText = '取消';
    }

    let conText = '';
    if (Object.prototype.hasOwnProperty.call(this.options, 'text') &&
      this.options.text) {
      conText = this.options.text;
    }

    const $overlayContainer = $('<div class="pop-overlay"></div>');
    const $divContainer = $('<div class="pop-alert"></div>');
    const $imgContainer = $(`<div class="pop-logo"><img src=${tanchuangPng} width=100 height=100 /></div>`);
    const $messageContainer = $('<div class="pop-info"></div>');

    const $conContainer = $('<p class="pop-text"></p>');
    $conContainer.append(conText);

    let $confirmbtnContainer;
    if (Object.prototype.hasOwnProperty.call(this.options, 'confirmBtnLink') &&
      this.options.confirmBtnLink) {
      $confirmbtnContainer = $(`<div class="pop-horizal-box pop-top-border" style="line-height:28px"><a href="${this.options.confirmBtnLinkUrl}" class="btn btn-default confirm-btn">${confirmBtnText}</button></div>`);
    } else {
      $confirmbtnContainer = $(`<div class="pop-horizal-box pop-top-border"><button class="btn btn-default confirm-btn">${confirmBtnText}</button></div>`);
      $confirmbtnContainer.on('click', this.confirmHandle.bind(this));
    }

    let $middlebtnContainer;
    if (Object.prototype.hasOwnProperty.call(this.options, 'middleBtnLink') &&
      this.options.middleBtnLink) {
      $middlebtnContainer = $(`<div class="pop-horizal-box pop-top-border" style="border-top:none"><a style="padding-top:10px" href="${this.options.middleBtnLinkUrl}" class="btn btn-default confirm-btn">${middleBtnText}</button></div>`);
    } else {
      $middlebtnContainer = $(`<div class="pop-horizal-box pop-top-border" style="border-top:none"><button class="btn btn-default confirm-btn">${middleBtnText}</button></div>`);
      $middlebtnContainer.on('click', this.middleHandle.bind(this));
    }

    const $cancelbtnContainer = $(`<div class="pop-horizal-box no-bottom-border"><button class="btn btn-default cancel-btn">${cancelBtnText}</button></div>`);
    $cancelbtnContainer.on('click', this.cancelHandle.bind(this));

    $messageContainer.append($conContainer);
    if (!this.options.hideConfirmBtn) {
      $messageContainer.append($confirmbtnContainer);
    }

    if (this.options.middleBtnShow) {
      $messageContainer.append($middlebtnContainer);
    }

    if (!this.options.hideCancelBtn) {
      if (this.options.hideConfirmBtn) {
        $cancelbtnContainer.css({
          'border-top': '1px solid #f1f1f1',
        });
      }

      $messageContainer.append($cancelbtnContainer);
    }

    $divContainer.append($messageContainer);
    this.parent.append($overlayContainer);
    this.parent.append($divContainer);
    this.parent.append($imgContainer);

    $('body').append(this.parent);
    this.containerObj = $('.pop-container');
  }

  confirmHandle() {
    this.closeBoxHandle();
    if (Object.prototype.hasOwnProperty.call(this.options, 'confirmFunc') &&
      this.options.confirmFunc) {
      this.options.confirmFunc();
    }
  }

  cancelHandle() {
    this.closeBoxHandle();
    if (Object.prototype.hasOwnProperty.call(this.options, 'cancelFunc') &&
      this.options.cancelFunc) {
      this.options.cancelFunc();
    }
  }

  middleHandle() {
    this.closeBoxHandle();
    if (Object.prototype.hasOwnProperty.call(this.options, 'middleFunc') &&
      this.options.middleFunc) {
      this.options.middleFunc();
    }
  }

  closeBoxHandle() {
    console.log(this.containerObj);
    this.containerObj.remove();
  }
}

class Popbox {
  static pop(options, func) {
    const box = new Box(options, func);
    box.init();
  }

  static closePop() {
    $('.pop-container').remove();
  }
}

export default Popbox;
```

src/index.css

```css
/*覆层*/

.overlay-component-bg {
  position: fixed;
  width: 100%;
  height: 100%;
  bottom: 0;
  left: 0;
  visibility: hidden;
  z-index: 10;
  background: rgba(0, 0, 0, 0);
  -webkit-transition: all .2s;
  -moz-transition: all .2s;
  -ms-transition: all .2s;
  -o-transition: all .2s;
  transition: all .2s;
}

.overlay-bg-show {
  background: rgba(0, 0, 0, 0.3);
  visibility: visible;
}

/* request loading */

.request-loading {
  position: fixed;
  height: 60px;
  top: 50%;
  left: 50%;
  text-align: center;
  width: 60px;
  background: rgba(0, 0, 0, 0.3);
  visibility: visible;
  border-radius: 5px;
  z-index: 5000;
  margin-left: -30px;
}

.pop-container .pop-overlay {
  background-color: rgba(0, 0, 0, .4);
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  z-index: 1000;
  position: fixed;
}

.pop-container .pop-alert {
  display: block;
  width: 280px;
  min-height: 100px;
  z-index: 2000;
  background: 0 0;
  top: 50%;
  left: 50%;
  position: fixed;
  border-radius: 5px;
  margin-left: -140px;
  margin-top: -100px;
}

.pop-container .pop-logo {
  position: fixed;
  top: 50%;
  z-index: 30001;
  left: 50%;
  margin-left: -50px;
  margin-top: -150px;
}

.pop-container .pop-info {
  display: block;
  width: 100%;
  min-height: 100px;
  background: #fff;
  border-radius: 5px;
  padding-top: 55px;
}

.pop-container .pop-info .pop-text {
  text-align: center;
  padding-left: 15px;
  padding-right: 15px;
  padding-bottom: 10px;
  margin-bottom: 10px;
  font-size: 16px;
}

.pop-container .pop-info .pop-top-border {
  border-top: 1px solid #f1f1f1;
}

.pop-container .pop-info .pop-horizal-box {
  height: 40px;
  border-bottom: 1px solid #f1f1f1;
  text-align: center;
}

.pop-container .pop-info .no-bottom-border {
  border-bottom: none
}

.pop-info .pop-horizal-box .confirm-btn {
  height: 100%;
  border: none;
  width: 100%;
  box-shadow: none;
  background: #fff;
  color: #43bae9;
  font-size: 15px;
  outline: none;
}

.pop-info .pop-horizal-box .cancel-btn {
  height: 100%;
  border: none;
  width: 100%;
  box-shadow: none;
  background: #fff;
  color: #43bae9;
  font-size: 15px;
  outline: none;
}
```

index.html

```html
<html>
  <head>
    <meta charset=UTF-8>
    <meta http-equiv=X-UA-Compatible>
    <meta name=format-detection content="telephone=no">
    <meta name=viewport content="width=device-width,initial-scale=1,minimum-scale=1,maximum-scale=1,user-scalable=no">
    <title>Popbox Test</title>
    <script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
    <script src="./dist/Popbox.min.js"></script>
  </head>
  <body>
    <div>Popbox</div>
    <script>
      $(() => {
        window.Popbox.default.pop({
          text: '这个是一个提示',
          confirmBtnText: '联系客服',
          cancelBtnText: '好的，我知道了',
          confirmFunc: () => {
            console.log('asda');
          },
        });
      });
    </script>
  </body>
</html>
```

项目目录结构

```bash
├── index.html
├── package-lock.json
├── package.json
├── src
│   ├── images
│   │   └── tanchuang.png
│   ├── index.js
│   ├── lib
│   │   └── Util.js
│   └── styles
│       └── index.css
└── webpack.config.js
```

打开index.html是不是运行后没有./dist/Popbox.min.js这个文件，没关系，执行下面的命令

```bash
npx webpack
```

# npx - 是node本身提供的一个功能，需要的具体了解的可以百度或者Google  
再打开看看

目前仅适用于app web端，你可以不用使用我写的lib，但是方法是一样的。  
提示  
注意看package.json，里面的版本号很重要，不同的版本可能会导致不同的异常，可能你就要重新埰坑了。

```bash
Demo环境
mac os
npm - 6.0.1
node - v8.9.4
```

项目地址：[https://github.com/durban89/webpack4-library](https://github.com/durban89/webpack4-demo)
