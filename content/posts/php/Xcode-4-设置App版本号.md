---
title: "Xcode 4 设置App版本号"
date: "2025-06-17 17:20:42"
slug: "xcode-4-she-zhi-app-ban-ben-hao"
categories: ["技术"]
tags: ["Xcode"]
aliases:
  - "/2025/06/17/Xcode-4-设置App版本号/"
  - "/2025/06/17/Xcode-4-设置App版本号.html"
  - "/Xcode-4-设置App版本号/"
  - "/Xcode-4-设置App版本号.html"
  - "/2025/06/17/xcode-4-she-zhi-app-ban-ben-hao/"
  - "/2025/06/17/xcode-4-she-zhi-app-ban-ben-hao.html"
  - "/xcode-4-she-zhi-app-ban-ben-hao.html"
---
刚接触ios开发的童鞋应该会对于app版本号吗有些疑问，因为target不仅仅在summary中有版本号，同样在Info.plist等地方也有版本号码的地方，一头乱码，不知吗？其实xcode在summary中已经将app最基本的设置进行了全面的封装，其余的plist，build setting等地方会跟着summary设置的改变而改变。  
  
一个version，一个build，都是设置版本的地方，有什么区别呢？  
  
在ios中(Android等工程中也一样),有两种version，一种是 CFBundleVersion ("Bundle Version")，也就是我们看到的version,另一种是CFBundleShortVersionString ("Bundle version string, short")，也就是我们看到的Build。  
  
普通情况下，我们只使用version即可，设置为"1.0", "1.1", "2.0" , etc，但如果你要使用两个版本号时候，需要将build设置为1,2,3...等递增的整数，有什么用呢？  
  
version我们可以通过AppStore、itunes或其它软件看到，是给用户看的，而build是我们在团队开发中内部只用的，只有我们自己可以看到。比如团队打算发布1.0版本的时候，会发布很多build版本供测试或QA团队进行测试，你发布了很多build，因为一直在修改着代码，因此当你收到一条bug信息时候，你怎么知道是那个build引起的问题呢，这时候build版本号的有点就可以体现出来了，不是吗。  
  
我这里有一段代码，可以在xcode编译时候自动增加build号码。  
  
先把 Info.plist 里的版本号改成某个数字，然后 Targets → your target → Build Phases → Run Script 的地方加上：

```objectivec
version=`/usr/libexec/PlistBuddy -c "Print CFBundleVersion" $PRODUCT_SETTINGS_PATH`
version=`expr $version + 1`
/usr/libexec/PlistBuddy -c "Set :CFBundleVersion $version" $PRODUCT_SETTINGS_PATH
#/usr/libexec/PlistBuddy -c "Set :CFBundleShortVersionString $version" $PRODUCT_SETTINGS_PATH 这行代码会让version也自增，一般不需要
```

参考：http://blog.csdn.net/shencaifeixia1/article/details/8221273#
