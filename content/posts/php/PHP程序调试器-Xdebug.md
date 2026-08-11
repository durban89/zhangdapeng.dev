---
title: "PHP程序调试器-Xdebug"
date: "2025-06-20 11:08:01"
slug: "php-cheng-xu-tiao-shi-qi-xdebug"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/20/PHP程序调试器-Xdebug/"
  - "/2025/06/20/PHP程序调试器-Xdebug.html"
  - "/PHP程序调试器-Xdebug/"
  - "/PHP程序调试器-Xdebug.html"
  - "/2025/06/20/php-cheng-xu-tiao-shi-qi-xdebug/"
  - "/2025/06/20/php-cheng-xu-tiao-shi-qi-xdebug.html"
  - "/php-cheng-xu-tiao-shi-qi-xdebug.html"
---
XDebug是什么  
  
XDebug是一个开放源代码的PHP程序调试器(即一个Debug工具)，可以用来跟踪，调试和分析PHP程序的运行状况。  
安装XDebug  
  
访问 www.xdebug.org ，根据版本号与自己的操作系统、PHP版本下载合适的。  
编辑php.ini，有些集合环境已自带xdebug的配置，如果没有则自己手动加入下面几行：

```php
[xdebug]
zend_extension=/usr/lib/php5/20090626+lfs/xdebug.so
xdebug.auto_trace = on
xdebug.auto_profile = on
xdebug.collect_params = on
xdebug.collect_return = on
xdebug.profiler_enable = on
xdebug.trace_output_dir = "/var/log/trace_xdebug_log"
xdebug.profiler_output_dir = "/var/log/profiler_xdebug_log"
```

XDebug参数简介：  
  
zend_extension 加载xdebug扩展  
xdebug.auto_trace 自动打开打开函数调用监测  
xdebug.auto_profile 自动打开性能监测  
xdebug.trace_output_dir 设定函数调用监测信息的输出文件的路径。  
xdebug.profiler_output_dir 设定效能监测信息输出文件的路径。  
xdebug.collect_params 打开收集“函数参数”的功能。将函数调用的参数值列入函数过程调用的监测信息中。  
xdebug.collect_return 打开收集“函数返回值”的功能。将函数的返回值列入函数过程调用的监测信息中。  
重启Nginx,php-fpm。  
写一个test.php，内容为<?php phpinfo(); ?>，如果输出的内容中有看到xdebug，说明安装配置成功。或者去/home/ad/xdebug_log下看看是不是日志已经出来了。  
  
关于xdebug.trace_format=1，如果你使用触发方式启用代码追踪：（xdebug.auto_trace = 0;xdebug.trace_enable_trigger = 1），那么，你可以在URL里添加XDEBUG_TRACE，例如：localhost/test.php?XDEBUG_TRACE，或者localhost//test.php?XDEBUG_TRACE=1（任意值）。  
  
是不是觉得很麻烦，那么装个插件，让它来帮你。Chrome XDEBUG Helper，使用它，你可以切换3种状态，disabled ，debugging enabled，profiling enabled（下篇详细介绍），然后切换到debugging enabled。运行该脚本，（去掉URL里的?XDEBUG_TRACE），就可以代码跟踪了。  
  
使用xdebug_start_trace()和xdebug_stop_trace()可以手动追踪你的代码执行情况。

```bash
xdebug_start_trace();
//your code required to trace
xdebug_stop_trace();
```

设定 xdebug.auto_trace = 1 将在执行所有 PHP 脚本之前先启用自动跟踪。另外，您可以通过代码设定 xdebug.auto_trace = 0，并分别使用 xdebug_start_trace() 和 xdebug_stop_trace() 函数启用和禁用跟踪。但是，如果 xdebug.auto_trace 为 1，则可以在包括配置好的 auto_prepend_file 之前先启动跟踪。  
  
选项 xdebug.trace_ouput_dir 和 xdebug.trace_output_name 用于控制保存跟踪输出的位置。在这里，所有文件都被保存到 /tmp/traces 中，并且每个跟踪文件都以 trace 为开头，后接 PHP 脚本的名称（%s）以及进程 ID（%p）。所有 Xdebug 跟踪文件都以 .xt 后缀结尾。  
  
默认情况下，XDebug 将显示时间、内存使用量、函数名和函数调用深度字段。如果将 xdebug.trace_format 设为 0，则输出将符合人类阅读习惯（将参数设为 1 则为机器可读格式）。此外，如果指定 xdebug.show_mem_delta = 1，则可以查看内存使用量是在增加还是在减少，而如果指定 xdebug.collect_params = 4，则可以查看传入参数的类型和值。要监视每个函数返回的值，请设定 xdebug.collect_return = 1。

PS:  
结果是测试失败，因为我是在虚拟机里面测试的，线路不通，端口的配置有点问题，做了这样的调整

```bash
xdebug.remote_enable=1
xdebug.remote_port=9000
xdebug.remote_host="192.168.0.103"
xdebug.remote_handler="dbgp"
xdebug.remote_mode="req"
```

结果还是一样，提示

```bash
Notice: Trace could not be started in /home/davidzhang/local.ubuntu.test.com/index.php on line 4

Call Stack:
    0.0002     330764   1. {main}() /home/davidzhang/local.ubuntu.test.com/index.php:0
    0.0002     330808   2. xdebug_start_trace() /home/davidzhang/local.ubuntu.test.com/index.php:4

asasdasd
Notice: Function trace was not started in /home/davidzhang/local.ubuntu.test.com/index.php on line 6

Call Stack:
    0.0002     330764   1. {main}() /home/davidzhang/local.ubuntu.test.com/index.php:0
    0.0003     330808   2. xdebug_stop_trace() /home/davidzhang/local.ubuntu.test.com/index.php:6
```

求大神帮助
