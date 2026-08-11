---
title: "Nodejs 应用性能分析"
date: "2025-07-03 16:50:02"
slug: "nodejs-ying-yong-xing-neng-fen-xi"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/03/Nodejs-应用性能分析/"
  - "/2025/07/03/Nodejs-应用性能分析.html"
  - "/Nodejs-应用性能分析/"
  - "/Nodejs-应用性能分析.html"
  - "/2025/07/03/nodejs-ying-yong-xing-neng-fen-xi/"
  - "/2025/07/03/nodejs-ying-yong-xing-neng-fen-xi.html"
  - "/nodejs-ying-yong-xing-neng-fen-xi.html"
---
node.js 从 4.4.0 版本开始内置了 profiler， `--prof` 命令选项运行应用会在当前目录生成性能日志文件。

简单记录下使用方法

运行的时候加上 --prof 参数

```bash
node app.js --prof
```

运行后会在当前目录生成一个类似：isolate-0x1d1e1b0-v8-10041.log这样的文件

执行如下命令来分析程序的性能

```bash
node --prof-process isolate-0x1d1e1b0-v8-10041.log
```

具体解析分析的结果请看参考文章

参考：

[诊断 node.js 应用 CPU 占用过高的问题](http://blog.kankanan.com/article/8bca65ad-node.js-5e947528-cpu-536075288fc79ad8768495ee9898.html)

[Easy profiling for Node.js Applications | Node.js](https://nodejs.org/en/docs/guides/simple-profiling/)
