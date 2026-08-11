---
title: "jQuery获取和设置Select选项方法"
date: "2025-06-17 15:51:13"
slug: "jquery-huo-qu-he-she-zhi-select-xuan-xiang-fang-fa"
categories: ["技术"]
tags: ["jQuery", "JavaScript"]
aliases:
  - "/2025/06/17/jQuery获取和设置Select选项方法/"
  - "/2025/06/17/jQuery获取和设置Select选项方法.html"
  - "/jQuery获取和设置Select选项方法/"
  - "/jQuery获取和设置Select选项方法.html"
  - "/2025/06/17/jquery-huo-qu-he-she-zhi-select-xuan-xiang-fang-fa/"
  - "/2025/06/17/jquery-huo-qu-he-she-zhi-select-xuan-xiang-fang-fa.html"
  - "/jquery-huo-qu-he-she-zhi-select-xuan-xiang-fang-fa.html"
---
获取Select ：  
获取select 选中的 text:

```javascript
$("#select_id”).find("option:selected”).text();
```

获取select选中的 value:

```javascript
$("#select_id option:selected”).val();
($("#select_id”).val();这个方法是错误的)
```

获取select选中的索引:

```javascript
$("#select_id ").get(0).selectedIndex;
```

设置select:  
设置select 选中的索引：

```javascript
$("#select_id ").get(0).selectedIndex=index;//index为索引值
```

设置select 选中的value：

```javascript
$("#select_id ").attr("value”,”Normal");
$("#select_id ").val("Normal”);
$("#select_id ").get(0).value = value;
```

设置select 选中的text:

```javascript
var count=$("#select_id ").find("option”).length;
for(var i=0;i<count;i++)
{           
	if($("#select_id ").get(0).options[i].text == text)
	{
		$("#select_id ").get(0).options[i].selected = true;
		break;
	}
}
```

select根据value默认选中

```javascript
$("#SelectID option[value='selectValue']").attr("selected”,true)
```

清空 Select:

```javascript
$("#select_id ").empty();
$("#veg1″).find("option”).clone().appendTo("#veg2″);   添加另一个select option
$("#veg2″).get(0).selectedIndex=2; 设置选中项
```
