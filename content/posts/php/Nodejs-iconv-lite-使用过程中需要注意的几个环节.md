---
title: "Nodejs iconv-lite 使用过程中需要注意的几个环节"
date: "2025-07-01 11:52:51"
slug: "nodejs-iconv-lite-shi-yong-guo-cheng-zhong-xu-yao-zhu-yi-de-ji-ge-huan-jie"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/07/01/Nodejs-iconv-lite-使用过程中需要注意的几个环节/"
  - "/2025/07/01/Nodejs-iconv-lite-使用过程中需要注意的几个环节.html"
  - "/Nodejs-iconv-lite-使用过程中需要注意的几个环节/"
  - "/Nodejs-iconv-lite-使用过程中需要注意的几个环节.html"
  - "/2025/07/01/nodejs-iconv-lite-shi-yong-guo-cheng-zhong-xu-yao-zhu-yi-de-ji-ge-huan-jie/"
  - "/2025/07/01/nodejs-iconv-lite-shi-yong-guo-cheng-zhong-xu-yao-zhu-yi-de-ji-ge-huan-jie.html"
  - "/nodejs-iconv-lite-shi-yong-guo-cheng-zhong-xu-yao-zhu-yi-de-ji-ge-huan-jie.html"
---
最近在使用Nodejs的一个库Iconv-lite，有时候会报出这样一个提示

> Iconv-lite warning: decode()-ing strings is deprecated. Refer to https://github.com/ashtuchkin/iconv-lite/wiki/Use-Buffers-when-decoding

已经给出了对应的Refer。

具体详情见：https://github.com/ashtuchkin/iconv-lite/wiki/Use-Buffers-when-decoding
其实看完之后，很简单就是
如果有一个Buffer数据的话，你进行了toString()后，就已经进行了一层默认的decode操作，一般默认的是utf-8，
所以如果你在进行iconv.decode()的时候，就会出现一个提示，这个在最新版本会出现这个问题，其他的版本我就不知道了，
如果你在使用的过程中，decode之后，没有效果的话，可以试试，在decode之前先不要任何操作，直接将Buffer数据进行
decode，进过测试，直接decode(Bufffer)数据会效果比较好，谁用谁知道。


