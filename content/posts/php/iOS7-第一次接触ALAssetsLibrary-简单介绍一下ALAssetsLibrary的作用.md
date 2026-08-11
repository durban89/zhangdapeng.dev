---
title: "iOS7 第一次接触ALAssetsLibrary，简单介绍一下ALAssetsLibrary的作用"
date: "2025-06-27 09:45:41"
slug: "ios7-di-yi-ci-jie-chu-alassetslibrary-jian-dan-jie-shao-yi-xia-alassetslibrary-de-zuo-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/iOS7-第一次接触ALAssetsLibrary，简单介绍一下ALAssetsLibrary的作用/"
  - "/2025/06/27/iOS7-第一次接触ALAssetsLibrary，简单介绍一下ALAssetsLibrary的作用.html"
  - "/iOS7-第一次接触ALAssetsLibrary，简单介绍一下ALAssetsLibrary的作用/"
  - "/iOS7-第一次接触ALAssetsLibrary，简单介绍一下ALAssetsLibrary的作用.html"
  - "/2025/06/27/iOS7-第一次接触ALAssetsLibrary-简单介绍一下ALAssetsLibrary的作用/"
  - "/2025/06/27/iOS7-第一次接触ALAssetsLibrary-简单介绍一下ALAssetsLibrary的作用.html"
  - "/2025/06/27/ios7-di-yi-ci-jie-chu-alassetslibrary-jian-dan-jie-shao-yi-xia-alassetslibrary-de-zuo-y/"
  - "/2025/06/27/ios7-di-yi-ci-jie-chu-alassetslibrary-jian-dan-jie-shao-yi-xia-alassetslibrary-de-z.html"
  - "/ios7-di-yi-ci-jie-chu-alassetslibrary-jian-dan-jie-shao-yi-xia-alassetslibrary-de-zuo-yong.html"
---
IOS7 第一次接触`ALAssetsLibrary`，简单介绍一下`ALAssetsLibrary`的作用

ALAssetsLibrary介绍

- ALAssetsLibrary提供了访问iOS设备下”照片”应用下所有照片和视频的接口；

- 从ALAssetsLibrary中可读取所有的相册数据,即ALAssetsGroup对象列表；

- 从每个ALAssetsGroup中可获取到其中包含的照片或视频列表,即ALAsset对象列表；
  每个ALAsset可能有多个representations表示,即ALAssetRepresentation对象，使用其defaultRepresentation方法可获得其默认representations，使用`[assetvalueForProperty:ALAssetPropertyRepresentations]`可获取其所有representations的UTI数组。


- 从ALAsset对象可获取缩略图thumbnail或aspectRatioThumbnail；
  从ALAssetRepresentation对象可获取全尺寸图片（fullResolutionImage），全屏图片（fullScreenImage）及图片的各种属性:orientation，dimensions，scale，url，metadata等。

其层次关系为ALAssetsLibrary -> ALAssetsGroup -> ALAsset -> ALAssetRepresentation。

具体的使用详情可以去这边看下的[使用ALAssetsLibrary读取所有照片](http://www.winddisk.com/2013/06/30/%E4%BD%BF%E7%94%A8alassetslibrary%E8%AF%BB%E5%8F%96%E6%89%80%E6%9C%89%E7%85%A7%E7%89%87/)，有中文的翻译的，记录吧

---

参考文章：

http://t.cn/zRVM33Q

