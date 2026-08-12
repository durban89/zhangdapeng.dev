---
title: "Homebrew Error: Cask 'java' is unreadable: undefined method `undent' for #"
date: "2025-07-14 16:22:17"
slug: "homebrew-error-cask-java-is-unreadable-undefined-method-undent-for"
categories: ["技术"]
tags: ["Homebrew"]
aliases:
  - "/2025/07/14/Homebrew-Error--Cask-java-is-unreadable--undefined-method-undent-for.html"
  - "/2025/07/14/homebrew-error-cask-java-is-unreadable-undefined-method-undent-for/"
  - "/2025/07/14/homebrew-error-cask-java-is-unreadable-undefined-method-undent-for.html"
  - "/homebrew-error-cask-java-is-unreadable-undefined-method-undent-for.html"
---
今天在执行`brew doctor`的时候出现如下错误：

```bash
$ brew doctor
Error: Cask 'java' is unreadable: undefined method `undent' for #<String:0x00007f86a64ab968>
```

原因为某次更新之后，配置文件增加了某些不必要的字段。更要命的是，不能执行卸载命令来删除出问题的安装包。解决方法为删除这个字段。

方案如下：

```bash
$ find "$(brew --prefix)/Caskroom/"java'/.metadata' -type f -name '*.rb' | xargs grep 'EOS.undent' --files-with-matches | xargs sed -i '' 's/EOS.undent/EOS/'
```

或者下面（我的是java）

```bash
$ find "$(brew --prefix)/Caskroom/"java7'/.metadata' -type f -name '*.rb' | xargs grep 'EOS.undent' --files-with-matches | xargs sed -i '' 's/EOS.undent/EOS/'
```

操作完之后在更新下brew

下面的操作是基于java（因为我的是java）

```bash
$ brew uninstall java 
```

```bash
$ brew cleanup
```

```bash
$ brew update
```

```bash
$ brew upgrade
```

参考文章地址： https://www.mobibrw.com/2020/26381
