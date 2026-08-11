---
title: "JavaScript的中的test和match，结果你不敢相信"
date: "2025-06-30 15:57:08"
slug: "javascript-de-zhong-de-test-he-match-jie-guo-ni-bu-gan-xiang-xin"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/30/JavaScript的中的test和match，结果你不敢相信/"
  - "/2025/06/30/JavaScript的中的test和match，结果你不敢相信.html"
  - "/JavaScript的中的test和match，结果你不敢相信/"
  - "/JavaScript的中的test和match，结果你不敢相信.html"
  - "/2025/06/30/JavaScript的中的test和match-结果你不敢相信/"
  - "/2025/06/30/JavaScript的中的test和match-结果你不敢相信.html"
  - "/2025/06/30/javascript-de-zhong-de-test-he-match-jie-guo-ni-bu-gan-xiang-xin/"
  - "/2025/06/30/javascript-de-zhong-de-test-he-match-jie-guo-ni-bu-gan-xiang-xin.html"
  - "/javascript-de-zhong-de-test-he-match-jie-guo-ni-bu-gan-xiang-xin.html"
---
大家看下代码，这个test和match还是晕了我很久的。

```js
var __parsers = [];
__parsers.push({'regExp':/.*one.*/g});
__parsers.push({'regExp':/.*two.*/g});
__parsers.push({'regExp':/.*three.*/g});
__parsers.push({'regExp':/.*four.*/g});
__parsers.push({'regExp':/.*five.*/g});
__parsers.push({'regExp':/.*six.*/g});
__parsers.push({'regExp':/.*seven.*/g});
__parsers.push({'regExp':/.*eight.*/g});

var matchParser = function(subject){
	for (var i = 0; i < __parsers.length; i++) {
	    // console.log('RegExp:',__parsers[i].regExp);
		if(subject.match(__parsers[i].regExp)){
		  return __parsers[i];
		}
	}
	throw new Error('No Match');
}

var testParser = function(subject){
	for (var i = 0; i < __parsers.length; i++) {
	    // console.log('RegExp:',__parsers[i].regExp);
		if (__parsers[i].regExp.test(subject)) {
			return __parsers[i];
		}
	}
	throw new Error('No Match');
}
```

简单的测试代码就这些。我们用一个循环来执行。

**//第一种测试**

```js
for(var i=0;i<5;i++){
	var subject = 'two';
	try{
		console.log(testParser(subject));
	}catch(err){
		console.log(err.message);
	}
}
```

//结果

```bash
{ regExp: /.*two.*/g }
No Match
{ regExp: /.*two.*/g }
No Match
{ regExp: /.*two.*/g }
```

看吧，还是有没有匹配到的吧。罪过啊。

**//第二种测试**

```js
for(var i=0;i<5;i++){
	var subject = 'two';
	try{
		console.log(matchParser(subject));
	}catch(err){
		console.log(err.message);
	}
}
```

//结果

```bash
{ regExp: /.*two.*/g }
{ regExp: /.*two.*/g }
{ regExp: /.*two.*/g }
{ regExp: /.*two.*/g }
{ regExp: /.*two.*/g }
```

你们看，是不是瞬间很开心啊。

可以使用nodejs执行整理执行一下。被坑了的感觉有木有啊！

可以看出来，使用match的全部匹配出来了，为什么，给你一个可想的空间吧。match完胜啊。


