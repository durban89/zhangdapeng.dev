---
title: "苹果官方 Crash文件分析方法 （iOS系统Crash文件分析方法）"
date: "2025-06-20 11:50:43"
slug: "ping-guo-guan-fang-crash-wen-jian-fen-xi-fang-fa-ios-xi-tong-crash-wen-jian-fen-xi-fang-fa"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/苹果官方-Crash文件分析方法-（iOS系统Crash文件分析方法）/"
  - "/2025/06/20/苹果官方-Crash文件分析方法-（iOS系统Crash文件分析方法）.html"
  - "/苹果官方-Crash文件分析方法-（iOS系统Crash文件分析方法）/"
  - "/苹果官方-Crash文件分析方法-（iOS系统Crash文件分析方法）.html"
  - "/2025/06/20/苹果官方-Crash文件分析方法-iOS系统Crash文件分析方法/"
  - "/2025/06/20/苹果官方-Crash文件分析方法-iOS系统Crash文件分析方法.html"
  - "/2025/06/20/ping-guo-guan-fang-crash-wen-jian-fen-xi-fang-fa-ios-xi-tong-crash-wen-jian-fen-xi-fang/"
  - "/2025/06/20/ping-guo-guan-fang-crash-wen-jian-fen-xi-fang-fa-ios-xi-tong-crash-wen-jian-fen-xi-.html"
  - "/ping-guo-guan-fang-crash-wen-jian-fen-xi-fang-fa-ios-xi-tong-crash-wen-jian-fen-xi-fang-fa.html"
---
对于提交的苹果官方的app，在审核的时候会给我们一些crash文件，对于这些有用的文件，里面是关于我们的bug的一些信息，那么该如何去调试呢  
第一步：在任意目录创建一个目录，用来调试crash，我这里创建一个crash目录  
第二步：将之前Archive的文件copy到crash目录里面

其中包括两个文件.app和.app.dSYM

如果找不到的话可以按照下面的步骤进行

先到Organizer

1，找到提交那个时刻的Archive文件，选中，show in Finder

2，然后到达这里，然后再选中红色区域，会出现3中所示的提示

3，ok显示包内容，然后自己找找吧，肯定会有的

copy就好了

第三步：将symbolicatecrash工具copy到crash目录

找不到这个文件可以去

```bash
/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/PrivateFrameworks/DTDeviceKit.framework/Versions/A/Resources
```

这里看看，应该就会有了。

第四步：将要调试的crash文件copy到crash目录

这个crash文件，这里是来自苹果官方的，其实有时候也是来自其他的用户的电脑上的。  
第五步：通过命令进行测试  
打开终端，转到crash目录  
执行如下命令：

```bash
./symbolicatecrash ./2013-08-16-035933_DLiPad.crash ./appname.app.dSYM > symbol.crash
cat ./symbol.crash
```

结果如下：

```bash
Incident Identifier: 5434D911-E207-4D79-9139-40EA4EA76B45
CrashReporter Key:   d11ed3a4adbb0d9ca4d6016e73e439640f95f289
Hardware Model:      xxx
Process:         appname [8158]
Path:            /var/mobile/Applications/2AB1E8EB-6ECE-44F4-8195-4042339DD359/appname.app/appname
Identifier:      appname
Version:         ??? (???)
Code Type:       ARM (Native)
Parent Process:  launchd [1]

Date/Time:       2013-08-16 03:59:33.513 +0800
OS Version:      iOS 6.1.3 (10B329)
Report Version:  104

Exception Type:  EXC_CRASH (SIGABRT)
Exception Codes: 0x0000000000000000, 0x0000000000000000
Crashed Thread:  0

Last Exception Backtrace:
0   CoreFoundation                    0x3126029e 0x3119e000 + 795294
1   libobjc.A.dylib               0x3910497a 0x390fc000 + 35194
2   UIKit                         0x333f537c 0x33065000 + 3736444
3   UIKit                         0x3323758e 0x33065000 + 1910158
4   UIKit                         0x330c079c 0x33065000 + 374684
5   UIKit                         0x33068c34 0x33065000 + 15412
6   UIKit                         0x330686c8 0x33065000 + 14024
7   UIKit                         0x33068116 0x33065000 + 12566
8   GraphicsServices                  0x34d5c59e 0x34d56000 + 26014
9   GraphicsServices                  0x34d5c1ce 0x34d56000 + 25038
10  CoreFoundation                    0x3123516e 0x3119e000 + 618862
11  CoreFoundation                    0x31235112 0x3119e000 + 618770
12  CoreFoundation                    0x31233f94 0x3119e000 + 614292
13  CoreFoundation                    0x311a6eb8 0x3119e000 + 36536
14  CoreFoundation                    0x311a6d44 0x3119e000 + 36164
15  UIKit                         0x330bf480 0x33065000 + 369792
16  UIKit                         0x330bc2fc 0x33065000 + 357116
17  appname                            0x000cf358 0xce000 + 4952
18  libdyld.dylib                 0x3953bb1c 0x3953a000 + 6940


Thread 0 name:  Dispatch queue: com.apple.main-thread
Thread 0 Crashed:
0   libsystem_kernel.dylib            0x39602350 __pthread_kill + 8
1   libsystem_c.dylib             0x3957911e pthread_kill + 54
2   libsystem_c.dylib             0x395b596e abort + 90
3   libc++abi.dylib               0x38b53d4a abort_message + 70
4   libc++abi.dylib               0x38b50ff4 default_terminate() + 20
5   libobjc.A.dylib               0x39104a74 _objc_terminate() + 144
6   libc++abi.dylib               0x38b51078 safe_handler_caller(void (*)()) + 76
7   libc++abi.dylib               0x38b51110 std::terminate() + 16
8   libc++abi.dylib               0x38b52594 __cxa_rethrow + 84
9   libobjc.A.dylib               0x391049cc objc_exception_rethrow + 8
10  CoreFoundation                    0x311a6f1c CFRunLoopRunSpecific + 452
11  CoreFoundation                    0x311a6d44 CFRunLoopRunInMode + 100
12  UIKit                         0x330bf480 -[UIApplication _run] + 664
13  UIKit                         0x330bc2fc UIApplicationMain + 1116
14  appname                                0x000cf358 0xce000 + 4952
15  libdyld.dylib                 0x3953bb1c start + 0

Thread 1:
0   libsystem_kernel.dylib            0x39602d98 __workq_kernreturn + 8
1   libsystem_c.dylib             0x39550cf6 _pthread_workq_return + 14
2   libsystem_c.dylib             0x39550a12 _pthread_wqthread + 362
3   libsystem_c.dylib             0x395508a0 start_wqthread + 4

Thread 2 name:  Dispatch queue: com.apple.libdispatch-manager
Thread 2:
0   libsystem_kernel.dylib            0x395f2648 kevent64 + 24
1   libdispatch.dylib             0x39522974 _dispatch_mgr_invoke + 792
2   libdispatch.dylib             0x39522654 _dispatch_mgr_thread$VARIANT$mp + 32

Thread 3:
0   libsystem_kernel.dylib            0x39602d98 __workq_kernreturn + 8
1   libsystem_c.dylib             0x39550cf6 _pthread_workq_return + 14
2   libsystem_c.dylib             0x39550a12 _pthread_wqthread + 362
3   libsystem_c.dylib             0x395508a0 start_wqthread + 4

Thread 4 name:  WebThread
Thread 4:
0   libsystem_kernel.dylib            0x395f1eb4 mach_msg_trap + 20
1   libsystem_kernel.dylib            0x395f2048 mach_msg + 36
2   CoreFoundation                    0x31235040 __CFRunLoopServiceMachPort + 124
3   CoreFoundation                    0x31233d9e __CFRunLoopRun + 878
4   CoreFoundation                    0x311a6eb8 CFRunLoopRunSpecific + 352
5   CoreFoundation                    0x311a6d44 CFRunLoopRunInMode + 100
6   WebCore                       0x37196500 RunWebThread(void*) + 440
7   libsystem_c.dylib             0x3955b30e _pthread_start + 306
8   libsystem_c.dylib             0x3955b1d4 thread_start + 4

Thread 0 crashed with ARM Thread State (32-bit):
    r0: 0x00000000    r1: 0x00000000      r2: 0x00000000      r3: 0x3b0f8534
    r4: 0x00000006    r5: 0x3b0f8b88      r6: 0x1d844f24      r7: 0x2fd329f4
    r8: 0x1d844f00    r9: 0x00000300     r10: 0x334de04b     r11: 0x1c535350
    ip: 0x00000148    sp: 0x2fd329e8      lr: 0x39579123      pc: 0x39602350
  cpsr: 0x00000010
......
```

再执行如下命令：

```bash
dwarfdump --lookup 0x000cf358 --arch armv7 appname.app.dSYM/
```

关键是在这里`0x000cf358`，他是来自这里的

```bash
0   libsystem_kernel.dylib            0x39602350 __pthread_kill + 8
1   libsystem_c.dylib             0x3957911e pthread_kill + 54
2   libsystem_c.dylib             0x395b596e abort + 90
3   libc++abi.dylib               0x38b53d4a abort_message + 70
4   libc++abi.dylib               0x38b50ff4 default_terminate() + 20
5   libobjc.A.dylib               0x39104a74 _objc_terminate() + 144
6   libc++abi.dylib               0x38b51078 safe_handler_caller(void (*)()) + 76
7   libc++abi.dylib               0x38b51110 std::terminate() + 16
8   libc++abi.dylib               0x38b52594 __cxa_rethrow + 84
9   libobjc.A.dylib               0x391049cc objc_exception_rethrow + 8
10  CoreFoundation                    0x311a6f1c CFRunLoopRunSpecific + 452
11  CoreFoundation                    0x311a6d44 CFRunLoopRunInMode + 100
12  UIKit                         0x330bf480 -[UIApplication _run] + 664
13  UIKit                         0x330bc2fc UIApplicationMain + 1116
14  应用的名称                                0x000cf358 0xce000 + 4952
15  libdyld.dylib                 0x3953bb1c start + 0
```

结果如下：

```objectivec
----------------------------------------------------------------------
 File: appname.app.dSYM/Contents/Resources/DWARF/appname (armv7)
----------------------------------------------------------------------
Looking up address: 0x00000000000cf358 in .debug_info... found!

0x0015d390:
 Compile Unit: length = 0x00001fc6  version = 0x0002  abbr_offset = 
0x00000000  addr_size = 0x04  (next CU at 0x0015f35a)

0x0015d39b: TAG_compile_unit [1] *
             AT_producer( "Apple LLVM version 4.2 (clang-425.0.24) (based on LLVM 3.2svn)" )
             AT_language( DW_LANG_ObjC )
             AT_name( "/Users/zhy/Downloads/ios/xxx/xxx/library/ASIHttpRequest/ASIDownloadCache.m" )
             AT_low_pc( 0x000ccfc0 )
             AT_stmt_list( 0x0002cf0b )
             AT_comp_dir( "/Users/zhy/Downloads/ios/vlink_app_xunyi" )
             AT_APPLE_major_runtime_vers( 0x02 )

0x0015dd38:     TAG_subprogram [53] *
                 AT_name( "-[ASIDownloadCache isCachedDataCurrentForRequest:]" )
                 AT_decl_file( "/Users/zhy/Downloads/ios/xxx/xxx/library/ASIHttpRequest/ASIDownloadCache.m" )
                 AT_decl_line( 315 )
                 AT_prototyped( 0x01 )
                 AT_type( {0x0015d490} ( BOOL ) )
                 AT_APPLE_isa( 0x01 )
                 AT_low_pc( 0x000cf278 )
                 AT_high_pc( 0x000cf9e2 )
                 AT_frame_base( r7 )
                 AT_object_pointer( {0x0015dd54} )

0x0015dd86:         TAG_lexical_block [10] *
                     AT_low_pc( 0x000cf2ca )
                     AT_high_pc( 0x000cf9de )
Line table dir : '/Users/zhy/Downloads/ios/xxx/xxx/library/ASIHttpRequest'
Line table file: 'ASIDownloadCache.m' line 320, column 3 with start address 0x00000000000cf340

Looking up address: 0x00000000000cf358 in .debug_frame... found!

0x00007290: FDE
        length: 0x0000000c
   CIE_pointer: 0x00000000
    start_addr: 0x000cf278 -[ASIDownloadCache isCachedDataCurrentForRequest:]
    range_size: 0x0000076a (end_addr = 0x000cf9e2)
  Instructions: 0x000cf278: CFA=4294967295+4294967295
```

到这里就知道问题所在了吧

```bash
Line table dir : '/Users/zhy/Downloads/ios/xxx/xxx/library/ASIHttpRequest'
Line table file: 'ASIDownloadCache.m' line 320, column 3 with start address 0x00000000000cf340
```

如果有多个crash文件的话，可以重复操作一遍就好了。
