---
title: "NSURLCache 和 NSCachedURLResponse 的简单介绍记录"
date: "2025-06-27 10:07:20"
slug: "nsurlcache-he-nscachedurlresponse-de-jian-dan-jie-shao-ji-lu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/NSURLCache-和-NSCachedURLResponse-的简单介绍记录/"
  - "/2025/06/27/NSURLCache-和-NSCachedURLResponse-的简单介绍记录.html"
  - "/NSURLCache-和-NSCachedURLResponse-的简单介绍记录/"
  - "/NSURLCache-和-NSCachedURLResponse-的简单介绍记录.html"
  - "/2025/06/27/NSURLCache-NSCachedURLResponse-的简单介绍记录/"
  - "/2025/06/27/NSURLCache-NSCachedURLResponse-的简单介绍记录.html"
  - "/2025/06/27/nsurlcache-he-nscachedurlresponse-de-jian-dan-jie-shao-ji-lu/"
  - "/2025/06/27/nsurlcache-he-nscachedurlresponse-de-jian-dan-jie-shao-ji-lu.html"
  - "/nsurlcache-he-nscachedurlresponse-de-jian-dan-jie-shao-ji-lu.html"
---
NSURLCache 和 NSCachedURLResponse 的简单介绍记录

#### [NSURLCache](#1)

1、初始化相关的几个方法：

* sharedURLCache；
* setSharedURLCache；
* initWithMemoryCapacity

sharedURLCache方法返回一个NSURLCache实例。

默认情况下，内存是4M，4 * 1024 * 1024；Disk为20M，20 * 1024 ＊ 1024；路径在(NSHomeDirectory)/Library/Caches/(current application name, [[NSProcessInfo processInfo] processName])

setSharedURLCache可以通过这个方法来改变默认的NSURLCache。通过initWithMemoryCapacity来定制自己的NSURLCache。

2、cache使用相关的几个方法：

* cachedResponseForRequest；
* storeCachedResponse；
* removeCachedResponseForRequest；

removeAllCachedResponses

`- (NSCachedURLResponse *)cachedResponseForRequest:(NSURLRequest *)request;`

如果对应的NSURLRequest没有cached的response那么返回nil

`- (void)storeCachedResponse:(NSCachedURLResponse *)cachedResponse forRequest:(NSURLRequest *)request;`

为特定的NSURLRequest做cache

`- (void)removeCachedResponseForRequest:(NSURLRequest *)request;`

移除特定NSURLRequest的cache

`- (void)removeAllCachedResponses;`

移除所有的cache

3、property方法

`- (NSUInteger)memoryCapacity;`

`- (NSUInteger)diskCapacity;`

`- (void)setMemoryCapacity:(NSUInteger)memoryCapacity;`

可能会导致内存中的内存被截断

`- (void)setDiskCapacity:(NSUInteger)diskCapacity;`

`- (NSUInteger)currentMemoryUsage;`

`- (NSUInteger)currentDiskUsage;`

4、 Misc

a. NSURLCache在每个UIWebView的的NSURLRequest请求中都会被调用。

b. iOS设备上NSURLCache默认只能进行内存缓存。可以通过子类化NSURLCache来实现自定义的版本从而实现在DISK上缓存内容。

c. 需要重写cachedResponseForRequest，这个会在请求发送前会被调用，从中我们可以判定是否针对此NSURLRequest返回本地数据。

d. 如果本地没有缓存就调用下面这条语句：return [super cachedResponseForRequest:request];

#### [NSCachedURLResponse](#2)

包装了一下系统缓存机制的对象，保持了缓存对象的个性和特性。

1、 NSURLCacheStoragePolicy 缓存策略有三种

```objectivec
enum
{
    NSURLCacheStorageAllowed,
    NSURLCacheStorageAllowedInMemoryOnly,
    NSURLCacheStorageNotAllowed,
};
```

默认是第一种。不过在iOS的上官方文档上有这么一个解释：

Important: iOS ignores this cache policy, and instead treats it asNSURLCacheStorageAllowedInMemoryOnly.

 也就是说iOS上只有内存缓存，没有磁盘缓存。

2、构造方法

- `- (id)initWithResponse:(NSURLResponse *)response data:(NSData *)data;`
- `- (id)initWithResponse:(NSURLResponse *)response data:(NSData *)data userInfo:(NSDictionary *)userInfo storagePolicy:(NSURLCacheStoragePolicy)storagePolicy;`

3、Open API

- `- (NSURLResponse *)response;`
- `- (NSData *)data;`
- `- (NSDictionary *)userInfo;`
- `- (NSURLCacheStoragePolicy)storagePolicy;`

还是蛮详细的。

---

参考文章：

http://hi.baidu.com/marktian/item/e45af273bbc1eb14d0dcb3f4

http://o0o0o0o.iteye.com/blog/1326713

