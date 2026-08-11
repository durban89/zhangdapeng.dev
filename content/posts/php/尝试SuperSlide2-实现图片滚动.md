---
title: "尝试SuperSlide2,实现图片滚动"
date: "2025-06-27 14:14:33"
slug: "chang-shi-superslide2-shi-xian-tu-pian-gun-dong"
categories: ["技术"]
tags: ["SuperSlide", "JavaScript"]
aliases:
  - "/2025/06/27/尝试SuperSlide2,实现图片滚动/"
  - "/2025/06/27/尝试SuperSlide2,实现图片滚动.html"
  - "/尝试SuperSlide2,实现图片滚动/"
  - "/尝试SuperSlide2,实现图片滚动.html"
  - "/2025/06/27/尝试SuperSlide2-实现图片滚动/"
  - "/2025/06/27/尝试SuperSlide2-实现图片滚动.html"
  - "/2025/06/27/chang-shi-superslide2-shi-xian-tu-pian-gun-dong/"
  - "/2025/06/27/chang-shi-superslide2-shi-xian-tu-pian-gun-dong.html"
  - "/chang-shi-superslide2-shi-xian-tu-pian-gun-dong.html"
---
尝试SuperSlide2,实现图片滚动，感觉很强大，这里只是简单的演示其中一种类型，想看更多类型的话，可以去http://www.superslide2.com 查看，这里贴一下自己演示的代码，期望对使用的朋友所有启发，我这里是结合了两个例子实现的

css代码：

```css
.focus-item ul li.item{
    text-align: center;
}
.scroll-area .prev,.scroll-area .next{
    position: absolute;
    bottom: 590px;
    width: 29px;
    height: 64px;
    opacity: 0.6;
    overflow: hidden;
    display: none;
    text-indent: -999px;
    border: medium none;
    background: url('/images/arrowLR.png') no-repeat scroll 0% 0% transparent;
}
.scroll-area .prev{
    left: 0px;
    background-position: -50px 0px;
}
.scroll-area .next{
    right: 0px;
}
.scroll-area .bdOn .prev,.scroll-area .bdOn .next{
    display: block;
}

.scroll-area .focus-hd{
    /*width: 832px;*/
    /*left: 60px;*/
    /*position: absolute;*/
    /*height: 100px;*/
    /*overflow: hidden;*/
    left: 63px;
    position: absolute;
}

.focus-hd .sNext, .focus-hd .sPrev{
    float: left;
    display: block;
    width: 14px;
    height: 47px;
    text-indent: -9999px;
    background: url('/images/sprites1008.png') no-repeat scroll 0px -3046px transparent;
}
.focus-hd .sNext{
    background-position: 0px -2698px;
}

.focus-hd .show_bottom_nav {
    float: left;
    margin: 0px 6px;
    display: inline;
    width: 832px;
    overflow: hidden;
}
.focus-hd .show_bottom_nav ul li{
    margin-left:15px;
}
```

html演示代码：

```html
<div id="" class="scroll-area">
    <div class="focus-item">
        <ul>
            <li data-bottom-thumb="/attachments/news_gallery/20140528162328_454.jpg" class="item" data-text-id="#thumbTxt1">
                <img src="/attachments/news_gallery/20140528162328_454.jpg" alt="标题1" />
            </li>
            <li data-bottom-thumb="/attachments/news_gallery/20140528162328_733.jpg" class="item" data-text-id="#thumbTxt2">
                <img src="/attachments/news_gallery/20140528162328_733.jpg" alt="标题2" />
            </li>
        </ul>
        <a class="prev" href="javascript:void(0)"></a>
        <a class="next" href="javascript:void(0)"></a>
    </div>


    <div class="focus-hd" style="">
        <a class="sPrev prevStop" href="javascript:void(0)">←</a>
        <div class="show_bottom_nav">
            <ul>
                <li data-bottom-thumb="/attachments/news_gallery/20140528162328_454.jpg" class="item" data-text-id="#thumbTxt1" style="float: left">
                    <img style="width: 150px;height: 100px" src="/attachments/news_gallery/20140528162328_454.jpg" alt="标题1" />
                </li>
                <li data-bottom-thumb="/attachments/news_gallery/20140528162328_733.jpg" class="item" data-text-id="#thumbTxt2" style="float: left">
                    <img style="width: 150px;height: 100px" src="/attachments/news_gallery/20140528162328_733.jpg" alt="标题2" />
                </li>
            </ul>
        </div>
        <a class="sNext" href="javascript:void(0)">→</a>
    </div>
</div>
```

js脚本代码：

```js
jQuery(".scroll-area").slide({titCell:'.focus-hd li',mainCell:'.focus-item ul',delayTime:0,trigger:0,autoPlay:true});
jQuery(".scroll-area .focus-item").hover(function(){jQuery(this).addClass("bdOn")},function(){jQuery(this).removeClass('bdOn')});
//小标签的导航
jQuery(".scroll-area .show_bottom_nav").slide({ mainCell:"ul",delayTime:100,vis:5,effect:"left",autoPage:true,prevCell:".sPrev",nextCell:".sNext" });
```


