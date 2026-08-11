---
title: "结合bootstrap自定义table列表"
date: "2025-06-17 15:50:38"
slug: "jie-he-bootstrap-zi-ding-yi-table-lie-biao"
categories: ["技术"]
tags: ["Bootstrap", "HTML", "CSS"]
aliases:
  - "/2025/06/17/结合bootstrap自定义table列表/"
  - "/2025/06/17/结合bootstrap自定义table列表.html"
  - "/结合bootstrap自定义table列表/"
  - "/结合bootstrap自定义table列表.html"
  - "/2025/06/17/jie-he-bootstrap-zi-ding-yi-table-lie-biao/"
  - "/2025/06/17/jie-he-bootstrap-zi-ding-yi-table-lie-biao.html"
  - "/jie-he-bootstrap-zi-ding-yi-table-lie-biao.html"
---
使用bootstrap这个方便的web UI框架，方便了自己，少些了很多的代码，至少兼容性方面，我觉的我就不用操心了，呵呵。

看看我自定义的table列表

css代码:

```css
table.smoth{width:100%}
table.smoth thead tr.caption td.item{background-color: #E4E4E4;border:1px solid #ccc}
table.smoth tbody tr.list td{border:1px solid #ccc}
table.smoth tbody tr.list:nth-child(odd) td{background-color:  #fff}
table.smoth tbody tr.list:nth-child(even) td{background-color: #F2F2F2}
```

html代码：

```html
<div class="table">
	<table class='smoth' >
		<thead>
			<tr class='caption'>
				<td class='item'>电视剧名称</td>
				<td class='item'>上线日期</td>
				<td class='item'>ITV状态</td>
				<td class='item'>导演</td>
				<td class='item'>编剧</td>
				<td class='item'>主演</td>
			</tr>
		</thead>
		<tbody>
			<?php for($i = 0; $i < 10; $i++):?>
			<tr class='list'>
				<td>咱俩的事</td>
				<td>2013-01-13</td>
				<td>是</td>
				<td>David Zhang</td>
				<td>David</td>
				<td>Zhang</td>
			</tr>
			<?php endfor;?>
		</tbody>
	</table>
</div>
```

加入了一点php代码，实则是一个简单的循环

图片展示

![](http://g.hiphotos.bdimg.com/album/s%3D1400%3Bq%3D90/sign=46493e1a64380cd7e21ea6e991749645/43a7d933c895d1435b7c258972f082025aaf0716.jpg)
