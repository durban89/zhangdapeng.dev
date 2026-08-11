---
title: "结合jQuery.lazyload和masonry实现瀑布流"
date: "2025-06-27 14:14:30"
slug: "jie-he-jquerylazyload-he-masonry-shi-xian-pu-bu-liu"
categories: ["技术"]
tags: ["jQuery", "JavaScript"]
aliases:
  - "/2025/06/27/结合jQuery.lazyload和masonry实现瀑布流/"
  - "/2025/06/27/结合jQuery.lazyload和masonry实现瀑布流.html"
  - "/结合jQuery.lazyload和masonry实现瀑布流/"
  - "/结合jQuery.lazyload和masonry实现瀑布流.html"
  - "/2025/06/27/结合jQuery-lazyload和masonry实现瀑布流/"
  - "/2025/06/27/结合jQuery-lazyload和masonry实现瀑布流.html"
  - "/2025/06/27/jie-he-jquerylazyload-he-masonry-shi-xian-pu-bu-liu/"
  - "/2025/06/27/jie-he-jquerylazyload-he-masonry-shi-xian-pu-bu-liu.html"
  - "/jie-he-jquerylazyload-he-masonry-shi-xian-pu-bu-liu.html"
---
结合jQuery.lazyload和masonry实现瀑布流

这里主要是使用jQuery.lazyload配合masonry实现瀑布流的重新排列，有时候网站的速度慢，图片加载慢，获取不到图片的

宽度和高度，所以使用lazyload可以在图片加载完之后，进行瀑布流的重新排列。

实现方法如下：

```js
/**
 * 自动刷新
 * @type {*|jQuery|HTMLElement}
 */
var $container = $('#main');
$container.imagesLoaded( function(){
    $container.masonry({
        itemSelector : '.item',
        columnWidth:205,
	    gutterWidth:10,
        isAnimated: true
    });
});
var pre_href;
//滚动
$(window).scroll(function(){
    // 当滚动到最底部以上100像素时， 加载新内容
    if ($(document).height() - $(this).scrollTop() - $(this).height()<100) {
        ajax_load_data();
    }
});

function ajax_load_data(){
    var href = $('#page-nav').find('.nextprev').attr('href');
    if(href && href != pre_href){
        console.log('href = '+href);
        pre_href = href;

        $.ajax({
            url:href,//获取元素列表的地址
            data:{'act':'ajax_wap_index'},
            dataType:'json',
            type:'post',
            beforeSend:function(){
                show_loading_body();
            },
            complete:function(){
                show_loading_body();
            },
            success:function(data){
                if(data.status != undefined && data.status == 'ok'){
                    if(data.html){
                        var $boxes = $( data.html );
                        $container.append( $boxes ).masonry("appended", $boxes, true);//追加元素
                        $container.imagesLoaded(function () {
                            $container.masonry();
                        });//加载完图片后，会实现自动重新排列。【这里是重点】
                    }

                    if(data.str_pages){
                        $('#page-nav').html(data.str_pages);//设置下一个分页的地址。【可以自己补充】
                    }
                }
            }
        });
    }
}
```
