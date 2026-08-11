---
title: "Koa+React实现form表单上传文件"
date: "2025-07-02 16:00:49"
slug: "koareact-shi-xian-form-biao-dan-shang-chuan-wen-jian"
categories: ["技术"]
tags: ["KoaJS", "ReactJS"]
aliases:
  - "/2025/07/02/Koa+React实现form表单上传文件/"
  - "/2025/07/02/Koa+React实现form表单上传文件.html"
  - "/Koa+React实现form表单上传文件/"
  - "/Koa+React实现form表单上传文件.html"
  - "/2025/07/02/koareact-shi-xian-form-biao-dan-shang-chuan-wen-jian/"
  - "/2025/07/02/koareact-shi-xian-form-biao-dan-shang-chuan-wen-jian.html"
  - "/koareact-shi-xian-form-biao-dan-shang-chuan-wen-jian.html"
---
在nodejs里面通过html的表单上传图片，跟php比较起来还是麻烦一些，特别是在react中使用表单提交含有文件的数据。

最近也在做这个操作，找了很多资料，一直都是有个co-busboy这个，其实它也是基于busboy去封装的，不过这个更适合在koa里面使用。

以往的表单提交，我们用浏览器去debug的时候，会看到，提交了一个post提交的数据，这个一般只是值的提交，不包括有文件，但是在react中，

好像就更加复杂了一些，对于表单提交要单独自己写一个提交的事件去处理，累死submit这样的jquey函数。

而且提交成功后，我们用chrome去debug的时候，会发现提交的是一个Request Payload这样的，跟Form Data不一样，而且我们在koa中，

用body也是获取不到对应的值的，一切都是繁琐加着繁琐，自己考虑一下，像php这样的，是人家都帮你做好了，用起来很顺手，最终需要解决的就是，

如果把提交的data从header中去解析出来，其实busboy做的还是很好的。下面我大概说下我是如何去操作的。

web使用的jquery，通过FormData

在componentDidMount方法中初始化一下submit。

```js
let handleAction = this.props.handleAction;
$("#BackgroundForm").submit(function(e){
  let formData = new FormData($(this)[0]);
  $.ajax({
    url:'/theapp/upload/background',
    data:formData,
    dataType:'json',
    type:'post',
    cache: false,
    contentType: false,
    processData: false,
    beforeSend:function(){
      $('#submitButton').attr('disabled',true);
    },
    success:function(data){
      if(data.success == true){
        handleAction(true);
        $('#errorContainer').html('').hide();
      }else if(data.success == false){
        let message = '<ul><li>'+data.message+'!</li></ul>';
        $('#errorContainer').html(message).show();
        $('#submitButton').attr('disabled',false);
      }
    },error:function(err){
      console.log(err);
    }
  });
  return false;
});
```

在server中的操作是这样的

```js
const upload = function (ctx, key, streamName) {
  return new Promise(function (resolve, reject) {
    ctx.qiniuClient.upload(fs.createReadStream(streamName), key, function (err, result) {
      if (err) {
        return reject(err);
      }
      resolve(result);
    });
  });
};
theapp.post('/upload/background', co.wrap(function *(ctx, next) {
  let parts = parse(ctx.req);
  let part;
  //初始化数据
  let title = '';
  let theme = '';
  let theorder = '';
  let token = '';
  let big_url;
  let thumb_url;
  //获取form-data提交的数据
  while (part = yield parts) {
    if (Array.isArray(part)) {
      let name = part[0];
      let value = part[1];
      if (name == 'title') {
        title = value;
      }
      if (name == 'theme') {
        theme = value;
      }
      if (name == 'theorder') {
        theorder = value;
      }
      if (name == 'access_token') {
        token = value;
      }
    } else {
      let streamName = '/tmp/' + Math.random();
      let stream = fs.createWriteStream(streamName);
      part.pipe(stream);
      if (part.fieldname == 'big_url') {
        big_url = streamName;
      }
      if (part.fieldname == 'thumb_url') {
        thumb_url = streamName;
      }
    }
  }
  if (!big_url) {
    throw new Error('请上传背景大图');
  }
  if (!thumb_url) {
    throw new Error('请上传背景小图');
  }
  if (!title) {
    fs.unlinkSync(big_url);
    fs.unlinkSync(thumb_url);
    throw new Error('名称不能为空');
  }
  if (!theme) {
    fs.unlinkSync(big_url);
    fs.unlinkSync(thumb_url);
    throw new Error('主题不能为空');
  }
  if (!theorder) {
    theorder = 0;
  }
  //名称判断存在
  const url = ctx.config.hostDomain + '/admin/query';
  const sql = `SELECT * FROM qeeniao.app_dft_background WHERE title = '${title}'`;
  const options = {
    timeout: ctx.config.httpTimeout,
    method: 'POST',
    data: {'sql': sql, 'access_token': token}
  };
  const requestData = yield urllib.request(url, options);
  let data = requestData.data.toString();
  data = JSON.parse(data);
  if (data.length > 0) {
    fs.unlinkSync(big_url);
    fs.unlinkSync(thumb_url);
    throw new Error('名称已经存在');
  }
  //上传图片
  let big_res = yield upload(ctx, {
    'key': 'image/background/hd/' + title + '.jpg'
  }, big_url);
  big_url = big_res['url'];
  let thumb_res = yield upload(ctx, {
    'key': 'image/background/thumbnail/' + title + '.jpg'
  }, thumb_url);
  thumb_url = thumb_res['url'];
  //提交数据库
  let postData = {
    'title': title,
    'theme': theme,
    'theorder': theorder,
    'big_url': big_url,
    'thumb_url': thumb_url,
    'access_token': token
  };
  let postUrl = ctx.config.hostDomain + '/admin/add/background';
  let postoptions = {
    timeout: ctx.config.httpTimeout,
    method: 'POST',
    data: postData
  };
  let postRes = yield urllib.request(postUrl, postoptions);
  postRes = postRes.data.toString();
  postRes = JSON.parse(postRes);
  ctx.body = postRes;
}));
```

这里使用了一个qn的库

在启动的时候我把他加入了context中

```js
app.context.qiniuClient = qn.create({
  accessKey: "Your accessKey",
  secretKey: "Your secretKey",
  bucket: "Your bucket",
  origin: 'Your origin'
});
```

这样处理起来就没问题了，其实要是如果koa把busboy自己封装起来是最好的。


