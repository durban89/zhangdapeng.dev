---
title: "转载：vscode 的 golang 提示很慢"
date: "2025-08-05 09:48:26"
slug: "zhuan-zai-vscode-de-golang-ti-shi-hen-man"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/转载：vscode-的-golang-提示很慢/"
  - "/2025/08/05/转载：vscode-的-golang-提示很慢.html"
  - "/转载：vscode-的-golang-提示很慢/"
  - "/转载：vscode-的-golang-提示很慢.html"
  - "/2025/08/05/zhuan-zai-vscode-de-golang-ti-shi-hen-man/"
  - "/2025/08/05/zhuan-zai-vscode-de-golang-ti-shi-hen-man.html"
  - "/zhuan-zai-vscode-de-golang-ti-shi-hen-man.html"
---
好文章就应该转载起来

最近一直在vscode下开发golang，这个方法跳转真的很慢，找了很久今天终于解决了，如果你也遇到，希望对你有用

如果你用vscode开发golang，发现golang的提示很慢或者跳转很慢，很可能是你没有使用gopls。

是真的没有使用不过用了之后，真的会很快

如下配置请参考，我是参考了第一个安装方式就可以了

下文截取自：http://www.seaxiang.com/blog/eQ3MJr

安装`gopls`

安装方式一  
打开 VS Code 的 setting, 搜索 `go.useLanguageServe`, 并勾选上。默认情况下, Go 扩展会提示你安装 gopls。

安装方式二  
另外也有可能是网络的问题, 直接去 https://github.com/golang/tools/tree/master/gopls  
下载, 然后使用`go isntall github.com/golang/tools/cmd/gopls`安装。

安装方式三  
网络好, 或者设置 goproxy 代理后, 可以直接手动安装 gopls, 官方提示不要使用 -u。

```bash
go get golang.org/x/tools/gopls@latest
```

配置  
装完之后, 添加如下的配置, 如果使用第一种安装方式, 那么第一行已经存在了:

```json
"go.useLanguageServer": true,
"[go]": {
    "editor.snippetSuggestions": "none",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
},
"gopls": {
    "usePlaceholders": true, // add parameter placeholders when completing a function
    "completionDocumentation": true // for documentation in completion items
},
"files.eol": "\n", // formatting only supports LF line endings
```
