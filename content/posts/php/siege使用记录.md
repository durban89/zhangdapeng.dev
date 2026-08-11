---
title: "siege使用记录"
date: "2025-07-10 11:52:12"
slug: "siege-shi-yong-ji-lu"
categories: ["技术"]
tags: ["Siege"]
aliases:
  - "/2025/07/10/siege使用记录/"
  - "/2025/07/10/siege使用记录.html"
  - "/siege使用记录/"
  - "/siege使用记录.html"
  - "/2025/07/10/siege-shi-yong-ji-lu/"
  - "/2025/07/10/siege-shi-yong-ji-lu.html"
  - "/siege-shi-yong-ji-lu.html"
---
Siege is an http load tester and benchmarking utility

参数说明:

-C,或-config 在屏幕上打印显示出当前的配置,配置是包括在他的配置文件$HOME/.siegerc 中,可以编辑里面的参数,这样每次siege 都会按照它运行.  
-v 运行时能看到详细的运行信息  
-c n,或-concurrent=n 模拟有n个用户在同时访问,n不要设得太大,因为越大,siege 消耗本地机器的资源越多  
-i,-internet 随机访问urls.txt中的url列表项,以此模拟真实的访问情况(随机性),当 urls.txt存在是有效  
-d n,-delay=n hit每个url之间的延迟,在0-n之间  
-r n,-reps=n 重复运行测试n次,不能与 -t同时存在  
-t n,-time=n 持续运行siege ‘n’秒(如10S),分钟(10M),小时(10H)  
-l 运行结束,将统计数据保存到日志文件中siege .log,一般位于/usr/local/var/siege  .log中,也可在.siegerc中自定义  
-R SIEGERC,-rc=SIEGERC 指定用特定的siege 配置文件来运行,默认的为$HOME/.siegerc  
-f FILE, -file=FILE 指定用特定的urls文件运行siege ,默认为urls.txt,位于siege 安装目录下的etc/urls.txt  
-u URL,-url=URL 测试指定的一个URL,对它进行”siege “,此选项会忽略有关urls文件的设定

```bash
Transactions:		          62 hits
Availability:		       98.41 %
Elapsed time:		       16.35 secs
Data transferred:	        0.65 MB
Response time:		        3.72 secs
Transaction rate:	        3.79 trans/sec
Throughput:		        0.04 MB/sec
Concurrency:		       14.09
Successful transactions:          62
Failed transactions:	           1
Longest transaction:	       15.53
Shortest transaction:	        0.00
```

测试结果参数说明:

Transactions:                  28759 hits         #完成28759次处理  
Availability:                  94.97 %              #94.97 % 成功率  
Elapsed time:                  33.58 secs         #耗时33.58秒  
Data transferred:              46.84 MB           #传输数据46.84M  
Response time:                  0.04 secs         #响应时间0.04秒  
Transaction rate:             856.43 trans/sec    #平均每秒完成856.43次处理,也就是QPS  
Throughput:                     1.40 MB/sec       #平均每秒传送数据  
Concurrency:                   35.48              #实际最高并发连接数  
Successful transactions:       28759              #成功处理次数  
Failed transactions:            1523              #失败处理次数  
Longest transaction:            7.05              #请求响应最长时间  
Shortest transaction:           0.00              #请求响应最短时间
