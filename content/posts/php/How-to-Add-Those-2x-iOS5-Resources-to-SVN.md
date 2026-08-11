---
title: "How to Add Those @2x iOS5 Resources to SVN"
date: "2025-06-20 10:36:37"
slug: "how-to-add-those-2x-ios5-resources-to-svn"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/20/How-to-Add-Those-@2x-iOS5-Resources-to-SVN/"
  - "/2025/06/20/How-to-Add-Those-@2x-iOS5-Resources-to-SVN.html"
  - "/How-to-Add-Those-@2x-iOS5-Resources-to-SVN/"
  - "/How-to-Add-Those-@2x-iOS5-Resources-to-SVN.html"
  - "/2025/06/20/How-to-Add-Those-2x-iOS5-Resources-to-SVN/"
  - "/2025/06/20/How-to-Add-Those-2x-iOS5-Resources-to-SVN.html"
  - "/2025/06/20/how-to-add-those-2x-ios5-resources-to-svn/"
  - "/2025/06/20/how-to-add-those-2x-ios5-resources-to-svn.html"
  - "/how-to-add-those-2x-ios5-resources-to-svn.html"
---
In order for your app to take full advantage of the iPhone 4 Retina Display, you'll need to add 2x resources to your iPhone project.  
  
If you're using SVN to manage your files, you'll be faced with something pretty annoying:

```bash
$ svn add xunYi7/library/images/blackArrow@2x.png
svn: warning: 'xunYi7/library/images/blackArrow' not found
```

This was incredibly frustrating for me, no matter how I tried to escape it: single quotes, double quotes, backslashes, etc. SVN refused to add.  
  
This is due to internal path recognizers in SVN. It expects the last at symbol to specify a revision. This is easily corrected by adding an at symbol to the end of your file:

```bash
$ svn add xunYi7/library/images/blackArrow@2x.png@
A  (bin)  xunYi7/library/images/blackArrow@2x.png
```

You'll still need to manually add each resource, but it's better than nothing. You could also use an IDE like Cornerstone, but I prefer the SVN CLI way of managing SVN.

这种项目中，svn也是有对应的解决方案的
