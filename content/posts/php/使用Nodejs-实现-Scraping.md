---
title: "使用Nodejs 实现 Scraping"
date: "2025-06-30 14:09:15"
slug: "shi-yong-nodejs-shi-xian-scraping"
categories: ["技术"]
tags: ["NodeJS"]
aliases:
  - "/2025/06/30/使用Nodejs-实现-Scraping/"
  - "/2025/06/30/使用Nodejs-实现-Scraping.html"
  - "/使用Nodejs-实现-Scraping/"
  - "/使用Nodejs-实现-Scraping.html"
  - "/2025/06/30/shi-yong-nodejs-shi-xian-scraping/"
  - "/2025/06/30/shi-yong-nodejs-shi-xian-scraping.html"
  - "/shi-yong-nodejs-shi-xian-scraping.html"
---
这里是使用Cheerio

第一个测试代码如下：

```js
var cheerio = require('cheerio'),
    $ = cheerio.load('<h2 class = "title">Hello world</h2>');

$('h2.title').text('Hello there!');
$('h2').addClass('welcome');

$.html();
//=> <h2 class = "title welcome">Hello there!</h2>
```

如果你的代码是放在本地文件的话，可以使用如下代码

```js
var $ = require('cheerio')
var fs = require('fs')

var htmlString = fs.readFileSync('index.html').toString()
var parsedHTML = $.load(htmlString)

// query for all elements with class 'foo' and loop over them
parsedHTML('.foo').map(function(i, foo) {
  // the foo html element into a cheerio object (same pattern as jQuery)
  foo = $(foo)
  console.log(foo.text())
})
```

同样的，你也可以使用request模块获取远程的html页面

```js
var $ = require('cheerio')
var request = require('request')

function gotHTML(err, resp, html) {
  if (err) return console.error(err)
  var parsedHTML = $.load(html)
  // get all img tags and loop over them
  var imageURLs = []
  parsedHTML('a').map(function(i, link) {
    var href = $(link).attr('href')
    if (!href.match('.png')) return
    imageURLs.push(domain + href)
  })
}

var domain = 'http://substack.net/images/'
request(domain, gotHTML)
```

最后一个例子是获取页面的img二进制文件，然后使用[picture-tube](http://npmjs.org/picture-tube)和[Stream API](https://github.com/substack/stream-handbook)把他渲染出来

```js
var pictureTube = require('picture-tube')

var randomIndex = Math.floor(Math.random() * imageURLs.length)
var randomImage = imageURLs[randomIndex]
request(randomImage).pipe(pictureTube()).pipe(process.stdout)
```


