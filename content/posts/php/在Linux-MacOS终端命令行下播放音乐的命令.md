---
title: "在Linux/MacOS终端命令行下播放音乐的命令"
date: "2025-06-30 15:57:18"
slug: "zai-linuxmacos-zhong-duan-ming-ling-xing-xia-bo-fang-yin-yue-de-ming-ling"
categories: ["技术"]
tags: ["Linux", "MacOS"]
aliases:
  - "/2025/06/30/在Linux/MacOS终端命令行下播放音乐的命令/"
  - "/2025/06/30/在Linux/MacOS终端命令行下播放音乐的命令.html"
  - "/在Linux/MacOS终端命令行下播放音乐的命令/"
  - "/在Linux/MacOS终端命令行下播放音乐的命令.html"
  - "/2025/06/30/在Linux-MacOS终端命令行下播放音乐的命令/"
  - "/2025/06/30/在Linux-MacOS终端命令行下播放音乐的命令.html"
  - "/2025/06/30/zai-linuxmacos-zhong-duan-ming-ling-xing-xia-bo-fang-yin-yue-de-ming-ling/"
  - "/2025/06/30/zai-linuxmacos-zhong-duan-ming-ling-xing-xia-bo-fang-yin-yue-de-ming-ling.html"
  - "/zai-linuxmacos-zhong-duan-ming-ling-xing-xia-bo-fang-yin-yue-de-ming-ling.html"
---
linux或者macosx 中可以按住那个sox这个库，可以使用play xxx.mp3来进行播放音乐

自己去找这个对应的源来按照那个就好了。

这里是用MacOS安装的。

```bash
brew install sox
```

Ubuntu的话 可以试试这个命令：

```bash
sudo apt-get install sox
```

这样就ok了

我自己下载了mp3音乐，直接执行下面的命令就可以播放音乐了。

```bash
play xxxx.mp3
```

突发奇想如何把他用nodejs实现呢，child_proccess.exec这个方法就可以实现了。

```js
var child_process = require('child_process');
var mp3 = '/xxx/xxx/Downloads/small_apple.mp3';
child_process.exec('play '+mp3,function(err,stdout,stderr){
  console.log(err.message.yellow);
  console.log(stdout.blue);
  console.log(stdout.red);
});
```

把此代码保存为playmusic.js就好了。

然后执行node命令就好了

```bash
node playmusic.js
```

---

我又发现一个奇葩，我呆住了，nodejs有个库叫做player，可以直接进行播放的，其实原理是一样的，来吧，代码

```js
var Player = require('player');
// create player instance 
var player = new Player('/xxx/xxx/Downloads/small_apple.mp3');
 
// play now and callback when playend 
player.play(function(err, player){
  console.log('playend!');
});
 
// event: on playend 
player.on('playend',function(item){
  // return a playend item 
  console.log('src:' + item + ' play done, switching to next one ...');
  player.play();
});
```


