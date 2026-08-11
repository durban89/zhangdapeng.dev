---
title: "在使用sublime text 3的误区"
date: "2025-07-01 15:03:56"
slug: "zai-shi-yong-sublime-text-3-de-wu-qu"
categories: ["技术"]
tags: ["Sublime"]
aliases:
  - "/2025/07/01/在使用sublime-text-3的误区/"
  - "/2025/07/01/在使用sublime-text-3的误区.html"
  - "/在使用sublime-text-3的误区/"
  - "/在使用sublime-text-3的误区.html"
  - "/2025/07/01/zai-shi-yong-sublime-text-3-de-wu-qu/"
  - "/2025/07/01/zai-shi-yong-sublime-text-3-de-wu-qu.html"
  - "/zai-shi-yong-sublime-text-3-de-wu-qu.html"
---
问题出现的情况是，我喜欢使用sublime text 写博客，写完后在粘贴进去。

也是我就新建一个，但是没有保存，因为我觉的，反正写完就删除了，结果呢，写汉字的时候就会非常的慢。

这个问题一直都有，还特意去google上搜索了一下，也未果。

今天突然来了灵感，我发现原因是我没有保存，于是我试了一下，结果果然，保存一个临时一个地方再进行操作就块了很多。

分析原因:应该是内存的问题，我没有保存文件的话，数据应该临时存到内存或者其他地方了，反正应该不是硬盘，内存不够的话，就会

出现很慢计算，我觉的是这个原因，其实这个问题也是有的，我觉得处理逻辑是应该将为保存的文件临时存到/tmp这样的类似目录，

如果正式存储的话在进行切换，删除tmp目录的文件，其实就是copy一份啦。要不然就给个提示嘛，说不行了，内容太多了，哈哈


