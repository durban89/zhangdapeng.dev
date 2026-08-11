---
title: "React中上传图片到qiniu"
date: "2025-07-02 16:00:46"
slug: "react-zhong-shang-chuan-tu-pian-dao-qiniu"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/02/React中上传图片到qiniu/"
  - "/2025/07/02/React中上传图片到qiniu.html"
  - "/React中上传图片到qiniu/"
  - "/React中上传图片到qiniu.html"
  - "/2025/07/02/react-zhong-shang-chuan-tu-pian-dao-qiniu/"
  - "/2025/07/02/react-zhong-shang-chuan-tu-pian-dao-qiniu.html"
  - "/react-zhong-shang-chuan-tu-pian-dao-qiniu.html"
---
在React中使用qiniu上传图片，实现方式有很多种，一种是在web端实现上传，一种是在server端实现上传

这里我说下我是如何在web端实现上传图片到七牛的

七牛的官方已经有了javascript的使用说明我这里就不重复了。

使用React首先是要把qiniu提供的js引入，由于我这里是使用的webpack，所以我就直接放在了引入文件中，

这样我就可以全局引用了。

```js
require('./qiniu.js');
```

在组件中把qiniu的对象引入进来

```js
const Qiniu = require('qiniu');
```

然后在componentDidMount这个方法中去初始化

```js
//七牛上传大图
let uploader = Qiniu.uploader({
  runtimes: 'html5,flash,html4',
  browse_button: 'pickfiles',
  uptoken : this.props.uptoken,
  domain: 'http://7u2r0u.com2.z0.glb.qiniucdn.com/',//这里换成自己的
  container: 'app-background-container',
  max_file_size: '100mb',
  flash_swf_url: 'https://cdn.bootcss.com/plupload/2.1.7/Moxie.swf',
  max_retries: 3,
  dragdrop: true,
  drop_element: 'app-background-container',
  chunk_size: '4mb',
  auto_start: true,
  init: {
    'FilesAdded': function(up, files) {
      console.log('上传 FilesAdded');
      plupload.each(files, function(file) {
        // 文件添加进队列后,处理相关的事情
        console.log(file);
      });
    },
    'BeforeUpload': function(up, file) {
      // 每个文件上传前,处理相关的事情
      console.log('上传 Before Upload');
      console.log(up);
      console.log(file);
      $('#app-background-container .showpick').hide();
      $('#big_url').val('');
    },
    'UploadProgress': function(up, file) {
      console.log('上传 UploadProgress');
      console.log(up);
      console.log(file);
    },
    'FileUploaded': function(up, file, info) {
      console.log('====上传完成====');
      let domain = up.getOption('domain');
      let res = JSON.parse(info);
      let sourceLink = domain + res.key;
      console.log(sourceLink);
      $('#app-background-container .showpick').attr('href',sourceLink);
      $('#app-background-container .showpick img').attr('src',sourceLink);
      $('#big_url').val(sourceLink);
      $('#app-background-container .showpick').show();
    },
    'Error': function(up, err, errTip) {
      //上传出错时,处理相关的事情
      console.log('====上传失败====');
      console.log(err);
      console.log(errTip);
    },
    'UploadComplete': function() {
      console.log('====上传完毕====');
    }
  }
});
```

在render中需要把

```html
<a className="btn btn-default btn-primary" id="pickfiles" href="#">
  <i className="glyphicon glyphicon-plus"> </i>
  <span>上传背景大图</span>
</a>
```

放进去，一定要注意id的值

千万别忘记了plupload这个插件，自己去google下就可以找到的，因为我把这个plupload做为一个externals，

所以在webpack的config中加入了

```js
externals:{
  'moment': true,
  'jquery':'jQuery',
  'plupload':true,//重点在这里
  'format':true,
  'bootstrap':true,
  'fancybox':true,
  'co':true,
  '_':'lodash',
  'async':true,
  'datetimepicker':true,
  'selectpicker':true,
  'sweetalert':true,
  'highcharts':'Highcharts',
  'director':'Router'
},
```


