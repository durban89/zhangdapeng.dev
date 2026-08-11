---
title: "使用brew cask来安装Mac应用"
date: "2025-07-01 15:03:47"
slug: "shi-yong-brew-cask-lai-an-zhuang-mac-ying-yong"
categories: ["技术"]
tags: ["MacOS", "Brew"]
aliases:
  - "/2025/07/01/使用brew-cask来安装Mac应用/"
  - "/2025/07/01/使用brew-cask来安装Mac应用.html"
  - "/使用brew-cask来安装Mac应用/"
  - "/使用brew-cask来安装Mac应用.html"
  - "/2025/07/01/shi-yong-brew-cask-lai-an-zhuang-mac-ying-yong/"
  - "/2025/07/01/shi-yong-brew-cask-lai-an-zhuang-mac-ying-yong.html"
  - "/shi-yong-brew-cask-lai-an-zhuang-mac-ying-yong.html"
---
# [**简介**](#1)

brew cask是一个用命令行管理Mac下应用的工具，它是基于homebrew的一个增强工具。

homebrew可以管理Mac下的命令行工具，例如imagemagick, nodejs，如下所示：

```bash
brew install imagemagick
brew install node
```

而使用上brew cask之后，你还可以用它来管理Mac下的Gui程序，例如qq, chrome, evernote等，如下所示：

```bash
brew cask install qq
brew cask install google-chrome
brew cask install evernote
```

# [安装](#2)

安装homebrew

用以下一行命令即可安装homebrew

```bash
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

之后执行 brew doctor 命令可以看看homebrew的环境是否正常。通常第一次安装完brew之后，还需要安装苹果的Command Line Tools。

安装cask

用如下命令来安装cask:

```bash
brew tap phinze/cask
brew install brew-cask
```

# [LaunchRocket](#3)

LaunchRocket是一个管理brew安装的service的工具，安装之后可以看所有的service的运行状态，如下图所示：

安装LaunchRocket就要用到我刚刚提的brew cask，用如下命令即可：

```bash
brew tap jimbojsb/launchrocket
brew cask install launchrocket
```


