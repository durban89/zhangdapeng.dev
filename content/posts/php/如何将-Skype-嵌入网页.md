---
title: "如何将 Skype 嵌入网页"
date: "2025-06-30 11:48:54"
slug: "ru-he-jiang-skype-qian-ru-wang-ye"
categories: ["技术"]
tags: ["Skype", "JavaScript"]
aliases:
  - "/2025/06/30/如何将-Skype-嵌入网页/"
  - "/2025/06/30/如何将-Skype-嵌入网页.html"
  - "/如何将-Skype-嵌入网页/"
  - "/如何将-Skype-嵌入网页.html"
  - "/2025/06/30/ru-he-jiang-skype-qian-ru-wang-ye/"
  - "/2025/06/30/ru-he-jiang-skype-qian-ru-wang-ye.html"
  - "/ru-he-jiang-skype-qian-ru-wang-ye.html"
---
第一次使用，skype嵌入网页，还真是没有类似微博那么简单，不过功能很强大

Html代码：

```html
<div id="skype" style="position:absolute;text-align:right;top:200px;width:100%">
<a href="skype:david_tompeng?call">
    <img src="http://mystatus.skype.com/smallclassic/david_tompeng" style="border: none;" alt="My status" />
</a>
</div>
```

不能浮动，加个js

```html
<script>
    $.fn.smartFloat = function() {
        var position = function(element) {
            var top = element.position().top; //当前元素对象element距离浏览器上边缘的距离
            var pos = element.css("position"); //当前元素距离页面document顶部的距离
            $(window).scroll(function() { //侦听滚动时
                var scrolls = $(this).scrollTop();
                if (scrolls > top) { //如果滚动到页面超出了当前元素element的相对页面顶部的高度
                    if (window.XMLHttpRequest) { //如果不是ie6
                        element.css({ //设置css
                            position: "fixed", //固定定位,即不再跟随滚动
                            top: 200 //距离页面顶部为0
                        }).addClass("shadow"); //加上阴影样式.shadow
                    } else { //如果是ie6
                        element.css({
                            top: scrolls  //与页面顶部距离
                        });
                    }
                }else {
                    element.css({ //如果当前元素element未滚动到浏览器上边缘，则使用默认样式
                        position: pos,
                        top: top
                    }).removeClass("shadow");//移除阴影样式.shadow
                }
            });
        };
        return $(this).each(function() {
            position($(this));
        });
    };
 
    $(function(){
        $("#skype").smartFloat();
    })
</script>
```

不要忘记引入检测代码

```html
<script type="text/javascript" src="http://download.skype.com/share/skypebuttons/js/skypeCheck.js"></script>
```

