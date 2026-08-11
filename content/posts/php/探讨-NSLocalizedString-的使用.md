---
title: "探讨 NSLocalizedString 的使用"
date: "2025-06-19 10:48:38"
slug: "tan-tao-nslocalizedstring-de-shi-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/19/探讨-NSLocalizedString-的使用/"
  - "/2025/06/19/探讨-NSLocalizedString-的使用.html"
  - "/探讨-NSLocalizedString-的使用/"
  - "/探讨-NSLocalizedString-的使用.html"
  - "/2025/06/19/tan-tao-nslocalizedstring-de-shi-yong/"
  - "/2025/06/19/tan-tao-nslocalizedstring-de-shi-yong.html"
  - "/tan-tao-nslocalizedstring-de-shi-yong.html"
---
程序本地化是扩展应用市场的重要砝码.iOS提供了简便的方法来实现本地化,其中用的最多的就是NSLocalizedString.

首先查看下NSLocalizedString是什么:

```objectivec
#define NSLocalizedString(key, comment) \
        [[NSBundle mainBundle] localizedStringForKey:(key) value:@"" table:nil]
#define NSLocalizedStringFromTable(key, tbl, comment) \
        [[NSBundle mainBundle] localizedStringForKey:(key) value:@"" table:(tbl)]
#define NSLocalizedStringFromTableInBundle(key, tbl, bundle, comment) \
        [bundle localizedStringForKey:(key) value:@"" table:(tbl)]
#define NSLocalizedStringWithDefaultValue(key, tbl, bundle, val, comment) \
        [bundle localizedStringForKey:(key) value:(val) table:(tbl)]
```

这里我们只看第一个

这是一个宏,本质上是调用了函数 locakizedStrigForKey:.这样,这个宏做的其实就是在当前bundle中查找资源文件名Localizable.strings

中键值key所指向的字符串.这样就不难理解还有诸如:NSLocalizedStringFromTable的宏了.

下面我们就来具体实现一下.

新建任一工程,然后添加新文件Localizable.strings

然后选择文件属性中的"Make File Localizable",页面自然跳转,再选择"General"选项卡时就会发现"Add Localization"了.

默认有English,我们可以添加zh-hans ,然后在相应的文件中输入: "NAME" = "你好",这样在代码中只需要简单的调用:

```objectivec
nameLabel.text = NSLocalizedString(@"NAME",nil);
```

此时在工程文件下出现了 \*.lpjo的文件夹,下面安置了相应的本地化文件.由此可以判断,对于其他资源文件如图片,xib文件都可以进行本地化.

最后,我们再实现对程序名称的本地化.

在工程的info.plist文件的属性中选择"Make File Localizable",然后会发现工程下出现InfoPlist.strings的文件,如法炮制,添加zh-hans,并在

相应的文件中添加"CFBundleDisplayName" = "中文名称" 即可.这样,你会发现你的机器上程序名称变成了中文.

PS:我还遇到一个问题,就是在本地化的时候语言代码是需要手工添加的,apple的文档上说所有的语言代码可以从ISO639( http://www.loc.gov/standards/iso639-2/php/English\_list.php)查询,可这个列表上中文对应的是chi/zho.而这显然没有区分简体和繁体中文.
