---
title: "新手入门NestJS（一）- 为什么选用NestJS"
date: "2025-07-14 14:54:34"
slug: "xin-shou-ru-men-nestjs-yi-wei-shen-me-xuan-yong-nestjs"
categories: ["技术"]
tags: ["NestJS"]
aliases:
  - "/2025/07/14/新手入门NestJS（一）-为什么选用NestJS/"
  - "/2025/07/14/新手入门NestJS（一）-为什么选用NestJS.html"
  - "/新手入门NestJS（一）-为什么选用NestJS/"
  - "/新手入门NestJS（一）-为什么选用NestJS.html"
  - "/2025/07/14/新手入门Nest.js-一-为什么选用Nest.js/"
  - "/2025/07/14/新手入门Nest.js-一-为什么选用Nest.js.html"
  - "/2025/07/14/xin-shou-ru-men-nestjs-yi-wei-shen-me-xuan-yong-nestjs/"
  - "/2025/07/14/xin-shou-ru-men-nestjs-yi-wei-shen-me-xuan-yong-nestjs.html"
  - "/xin-shou-ru-men-nestjs-yi-wei-shen-me-xuan-yong-nestjs.html"
---
最近开发一个小的项目  
出于几点考虑，最后选择了这个`Nest.js`

1、方便部署，部署不复杂  
2、语法不难  
3、提供了很多够用的工具

首先我想到的是用PHP的框架，毕竟用起来很方便，但是想来想去似乎php的安装有点复杂，也许有人会说，那么多提供了现成的php服务器，随便搞一个，部署起来很方便。  
说的没错，但我的情况是，我想自己买台服务器，需要自己部署，因为别人部署的我也不是很放心  
另外php的安装说实话，我头痛的几个问题就是，安装php的时候，你要知道自己项目用到了哪些扩展，需要根据这个扩展指定对应的安装参数，这个第一次安装还好，后期项目迁移就不好了  
如果我有记录能一下子找到还好如果找不到，就比较头痛  
估计也有人会说，现在的docker不是很好用，我想说的是，作为一个初来乍到的开发者，如果能给我足够的空间而且性价比高的话我会考虑的，一般一个docker安装下来出去本身代码大小，加上docker镜像的大小，空间很快被占用了  
所以我比较熟悉的Laravel、Yii2等框架，我放弃了

于是开始思考我熟悉的另外一门用Python开发的框架，一个是Flask，一个是Django  
思来想去，最后也是放弃了  
第一个Django的重量级，以及配置的复杂性，Django是不考虑了。另外我自己以为很精简的Flask，虽然可扩展性高，但是社区似乎不活跃，经常用的库也是没有怎么更新了，关键是flask并没有经常更新，感觉不够火热  
所以Flask，Laravel被我放弃了

最后熟悉的另外一门Javascript，后端Nodejs  
让我眼前一亮，但是最近几年也不是很火  
而且比较火的Express、Koajs等框架，也都是非常精简，至于工具的话，还是没有一个好的生态圈  
但是唯一让我发下Nest.js这个框架还是不错的选择

第一个部署上就不说了，安装好node之后，代码库拉过来，install一下就可以部署完成  
第二个语法真的不难，现在不管前端后端，稍微会程序开发的，Javascript还是多多少少就会的，外加Typescript的协助，可以在开发上很顺手  
第三个工具够用，可以去官网看看文档，这里不多介绍  
之后我在继续分享关于Nest.js的使用体验
