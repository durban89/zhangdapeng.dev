---
title: "PHP中Push(推送)技术的探讨"
date: "2025-06-23 16:26:40"
slug: "php-zhong-push-tui-song-ji-shu-de-tan-tao"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/23/PHP中Push(推送)技术的探讨/"
  - "/2025/06/23/PHP中Push(推送)技术的探讨.html"
  - "/PHP中Push(推送)技术的探讨/"
  - "/PHP中Push(推送)技术的探讨.html"
  - "/2025/06/23/PHP中Push-推送-技术的探讨/"
  - "/2025/06/23/PHP中Push-推送-技术的探讨.html"
  - "/2025/06/23/php-zhong-push-tui-song-ji-shu-de-tan-tao/"
  - "/2025/06/23/php-zhong-push-tui-song-ji-shu-de-tan-tao.html"
  - "/php-zhong-push-tui-song-ji-shu-de-tan-tao.html"
---
随着人们对Web即时应用需求的不断上升，Server Push(推送)技术在聊天、消息提醒尤其是社交网络等方面开始兴起，成为实时应用的数据流核心。这篇日志试图探讨的便是各种适合于PHP的Push的实现方式以及其优劣。

### [什么是Server Push](#1)

想象在聊天应用中，如果使用传统的ajax来承担消息的传入，那么一般是通过每隔一定时间拉取一次信息的方式实现，但是其实这种方式有大量查询是浪费的。聊天等Web应用更需要服务器在特定时间来主动告知前端有新的消息(Push)，而不是前端每时每刻问服务器：“来消息了吗？”(Pull)。这也正是为什么这个技术常被叫做反向ajax。

其他别名：Comet，反向Ajax

### [如何实现Push](#2)

其实所谓的推送技术也没有多么复杂，目前从大类上有3种，一种仍然建立在ajax基础上，还有一种建立在框架基础上，最后一种抛弃了传统的HTTP协议，使用Flash或者HTML5的WebSockets技术。接下来将对这三种类别产生的不同的方式进行探讨。

1) Ajax 长轮询

Ajax长轮询从本质上来说仍然是一种pull，但是实时性较高，无用请求减少很多，是一种不错的Push实现方案。不过它只减少了网络上的无谓消耗。

核心: 客户端发起一个ajax请求，服务端将请求搁置(pending)或者说挂起，直到到了超时时间(timeout)或需要推送时返回；客户端则等待ajax返回后处理数据，再发起下一个ajax请求。

优点: 兼容性较高，实现简单

缺点: 对于php这种语言来说，如果要做到实时，那么服务端就要承受大得多的压力，因为搁置到什么时候往往是不确定的，这就要php脚本每次搁置都进行一个while循环。  
当然，如果服务器刷新每秒级，那尚可接受，只是实时性上退化了。

注意: 浏览器有连接数限制。我得出的结论是如果当前页面上有一个ajax请求处于等待返回状态，那么其他ajax请求都会被搁置(Chrome, Firefox已测)。似乎跟页面标记有关，一个规范的HTML可以同时有多个请求。如果页面有一般ajax需求怎么办？解决方法是开个框架，框架中使在另一个域名下进行Comet长轮询，需要注意跨域问题。

PHP实现:[Jquery+php实现comet](http://tech.techweb.com.cn/thread-439108-1-1.html)

相关:[Ajax跨域和js跨域解决方案](http://blog.csdn.net/zabcd117/article/details/2061669)

2) Frame 长连接

受到ajax启发，出现了框架下的长连接。

核心: Frame中发起一个普通请求，服务器将其搁置；需要推送时输出直接执行  
脚本，然后继续保持连接。如果担心超时问题可以改成框架论询。

优点: 与1一样具有高兼容特性

缺点: 最大的问题是如果框架在载入，那么浏览器就好一直显示“载入中”，这就弱爆了(解决方法参见文末的相关阅读资源)。同样服务器也要能hold住大量循环……另外，是否有同域连接限制没测试。

3) Flash/HTML5 WebSockets

用flash来发起WebSockets，秒杀前面一切问题。

优点: 标准化, RealTime, Push

缺点: 服务器需要能应对WebSockets；还有如果既没有Flash又不支持HTML5的怎么办？

PHP实现:[Start Using HTML5 WebSockets Today](http://net.tutsplus.com/tutorials/javascript-ajax/start-using-html5-websockets-today/)

4) 使用兼容封装层(socket.io)

以上每种方法都有优劣，那么终极解决方案便是合在一起！能WebSockets时候就WebSockets，不支持HTML5特性就退化到Flash，没有Flash则退化到Ajax长轮询。这也是我的Rainbowfish所采用的方式。

优点: 高度封装，编写非常容易，几乎不需要关心如何去实现的。实时，超低负载，高并发。

缺点: 其实算不上缺点，socket.io的服务器端要求是node.js，而不是php。

个人看法: 如果你是独立主机，能运行程序，那么socket.io配合node.js是个非常高效的选择。为什么呢？因为它还可以避免php的服务端高负载。

Rainbowfish的消息系统通过这种方式实现: 所有客户端都通过socket.io挂在nodejs服务器上(注意: 只是挂着，不需要任何循环，因为它是事件驱动的)；需要推送消息了，服务器就与nodejs通信(比如访问某个地址来实现)，告诉它推送什么消息到哪里；nodejs收到推送信号后，则通过socket.io实时传输数据给浏览器。这个其实也是一条单向的路，因为nodejs服务器不具备与php通信的能力，实际上也不需要，网页上直接连php就可以了。

### [结束语](#3)

事实上，第一个方法(Ajax Long Pull)是一个不错的方法，只是如果使用php完成的话服务器负载上有点大，但这其实是通病；而最后列举的socket.io方案完全避免了这个问题，因为它属于另一种架构，并且这种组合也可以配合几乎所有的脚本语言实现push。

对于实时性要求非常高的应用，或许使用php实现实时部分并不是一个好的选择，将会面临非常大的服务器负载(可以通过编写支持等待事件的扩展来解决这个问题)；如果只是消息提示等，则可以调整服务器上刷新的间隔降低到秒的级别，负载尚可接受。不过无论哪种用途，配合那些非阻塞语言或许才是最好的选择。

### [相关阅读](#4)

[How to implement COMET with PHP](http://www.zeitoun.net/articles/comet_and_php/start)

[Start Using HTML5 WebSockets Today](http://net.tutsplus.com/tutorials/javascript-ajax/start-using-html5-websockets-today/)

[Comet(Wikipedia)](https://en.wikipedia.org/wiki/Comet_%28programming%29)

[Ajax跨域和js跨域解决方案](http://blog.csdn.net/zabcd117/article/details/2061669)

[Jquery+php实现comet](http://tech.techweb.com.cn/thread-439108-1-1.html)


