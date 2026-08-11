---
title: "iOS plist的使用"
date: "2025-06-10 11:52:11"
slug: "ios-plist-de-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/10/iOS-plist的使用/"
  - "/2025/06/10/iOS-plist的使用.html"
  - "/iOS-plist的使用/"
  - "/iOS-plist的使用.html"
  - "/2025/06/10/ios-plist-de-shi-yong/"
  - "/2025/06/10/ios-plist-de-shi-yong.html"
  - "/ios-plist-de-shi-yong.html"
---
1，创建  
按command +N快捷键创建，或者File —> New —> New File，选择Mac OS X下的Property List  
创建plist文件名为plistdemo。

打开plistdemo文件，在空白出右键,右键选择Add row 添加数据,添加成功一条数据后，在这条数据上右键看到 value Type选择Dictionary。点加号添加数据。

创建完成之后用source code查看到plist文件是一个xml格式的文件。

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>one</key>
	<array>
		<string>chenglong</string>
		<string>lilianjie</string>
		<string>zhenzidan</string>
		<string>shixiaolong</string>
	</array>
	<key>two</key>
	<array>
		<string>liushishi</string>
		<string>tangyan</string>
		<string>zhangziyi</string>
		<string>yangmi</string>
	</array>
</dict>
</plist>
```

读取数据的方式，和方法可以参考下面的代码：

```objectivec
- (void)viewDidLoad
{
    [super viewDidLoad];

    //取得person.plist绝对路径
    //person.plist本身是一个NSDictionary,以键-值的形式存储字符串数组
    NSString *path=[[NSBundle mainBundle] pathForResource:@"person" ofType:@"plist"];
    
    //转换成NSDictionary对象
    NSDictionary *dict=[[NSDictionary alloc] initWithContentsOfFile:path];
    
    self.names=dict;
    
    //重置
    [self resetSearch];
    
    //重新载入数据
    [self.table reloadData];
    
}
```

我是直接放在了viewDidLoad这个方法中

