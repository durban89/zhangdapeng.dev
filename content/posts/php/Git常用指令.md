---
title: "Git常用指令"
date: "2025-06-13 11:27:40"
slug: "git-chang-yong-zhi-ling"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/06/13/Git常用指令/"
  - "/2025/06/13/Git常用指令.html"
  - "/Git常用指令/"
  - "/Git常用指令.html"
  - "/2025/06/13/git-chang-yong-zhi-ling/"
  - "/2025/06/13/git-chang-yong-zhi-ling.html"
  - "/git-chang-yong-zhi-ling.html"
---
### [创建一个新的repository：](#1)

先在github上创建并写好相关名字，描述。(github的创建，可以参考这里https://help.github.com/articles/create-a-repo)  
  
如果我们创建了hello-world，那么下面的操作如下：

```bash
$cd ~/hello-world  //到hello-world目录
$git init 	//初始化
$git add .//把所有文件加入到索引（不想把所有文件加入，可以用gitignore或add 具体文件)
$git commit                                                               //提交到本地仓库，然后会填写更新日志( -m “更新日志”也可)
$git remote add origin xx@xx:zhangda89/hello-world.git            //增加到remote
$git push origin master                                                    //push到github上
```

### [更新项目（新加了文件）：](#2)

```bash
$cd ~/hello-world
$git add . //这样可以自动判断新加了哪些文件，或者手动加入文件名字
$git commit //提交到本地仓库
$git push origin master //不是新创建的，不用再add 到remote上了
```

### [更新项目（没新加文件，只有删除或者修改文件）：](#3)

```bash
$cd ~/hello-world
$git commit -a //记录删除或修改了哪些文件
$git push origin master //提交到github
```

### [忽略一些文件，比如*.o等:](#4)

```bash
$cd ~/hello-world
$vim .gitignore  //把文件类型加入到.gitignore中，保存
```

然后就可以git add . 能自动过滤这种文件

### [clone代码到本地：](#5)

```bash
$git clone xx@xx:zhangda89/hello-world.git //假如本地已经存在了代码，而仓库里有更新，把更改的合并到本地的项目：
$git fetch origin   //获取远程更新
$git merge origin/master  //把更新的内容合并到本地分支
```

### [撤销](#6)

```bash
$git reset
```

### [删除](#7)

```bash
$git rm  * // 不是用rm
```

### [常见错误](#8)

- `git remote add origin git@github.com:zhangda89/hello-world.git`
  
错误提示：`fatal: remote origin already exists.  `
  
解决办法： `$git remote rm origin  `
  
然后在执行：`$git remote add origin git@github.com:zhangda89/hello-world.git` 就不会报错误了  
  
- `git push origin master  `
  
错误提示：`error:failed to push som refs to  `
  
解决办法： `$git pull origin master` //先把远程服务器github上面的文件拉先来，再push 上去。
