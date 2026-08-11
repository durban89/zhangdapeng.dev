---
title: "npm profile 新功能介绍"
date: "2025-07-08 15:15:53"
slug: "npm-profile-xin-gong-neng-jie-shao"
categories: ["技术"]
tags: ["NPM"]
aliases:
  - "/2025/07/08/npm-profile-新功能介绍/"
  - "/2025/07/08/npm-profile-新功能介绍.html"
  - "/npm-profile-新功能介绍/"
  - "/npm-profile-新功能介绍.html"
  - "/2025/07/08/npm-profile-xin-gong-neng-jie-shao/"
  - "/2025/07/08/npm-profile-xin-gong-neng-jie-shao.html"
  - "/npm-profile-xin-gong-neng-jie-shao.html"
---
npm新版本新推来一个功能，npm profile，这个可以更改自己简介信息的命令，以后可以不用去登录网站来修改自己的简介了

具体的这个功能的支持大概是在6这个版本如果你的npm版本没有这个命令的话，建议升级试下

```bash
npm install -g npm
```

npm profiles主要作用是更改registry profile的设置，刚开始我很蒙圈，不知道啥时profile，直接叫用户信息不就可以了吗？但我们通过官网的地址登录后，点击右侧的自己的头像会发现，点击后会出现一个下拉列表，列表里面有个"Profile Settings"，于是乎我好像明白了。其实就是更改自己的用户信息而已。可以进入里面看下，基本信息跟我们稍后列表来profile支持的选项是一样的。

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1531922798/gowhich/npm_profile_1.png)  
npm profile 的简介如下

```bash
npm profile get [--json|--parseable] [<property>]
npm profile set [--json|--parseable] <property> <value>
npm profile set password
npm profile enable-2fa [auth-and-writes|auth-only]
npm profile disable-2fa
```

主要功能也就上面这些，跟我上面的截图的内容差不多一致，以后如果增加了相应的选项的话，应该也会更新对应的配置选项

下面详细了解下具体的情况

在registry中更改您的个人profile信息。  
如果使用的是non-npmjs registry，则无法使用此功能。

### **npm profile get [<property>]:**

展示所有profile中的属性或者一个或者更多的属性，比如我的属性包括如下

```bash
┌─────────────────┬──────────────────────────────────┐
│ name            │ durban                           │
├─────────────────┼──────────────────────────────────┤
│ email           │ xx@xx (verified) │
├─────────────────┼──────────────────────────────────┤
│ two-factor auth │ disabled                         │
├─────────────────┼──────────────────────────────────┤
│ fullname        │ durban zhang                     │
├─────────────────┼──────────────────────────────────┤
│ homepage        │ www.gowhich.com                  │
├─────────────────┼──────────────────────────────────┤
│ freenode        │                                  │
├─────────────────┼──────────────────────────────────┤
│ twitter         │                                  │
├─────────────────┼──────────────────────────────────┤
│ github          │                                  │
├─────────────────┼──────────────────────────────────┤
│ created         │ 2015-03-18T02:35:58.918Z         │
├─────────────────┼──────────────────────────────────┤
│ updated         │ 2018-07-17T06:27:25.590Z         │
└─────────────────┴──────────────────────────────────┘
```

这个提示下如果你在运行

```bash
npm profile
```

之后没有出现我上面说的情况的话，会有一个问题就是你还没有进行登录，需要执行

```bash
npm login
```

进行登录操作

### **npm profile set <property> <value>:**

设置profile中属性的值，可以设置的属性包括下面的几个  
email, fullname, homepage, freenode, twitter, github

### **npm profile set password:**

修改你的密码。这个是一个交互的功能，你将被提示去输入你当前的密码和一个新的密码，如果开启了双重认证[two-factor authentication]的话，还需要输入一个OTP[动态口令]

### **npm profile enable-2fa [auth-and-writes|auth-only]:**

允许使用双重认证[two-factor authentication]，默认是auth-and-writes模式。  
模式的话有如下几种

> auth-only: 当登录或者是修改账户信息是需要OTP[动态口令]。这个OTP[动态口令]在网站和命令行都会被需要的。  
> auth-and-writes: 在auth-only的所有时间都需要OTP[动态口令]，并且在发布模块，设置最新的dist-tag或通过npm access和npm owner更改访问权时也需要一个OTP[动态口令]。

### **npm profile disable-2fa:**

禁止使用双重认证[two-factor authentication]

所有npm profile子命令都接受--json和--parseable，并将根据这些命令调整其输出。  
其中一些命令可能在non-npmjs registry中不可用。
