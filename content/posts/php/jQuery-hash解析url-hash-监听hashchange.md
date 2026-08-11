---
title: "jQuery.hash解析url hash，监听hashchange"
date: "2025-06-27 09:45:18"
slug: "jqueryhash-jie-xi-url-hash-jian-ting-hashchange"
categories: ["技术"]
tags: ["JavaScript", "jQuery"]
aliases:
  - "/2025/06/27/jQuery.hash解析url-hash，监听hashchange/"
  - "/2025/06/27/jQuery.hash解析url-hash，监听hashchange.html"
  - "/jQuery.hash解析url-hash，监听hashchange/"
  - "/jQuery.hash解析url-hash，监听hashchange.html"
  - "/2025/06/27/jQuery-hash解析url-hash-监听hashchange/"
  - "/2025/06/27/jQuery-hash解析url-hash-监听hashchange.html"
  - "/2025/06/27/jqueryhash-jie-xi-url-hash-jian-ting-hashchange/"
  - "/2025/06/27/jqueryhash-jie-xi-url-hash-jian-ting-hashchange.html"
  - "/jqueryhash-jie-xi-url-hash-jian-ting-hashchange.html"
---
#### [什么是hashsearch、hashpath](#1)

其实那，hashsearch、hashpath这两个词是我自造的。在javascript语言里称url改变该部分不会影响页面重新加载的部分为hash，在后台语言里称之为fragment（碎片）。在这里，我们统称为hash。

在js里获取hash部分，可以使用如下语句获取：

// 获取当前浏览器的hash部分

// 如浏览器的url为：http://qianduanblog.com/#helloworld

var hash=location.hash;//=>"#helloworld"

在html发展的历史中，以前使用hash的作用很简单，就是做锚点使用。hash的“#”和CSS里的“#”是相同的意思，表示id。url的hash部分为#123，那么就会在页面打开的时候直接定位到id=123的元素位置。这个特性，已经被所有浏览器所接受并支持。通常这一功能用作于文章的目录部分，表示索引作用。

如下示例：

```html
<!doctype html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>指向id=123的内容</title>
	<style>
	div
	{
		height: 200px;
		margin-bottom: 10px;
		background: #eee;
	}
	</style>
</head>
<body>
	<a href="#123">点击这里立即跳转到id=123的元素位置</a>
	<div id="121">id=121</div>
	<div id="122">id=122</div>
	<div id="123">id=123</div>
	<div id="124">id=124</div>
	<div id="125">id=125</div>
</body>
</html>
```

如上例子，点击a链接就改变了当前url的hash，指向了hash指向的位置。当前了，如果为hash的id的元素不存在的话，那么各个浏览器的反应是各不相同的，部分高级浏览器不会改变页面滚动条的位置，部分低级浏览器会直接跳转到页面顶部。

说到这里，要解释下什么是hashsearch、hashpath了。从字面可以理解，`hashsearch=hash+search`，`hashpath=hash+path`。可能在专业术语里已经有这两个字了，但都与这篇文章无关，因为这俩个词是自造的。什么是hash，我们已经知道了。

那什么是search呢？

在url中有一部分是search部分，如：

```javascript
http://qianduanblog.com/?name=aaa&age=100
http://qianduanblog.com/?name=bbb&age=10
```

url的“?”后面的部分称之为search值，是被后台程序所接收的。

path又是什么呢？

如下：

```javascript
http://qianduanblog.com/name/aaa/age/100
http://qianduanblog.com/name/bbb/age/10
```

一眼就看出来了，search和path的不同点，通常我们都把search的url重定向成path类型的。

所以，由上可知，hashsearch、hashpath分别指的是：

```javascript
http://qianduanblog.com/#?name=aaa&age=100
http://qianduanblog.com/#!name/aaa/age/100
```

规范1：hashsearch的开头部分为“#?”，而hashpath的开头部分为“#!”，多个“#”会被忽略，多个“?”或“!”会被最后一个“?”或“!”所覆盖，如下：

```javascript
http://qianduanblog.com/#!name/aaa/age/100
http://qianduanblog.com/#####!!!!!!name/aaa/age/100
http://qianduanblog.com/#####????!name/aaa/age/100
```

以上3个url的hash会被解析成相同的结果。

规范2：hash部分的解析以开头的协议规定（“?”表示search类型，“!”表示path类型），与后面的内容无关，不符合规范的部分会被抛弃解析。

#### [哪些地方可以用hashsearch、hashpath](#2)

也许我们都认为url的hash是个小角色，它的作用微乎其微，就像当初我们认为ajax很渺小一样可笑。值得回味的是，把ajax发扬光大的谷歌同样在把url的hash也再次推向时代的前言，它是随着ajax的出现，诞生的一种新型url结构。

先看看如下几个url：

```javascript
http://qianduanblog.com/#!user/aaa
http://qianduanblog.com/#!user/bbb
http://qianduanblog.com/#!user/ccc
http://qianduanblog.com/#!user/ddd
```

从url的结构，很明显的看出来，这四个url的目的肯定是不同的，分别表示aaa、bbb、ccc、ddd四个用户所见的页面，但是有一点相同的是，这四个url是同一个页面，在浏览器打开的时候，只请求一次，不会分别请求。这是hash在url中发挥的重要特性。

有这样一个疑问了，既然页面相同的，那么四个用户的页面又如何区分呢？这里必须用到ajax，在页面载入之后，ajax载入四个用户独特的内容。

在当今，hash部分通常应用于单页面应用的丰富表现里，国外很多网站（twitter、谷歌等）已经这样做了，同样国内的如网易邮箱也这样做了。这样做的好处是：

1. 页面只需要一次加载。
2. 页面体验流畅，反应速度快。
3. 页面内容按需加载，减轻服务器压力。
4. 页面可以适配搜索引擎。

前3条的意思很明显，第4条的详细内容，我在这里就不说了，大家有兴趣可以去查看谷歌的介绍文字：jquery插件2：jquery.hash解析url hash，监听hashchange https://developers.google.com/webmasters/ajax-crawling/docs/getting-started。大概的意思是hashpath是可以被搜索引擎认识的，而hashsearch则不可以（目前）。所以，我们可以根据内容的不同来选择不同的hash类型。

#### [jquery.hash及hashchange](#3)

说明：jquery.hash.js默认的hashType为hashpath，其标示符为”!“，而hashsearch的标示符为”?”。

3.1、解析hash

按照以上的hash规则，我们可以把hash解析成键值对，$.hash();就可以直接解析，例：

```javascript
// http://qianduanblog.com/#!a/1/b/2/c/3
// http://qianduanblog.com/#?a=1&b=2&c=3
// $.hash();
// =>{a:"1",b:"2",c:"3"}
```

 3.2、读取hash

把hash解析成了键值对（json对象），读取它就很好办了，例：

```javascript
// http://qianduanblog.com/#!a/1/b/2/c/3
// http://qianduanblog.com/#?a=1&b=2&c=3
$.hash("a");
// =>"1"
$.hash(["a","b"]);
// =>{a:"1",b:"2"}
```

3.3、设置hash

设置hash的值也很简单，如：

```javascript
// 单个设置
$.hash("a","11");
// =>http://qianduanblog.com/#!a/11/b/2/c/3
// 单个设置的时候同时修改hash类型
$.hash("a","11","?");
// =>http://qianduanblog.com/#?a=11&b=2&c=3
// 多个设置
$.hash({a:111,b:222});
// =>http://qianduanblog.com/#?a=111&b=222&c=3
// 多个设置的时候同时修改hash类型
$.hash({a:111,b:222},"!");
// =>http://qianduanblog.com/#!a/111/b/222/c/3
```

3.4、删除hash

删除hash操作也很简单，例：

```javascript
// 删除单个
$.hash("a",null)
// =>http://qianduanblog.com/#!b/222/c/3
// 删除多个
$.hash(["a","b"],null)
// =>http://qianduanblog.com/#!c/3
```

3.5、清空hash

清空操作一如既往的方便，例：

```javascript
$.hash(null);
// =>http://qianduanblog.com/#
```

3.6、监听hashchange

监听的使用方法也很便捷，例：

```javascript
// 单监听，当监听的变量发生变化时触发
// 假设a值由1变化为2
$.hash("listen","a",function(oldObj,newObj){
// 当hash中的a值发生变化就会触发监听事件
// 回调函数有2个参数
// 参数1：旧值的对象，如这里监听的是a，那么其为{a:1}
// 参数2：现值的对象，如这里监听的是a，那么其为{a:2}
});
// 并监听，当监听的变量都同时发生变化时才触发
// 假设b由2=>3
// 假设c由3=>4
$.hash("listenAnd",["b","c"],function(oldObj,newObj){
// 参数1：旧值的对象，如这里监听的是b、c，那么其为{b:2,c:3}
// 参数2：现值的对象，如这里监听的是b、c，那么其为{b:3,c:4}
});
// 或监听，当监听的变量任何一个发生变化时都触发
// 假设d由4=>5
// 假设e没变5=>5
$.hash("listenOr",["d","e"],function(oldObj,newObj){
// 参数1：旧值的对象，如这里监听的是d、e，那么其为{d:4,e:5}
// 参数2：现值的对象，如这里监听的是d、e，那么其为{b:5,e:5}
});
```

#### [插件下载及演示](#4)

下载地址：

http://festatic.aliapp.com/#jquery.hash

http://festatic.aliapp.com/js/jquery.hash/#!a/1/b/2/c/3

---

参考文章：

http://qianduanblog.com/2003.html

