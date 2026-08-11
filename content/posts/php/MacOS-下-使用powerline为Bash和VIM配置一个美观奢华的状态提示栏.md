---
title: "MacOS 下 使用powerline为Bash和VIM配置一个美观奢华的状态提示栏"
date: "2025-07-01 11:36:21"
slug: "macos-xia-shi-yong-powerline-wei-bash-he-vim-pei-zhi-yi-ge-mei-guan-she-hua-de-zhuang-tai-ti-shi-lan"
categories: ["技术"]
tags: ["MacOS"]
aliases:
  - "/2025/07/01/MacOS-下-使用powerline为Bash和VIM配置一个美观奢华的状态提示栏/"
  - "/2025/07/01/MacOS-下-使用powerline为Bash和VIM配置一个美观奢华的状态提示栏.html"
  - "/MacOS-下-使用powerline为Bash和VIM配置一个美观奢华的状态提示栏/"
  - "/MacOS-下-使用powerline为Bash和VIM配置一个美观奢华的状态提示栏.html"
  - "/2025/07/01/macos-xia-shi-yong-powerline-wei-bash-he-vim-pei-zhi-yi-ge-mei-guan-she-hua-de-zhuang-t/"
  - "/2025/07/01/macos-xia-shi-yong-powerline-wei-bash-he-vim-pei-zhi-yi-ge-mei-guan-she-hua-de-zhua.html"
  - "/macos-xia-shi-yong-powerline-wei-bash-he-vim-pei-zhi-yi-ge-mei-guan-she-hua-de-zhuang-tai-ti-s.html"
---
**开始Mac上安装powerline**

首先我们需要下载安装powerline。在正式安装之前先啰嗦几句powerline的代码结构，github上的powerline项目下涵盖了用于适配各种APP(bash，vim等)的代码。因此，你完全可以在Mac任何一个地方下载该代码包，然后将不同的APP配置使用这个路径，以Plugin形式加载。为了方便读者选择性安装，本文对于不同的程序将分开给出安装路径和配置。

先确定本机环境有一套版本大于等于2.7的Python的环境。如果没有合适环境的话，可以通过homebrew安装，这里不多做赘述。

```bash
shell> python -v
Python 2.7.9
```

然后通过pip安装powerline：

```bash
shell> pip install powerline-status
```

安装完成后通过pip show powerline-status查看powerline所处的具体路径。注意：这个路径很重要，会用在之后的配置环节

```bash
shell> pip show powerline-status
Name: powerline-status
Version: 2.0
Location: /Library/Python/2.7/site-packages
Requires:
```

**配置Bash使用powerline**

配置方法很简单，只需要在Bash配置文件(例如：/etc/bashrc，~/.bashrc，~/.bash\_profile)中增加一行调用安装路径下的bindings/bash/powerline.sh即可。这样每次调用生成新的Bash窗口时，都会自动执行powerline.sh文件中的内容。下面以~/.bash\_profile为例：

```bash
shell> echo << EOF >> ~/.bash_profile 
. /Library/Python/2.7/site-packages/powerline/bindings/bash/powerline.sh
EOF
shell> . /Library/Python/2.7/site-packages/powerline/bindings/bash/powerline.sh
```

注意：根据python安装方式的不同，你的powerline所在路径也可能不同。如果你是通过python官网或者apple store通过安装工具安装的python，那么你的powerline安装路径就是/Library/Python/2.7/site-packages/powerline/。如果你是通过brew install python的话，那么你的powerline路径可能会有不同。请根据实际情况修改上面的命令。

**Teriminal字体配置**

执行完上面两步后，不出意外powerline就已经开始工作了。但是你会发现Bash提示符会是一些非常恶心的符号。

出现这样情况的原因是powerline为了美观自己造了一些符号，而这些符号不在Unicode字库内（如果你不知道Unicode字库是什么的话可以看下博主以前的相关介绍）。所以想要powerline正常显示的话，需要安装特殊处理过的字体。好在有一位热心人的帮助，他把大部分的程序猿常用的等宽字体都打上了powerline patch使得我们的这部配置将异常简单。首先我们从github上下载并安装字体：

```bash
shell> git clone https://github.com/powerline/fonts.git
shell> cd fonts
shell> ./install.sh
```

安装完成后我们就可以在iTerm2或者Terminal的字体选项里看到并选择多个xxx for powerline的字体了。\*注意：对于ASCII fonts和non-ASCII fonts都需要选择for powerline的字体

**VIM相关配置**

这部分我们将介绍如何为VIM配置powerline。首先你需要确保你的vim编译时开启了python支持。如果通过python --version|grep +python没有结果的话，那么你需要通过brew install vim --with-python --with-ruby --with-perl重新编译安装vim，或者使用brew install macvim --env-std --override-system-vim安装macvim。

然后，你只需要在~/.vimrc中加上以下部分，VIM就能够正常加载powerline功能了：

注意：其中set rtp+=/Library/Python/2.7/site-packages/powerline/bindings/vim和上文一样需要按照自己的实际情况调整。

```bash
set rtp+=/Library/Python/2.7/site-packages/powerline/bindings/vim
" These lines setup the environment to show graphics and colors correctly.
set nocompatible
set t_Co=256
 
let g:minBufExplForceSyntaxEnable = 1
python from powerline.vim import setup as powerline_setup
python powerline_setup()
python del powerline_setup
 
if ! has('gui_running')
   set ttimeoutlen=10
   augroup FastEscape
      autocmd!
      au InsertEnter * set timeoutlen=0
      au InsertLeave * set timeoutlen=1000
   augroup END
endif
 
set laststatus=2 " Always display the statusline in all windows
set guifont=Inconsolata\ for\ Powerline:h14
set noshowmode " Hide the default mode text (e.g. -- INSERT -- below the statusline
```

如果有不明白的可以借鉴这篇文章：

https://coderwall.com/p/yiot4q/setup-vim-powerline-and-iterm2-on-mac-os-x


