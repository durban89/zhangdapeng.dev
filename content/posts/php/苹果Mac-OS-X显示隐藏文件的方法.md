---
title: "苹果Mac OS X显示隐藏文件的方法"
date: "2025-07-03 17:37:28"
slug: "ping-guo-mac-os-x-xian-shi-yin-cang-wen-jian-de-fang-fa"
categories: ["技术"]
tags: ["MacOS"]
aliases:
  - "/2025/07/03/苹果Mac-OS-X显示隐藏文件的方法/"
  - "/2025/07/03/苹果Mac-OS-X显示隐藏文件的方法.html"
  - "/苹果Mac-OS-X显示隐藏文件的方法/"
  - "/苹果Mac-OS-X显示隐藏文件的方法.html"
  - "/2025/07/03/ping-guo-mac-os-x-xian-shi-yin-cang-wen-jian-de-fang-fa/"
  - "/2025/07/03/ping-guo-mac-os-x-xian-shi-yin-cang-wen-jian-de-fang-fa.html"
  - "/ping-guo-mac-os-x-xian-shi-yin-cang-wen-jian-de-fang-fa.html"
---
打开“终端”，根据自己的版本选择命令

早期的OS X（10.6~10.8）系统可以使用如下两条命令来开始或者关闭系统隐藏文件的显示：

```bash
defaults write com.apple.Finder AppleShowAllFiles Yes && killall Finder //显示隐藏文件
defaults write com.apple.Finder AppleShowAllFiles No && killall Finder //不显示隐藏文件
```

当升级到OS X 10.9 Mavericks版本之后，这两条命令需要做一些修改，变成了如下命令：

```bash
defaults write com.apple.finder AppleShowAllFiles Yes && killall Finder //显示隐藏文件
defaults write com.apple.finder AppleShowAllFiles No && killall Finder //不显示隐藏文件
```

复制命令，在“终端”中粘贴命令，按下enter键--执行。
