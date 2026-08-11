---
title: "Nodejs 通过 fs.createWriteStream 保存文件"
date: "2025-07-03 17:37:21"
slug: "nodejs-tong-guo-fscreatewritestream-bao-cun-wen-jian"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-通过-fs.createWriteStream-保存文件/"
  - "/2025/07/03/Nodejs-通过-fs.createWriteStream-保存文件.html"
  - "/Nodejs-通过-fs.createWriteStream-保存文件/"
  - "/Nodejs-通过-fs.createWriteStream-保存文件.html"
  - "/2025/07/03/nodejs-tong-guo-fscreatewritestream-bao-cun-wen-jian/"
  - "/2025/07/03/nodejs-tong-guo-fscreatewritestream-bao-cun-wen-jian.html"
  - "/nodejs-tong-guo-fscreatewritestream-bao-cun-wen-jian.html"
---
工作中难免会遇到处理大文件的时候，有这种stream的处理方式，就不需要一次处理太大的文件，从而导致内存不够用，或者内存占用太多。

fs.createWriteStream 似乎不会自己创建不存在的文件夹，所以在使用之前需要注意，保存文件的文件夹一定要提前创建。

```js
const path = '/xxxxxx/ddd/';

if (!fs.existsSync(path)) {
  fs.mkdirSync(path);
}
```

创建完文件夹，我们就可以进行文件添加操作了。我们希望在使用文件添加操作的时候是通过saveFile(filePath, fileData);这样的方式来调用。

这里我采用了Promise的方式，个人比较喜欢这样的方式

```js
  /**
   * [saveFileWithStream description]
   * @param  {String} filePath [文件路径]
   * @param  {Buffer} readData [Buffer 数据]
   */
  static saveFile(filePath, fileData) {
    return new Promise((resolve, reject) => {
      // 块方式写入文件
      const wstream = fs.createWriteStream(filePath);

      wstream.on('open', () => {
        const blockSize = 128;
        const nbBlocks = Math.ceil(fileData.length / (blockSize));
        for (let i = 0; i < nbBlocks; i += 1) {
          const currentBlock = fileData.slice(
            blockSize * i,
            Math.min(blockSize * (i + 1), fileData.length),
          );
          wstream.write(currentBlock);
        }

        wstream.end();
      });
      wstream.on('error', (err) => { reject(err); });
      wstream.on('finish', () => { resolve(true); });
    });
  }
```

实际调用的时候，如下

```js
try {
  await saveFileWithStream(filePath, fileData); // 这里的fileData是Buffer类型
} catch (err) {
  console.log(err.stack);
}
```
