---
title: "ReactJS中上传图片到qiniu(2017-05-10更新)"
date: "2025-07-03 17:11:26"
slug: "reactjs-zhong-shang-chuan-tu-pian-dao-qiniu2017-05-10-geng-xin"
categories: ["技术"]
tags: ["ReactJS"]
aliases:
  - "/2025/07/03/ReactJS中上传图片到qiniu(2017-05-10更新)/"
  - "/2025/07/03/ReactJS中上传图片到qiniu(2017-05-10更新).html"
  - "/ReactJS中上传图片到qiniu(2017-05-10更新)/"
  - "/ReactJS中上传图片到qiniu(2017-05-10更新).html"
  - "/2025/07/03/ReactJS中上传图片到qiniu-2017-05-10更新/"
  - "/2025/07/03/ReactJS中上传图片到qiniu-2017-05-10更新.html"
  - "/2025/07/03/reactjs-zhong-shang-chuan-tu-pian-dao-qiniu2017-05-10-geng-xin/"
  - "/2025/07/03/reactjs-zhong-shang-chuan-tu-pian-dao-qiniu2017-05-10-geng-xin.html"
  - "/reactjs-zhong-shang-chuan-tu-pian-dao-qiniu2017-05-10-geng-xin.html"
---
之前有写过类似的一篇文章，有位同学突然找来解惑，发现自己采用了另外的一个方法，这里也分享下，希望对使用reactjs的同学有帮助。

逻辑思路是这样子的，在componentDidMount中实现更新dom的操作，异步加载需要的资源文件，然后在加载完后实现qiniu的初始化操作。这里就不需要在webpack或者其他打包工具中去引入qiniu的包文件，导致打完包的文件过大了。

我这里使用了nodejs的库scriptjs，

```js
const $S = require('scriptjs');
```

可以实现异步的加载文件，当然你也可以使用你认为更好的，当然也别忘记告诉我下。以下为代码实现部分：

```js
async componentDidMount() {

  let uploadToken = await this.getUploadToken();

  $S([
    'https://dn-kdjz.qbox.me/js/plupload/2.1.1/plupload.full.min.js',
    'https://dn-kdjz.qbox.me/js/qiniu-js-sdk/1.0.17.2/qiniu.min.js'
  ], 'uploadBundle');

  $S.ready('uploadBundle', () => {

    // 证件合影
    let options1 = {
      runtimes: 'html5,flash,html4',
      browse_button: 'photoId',
      uptoken: uploadToken,
      get_new_uptoken: false,
      domain: 'https://xxxx.xxxxxx', // bucket域名，下载资源时用到，必需
      container: 'photoIdContainer', // 上传区域DOM ID，默认是browser_button的父元素
      max_file_size: '100mb', // 最大文件体积限制
      flash_swf_url: '/js/plupload/2.2.1/Moxie.swf', //引入flash，相对路径
      max_retries: 3, // 上传失败最大重试次数
      dragdrop: true, // 开启可拖曳上传
      drop_element: 'photoIdContainer', // 拖曳上传区域元素的ID，拖曳文件或文件夹后可触发上传
      chunk_size: '4mb', // 分块上传时，每块的体积
      auto_start: true, // 选择文件后自动上传，若关闭需要自己绑定事件触发上传
      init: {
        'FilesAdded': (up, files) => {
          plupload.each(files, function(file) {
            // 文件添加进队列后，处理相关的事情
          });
        },
        'BeforeUpload': (up, file) => {
          // 每个文件上传前，处理相关的事情
        },
        'UploadProgress': (up, file) => {
          // 每个文件上传时，处理相关的事情
        },
        'FileUploaded': async(up, file, info) => {
          // 查看简单反馈
          let domain = up.getOption('domain');
          let res = JSON.parse(info);
          let sourceLink = await this.getDownloadUrl(res.key);
          this.setState({
            photoIdKey: res.key,
            photoId: sourceLink
          })
        },
        'Error': (up, err, errTip) => {
          //上传出错时，处理相关的事情
          console.log(err);
        },
        'UploadComplete': () => {
          //队列文件处理完毕后，处理相关的事情
          console.log('上传完成');
        },
        'Key': (up, file) => {
          let timestamp = parseInt((new Date().valueOf() / 1000));
          // 若想在前端对每个文件的key进行个性化处理，可以配置该函数
          // 该配置必须要在unique_names: false，save_key: false时才生效
          let key = `idcard/${timestamp}_${file.name}`;
          return key
        }
      }
    };
    // 第一个按钮
    const uploader1 = Qiniu.uploader(options1);
  })
}
```

这里有个getUploadToken方法，这个方法是根据官方文档的策略实现了一个获取上传token的方法，此方法是通过访问服务端的接口来获取token。具体实现过程可以参考官方，不明白的也可以加群讨论。
