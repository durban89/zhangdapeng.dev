---
title: "Git查看某个文件的修改历史"
date: "2025-07-03 11:07:47"
slug: "git-cha-kan-mou-ge-wen-jian-de-xiu-gai-li-shi"
categories: ["技术"]
tags: ["Git"]
aliases:
  - "/2025/07/03/Git查看某个文件的修改历史/"
  - "/2025/07/03/Git查看某个文件的修改历史.html"
  - "/Git查看某个文件的修改历史/"
  - "/Git查看某个文件的修改历史.html"
  - "/2025/07/03/git-cha-kan-mou-ge-wen-jian-de-xiu-gai-li-shi/"
  - "/2025/07/03/git-cha-kan-mou-ge-wen-jian-de-xiu-gai-li-shi.html"
  - "/git-cha-kan-mou-ge-wen-jian-de-xiu-gai-li-shi.html"
---
如何查看一个文件的修改历史记录：

# [第一个步骤](#1)

找到某个文件的修改历史

```bash
git log --pretty=oneline ./static/js/detail.js
```

结果会列出下面的结果

> e4f37d08ce8e9d729a824568f3a23d4eeb21ba30 恢复误删的js
>
> 85e4a01822b690da8b152d780271a12d9a3b8dd9 添加 反馈详情页面
>
> 0d3893c8c4f8b124ca50731f02334b70b88ebe5e 更新页面

# [第二个步骤](#2)

查看具体的历史修改记录

```bash
git show e4f37d08ce8e9d729a824568f3a23d4eeb21ba30
```

结果会看到如下的修改信息

> commit e4f37d08ce8e9d729a824568f3a23d4eeb21ba30
>
> Author: durban <[xx@xx](/cdn-cgi/l/email-protection)>
>
> Date:   Mon Dec 21 11:26:20 2015 +0800
>
>     恢复误删的js
>
> diff --git a/gulpfile.js b/gulpfile.js
>
> index 6563d1b..da42836 100644
>
> --- a/gulpfile.js
>
> +++ b/gulpfile.js
>
> @@ -78,6 +78,16 @@ gulp.task('fonts-replace', ['publish-fonts'], () => {
>
>      .pipe(gulp.dest('./static/css/tmp'));
>
>  });
>
> +gulp.task('images-replace', ['webpack','publish-images'], () => {
>
> +  return gulp.src(['./static/build/rev/images/\*.json', './.public/js/\*\*/\*.js'])
>
> +    .pipe(revCollector({
>
> +      dirReplacements: {
>
> +        '/images/': ''
>
> +      }
>
> +    }))
>
> +    .pipe(gulp.dest('./.public/js/\*\*/\*.js'));
>
> +});
>
> +

是不是很清晰。Yeah！

# [补充](#3)

**如果想查看单个文件的历史记录，也可以这样子的。**

```bash
git log -p filename
```


