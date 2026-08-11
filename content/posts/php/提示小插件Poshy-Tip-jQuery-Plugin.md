---
title: "提示小插件Poshy Tip jQuery Plugin"
date: "2025-06-17 15:51:08"
slug: "ti-shi-xiao-cha-jian-poshy-tip-jquery-plugin"
categories: ["技术"]
tags: ["HTML", "jQuery"]
aliases:
  - "/2025/06/17/提示小插件Poshy-Tip-jQuery-Plugin/"
  - "/2025/06/17/提示小插件Poshy-Tip-jQuery-Plugin.html"
  - "/提示小插件Poshy-Tip-jQuery-Plugin/"
  - "/提示小插件Poshy-Tip-jQuery-Plugin.html"
  - "/2025/06/17/ti-shi-xiao-cha-jian-poshy-tip-jquery-plugin/"
  - "/2025/06/17/ti-shi-xiao-cha-jian-poshy-tip-jquery-plugin.html"
  - "/ti-shi-xiao-cha-jian-poshy-tip-jquery-plugin.html"
---
关于Poshy Tip是个很简单的提示插件。我觉的还不错，下面做了一个简答的小例子

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head>
	<title>我的小提示</title>
	<meta http-equiv="Content-Type" content="text/html;charset=utf-8" />


	<!-- Tooltip classes -->
	<link rel="stylesheet" href="../src/tip-yellow/tip-yellow.css" type="text/css" />
	<link rel="stylesheet" href="../src/tip-violet/tip-violet.css" type="text/css" />
	<link rel="stylesheet" href="../src/tip-darkgray/tip-darkgray.css" type="text/css" />
	<link rel="stylesheet" href="../src/tip-skyblue/tip-skyblue.css" type="text/css" />
	<link rel="stylesheet" href="../src/tip-yellowsimple/tip-yellowsimple.css" type="text/css" />
	<link rel="stylesheet" href="../src/tip-twitter/tip-twitter.css" type="text/css" />
	<link rel="stylesheet" href="../src/tip-green/tip-green.css" type="text/css" />

	<!-- jQuery and the Poshy Tip plugin files -->
	<script type="text/javascript" src="includes/jquery-1.4.2.min.js"></script>
	<script type="text/javascript" src="../src/jquery.poshytip.js"></script>

	<!-- Setup examples on this page -->
	<script type="text/javascript">
		//<![CDATA[
		$(function(){

			$('#demo-basic').poshytip();
		});
		//]]>
	</script>
</head>

<body>

	<div id="content">
		<p><a id="demo-basic" title="小提示出现了，你好，我是小提示" href="#">快出来小提示</a></p>
	</div>
</body>
</html>
```

关键几个文件要引入

样式文件

```html
<link rel="stylesheet" href="../src/tip-yellow/tip-yellow.css" type="text/css" />
<link rel="stylesheet" href="../src/tip-violet/tip-violet.css" type="text/css" />
<link rel="stylesheet" href="../src/tip-darkgray/tip-darkgray.css" type="text/css" />
<link rel="stylesheet" href="../src/tip-skyblue/tip-skyblue.css" type="text/css" />
<link rel="stylesheet" href="../src/tip-yellowsimple/tip-yellowsimple.css" type="text/css" />
<link rel="stylesheet" href="../src/tip-twitter/tip-twitter.css" type="text/css" />
<link rel="stylesheet" href="../src/tip-green/tip-green.css" type="text/css" />
```

这里面的样式可以跟你自己的需要进行选择定制

脚本文件

```html
<script type="text/javascript" src="includes/jquery-1.4.2.min.js"></script>
<script type="text/javascript" src="../src/jquery.poshytip.js"></script>
```

这个大家都知道的

具体的演示文档，可以参考这个地址：http://vadikom.com/demos/poshytip/#download

读读英文文档还不错
