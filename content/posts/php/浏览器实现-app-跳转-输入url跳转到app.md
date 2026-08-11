---
title: "浏览器实现 app 跳转 输入url跳转到app"
date: "2025-06-20 10:36:32"
slug: "liu-lan-qi-shi-xian-app-tiao-zhuan-shu-ru-url-tiao-zhuan-dao-app"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/浏览器实现-app-跳转-输入url跳转到app/"
  - "/2025/06/20/浏览器实现-app-跳转-输入url跳转到app.html"
  - "/浏览器实现-app-跳转-输入url跳转到app/"
  - "/浏览器实现-app-跳转-输入url跳转到app.html"
  - "/2025/06/20/liu-lan-qi-shi-xian-app-tiao-zhuan-shu-ru-url-tiao-zhuan-dao-app/"
  - "/2025/06/20/liu-lan-qi-shi-xian-app-tiao-zhuan-shu-ru-url-tiao-zhuan-dao-app.html"
  - "/liu-lan-qi-shi-xian-app-tiao-zhuan-shu-ru-url-tiao-zhuan-dao-app.html"
---
最近想实现一个功能，就是在浏览器中输入url地址，实现app的跳转，实现这样的功能并不麻烦，通过将网上一些相关教程汇总以后就写了下面的教程分享。  
  
实现效果如下，在浏览器中输入“Lover://”之后就会打开这个程序，打开后程序中会显示跳转过来的链接地址。

第一步：配置info.plist

其中URL identifier 可以随便取，URL Schemes 就是实现跳转URL协议的名称（可以多个）

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1588986500/gowhich/846340-f29f11eb0c1a39e1.png.webp)  
然后，在视图控制器中加入代码，用于显示跳转过来的地址：

第二步：代码实现过程

在viewController里面添加一个显示信息的函数`+(void) showMessage:(NSString *)message;`

```objectivec
+(void) showMessage:(NSString *)message{

    NSLog(@"Message : %@",message);
}
```

在delegate里面调用一下

首先需要实现一个方法：`-(BOOL) application:(UIApplication *)application handleOpenURL:(NSURL *)url`

```objectivec
-(BOOL) application:(UIApplication *)application handleOpenURL:(NSURL *)url{
    if(!url){
        return NO;
    }
    
    NSString *urlString = [url absoluteString];
    [SafariToAppViewController showMessage:urlString];
    
    return YES;
}
```

就完成了这个看似很酷的功能，至于参数传递的问题，我这里做了一个颜色的取值

实现代码如下（在delegate中实现）：

```objectivec
-(BOOL) application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation{
    
    // You should be extremely careful when handling URL requests.
    // Take steps to validate the URL before handling it.
    
    // Check if the incoming URL is nil.
    if (!url)
        return NO;
    
    // Invoke our helper method to parse the incoming URL and extact the color
    // to display.
    UIColor *launchColor = [self extractColorFromLaunchURL:url];
    // Stop if the url could not be parsed.
    if (!launchColor)
        return NO;
    
    [SafariToAppViewController showMessage:[NSString stringWithFormat:@"%@",launchColor]];
    
    return  YES;

}

- (UIColor*)extractColorFromLaunchURL:(NSURL*)url
{
    // Hexadecimal color codes begin with a number sign (#) followed by six
    // hexadecimal digits.  Thus, a color in this format is represented by
    // three bytes (the number sign is ignored).  The value of each byte
    // corresponds to the intensity of either the red, blue or green color
    // components, in that order from left to right.
    // Additionally, there is a shorthand notation with the number sign (#)
    // followed by three hexadecimal digits.  This notation is expanded to
    // the six digit notation by doubling each digit: #123 becomes #112233.
    
    
    // Convert the incoming URL into a string.  The '#' character will be percent
    // escaped.  That must be undone.
    NSString *urlString = [[url absoluteString] stringByReplacingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
    // Stop if the conversion failed.
    if (!urlString)
        return nil;
    
    // Create a regular expression to locate hexadecimal color codes in the
    // incoming URL.
    // Incoming URLs can be malicious.  It is best to use vetted technology,
    // such as NSRegularExpression, to handle the parsing instead of writing
    // your own parser.
    NSError *error = nil;
    NSRegularExpression *regex = [NSRegularExpression regularExpressionWithPattern:@"#[0-9a-f]{3}([0-9a-f]{3})?"
                                                                           options:NSRegularExpressionCaseInsensitive
                                                                             error:&error];
    
    // Check for any error returned.  This can be a result of incorrect regex
    // syntax.
    if (error)
    {
        NSLog(@"%@", error);
        return nil;
    }
    
    // Extract all the matches from the incoming URL string.  There must be at least
    // one for the URL to be valid (though matches beyond the first are ignored.)
    NSArray *regexMatches = [regex matchesInString:urlString options:0 range:NSMakeRange(0, urlString.length)];
    if (regexMatches.count < 1)
        return nil;
    
    // Extract the first matched string
    NSString *matchedString = [urlString substringWithRange:[regexMatches[0] range]];
    
    // At this point matchedString will look similar to either #FFF or #FFFFFF.
    // The regular expression has guaranteed that matchedString will be no longer
    // than seven characters.
    
    // Extract an ASCII c string from matchedString.  The '#' character should not be
    // included.
    const char *matchedCString = [[matchedString substringFromIndex:1] cStringUsingEncoding:NSASCIIStringEncoding];
    
    // Convert matchedCString into an integer.
    unsigned long hexColorCode = strtoul(matchedCString, NULL, 16);
    
    CGFloat red, green, blue;
    
    if (matchedString.length-1 > 3)
        // If the color code is in six digit notation...
    {
        // Extract each color component from the integer representation of the
        // color code.  Each component has a value of [0-255] which must be
        // converted into a normalized float for consumption by UIColor.
        red = ((hexColorCode & 0x00FF0000) >> 16) / 255.0f;
        green = ((hexColorCode & 0x0000FF00) >> 8) / 255.0f;
        blue = (hexColorCode & 0x000000FF) / 255.0f;
    }
    else
        // The color code is in shorthand notation...
    {
        // Extract each color component from the integer representation of the
        // color code.  Each component has a value of [0-255] which must be
        // converted into a normalized float for consumption by UIColor.
        red = (((hexColorCode & 0x00000F00) >> 8) | ((hexColorCode & 0x00000F00) >> 4)) / 255.0f;
        green = (((hexColorCode & 0x000000F0) >> 4) | (hexColorCode & 0x000000F0)) / 255.0f;
        blue = ((hexColorCode & 0x0000000F) | ((hexColorCode & 0x0000000F) << 4)) / 255.0f;
    }
    
    // Create and return a UIColor object with the extracted components.
    return [UIColor colorWithRed:red green:green blue:blue alpha:1.0f];
}
```
