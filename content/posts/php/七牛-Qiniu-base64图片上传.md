---
title: "七牛（Qiniu）base64图片上传"
date: "2025-07-10 11:52:37"
slug: "qi-niu-qiniu-base64-tu-pian-shang-chuan"
categories: ["技术"]
tags: ["Base64"]
aliases:
  - "/2025/07/10/七牛（Qiniu）base64图片上传/"
  - "/2025/07/10/七牛（Qiniu）base64图片上传.html"
  - "/七牛（Qiniu）base64图片上传/"
  - "/七牛（Qiniu）base64图片上传.html"
  - "/2025/07/10/七牛-Qiniu-base64图片上传/"
  - "/2025/07/10/七牛-Qiniu-base64图片上传.html"
  - "/2025/07/10/qi-niu-qiniu-base64-tu-pian-shang-chuan/"
  - "/2025/07/10/qi-niu-qiniu-base64-tu-pian-shang-chuan.html"
  - "/qi-niu-qiniu-base64-tu-pian-shang-chuan.html"
---
参考函数如下

实现原理，将base64图片进行分割，取出图片真实的字符串，并获取这个真实图片串的大小，然后提交到七牛

```js
// 上传图片token
var uploadToken = 'xxxxx';

function putb64(base64Data, uploadKey, callback){
  // 原始base64图片数据处理 返回一个 真实图片数据大小值 和 真实图片数据值
  var imgSizeData = this.getBase64ImgSize(base64Data); // - 解释1

  // 获取大小
  var len = parseInt(imgSizeData.fileSize, 10);

  var data = imgSizeData.base64Data;

  // key的base64处理
  var key = this.base64Key(uploadKey); // - 解释2

  // 请求地址拼接 - 注意这里的http 如果网站是https的话换成https 不然在客户端尤其是iOS 端会出现异常
  var url = "http://upload.qiniup.com/putb64/"+len+'/key/'+key;

  // 七牛cdn绑定的域名
  var domain = 'https://xx.com';

  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange=function(){
    if (xhr.readyState==4){
      // json 解析
      var data = JSON.parse(xhr.responseText);

      // 将代码拼接后返回给程序调用
      callback(domain + '/' + data.key);
      return true;
    }
  }
  xhr.open("POST", url, true);

  // 请求头信息设置
  xhr.setRequestHeader("Content-Type", "application/octet-stream");
  xhr.setRequestHeader("Authorization", "UpToken " + uploadToken + "");

  // 提交数据
  xhr.send(data);
}
```

官方参考: https://developer.qiniu.com/kodo/kb/1326/how-to-upload-photos-to-seven-niuyun-base64-code

解释1 - 请参考 [base64图片的大小计算及获取原图字节大小](https://www.gowhich.com/blog/996)

解释2 - 请参考 [javascript的base64实现及使用](https://www.gowhich.com/blog/997)
