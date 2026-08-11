---
title: "webapp中vuejs组合qiniu js sdk实现上传视频功能"
date: "2025-07-11 11:16:09"
slug: "webapp-zhong-vuejs-zu-he-qiniu-js-sdk-shi-xian-shang-chuan-shi-pin-gong-neng"
categories: ["技术"]
tags: ["JavaScript", "VueJS"]
aliases:
  - "/2025/07/11/webapp中vuejs组合qiniu-js-sdk实现上传视频功能/"
  - "/2025/07/11/webapp中vuejs组合qiniu-js-sdk实现上传视频功能.html"
  - "/webapp中vuejs组合qiniu-js-sdk实现上传视频功能/"
  - "/webapp中vuejs组合qiniu-js-sdk实现上传视频功能.html"
  - "/2025/07/11/webapp-zhong-vuejs-zu-he-qiniu-js-sdk-shi-xian-shang-chuan-shi-pin-gong-neng/"
  - "/2025/07/11/webapp-zhong-vuejs-zu-he-qiniu-js-sdk-shi-xian-shang-chuan-shi-pin-gong-neng.html"
  - "/webapp-zhong-vuejs-zu-he-qiniu-js-sdk-shi-xian-shang-chuan-shi-pin-gong-neng.html"
---
采用七牛的SDK方式上传（qiniu sdk文件可以去官网示例页面下载，放在github上的文件需要自己下载后打包的，很麻烦）

首先看下公用的上传函数

```javascript
function uploadWithSDK (file, token, putExtra, config, domain) {
  var self = this;

  var finishedAttr = [];

  var compareChunks = [];

  var observable;

  if (file) {
    // var key = file.name;
    var key = 'activity/' + (new Date().valueOf()) + '/' + self.uploadKey;
    putExtra.params["x:name"] = key.split(".")[0];

    // 设置next,error,complete对应的操作，分别处理相应的进度信息，错误信息，以及完成后的操作
    var error = function (err) {
      console.log('err = ', err);
      self.uploading = false;
    };

    var complete = function (res) {
      console.log('res = ', res);
      self.uploading = false;
      self.uploaded = true;
      var url = self.domain + '/' + res.key;
      console.log(url);
      self.videoUrl = url
    };

    var next = function (response) {
      var chunks = response.chunks || [];
      var total = response.total;
      console.log('total = ', total);
      console.log('chunks = ', chunks);
      self.uploadPercent = (total.percent + '').substr(0, 5) + '%';
    };

    var subObject = {
      next: next,
      error: error,
      complete: complete
    };

    var subscription;

    // 调用sdk上传接口获得相应的observable，控制上传和暂停
    observable = qiniu.upload(file, key, token, putExtra, config);

    subscription = observable.subscribe(subObject);

    // subscription.unsubscribe();
  }
}
```

调用上传视频函数

```javascript
function uploadVideo(event) {
  var file = event.target.files[0];
  // this.uploading = true;

  console.log(file);
  console.log(file.size);

  var config = {
    useCdnDomain: true,
    disableStatisticsReport: false,
    retryCount: 6,
    region: qiniu.region.z0
  };

  var putExtra = {
    fname: "",
    params: {},
    mimeType: null
  };

  uploadWithSDK(file, this.uploadToken, putExtra, config, this.domain);
}
```

触发file的click事件

```javascript
function upload() {
  this.$refs.fileElem.dispatchEvent(new MouseEvent('click'));
}
```

从上面代码可以看出， 代码适用于vuejs中，但是触发click的话，只要是js代码都能实现

vuejs中视频上传相关变量初始化

```javascript
data: {
  uploadToken: '',
  domain: '',
  uploadKey: '',
  randomKey: '',
  uploading: false,
  uploaded: false,
  videoUrl: '',
  uploadPercent: '',
}
```

vuejs中上传视频隐藏表单的HTML

```html
<!-- 上传图片的隐藏元素 -->
<div style="display:none">
  <form id="fileElem1">
    <input ref=fileElem type="file" class="file" accept="video/*" name="img" @change="uploadVideo($event)" style="display: none">
  </form>
</div>
```

vuejs中上传视频按钮部分

```html
<span @click='upload' style="">上传视频</span>
```

这里七牛的sdk请去官网下载

想不通直接打包一个不挺好的嘛，自己下载下来非常麻烦。（实例地址 http://jssdk-v2.demo.qiniu.io/）
