---
title: "iOS6 UI状态保持和恢复"
date: "2025-06-19 10:48:24"
slug: "ios6-ui-zhuang-tai-bao-chi-he-hui-fu"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/iOS6-UI状态保持和恢复/"
  - "/2025/06/19/iOS6-UI状态保持和恢复.html"
  - "/iOS6-UI状态保持和恢复/"
  - "/iOS6-UI状态保持和恢复.html"
  - "/2025/06/19/ios6-ui-zhuang-tai-bao-chi-he-hui-fu/"
  - "/2025/06/19/ios6-ui-zhuang-tai-bao-chi-he-hui-fu.html"
  - "/ios6-ui-zhuang-tai-bao-chi-he-hui-fu.html"
---
关于iOS6 UI状态保持和恢复，是最近看到几个例子，里面有这个方法`encodeRestorableStateWithCoder`和`decodeRestorableStateWithCoder`，感觉很奇怪，都怪自己知识浅薄啊

其实呢使用这个是有原因的.

iOS设计规范中要求，当应用退出的时候（包括被终止运行时候），画面中UI元素状态需要保持的，当再次进来的时候看状态与退出是一样的。iOS6之后苹果提供以下API使得UI状态保持和恢复变得很容易了。  
在iOS6中我们可以在3地方实现状态保持和恢复：  
   
1,应用程序委托对象  
   
2,视图控制器  
   
3,自定义视图  
  
恢复标识是iOS6为了实现UI状态保持和恢复添加的设置项目。我们需要在应用程序委托对象AppDelegate代码部分做一些修改，添加的代码如下：



```objectivec
-(BOOL) application:(UIApplication *)application shouldSaveApplicationState:(NSCoder *)coder  
{  
  
    return YES;  
  
}  
  
-(BOOL) application:(UIApplication *)application shouldRestoreApplicationState:(NSCoder *)coder  
{  
  
    return YES;  
  
}  
  
- (void)application:(UIApplication *)application willEncodeRestorableStateWithCoder:(NSCoder *)coder  
{  
  
    [coder encodeFloat:2.0 forKey:@"Version"];  
  
}  
  
- (void)application:(UIApplication *)application didDecodeRestorableStateWithCoder:(NSCoder *)coder  
{  
  
    float lastVer = [coder decodeFloatForKey:@"Version"];  
  
    NSLog(@”lastVer = %f”,lastVer);  
  
}
```

其中`application:shouldSaveApplicationState:`在应用退出的时候调用，负责控制是否允许保存状态，返回YES情况是可以保存，NO是不保存。  
   
`application:shouldRestoreApplicationState:`是应用启动时候调用，负责控制是否恢复上次退出的时候的状态，返回YES情况是可以恢复，NO是不恢复。  
   
`application:willEncodeRestorableStateWithCoder:`方法是保存时候调用，在这个方法中实现UI状态或数据的保存，其中`[coder encodeFloat:2.0 forKey:@"Version"]`是保存简单数据。  
   
`application:didDecodeRestorableStateWithCoder:`方法是恢复时候调用，在这个方法中实现UI状态或数据的恢复，其中`[coder decodeFloatForKey:@"Version"]`语句是恢复上次保存的数据。  
   
要想实现具体画面中控件的保持和恢复，还需要在它视图控制器中添加一些代码，ViewController.m中添加的代码如下：

```objectivec
-(void)encodeRestorableStateWithCoder:(NSCoder *)coder  
{  
    [super encodeRestorableStateWithCoder:coder];  
    [coder encodeObject:self.txtField.text forKey:kSaveKey];  
}  

-(void)decodeRestorableStateWithCoder:(NSCoder *)coder  
{  
    [super decodeRestorableStateWithCoder:coder];  
    self.txtField.text = [coder decodeObjectForKey:kSaveKey];  
}
```

在iOS6之后视图控制器都添加了两个：`encodeRestorableStateWithCoder:`和`decodeRestorableStateWithCoder:`用来实现该控制器中的控件或数据的保存和恢复。其中`encodeRestorableStateWithCoder:` 方法是在保存时候调用，`[coder encodeObject:self.txtField.text forKey:kSaveKey]`语句是按照指定的键保存文本框的内容，`decodeRestorableStateWithCoder:`方法是在恢复时候调用，`[coder decodeObjectForKey:kSaveKey]`是恢复文本框内容时候调用，保存和恢复事实上就是向一个归档文件中编码和解码的过程。
