---
title: "sublime text 通过LSP搭建轻量级IDE"
date: "2025-07-15 10:29:00"
slug: "sublime-text-tong-guo-lsp-da-jian-qing-liang-ji-ide"
categories: ["技术"]
tags: ["Sublime"]
aliases:
  - "/2025/07/15/sublime-text-通过LSP搭建轻量级IDE/"
  - "/2025/07/15/sublime-text-通过LSP搭建轻量级IDE.html"
  - "/sublime-text-通过LSP搭建轻量级IDE/"
  - "/sublime-text-通过LSP搭建轻量级IDE.html"
  - "/2025/07/15/Sublime-text-通过LSP搭建轻量级IDE/"
  - "/2025/07/15/Sublime-text-通过LSP搭建轻量级IDE.html"
  - "/2025/07/15/sublime-text-tong-guo-lsp-da-jian-qing-liang-ji-ide/"
  - "/2025/07/15/sublime-text-tong-guo-lsp-da-jian-qing-liang-ji-ide.html"
  - "/sublime-text-tong-guo-lsp-da-jian-qing-liang-ji-ide.html"
---
之前在mac下开发，使用sublime text一直很苦脑的问题就是方法跳转很慢，尤其是使用golang开发的时候

之前的就不再多提了，应该多少跟我的配置也有关系或者是因为系统的原因

现在开发转到了Linux上 Ubuntu系统，感觉一切只要折腾就会变的越来越好

系统环境

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1675926044/2023-02-09_15-00.png)

这个就是我现在的环境

然后sublime text的版本是Sublime Text Build 4143

然后我说下我这天改用sublime开始开发php语言的项目和golang语言的项目的一些情况

其实我的电脑配置现在来说不算很高，这台电脑是我从我老婆手里拿来的，本来要扔掉的，不过我怕浪费就买了内存和硬盘做了升级，期间安装过windows 但是使用起来，不利于我的开发，配置起来相当麻烦，可能跟我之前一直使用mac有关系

今天我就说下两个配置 很方便

如果是开发php项目的话

请安装LSP+LSP-intelephense，就安装完就可以了

如果是开发golang项目的花

请安装LSP+LSP-gopls，也是安装完就可以了

期间我遇到过一个问题就是安装完LSP-gopls后，启动服务器的时候一直报错提示我go path不存在，这个原因是zsh和bash的原因

就是sublime默认使用了~/.profile

然后我就通过terminal启动sublime就可以了，让他获取到我现在使用的zsh配置

还有一个问题就是在使用LSP-intelephense的时候需要安装nodejs这个是文档上面没提到的，只要安装好就行了 推荐nvm
