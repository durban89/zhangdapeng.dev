---
title: "联想thinkpad e430 设置光驱启动"
date: "2025-06-12 17:45:26"
slug: "lian-xiang-thinkpad-e430-she-zhi-guang-qu-qi-dong"
categories: ["技术"]
tags: ["BIOS", "笔记本"]
aliases:
  - "/2025/06/12/联想thinkpad-e430-设置光驱启动/"
  - "/2025/06/12/联想thinkpad-e430-设置光驱启动.html"
  - "/联想thinkpad-e430-设置光驱启动/"
  - "/联想thinkpad-e430-设置光驱启动.html"
  - "/2025/06/12/lian-xiang-thinkpad-e430-she-zhi-guang-qu-qi-dong/"
  - "/2025/06/12/lian-xiang-thinkpad-e430-she-zhi-guang-qu-qi-dong.html"
  - "/lian-xiang-thinkpad-e430-she-zhi-guang-qu-qi-dong.html"
---
- 按F1进入BIOS，选择Security ，选择 Secure Boot,进入后关闭 Secure Boot 为Disabled 即可！

- 把Startup 的 UEFI/LEGACY BOOT 改为Both即可！

微软公司发布Win8系统以后，现在很多电脑厂商都把Win8系统出厂预装到笔记本当中，联想Thinkpad E430电脑也不例外，由于Win8系统的操作界面发生了很多改变，有很多人还不太喜欢使用电脑出厂预装的Win8系统，所以想要把Thinkpad E430电脑中出厂预装的Win8换成Win7的。  
  
　　对于笔记本电脑装系统，相信很多人都不陌生，但就有很多朋友问我，为什么我用U盘或是光盘对出厂预装了Win8系统的电脑安装系统，在按F12选择U盘或光盘启动的时候，老是进不去，画面闪动一下，又回到原来的界面，这是什么原因造成了的呢？  
  
　　有些人开始怀疑这是U盘或光盘坏了，或者是PE没有做好等原因，但拿到其它电脑上去，又成正常启动，这到底是那里出问题了呢？  
  
　　其实这不是你的U盘或PE出问题了，而是笔记本电脑预装Win8系统，采用了UEFI接口的原因，所以才会有一些PE无法兼容导致进不去，如果我们想要把预装的Win8系统换成Win7系统，我们只需要更改一下BIOS即可。  
  
- Win8换Win7更改BIOS的方法一：  
  
　　按开电源键，即可不停地按F1键，进入BIOS操作界面，按向右的方向键，选择“Security”，然后再按向下的方向键，选择最下面的“Secure Boot”，按回车键进入。  
  
把“Secure Boot"中的“Enabled”按回车键更改成“Disabled”。  
  
　　按Esc键返回上一级菜单，再按向右方向键，选择“Startup”，把“UEFI/Legacy Boot”中的“UEFI Only”改成“Both”即可，按“Fn+F10”保存，然后就可以和其它电脑一样正常安装系统了。  
  
- Win8换Win7更改BIOS的方法二：  
  
　　同样是按电源键后，不停地按F1进入BIOS操作界面，按向右方向键选择“Restart”，然后再把“- OS Optimized Defaults”中的“Enabled”改成“Disabled”，在更改过程中，会弹出提示，我们选择YES即可。  
  
　　然后再按“Fn+F9”重置BIOS设置，重置完成以后，按再“Fn+F10”保存设置即可，这时就同没有预装Win8系统的电脑重装系统的方法是一样的了。  
  
　　注：你可以根据自己需要，随意选择上面其中一种更改BIOS中UEFI接口的方法，只要执行了上面其中某种方法的操作，即可顺种地通过U盘或光盘启动来更换Win8操作系统。  
  
解决Win8系统换Win7以后，画面卡在“正在启动Windows”  
  
　　出厂预装Win8系统换成Win7，必须更换BIOS中的UEFI接口，然后再重装系统，但有人问我，系统通过ghost导入到电脑硬盘当中，重启时，画面就一直卡在“正在启动Windows”处，这是什么原因造成的。  
  
　　其实这主要是因为分区表错误的原因造成的，我们只需要运行PE系统的中DiskGenius分区工具，选择中电脑硬盘，再点文件边上的硬盘，在下拉菜单中点击“重建主引导记录（MBR）”即可，然后再按太阳城娱乐城正常操作对电脑硬盘进行重新分区并重装系统即可。  
  
公司刚买了一台E430，将uefi/legacy boot，由默认uefi only 修改为both。不过，需要把security---secure boot中的secure boot 由默认Enables 修改为Disabled.只有这样修改以后，uefi/legacy boot才变成可以修改的项目。  
如果想安XP，config-----serial ata(sata)中sata controller mode option由默认achi修改为compatibility.

来源:http://bbs.diannaodian.com/read-u-tid-161168.html
