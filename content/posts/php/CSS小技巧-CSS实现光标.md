---
title: "CSS小技巧 - CSS实现光标"
date: "2025-07-11 10:40:48"
slug: "css-xiao-ji-qiao-css-shi-xian-guang-biao"
categories: ["技术"]
tags: ["CSS"]
aliases:
  - "/2025/07/11/CSS小技巧-CSS实现光标/"
  - "/2025/07/11/CSS小技巧-CSS实现光标.html"
  - "/CSS小技巧-CSS实现光标/"
  - "/CSS小技巧-CSS实现光标.html"
  - "/2025/07/11/css-xiao-ji-qiao-css-shi-xian-guang-biao/"
  - "/2025/07/11/css-xiao-ji-qiao-css-shi-xian-guang-biao.html"
  - "/css-xiao-ji-qiao-css-shi-xian-guang-biao.html"
---
原理使用css的伪类':before'和':after'

如果想要光标在内容的后面

```css
.class:before {
	content: ''
}

.class:after {
	content: '';
	border-right: 2px solid #ffd500;
	height: 50%;
	opacity: 1;
	animation: focus .7s forwards infinite;
}

@keyframes focus {
	from {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}
```

如果想要光标在内容的前面

```css
.class:before {
	content: ''
	border-right: 2px solid #ffd500;
	height: 50%;
	opacity: 1;
	animation: focus .7s forwards infinite;
}

.class:after {
	content: '';
}

@keyframes focus {
	from {
		opacity: 1;
	}

	to {
		opacity: 0;
	}
}
```
