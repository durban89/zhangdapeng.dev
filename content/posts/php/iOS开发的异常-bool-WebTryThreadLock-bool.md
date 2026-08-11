---
title: "iOS开发的异常-bool _WebTryThreadLock(bool)"
date: "2025-06-17 14:43:26"
slug: "ios-kai-fa-de-yi-chang-bool-webtrythreadlockbool"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/17/iOS开发的异常-bool-WebTryThreadLock(bool)/"
  - "/2025/06/17/iOS开发的异常-bool-WebTryThreadLock(bool).html"
  - "/iOS开发的异常-bool-WebTryThreadLock(bool)/"
  - "/iOS开发的异常-bool-WebTryThreadLock(bool).html"
  - "/2025/06/17/iOS开发的异常-bool-WebTryThreadLock-bool/"
  - "/2025/06/17/iOS开发的异常-bool-WebTryThreadLock-bool.html"
  - "/2025/06/17/ios-kai-fa-de-yi-chang-bool-webtrythreadlockbool/"
  - "/2025/06/17/ios-kai-fa-de-yi-chang-bool-webtrythreadlockbool.html"
  - "/ios-kai-fa-de-yi-chang-bool-webtrythreadlockbool.html"
---
一般的问题是这样的

“`bool _WebTryThreadLock(bool)`, 0xxxxxx: Tried to obtain the web lock from a thread other than the main thread or the web thread. This may be a result of calling to UIKit from a secondary thread. Crashing now...”

原因: update ui in background thread.

解决办法: update ui in main thread.

示例:

```objectivec
dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
    // Do time-consuming task in background thread
    // Return back to main thread to update UI
    dispatch_sync(dispatch_get_main_queue(), ^{
        _profile = [[UITextView alloc] init];
        [_profile setFrame:CGRectMake(labelPersonProfileCaption.frame.origin.x, labelPersonProfileCaption.frame.origin.y + labelPersonProfileCaption.frame.size.height, width, height - 30.0)];
        
        _profile.layer.borderColor = [[UIColor lightGrayColor] CGColor];
        _profile.layer.borderWidth = 1.0;
        _profile.layer.cornerRadius = 10.0;
        _profile.delegate = self;
        _profile.text = @"";
        _profile.backgroundColor = [UIColor lightGrayColor];
        _profile.editable = NO;
        _profile.font = [UIFont systemFontOfSize:14.0];
        _profile.backgroundColor = [UIColor whiteColor];
        
        [_contentScroll addSubview:_profile];
    });
});
```

参考资料：http://blog.csdn.net/chuwachen/article/details/8718253
