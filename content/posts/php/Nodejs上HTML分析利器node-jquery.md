---
title: "Nodejs上HTML分析利器node-jquery"
date: "2025-06-17 15:51:25"
slug: "nodejs-shang-html-fen-xi-li-qi-node-jquery"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/17/Nodejs上HTML分析利器node-jquery/"
  - "/2025/06/17/Nodejs上HTML分析利器node-jquery.html"
  - "/Nodejs上HTML分析利器node-jquery/"
  - "/Nodejs上HTML分析利器node-jquery.html"
  - "/2025/06/17/nodejs-shang-html-fen-xi-li-qi-node-jquery/"
  - "/2025/06/17/nodejs-shang-html-fen-xi-li-qi-node-jquery.html"
  - "/nodejs-shang-html-fen-xi-li-qi-node-jquery.html"
---
Node.js解析HTML DOM的当然是htmlpaser，jsdom。然而个人更喜欢jQuery的风格，与web jQuery的统一API,所以选择了node-jquery.其代码部署在Github的https://github.com/coolaj86/node-jquery.

借助某人之手搞了个示例，代码如下：

```javascript
var $ = require('jquery');
String.format = function() {

	var s = arguments[0];

	for (var i = 0; i < arguments.length - 1; i++) {

		var reg = new RegExp("\\{" + i + "\\}", "gm");

		s = s.replace(reg, arguments[i + 1]);

	}

	return s;

};

$.get("https://github.com/popular/forked",function(html){

	var $doc = $(html);

	console.log("No.  name  language  star   forks  ")

	$doc.find("ul.repolist li.source").each(function(i,project){

		var $project = $(project);

		var name = $project.find("h3").text().trim();

		var language = $project.find("li:eq(0)").text().trim();

		var star = $project.find("li.stargazers").text().trim();

		var forks = $project.find("li.forks").text().trim();

		var row =String.format("{4} {0}  {1}  {2}  {3}",name, language,star,forks,i + 1 );

		console.log(row);

	});

});
```

参考：http://www.cnblogs.com/whitewolf/archive/2013/02/27/2935618.html
