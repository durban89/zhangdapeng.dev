---
title: "iOS开发判断网络状态"
date: "2025-06-17 15:51:01"
slug: "ios-kai-fa-pan-duan-wang-luo-zhuang-tai"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS开发判断网络状态/"
  - "/2025/06/17/iOS开发判断网络状态.html"
  - "/iOS开发判断网络状态/"
  - "/iOS开发判断网络状态.html"
  - "/2025/06/17/ios-kai-fa-pan-duan-wang-luo-zhuang-tai/"
  - "/2025/06/17/ios-kai-fa-pan-duan-wang-luo-zhuang-tai.html"
  - "/ios-kai-fa-pan-duan-wang-luo-zhuang-tai.html"
---
网站找过关于ISO网络的状态判断，官方也是有示例的，但是自己琢磨了一下，下面的代码还是可以不错的

```objectivec
/***
* 此函数用来判断是否网络连接服务器正常
* 需要导入Reachability类
*/
+ (BOOL)isExistenceNetwork
{
    BOOL isExistenceNetwork;
    Reachability *reachability = [Reachability reachabilityWithHostName:@""];  // 测试服务器状态
    
     switch([reachability currentReachabilityStatus]) {
            case NotReachable:
                  isExistenceNetwork = FALSE;
                  break;
             case ReachableViaWWAN:
                   isExistenceNetwork = TRUE;
                   break;
              case ReachableViaWiFi:
                    isExistenceNetwork = TRUE;
                    break;
     }
     return  isExistenceNetwork;
}
```

参考文章：http://www.cnblogs.com/pengyingh/articles/2382259.html
