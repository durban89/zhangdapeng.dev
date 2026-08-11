---
title: "为啥npm安装的时候devDependencies这里面的代码也安装了"
date: "2025-07-02 11:31:46"
slug: "wei-sha-npm-an-zhuang-de-shi-hou-devdependencies-zhe-li-mian-de-dai-ma-ye-an-zhuang-le"
categories: ["技术"]
tags: ["NPM"]
aliases:
  - "/2025/07/02/为啥npm安装的时候devDependencies这里面的代码也安装了/"
  - "/2025/07/02/为啥npm安装的时候devDependencies这里面的代码也安装了.html"
  - "/为啥npm安装的时候devDependencies这里面的代码也安装了/"
  - "/为啥npm安装的时候devDependencies这里面的代码也安装了.html"
  - "/2025/07/02/wei-sha-npm-an-zhuang-de-shi-hou-devdependencies-zhe-li-mian-de-dai-ma-ye-an-zhuang-le/"
  - "/2025/07/02/wei-sha-npm-an-zhuang-de-shi-hou-devdependencies-zhe-li-mian-de-dai-ma-ye-an-zhuang.html"
  - "/wei-sha-npm-an-zhuang-de-shi-hou-devdependencies-zhe-li-mian-de-dai-ma-ye-an-zhuang-le.html"
---
为啥npm安装的时候devDependencies这里面的代码也安装了，琢磨了好久，也搜索了很久，终于找到了答案，哈哈。其实觉得npm还是蛮智能的，只是自己比较低能了，没看npm的源码，测试结果是让我觉得，npm会根据`NODE_ENV`的环境变量值，来判断你当前的环境是开发环境和生产环境，然后根据环境来安装对应的依赖包。

解决方式就是：

```bash
export NODE_ENV=production
npm install --save
```

这样就会很快的将dependencies里面的包安装了，就会自动忽略掉devDependencies里面的依赖包了，就这么简单。


