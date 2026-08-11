---
title: "Golang开发之Sublime Text 3环境开发配置（GoSublime + LSP）"
date: "2025-08-05 09:48:42"
slug: "golang-kai-fa-zhi-sublime-text-3-huan-jing-kai-fa-pei-zhi-gosublime-lsp"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/Golang开发之Sublime-Text-3环境开发配置（GoSublime-+-LSP）/"
  - "/2025/08/05/Golang开发之Sublime-Text-3环境开发配置（GoSublime-+-LSP）.html"
  - "/Golang开发之Sublime-Text-3环境开发配置（GoSublime-+-LSP）/"
  - "/Golang开发之Sublime-Text-3环境开发配置（GoSublime-+-LSP）.html"
  - "/2025/08/05/Golang开发之Sublime-Text-3环境开发配置-GoSublime-+-LSP/"
  - "/2025/08/05/Golang开发之Sublime-Text-3环境开发配置-GoSublime-+-LSP.html"
  - "/2025/08/05/golang-kai-fa-zhi-sublime-text-3-huan-jing-kai-fa-pei-zhi-gosublime-lsp/"
  - "/2025/08/05/golang-kai-fa-zhi-sublime-text-3-huan-jing-kai-fa-pei-zhi-gosublime-lsp.html"
  - "/golang-kai-fa-zhi-sublime-text-3-huan-jing-kai-fa-pei-zhi-gosublime-lsp.html"
---
之所以在折腾Sublime Text 3是因为这个编辑器，是真的轻量化，现在总结下来，插件配置的好，管理的好，什么电脑性能瓶颈都是扯淡

Sublime Text 3开始用来开发Golang的时候，发现这个东西配置起来确实啰嗦，  
因为要安装很多插件，最后的效果也是比较卡或者根本就不起作用。  
后来网上看了很多在用VScode，于是也开始用VScode来开发Golang，但是经过一段时间，忍受不了VSCode的卡，不知道不是占用内存还是什么原因，总之如果开启两个项目的时候，创建个golang文件，保存的时候，就会卡在Language Server上，具体原因我也没细查，但是我搜索到了一个叫做LSP的东西，我猜测这个玩意应该是个插件

经过百度，google之后，确实有这个东西，解释如下

> LSP，全称 Language Server Protocol，即语言服务器协议，这是微软创建的一个协议（目前已有 Codenvy，Red Hat 和 Sourcegraph 等公司一起支持它的发展）。定义了在编辑器或 IDE 中与语言服务器之间使用的协议，该语言服务器提供诸如自动完成，转到定义，查找所有引用等语言功能。语言服务器索引格式（LSIF，其发音类似于“ else if”）的目标是支持开发工具或 Web UI 中的富代码导航，而不需要源代码的本地副本。
>
> 目前该协议得到了编辑器和语言社区的广泛支持。
>
> LSP 的官方网站：[点这里](https://microsoft.github.io/language-server-protocol/)，GitHub 地址：[点这里](https://github.com/Microsoft/language-server-protocol)。目前最新版本（2020-09-06）：3.15。
>
> --- 来源于网络

好了，知道有这个东西那就好办了

### 1、先安装GoSublime（之前部分随笔说不建议，是个误解，还是了解的不透彻）

安装步骤

找到Packages目录，然后将GoSublime clone到Packages目录下

```bash
git clone https://github.com/DisposaBoy/GoSublime
```

然后重启下Sublime Text 3

安装后打开用户配置，配置参考如下

```json
{
    "ignored_packages":[ 
        "Vintage"
    ],
    "env": {
        "GOPATH": "$HOME/.gvm/pkgsets/go1.15.3/global",
        "GOROOT": "$HOME/.gvm/gos/go1.15.3"
    },
    "auto_complete":true,
    "auto_match_enabled":true,
    "fmt_cmd" :[ "goimports" ],
    "autocomplete_suggest_imports": true
}
```

提示：goimports工具要提前安装

```bash
go get -u golang.org/x/tools/cmd/goimports
```

另外记住一个快捷键组合键`[Cmd+.][Cmd+x]`，可以打开一个margo.go的文件，里面便是代码格式化、Linter等相关的配置，具体如何修改可以参考官网，为了避免跟后面的LSP冲突，需要将margo.go文件中的GoCode功能注释掉

```bash
// Enable auto-completion
// gs: this replaces the `gscomplete_enabled` setting
// &golang.Gocode{
//     // show the function parameters. this can take up a lot of space
//     ShowFuncParams: true,
// },
```

PS：https://packagecontrol.io/packages/GoSublime 这里其实也没有说明如何安装

### 2、安装LSP

Cmd+Shift+p 选择 Package Control: Install Package ，输入关键字LSP

然后打开LSP配置，参考下面进行更改

```json
{
    "clients":
    {
        "gopls":
        {
            "command":
            [
                "/Users/durban/.gvm/pkgsets/go1.15.3/global/bin/gopls"
            ],
            "enabled": true,
            "languageId": "go",
            "scopes":
            [
                "source.go"
            ],
            "syntaxes":
            [
                "Packages/GoSublime/syntax/GoSublime-Go-Recommended.sublime-syntax"
            ]
        }
    }
}
```

这里多了一个 gopls 需要提前安装

```bash
go get -u golang.org/x/tools/gopls@latest
```

安装完之后重新启动Sublie Text 3，然后按键`Cmd+Shift+p` 选择 `LSP: Enable Language Server Globally` 然后选择 `gopls`

整个配置就结束了。

---

之前的配置是单独配置了LSP，感觉哪里好像不对，功能比较单一，部分功能还不如GoSublime，后面看到了[一篇文章](http://blog.ipushs.com/sublime-text-%E9%96%8B%E7%99%BC-golang-%E7%92%B0%E5%A2%83%E9%85%8D%E7%BD%AE/)  

给了我启发

暂时记录这些，应该还有未发现的更好的点，后续继续完善
