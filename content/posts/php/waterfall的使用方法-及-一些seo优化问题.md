---
title: "waterfall的使用方法 及 一些seo优化问题"
date: "2025-06-26 11:15:45"
slug: "waterfall-de-shi-yong-fang-fa-ji-yi-xie-seo-you-hua-wen-ti"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/26/waterfall的使用方法-及-一些seo优化问题/"
  - "/2025/06/26/waterfall的使用方法-及-一些seo优化问题.html"
  - "/waterfall的使用方法-及-一些seo优化问题/"
  - "/waterfall的使用方法-及-一些seo优化问题.html"
  - "/2025/06/26/waterfall-de-shi-yong-fang-fa-ji-yi-xie-seo-you-hua-wen-ti/"
  - "/2025/06/26/waterfall-de-shi-yong-fang-fa-ji-yi-xie-seo-you-hua-wen-ti.html"
  - "/waterfall-de-shi-yong-fang-fa-ji-yi-xie-seo-you-hua-wen-ti.html"
---
waterfall的版本很多，我这里只使用了其中的一个版本，下载地址是在这里<http://wlog.cn/waterfall/>

具体的使用方法很简单，博文里面也有介绍的，这里我简答的贴出自己的使用方法。

```javascript
<script>
$(function(){
    $('#container').waterfall({
        itemCls: 'item',
        colWidth: 230,
        gutterWidth: 15,
        gutterHeight: 15,
        checkImagesLoaded: true,
        dataType: 'html',
        path: function(page) {
            return '/ajax/?page=' + page;
        },
        callbacks:{
            /*
             * loadingError
             * @param {String} xhr , "end" "error"
             */
            loadingError: function($message, xhr) {
                $message.html('');
            },
            loadingStart:function($message, xhr){
                $message.html('');
            }
        }
    });
    $('.container-block').css({'visibility':'visible'})
});
</script>
```

不要忘记引入js文件

关于这中瀑布流的方式，对页面的seo是不是很好的，但是也是有解决方案的，第一种就是，页面初始化的时候，先展示500条数据。第二种方法是，页面加上侧边栏，进行必要的导航。

