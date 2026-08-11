---
title: "“切换Input，键盘会收起，然后完成切换到下一个input的时候键盘又弹出”问题解决方案"
date: "2025-08-04 18:07:29"
slug: "qie-huan-input-jian-pan-hui-shou-qi-ran-hou-wan-cheng-qie-huan-dao-xia-yi-ge-input-de-shi-hou-jian-pan-you-dan-chu-wen-ti-jie-jue-fang-an"
categories: ["技术"]
tags: ["小程序"]
aliases:
  - "/2025/08/04/“切换Input，键盘会收起，然后完成切换到下一个input的时候键盘又弹出”问题解决方案/"
  - "/2025/08/04/“切换Input，键盘会收起，然后完成切换到下一个input的时候键盘又弹出”问题解决方案.html"
  - "/“切换Input，键盘会收起，然后完成切换到下一个input的时候键盘又弹出”问题解决方案/"
  - "/“切换Input，键盘会收起，然后完成切换到下一个input的时候键盘又弹出”问题解决方案.html"
  - "/2025/08/04/切换Input-键盘会收起-然后完成切换到下一个input的时候键盘又弹出-问题解决方案/"
  - "/2025/08/04/切换Input-键盘会收起-然后完成切换到下一个input的时候键盘又弹出-问题解决方案.html"
  - "/2025/08/04/qie-huan-input-jian-pan-hui-shou-qi-ran-hou-wan-cheng-qie-huan-dao-xia-yi-ge-input-de-s/"
  - "/2025/08/04/qie-huan-input-jian-pan-hui-shou-qi-ran-hou-wan-cheng-qie-huan-dao-xia-yi-ge-input-.html"
  - "/qie-huan-input-jian-pan-hui-shou-qi-ran-hou-wan-cheng-qie-huan-dao-xia-yi-ge-input-de-shi-hou-.html"
---
关于微信小程序开发中的一个问题“切换Input，键盘会收起，然后完成切换到下一个input的时候键盘又弹出”，这个问题一直让人很纠结，我在开发中也遇到了此类问题，但是官方一直没有给出一个很好的答案，只是收集并在我们不知道的什么时候可能会给出解决方案，在这个等待过程中，可能会因为一个UI的体验流失一部分用户，这个谁知道呢，技术开发的遇到这个问题还是要想想办法如何解决  
我的解决原来是，一个text+textarea，如果以前做过页面开发做个IE的兼容处理，应该遇到过此类问题，原理是一致的  
text用来显示我们收入的内容，textarea用来控制输入，并将输入的内容存入要展示的字段中，其实如果是一个输入框的话问题也不大，现在我们要解决我们眼前的问题，就是多个输入框，虽然方案的解决办法实现起来有点复杂但是毕竟能够解决我们的眼前问题。

这里举个例子，以两个输入框为例子

```html
<view bindtap="input1Tap"><text>{{hisTitle}}</text></view><!-- 输入框1-展示内容的假输入框 -->
<view bindtap="input2Tap"><text>{{myTitle}}</text></view><!-- 输入框2-展示内容的假输入框 -->
```

这里输入框的样式根据自己的UI需求来完善就可以了

然后需要两个textarea，用来接收输入的内容，这个textarea因为要接收输入的内容，同时又要担任键盘弹出来，页面上推的任务，是的输入的内容能够立刻展现出来。

```html
<textarea style="position:absolute;top:604rpx;height:30rpx;left:-999999rpx;" focus="{{textareaNameFocus}}" bindinput="textareaNameInputEvent" value="{{hisTitle}}"></textarea>

<textarea style="position:absolute;top:724rpx;height:30rpx;left:-999999rpx;" focus="{{textareaNickFocus}}" bindinput="textareaNickInputEvent" value="{{myTitle}}" ></textarea>
```

我这里的两个textarea的top值都不一样，原因是每个textarea的top值的定位，其实恰好定位在了假输入框的下面，这样子看起来就好比输入框就在假的输入框的地方，正好让弹出的键盘知道输入框的位置，实现自动上推页面的功能。这里的值可以根据需求自己去调整，我这里截张图明确下意思

![](https://cdn.xiaorongmao.com/up/wechat_mini_program_1.png)

接下来实现textareaNameInputEvent和textareaNickInputEvent两个函数

```js
textareaNameInputEvent: function (e) {
  this.setData({
    hisTitle: (e.detail.value || '').replace(/\r\n/g, '').replace(/\n/g, ''),
  });
},

textareaNickInputEvent: function (e) {
  this.setData({
    myTitle: (e.detail.value || '').replace(/\r\n/g, '').replace(/\n/g, ''),
  });
},
```

还要实现下input1Tap和input2Tap函数

```js
input1Tap: function () {
  this.setData({
    textareaNameFocus: true,
    textareaNickFocus: false,
  });

  setTimeout(() => {
    this.setData({
      textareaNameFocus: true,
    });
  }, 500);
},

input2Tap: function () {
  this.setData({
    textareaNameFocus: false,
    textareaNickFocus: true,
  });

  setTimeout(() => {
    this.setData({
      textareaNickFocus: true,
    });
  }, 500);
},
```

这里的setTimeout其实是真正的解决了这个问题的主要原因，真机可能是由于键盘退出出现的之间间隔的设置在iOS和Android上表现不同导致。  
最后问题就解决了，不懂的可以加群来问
