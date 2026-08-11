---
title: "Nodejs 数据加密传输"
date: "2025-07-03 11:59:52"
slug: "nodejs-shu-ju-jia-mi-chuan-shu"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-数据加密传输/"
  - "/2025/07/03/Nodejs-数据加密传输.html"
  - "/Nodejs-数据加密传输/"
  - "/Nodejs-数据加密传输.html"
  - "/2025/07/03/nodejs-shu-ju-jia-mi-chuan-shu/"
  - "/2025/07/03/nodejs-shu-ju-jia-mi-chuan-shu.html"
  - "/nodejs-shu-ju-jia-mi-chuan-shu.html"
---
数据加密传输，这个目前我接触的几个方式，一个是密文传输，一个明文传输

密文传输，就是用密钥对数据加密，使用公钥对数据解密，传输的通道可以是https的也可以是http的。

明文传输，前提是建立一个安全的传输通道，这里使用证书对通道的安全做了防护，然后传输数据，使用的是明文。

比较专业的 可以后面慢慢分享，不过这里我就介绍下明文传输，如果是用nodejs建立安全通道

使用两个库，分别是urllib和request，这里的证书只介绍使用pfx文件

urllib库的方式

```js
const urllibRequest = (url, method, data, pfx, pass) => {
  return new Promise(function(resolve, reject) {
    let options = {
      data: data,
      method: method,
      pfx: pfx,
      passphrase: pass,
      rejectUnauthorized: false
    }
    urllib.request(url, options, function(err, data, res) {
      if (err) {
        return reject(err);
      }
      return resolve(data.toString());
    });
  });
}
```

request库的方法

```js
const httpRequest = (url, method, data, pfx, pass) => {
  return new Promise((resolve, reject) => {
    let options = {
      url: url,
      method: method,
      form: data,
      headers: {
        'Content-type': 'application/x-www-form-urlencoded'
      },
      agentOptions: {
        pfx: pfx,
        passphrase: pass,
        rejectUnauthorized: false
      }
    };
    request(options, function(err, httpResponse, data) {
      if (err) {
        return reject(err);
      }
      return resolve(data);
    })
  });
}
```


