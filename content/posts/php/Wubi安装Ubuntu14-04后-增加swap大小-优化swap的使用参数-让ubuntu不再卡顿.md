---
title: "Wubi安装Ubuntu14.04后，增加swap大小，优化swap的使用参数,让ubuntu不再卡顿"
date: "2025-07-01 11:35:59"
slug: "wubi-an-zhuang-ubuntu1404-hou-zeng-jia-swap-da-xiao-you-hua-swap-de-shi-yong-can-shu-rang-ubuntu-bu-zai-ka-dun"
categories: ["技术"]
tags: ["Wubi", "Ubuntu"]
aliases:
  - "/2025/07/01/Wubi安装Ubuntu14.04后，增加swap大小，优化swap的使用参数,让ubuntu不再卡顿/"
  - "/2025/07/01/Wubi安装Ubuntu14.04后，增加swap大小，优化swap的使用参数,让ubuntu不再卡顿.html"
  - "/Wubi安装Ubuntu14.04后，增加swap大小，优化swap的使用参数,让ubuntu不再卡顿/"
  - "/Wubi安装Ubuntu14.04后，增加swap大小，优化swap的使用参数,让ubuntu不再卡顿.html"
  - "/2025/07/01/Wubi安装Ubuntu14-04后-增加swap大小-优化swap的使用参数-让ubuntu不再卡顿/"
  - "/2025/07/01/Wubi安装Ubuntu14-04后-增加swap大小-优化swap的使用参数-让ubuntu不再卡顿.html"
  - "/2025/07/01/wubi-an-zhuang-ubuntu1404-hou-zeng-jia-swap-da-xiao-you-hua-swap-de-shi-yong-can-shu-ra/"
  - "/2025/07/01/wubi-an-zhuang-ubuntu1404-hou-zeng-jia-swap-da-xiao-you-hua-swap-de-shi-yong-can-sh.html"
  - "/wubi-an-zhuang-ubuntu1404-hou-zeng-jia-swap-da-xiao-you-hua-swap-de-shi-yong-can-shu-rang-ubun.html"
---
wubi安装ubuntu14.04后，终端输入free -m可以查到如下信息：

```bash
             total       used       free     shared    buffers     cached  
Mem:          1944       1801        143          0        557        706  
-/+ buffers/cache:        536       1407  
Swap:          255          255        0
```

也即内存为2G，虚拟内存为256M，这太小了尤其是使用大型IDE编辑源码的时候。因此将其增加到1G大小。具体步骤是：

1，新建/swap文件夹。然后cd进去，终端输入：

```bash
sudo dd if=/dev/zero of=swapfile bs=1024 count=1000000
```

最后的count就是虚拟内存的大小，后面有6个0，前面是1，表示1G.稍等约1分钟看到如下信息：

```bash
记录了1000000+0 的读入
记录了1000000+0 的写出
1024000000字节(1.0 GB)已复制，16.0863 秒，63.7 MB/秒
```

2，这个时候在swap目录下就生成了swapfile文件。终端输入：du -h swapfile 可以查看生成的文件swapfile大小为977M.

```bash
durban@ubuntu:/swap$ du -h swapfile
977Mswapfile
```

约等于1G.接下来需要将swapfile转换成Swap文件，终端输入：

```bash
sudo mkswap -f  swapfile
```

(mkswap是命令，后面的swapfile是swap文件夹下新生成的文件名字)

```bash
durban@ubuntu:/swap$ sudo mkswap -f  swapfile
[sudo] password for durban: 
正在设置交换空间版本 1，大小 = 999996 KiB
无标签， UUID=6c3c015d-9a42-4ced-b93c-a1635062e292
```

3,激活swap文件

终端输入：

```bash
sudo swapon swapfile
```

（swapon是命令，swapfile是文件名字）

然后再输入 free -m可以看到：

```bash
durban@ubuntu:/swap$ sudo swapon swapfile
durban@ubuntu:/swap$ free -m
             total       used       free     shared    buffers     cached
Mem:          3892       3693        199         92        209        850
-/+ buffers/cache:       2633       1258
Swap:         1232        247        984
```

Swap的大小1232 = 255（原来的） + 977 （新增加的）

如果要修改或者删除这个swapfile文件，需要先卸载这个swapfile。进入到swap目录，然后终端输入：

sudo sawpoff swapfile

这就卸载了。swapfile文件就可以删除了，否则会提示正在使用或忙 无法删除。

如果要一直保持这个新增的swap，通过切换到root

```bash
gedit /etc/fstab
```

在里面增加一句：

```bash
/swap/swapfile none swap defaults 0 0
```

关于这句话:

参考1:http://blog.csdn.net/mznewfacer/article/details/7334592 的命令是

```bash
/swap/swapfile none swap defaults 0 0
```

参考2:http://www.linuxidc.com/Linux/2010-09/28915.htm的命令是

```bash
/swap/swapfile /swap swap defaults 0 0
```

个人觉的第二个参数表示原来系统的swap文件夹，如果原系统没有swap文件夹，则用参考1里的命令。如果原系统本来就有/swap文件夹了，也即本来就有swap空间然后又新增加了一个，就用参考2的命令。 Ubuntu14.04上原本没有/swap文件夹，因此用参考1的命令。

另外，注意上面新建swap使用后，现有swap是两者之和。

这篇文章->http://www.blogjava.net/zygcs/archive/2011/09/02/357845.html

这里的方法大同小异，只不过是先

```bash
cd /host/ubuntu/disks/
```

可以看到有个swap.disk, 利用

```bash
du -h swap.disk
```

查看大小为255M，然后

```bash
sudo swapoff swap.disk
```

取消使用这个系统自带的交换空间,然后删除掉。

通过以下步骤我们可以修改系统自带的swap：

1).

```bash
sudo dd if=/dev/zero of=swap.disk bs=1M count=1k
```

 (创建1G的swap, 这步比较慢)

2).

```bash
sudo mkswap -f swap.disk
```

3).

```bash
sudo swapon /host/ubuntu/disks/swap.disk
```

 (这步更慢,大概1分钟不到）

这是在/host/ubuntu/disks/目录下创建的，名字为swap.disk. 本质是一样的。

再就是创建swap时大小是`bs*count`，如果bs=1M 则count =1k表示1G，如果bs=1024， count=1000000 表示1G，我觉的前者更精确。

=================================================

接下来是优化swap的使用参数，linux里有个参数swappiness。当值为0时最大限度的使用物理内存，物理内存使用完后再使用swap内存。为100时，最大限度的使用swap，并将内存中的数据也要搬到swap里处理，这是两个极端。默认的参数是60，根据这里将其改为10较优。步骤如下：

1，查看当前的swappiness

终端输入：

```bash
cat /proc/sys/vm/swappiness
```

2.修改swappiness值为10

```bash
$ sudo sysctl vm.swappiness=10
```

但是这只是临时性的修改，在你重启系统后会恢复默认的60，所以，还要做一步：

```bash
$ sudo gedit /etc/sysctl.conf
```

在这个文档的最后加上这样一行:

```bash
vm.swappiness=10
```

然后保存，重启。ok，你的设置就生效了。你会发现，现在乌斑兔儿跑得更快了！


