---
title: "Vim 之 vim-autoformat 自动切换使用本地或全局eslint"
date: "2025-07-03 17:11:50"
slug: "vim-zhi-vim-autoformat-zi-dong-qie-huan-shi-yong-ben-di-huo-quan-ju-eslint"
categories: ["技术"]
tags: ["Vim"]
aliases:
  - "/2025/07/03/Vim-之-vim-autoformat-自动切换使用本地或全局eslint/"
  - "/2025/07/03/Vim-之-vim-autoformat-自动切换使用本地或全局eslint.html"
  - "/Vim-之-vim-autoformat-自动切换使用本地或全局eslint/"
  - "/Vim-之-vim-autoformat-自动切换使用本地或全局eslint.html"
  - "/2025/07/03/vim-zhi-vim-autoformat-zi-dong-qie-huan-shi-yong-ben-di-huo-quan-ju-eslint/"
  - "/2025/07/03/vim-zhi-vim-autoformat-zi-dong-qie-huan-shi-yong-ben-di-huo-quan-ju-eslint.html"
  - "/vim-zhi-vim-autoformat-zi-dong-qie-huan-shi-yong-ben-di-huo-quan-ju-eslint.html"
---
最近使用vim变成javascript程序，自己的一些写代码的习惯并不是很好，需要经常通过格式化程序帮助自己来格式化代码，

vim-autoformat这个插件肯定是少不了，问题就是如何才能通过eslint来格式化代码，毕竟越来越多的高手都在用eslint来规范自己的代码，网上有些文章说的就是如何配置全局，但是我不喜欢全局配置，毕竟不是每个项目的内容都一样，而且版本可能也有要求，因地制宜才好，于是研究了下，自己摸索出来一个方法

```bash
" auto-formatter
function! ESlintFormatter()
    let l:npm_bin = ''
    let l:eslint = 'eslint'
    if executable('npm')
        let l:npm_bin = split(system('npm bin'), '\n')[0]
    endif
    if strlen(l:npm_bin) && executable(l:npm_bin . '/eslint')
        let l:eslint = l:npm_bin . '/eslint'
    endif
    let g:formatdef_eslint = '"SRC=eslint-temp-${RANDOM}.js; cat - >$SRC; ' . l:eslint . ' --fix $SRC >/dev/null 2>&1; cat $SRC | perl -pe \"chomp if eof\"; rm -f $SRC"'
endfunction
```

然后针对javascript类型的文件进行调用

```bash
autocmd FileType javascript :call ESlintFormatter()
```

这样就可以了。欢迎采用
