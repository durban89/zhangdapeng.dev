---
title: "iOS7 验证邮箱的合法性"
date: "2025-06-26 11:37:36"
slug: "ios7-yan-zheng-you-xiang-de-he-fa-xing"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/26/iOS7-验证邮箱的合法性/"
  - "/2025/06/26/iOS7-验证邮箱的合法性.html"
  - "/iOS7-验证邮箱的合法性/"
  - "/iOS7-验证邮箱的合法性.html"
  - "/2025/06/26/ios7-yan-zheng-you-xiang-de-he-fa-xing/"
  - "/2025/06/26/ios7-yan-zheng-you-xiang-de-he-fa-xing.html"
  - "/ios7-yan-zheng-you-xiang-de-he-fa-xing.html"
---
关于用于输入的邮箱地址的内容的合法性，在IOS7中的做法与之前的是一样的。

第一种方法：最简单的就是利用系统的NSPredicate

```objectivec
//利用正则表达式验证
-(BOOL)isValidateEmail:(NSString *)email {
    NSString *emailRegex = @"[A-Z0-9a-z._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}"; 
    NSPredicate *emailTest = [NSPredicate predicateWithFormat:@"SELF MATCHES %@", emailRegex]; 
    return [emailTest evaluateWithObject:email];
}
```

第二种方法：通过区分字符串

```objectivec
-(BOOL)validateEmail:(NSString*)email
{
    if((0 != [email rangeOfString:@"@"].length) &&
       (0 != [email rangeOfString:@"."].length))
    {
        NSCharacterSet* tmpInvalidCharSet = [[NSCharacterSet alphanumericCharacterSet] invertedSet];
        NSMutableCharacterSet* tmpInvalidMutableCharSet = [[tmpInvalidCharSet mutableCopy] autorelease];
        [tmpInvalidMutableCharSet removeCharactersInString:@"_-"];
        
        /*
         *使用compare option 来设定比较规则，如
         *NSCaseInsensitiveSearch是不区分大小写
         *NSLiteralSearch 进行完全比较,区分大小写
         *NSNumericSearch 只比较定符串的个数，而不比较字符串的字面值
         */
        NSRange range1 = [email rangeOfString:@"@"
                                      options:NSCaseInsensitiveSearch];
        
        //取得用户名部分
        NSString* userNameString = [email substringToIndex:range1.location];
        NSArray* userNameArray   = [userNameString componentsSeparatedByString:@"."];
        
        for(NSString* string in userNameArray)
        {
            NSRange rangeOfInavlidChars = [string rangeOfCharacterFromSet: tmpInvalidMutableCharSet];
            if(rangeOfInavlidChars.length != 0 || [string isEqualToString:@""])
                return NO;
        }
        
        //取得域名部分
        NSString *domainString = [email substringFromIndex:range1.location+1];
        NSArray *domainArray   = [domainString componentsSeparatedByString:@"."];
        
        for(NSString *string in domainArray)
        {
            NSRange rangeOfInavlidChars=[string rangeOfCharacterFromSet:tmpInvalidMutableCharSet];
            if(rangeOfInavlidChars.length !=0 || [string isEqualToString:@""])
                return NO;
        }
        
        return YES;
    }
    else {
       return NO;
    }
}
```

---

经过测试第一种方法好用。第二种方法尚未测试。

---

参考文章：

http://blog.csdn.net/justinjing0612/article/details/7310237

