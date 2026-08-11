---
title: "一款可以让你开发效率提高10陪的DIY神器 (看完后感觉真的不错)"
date: "2025-06-19 09:58:24"
slug: "yi-kuan-ke-yi-rang-ni-kai-fa-xiao-lv-ti-gao-10-pei-de-diy-shen-qi-kan-wan-hou-gan-jue-zhen-de-bu-cuo"
categories: ["技术"]
tags: ["Vim"]
aliases:
  - "/2025/06/19/一款可以让你开发效率提高10陪的DIY神器-(看完后感觉真的不错)/"
  - "/2025/06/19/一款可以让你开发效率提高10陪的DIY神器-(看完后感觉真的不错).html"
  - "/一款可以让你开发效率提高10陪的DIY神器-(看完后感觉真的不错)/"
  - "/一款可以让你开发效率提高10陪的DIY神器-(看完后感觉真的不错).html"
  - "/2025/06/19/一款可以让你开发效率提高10陪的DIY神器-看完后感觉真的不错/"
  - "/2025/06/19/一款可以让你开发效率提高10陪的DIY神器-看完后感觉真的不错.html"
  - "/2025/06/19/yi-kuan-ke-yi-rang-ni-kai-fa-xiao-lv-ti-gao-10-pei-de-diy-shen-qi-kan-wan-hou-gan-jue-z/"
  - "/2025/06/19/yi-kuan-ke-yi-rang-ni-kai-fa-xiao-lv-ti-gao-10-pei-de-diy-shen-qi-kan-wan-hou-gan-j.html"
  - "/yi-kuan-ke-yi-rang-ni-kai-fa-xiao-lv-ti-gao-10-pei-de-diy-shen-qi-kan-wan-hou-gan-jue-zhen-de-.html"
---
一款可以让你开发效率提高10陪的DIY神器   
关于这篇文章，我看完后，感觉确实不错，虽然我用的是MacVim。但是感觉还是差不多的。

对于学习php同学应该会很有帮助的。

> 终端下执行命令：whereis vim     将列出vim安装的路径。  
> 否则执行 sudo apt-get install vim 安装vim 。  
> 成功安装了vim，只需要在用户根目录下创建.vimrc文件，在配置文件下写入如下信息。  
> 比如：  
> "引号代表注释  
>   
> set hlsearch                  "高亮度反白  
> set backspace=2               "可随时用倒退键删除  
> set autoindent                 "自动缩排  
> set ruler                      "可显示最后一行的状态  
> set showmode                 "左下角那一行的状态  
> set nu                        "可以在每一行的最前面显示行号  
> set bg=dark                   "显示不同的底色色调  
> syntax on                     "进行语法检验，颜色显示  
> set wrap                      "自动折行  
> set shiftwidth=4  
> set tabstop=4  
> set softtabstop=4  
> set expandtab                  "将tab替换为相应数量空格  
> set smartindent  
>   
> ######下面可根据自己的需要，可以不选用#############  
> set guifont=Dorid Sans Mono:h14:uft8  "gvim字体设置  
> set encoding=utf8               "设置内部编码为utf8  
> set fileencoding=utf8            "当前编辑的文件编码  
> set fileencodings=uft8-bom,utf8,gbk,gb2312,big5   "打开支持编码的文件  
>   
> "解决consle输出乱码  
> language messages zh\_CN.utf-8  
> "解决菜单乱码  
> source $VIMRUNTIME/delmenu.vim  
> source $VIMRUNTIME/menu.vim  
>   
>   
> 一、如何安装phpcomplete插件  
> 如果是VIM7.0以上，不需要再下载 phpcomplete.vim 这个插件，因为安装时自带了，在目录/usr/share/vim/vim73/autoload/phpcomplete.vim中。  
> 在 ~/.vimrc 中添加这样两行：  
> filetype plugin on                                              
> autocmd FileType php set omnifunc=phpcomplete#CompletePHP  
>   
> 如何使用：  
> vi index.php  
> 插入一段php代码后比如：  
> htmlsp  
> 先按下 Ctrl+x进入^X模式,再按下 Ctrl+o， 就能看到提示列表框，以及对应的function，还有对应的函数定义比如参数等等  
> Ctrl+n, Ctrl+p 来上下选择，ESC 来取消提示  
>   
> 二、如何安装php documentor插件  
> http://www.vim.org/scripts/script.php?script\_id=1355  
> 根据官网提供的安装实例，我们进行以下操作：  
> 下载php-doc.vim  
> cp ./php-doc.vim /usr/share/vim/vim73/autoload/php-doc.vim  
>   
> install details  
> Installation  
> =========  
>   
> For example include into your .vimrc:  
>   
> vi  ~\.vimrc  
>   
> source /usr/share/vim/vim73/autoload/php-doc.vim  
> inoremap <C-P> <ESC>:call PhpDocSingle()<CR>i  
> nnoremap <C-P> :call PhpDocSingle()<CR>  
> vnoremap <C-P> :call PhpDocRange()<CR>  
>   
> 如何使用：  
> 在函数定义出注释按ctrl+p即可  
> [attachment=28886]  
>   
> 三、如何安装NERDTree插件  
> http://www.vim.org/scripts/script.php?script\_id=1658  
> 然后解压，解压缩后把plugin,doc,syntax,nerdtree\_plugin四个目录复制到/usr/share/vim/vim73/目录下，即可完成安装。  
> 进入vim后 :NERDTree开启  
>   
> 如何使用  
> 1、在终端界面，输入vim  
> 2、输入  :NERDTree ，回车  
> 3、进入当前目录的树形界面，通过h，j键或者小键盘上下键，能移动选中的目录或文件  
> 4、按u键到上级目录，按o键打开或者关闭文件。目录前面有+号，摁Enter会展开目录，文件前面是-号，摁Enter会在右侧窗口展现该文件的内容，并光标的焦点focus右侧。  
> 5、ctr+w+h  光标focus左侧树形目录，ctrl+w+l 光标focus右侧文件显示窗口。多次摁 ctrl+w，光标自动在左右侧窗口切换  
> 6、光标focus左侧树形窗口，摁? 弹出NERDTree的帮助，再次摁？关闭帮助显示  
> 7、输入:q回车，关闭光标所在窗口  
>   
> 四、如何安装neocomplcache代码自动补全函数提示（支持C/C++,java,python,PHP,javascrip众多语言 ）  
> http://www.vim.org/scripts/script.php?script\_id=2620  
> 然后解压，解压缩后把autoload,plugin,doc三个目录复制到/usr/share/vim/vim73/  
>   
> 添加一下内容到~/.vimrc文件中  
> if &term=="xterm"  
>   set t\_Co=8  
>   set t\_Sb=^[[4%dm  
>   set t\_Sf=^[[3%dm  
> endif  
> let g:neocomplcache\_enable\_at\_startup = 1  
>   
>   
> 五、如何安装zencodeing   引起美工业内13级地震的超级利器  
> http://www.vim.org/scripts/script.php?script\_id=2981 下载得到  
> 解压缩后把三个目录复制到/usr/share/vim/vim73/  
>   
> 方法二  
> 在用户根目录下创建～/ .vim文件夹 ，将加压后得到的三个目录放入此文件夹即可。  
> 测试是否安装成功 ：  
> 输入 html:4s  
> 按住Ctrl 再按下 “y” 和“，” 看到发生了什么？震惊了吗？？
