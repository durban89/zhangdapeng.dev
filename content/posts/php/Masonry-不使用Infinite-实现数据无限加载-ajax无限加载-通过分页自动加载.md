---
title: "Masonry 不使用Infinite 实现数据无限加载 ajax无限加载【通过分页自动加载】"
date: "2025-06-27 11:00:02"
slug: "masonry-bu-shi-yong-infinite-shi-xian-shu-ju-wu-xian-jia-zai-ajax-wu-xian-jia-zai-tong-guo-fen-ye-zi-dong-jia-zai"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/Masonry-不使用Infinite-实现数据无限加载-ajax无限加载【通过分页自动加载】/"
  - "/2025/06/27/Masonry-不使用Infinite-实现数据无限加载-ajax无限加载【通过分页自动加载】.html"
  - "/Masonry-不使用Infinite-实现数据无限加载-ajax无限加载【通过分页自动加载】/"
  - "/Masonry-不使用Infinite-实现数据无限加载-ajax无限加载【通过分页自动加载】.html"
  - "/2025/06/27/Masonry-不使用Infinite-实现数据无限加载-ajax无限加载-通过分页自动加载/"
  - "/2025/06/27/Masonry-不使用Infinite-实现数据无限加载-ajax无限加载-通过分页自动加载.html"
  - "/2025/06/27/masonry-bu-shi-yong-infinite-shi-xian-shu-ju-wu-xian-jia-zai-ajax-wu-xian-jia-zai-tong-/"
  - "/2025/06/27/masonry-bu-shi-yong-infinite-shi-xian-shu-ju-wu-xian-jia-zai-ajax-wu-xian-jia-zai-t.html"
  - "/masonry-bu-shi-yong-infinite-shi-xian-shu-ju-wu-xian-jia-zai-ajax-wu-xian-jia-zai-tong-guo-fen.html"
---
masonry 不使用Infinite 实现数据无限加载 ajax无限加载【通过分页自动加载】

```html
<!-- 引入文件 -->
<script type="text/javascript" src="/wap/js/masonry/jquery.masonry.min.js"></script>
<script type="text/javascript" src="/wap/js/masonry/js/jquery.infinitescroll.min.js"></script>

<div class="bg_e7">
    <div class="p4_3">
        <ul class="ul_mt4" id="masonry">
            {#foreach $list as $item#}<!-- foreach循环 多个DOM元素 -->
            <li class="masonry-item">
                <div class="dierg"></div>
                <div class="p04">
                    <div>
                        <a href='{#wap_url_reset("{#$item.mark#}/show","id/{#$item.oid#}")#}'>
                            <img width="143" src="{#$item.cover#}" />
                        </a>
                    </div>
                    <div class="p3_5">
                        <div class="h24_jc_c666">
                            <a href='{#wap_url_reset("{#$item.mark#}/show","id/{#$item.oid#}")#}'>
                                {#$item.o_title|cut_str:7#}
                            </a>
                        </div>
                        <div class="h20_c666">
                            <a href='{#wap_url_reset("{#$item.mark#}/show","id/{#$item.oid#}")#}'>
                                {#$item.o_content|cut_str_with_string:7#}
                            </a>
                        </div>
                        <div class="h22_lh20">
                            <div class='{#if $item.mark == "news"#}zx_img1{#elseif $item.mark == "case"#}anli_1{#elseif $item.mark == "activity"#}fbg1_bg{#/if#}'>
                                <a href='{#wap_url_reset("{#$item.mark#}/index")#}'>
                                    {#$wapcategory[$item.cid].cat_name#}
                                </a>
                            </div>
                            <div class="fr_cb2">
                                {#if $item.ccid#}
                                <strong class="color3">/</strong> <a href='{#wap_url_reset("{#$item.mark#}/index","cid/{#$item.cid#}-ccid/{#$item.ccid#}")#}'>{#$wapcategory[$item.ccid].cat_name#}</a>
                                {#/if#}
                            </div>
                        </div>
                    </div>
                </div>
                <div class="diyig"></div>
            </li>
            {#/foreach#}
        </ul>
    </div>

    <div id="page-nav" style="display: none">
        <div class="pages"><b class="page_icon">上一页</b><b>1</b><a href="?p=2">2</a><a href="?p=2" class="nextprev" rel="2">下一页</a></div>
    </div>

    <div class="h100_cboth"></div>
    <div class="min_w640"><div class="pdwei_img"><img src="/wap/images/wfd_img.jpg" width="100%" /><div class="dwenimg"><img src="/wap/images/gbi.png" /></div></div></div>
</div>
<script>
    $(function(){
        var $container = $('#masonry');
        $container.imagesLoaded( function(){
            $container.masonry({
                itemSelector : '.masonry-item',
                gutterWidth : 2,
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
                    url:href,
                    data:{'act':'ajax_wap_news'},
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
                                $container.append( $boxes ).masonry( 'appended', $boxes);
                            }

                            if(data.str_pages){
                                $('#page-nav').html(data.str_pages);
                            }
                        }
                    }
                });
            }
        }
    });
</script>
```

