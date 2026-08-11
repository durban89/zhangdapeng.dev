---
title: "iOS 将程序打包成ipa文件"
date: "2025-06-12 17:18:29"
slug: "ios-jiang-cheng-xu-da-bao-cheng-ipa-wen-jian"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/12/iOS-将程序打包成ipa文件/"
  - "/2025/06/12/iOS-将程序打包成ipa文件.html"
  - "/iOS-将程序打包成ipa文件/"
  - "/iOS-将程序打包成ipa文件.html"
  - "/2025/06/12/ios-jiang-cheng-xu-da-bao-cheng-ipa-wen-jian/"
  - "/2025/06/12/ios-jiang-cheng-xu-da-bao-cheng-ipa-wen-jian.html"
  - "/ios-jiang-cheng-xu-da-bao-cheng-ipa-wen-jian.html"
---
- 第一步
这里需要注意，要选择真机，否则Archive 会是灰色的。
点击后，系统会自动编译一次：

- 第二步：
在你刚刚生成的程序上点击右键，并且点击Show in Finder。

- 第三步：
在打开的窗口中选择 生成的文件 右键点击，显示包内容。

- 第四步：
你会看到一个上面有圆圈禁止符号的图标，这是一个重要的文件，不要关闭窗口，我们一会儿的操作需要用到它。

- 第五步：
打开iTunes 把上面一步的文件 拖拽至 iTunes 中。

- 第六步：
右键点击iTunes中生成的文件，点击Show in Finder。

- 第七步，也是最后一步。
现在显示的这个ipa 文件就是可以给其他机器安装的了。 如果，你安装的机器，没有在你程序的测试证书中，是不能够安装的。除非你的机器是越狱机，越狱机可以安装。
