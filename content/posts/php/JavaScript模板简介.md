---
title: "JavaScript模板简介"
date: "2025-06-17 15:51:20"
slug: "javascript-mu-ban-jian-jie"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/17/JavaScript模板简介/"
  - "/2025/06/17/JavaScript模板简介.html"
  - "/JavaScript模板简介/"
  - "/JavaScript模板简介.html"
  - "/2025/06/17/javascript-mu-ban-jian-jie/"
  - "/2025/06/17/javascript-mu-ban-jian-jie.html"
  - "/javascript-mu-ban-jian-jie.html"
---
除（Firefox）自带的XUL模板系统外，还可以使用JavaScript模板，这种方法也可以实现内容格式与结构的分离，但依赖于JavaScript模板引擎通过JavaScript业务逻辑将内容注入到模板中，不需要使用RDF/XML这样的技术

## [按语法风格](#1)

### [100%基于标准（没有自定义语法）](#1-1)

纯JavaScript（JavaScript函数调用生成HTML）

* [JsonML](http://jsonml.org/)(没有“浏览器端模板”)，也可以使用JavaScript的JSON子集
* [domMaster](http://vflash.ru/rr2jquery/?mdc) 和 nodejs [master\_texthtml](https://github.com/flash/master_texthtml)
* [Mootools Template Engine](http://mte.null-tech.com/) (null-tech.com)

纯HTML（使用JavaScript选择器找出正常的HTML，按业务逻辑填充）

* [PURE](http://beebole.com/pure/)
* [mustache](https://github.com/janl/mustache.js) (有一些设计逻辑，但语法简单)
* [Chain.js](https://wiki.github.com/raid-ox/chain.js) (死链接); [这里有说明](http://samuelmueller.com/2008/10/client-side-templates-using-asp-net-jquery-chain-js-and-taffydb)
* [LightningDOM](http://www.projectrecon.net/LightningDOM/Playground.html)
* [Mootools Template Engine](http://zealdev.wordpress.com/2008/02/22/mootools-template-engine-a-new-approach/)(zealdev.wordpress.com)

XSL

* [XSLTJS](http://johannburkard.de/software/xsltjs/) (实现跨浏览器支持的XSL模板)

E4X

* [E4X for templating](https://developer.mozilla.org/en/E4X_for_templating) (注意E4X已被废弃)

### [标准友好的（自定义属性或者语法，但大部分采用标准兼容的用法）](#1-2)

X/HTML/E4X/XUL 自定义属性和元素

* [Adobe Spry processing instruction attributes](http://labs.adobe.com/technologies/spry/samples/data_region/AttributeComboSample.html)
* [ASP.NET client templates](https://weblogs.asp.net/bleroy/archive/2008/09/02/using-client-templates-part-2-live-bindings.aspx)
* [Seethrough](https://github.com/bard/seethrough_js/wikis) (使用具有名称空间的[E4X](https://developer.mozilla.org/E4X)属性和元素，注意虽然E4X已被废弃)
* [XUL Templates](https://developer.mozilla.org/en-US/docs/en/XUL/Template_Guide) (只支持XUL)

纯JavaScript嵌入在HTML/XML设计逻辑（ASP/JSP/PHP或者大括号{}风格）

* [EJS (嵌入式JS)](http://embeddedjs.com/)
* [PureJSTemplate](http://www.javascriptr.com/2008/06/05/purejstemplate-a-pure-javascript-templating-engine-for-jquery/)
* [mjst](https://code.google.com/p/mjst/)

### [自定义用法](#1-3)

HTML + 大括号{} 使用自定义的设计逻辑

* [ASP.NET 客户端模板](https://weblogs.asp.net/bleroy/archive/2008/09/02/using-client-templates-part-2-live-bindings.aspx)
* [ExtJS中的模板](http://extjs.com/learn/Tutorial:Getting_Started_with_Templates) (死链接，可通过[archive.org](http://web.archive.org/web/20100602135658/http://www.extjs.com/learn/Tutorial:Getting_Started_with_Templates)获取)
* [JavaScriptTemplates](https://code.google.com/p/trimpath/wiki/JavaScriptTemplates)
* [JSmarty](https://code.google.com/p/jsmarty/) (借鉴与[Smarty](http://smarty.php.net/manual/en)，有更多功能和近期更新)
* [jQSmarty: jQuery Smarty Plugin](http://www.balupton.com/sandbox/jquery_smarty/) (死链接) ([这里有介绍](http://www.phpinsider.com/smarty-forum/viewtopic.php?p=47804))
* [JS Repeater](http://jsrepeater.devprog.com/)
* [JTemplates](http://jtemplates.tpython.com/)
* [mjst](https://code.google.com/p/mjst/)
* [Mjt](http://mjtemplate.org/)
* [mustache](https://github.com/janl/mustache.js) (感谢janl)
* [Templates in JQuery](http://plugins.jquery.com/project/jquerytemplate)
* [Templates in Prototype](http://www.prototypejs.org/api/template)
* [Whiskers.js](https://github.com/gsf/whiskers.js)

HTML + 没有名称空间的自定义元素和属性

* [distal](https://code.google.com/p/distal/)
* [mjst](https://code.google.com/p/mjst/)
* [Mjt](http://mjtemplate.org/)
* [google-jstemplate](https://code.google.com/p/google-jstemplate/wiki/HowToUseJsTemplate)

ASP/JSP风格的自定义逻辑，使用<%…%>

* [JavaScript Micro-Templating](http://ejohn.org/blog/javascript-micro-templating/) 语法与(asp|jsp|php)相似
* [BetterJavascriptTemplates](http://blog.markturansky.com/BetterJavascriptTemplates.html)
* [PureJSTemplate](http://www.javascriptr.com/2008/06/05/purejstemplate-a-pure-javascript-templating-engine-for-jquery/)
* [JSONML Browser-Side Templates](http://jsonml.org/BST/)
* [BabaJS](https://github.com/mrharel/babajs)
* [Templates in Prototype](http://www.prototypejs.org/api/template)

## [按特性](#2)

### [通过元素/节点匹配模板，将整个文档翻译到另一个](#2-1)

XSL

* [XSLTJS](http://johannburkard.de/software/xsltjs/) (跨浏览器使用的XSL模板)

