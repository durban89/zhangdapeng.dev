---
title: "Objective-C实现的在PHP中oauth加密算法"
date: "2025-06-26 10:32:45"
slug: "objective-c-shi-xian-de-zai-php-zhong-oauth-jia-mi-suan-fa"
categories: ["技术"]
tags: ["PHP", "Objective-C"]
aliases:
  - "/2025/06/26/Objective-C实现的在PHP中oauth加密算法/"
  - "/2025/06/26/Objective-C实现的在PHP中oauth加密算法.html"
  - "/Objective-C实现的在PHP中oauth加密算法/"
  - "/Objective-C实现的在PHP中oauth加密算法.html"
  - "/2025/06/26/Objective-C实现的-在PHP中oauth加密算法/"
  - "/2025/06/26/Objective-C实现的-在PHP中oauth加密算法.html"
  - "/2025/06/26/objective-c-shi-xian-de-zai-php-zhong-oauth-jia-mi-suan-fa/"
  - "/2025/06/26/objective-c-shi-xian-de-zai-php-zhong-oauth-jia-mi-suan-fa.html"
  - "/objective-c-shi-xian-de-zai-php-zhong-oauth-jia-mi-suan-fa.html"
---
说起这个算法，在php中我是这么实现的

```php
function generateSig ($params, $secret = '')
{
    if (empty($secret)) {
        $secret = $this->appSecret;
    }
    $str = '';
    ksort($params);
    foreach ($params as $k => $v) {
        if (! is_array($v)) {
            $str .= "$k=$v";
        } else {
            ksort($v);
            $str .= "$k=" . json_encode($v);
        }
    }
    return bin2hex(hash_hmac('sha1', $str, $secret, TRUE));
}
```

那么在ios的应用中，应该如何实现呢，纠结了半天，其实是很简单的，只是自己错把secret放进了加密数据中，导致结果出现问题。下面展示一下自己的object-c在ios中的实现过程。

```objectivec
+ (NSString *)getSignature:(NSDictionary *)parameters secret:(NSString *)secret
{
    NSMutableString *baseString = [[NSMutableString alloc] init];
    //排序
    NSArray *sortArray = [parameters.allKeys sortedArrayUsingSelector:@selector(compare:)];
    for(NSString *key in sortArray)
    {
        NSString *value = [parameters objectForKey:key];
        if(value && [value isKindOfClass:[NSString class]])
        {
            [baseString appendFormat:@"%@=%@", key, value];
        }
    }
    
    const char *cKey  = [secret cStringUsingEncoding:NSUTF8StringEncoding];
    const char *cData = [baseString cStringUsingEncoding:NSUTF8StringEncoding];
    
    uint8_t cHMAC[CC_SHA1_DIGEST_LENGTH];
    
    CCHmac(kCCHmacAlgSHA1, cKey, strlen(cKey), cData, strlen(cData), cHMAC);
    
    NSString *hash;
    NSMutableString* output = [NSMutableString stringWithCapacity:CC_SHA1_DIGEST_LENGTH * 2];
    for(int i = 0; i < CC_SHA1_DIGEST_LENGTH; i++)
        [output appendFormat:@"%02x", cHMAC[i]];
    hash = output;
    return hash;
}
```

在这里不能缺少的库是

```objectivec
#import <CommonCrypto/CommonDigest.h>
#import <CommonCrypto/CommonHMAC.h>
```

应该是下面这个，如果使用到MD5，上面那个是不能缺少的

