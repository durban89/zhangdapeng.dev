---
title: "Blocksit 瀑布流插件 实现瀑布流数据 异步加载（无限加载）"
date: "2025-06-27 10:59:59"
slug: "blocksit-pu-bu-liu-cha-jian-shi-xian-pu-bu-liu-shu-ju-yi-bu-jia-zai-wu-xian-jia-zai"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/Blocksit-瀑布流插件-实现瀑布流数据-异步加载（无限加载）/"
  - "/2025/06/27/Blocksit-瀑布流插件-实现瀑布流数据-异步加载（无限加载）.html"
  - "/Blocksit-瀑布流插件-实现瀑布流数据-异步加载（无限加载）/"
  - "/Blocksit-瀑布流插件-实现瀑布流数据-异步加载（无限加载）.html"
  - "/2025/06/27/Blocksit-瀑布流插件-实现瀑布流数据-异步加载-无限加载/"
  - "/2025/06/27/Blocksit-瀑布流插件-实现瀑布流数据-异步加载-无限加载.html"
  - "/2025/06/27/blocksit-pu-bu-liu-cha-jian-shi-xian-pu-bu-liu-shu-ju-yi-bu-jia-zai-wu-xian-jia-zai/"
  - "/2025/06/27/blocksit-pu-bu-liu-cha-jian-shi-xian-pu-bu-liu-shu-ju-yi-bu-jia-zai-wu-xian-jia-zai.html"
  - "/blocksit-pu-bu-liu-cha-jian-shi-xian-pu-bu-liu-shu-ju-yi-bu-jia-zai-wu-xian-jia-zai.html"
---
Blocksit 瀑布流插件 实现瀑布流数据 异步加载（无限加载）

```html
<div style="width:1000px; overflow:hidden; margin:0 auto">    
    <div class="kppcl" style="width:1008px; position:relative" id="kppcl">

        <div class="kppcld">
            <div class="kppcld_t">
                <div class="kpic"><a href='{#url_reset("activity/detail","id_{#$item.id#}")#}'><img src="{#$item.logo#}" width="322" /></a></div>
                <div class="kname"><a href='{#url_reset("activity/detail","id_{#$item.id#}")#}'>{#$item.title#}</a></div>
                <div class="kinfor">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <th>时&nbsp;&nbsp;&nbsp;&nbsp;间：</th>
                            <td>{#$item.start_date#}-{#$item.end_date#}</td>
                        </tr>
                        <tr>
                            <th>地&nbsp;&nbsp;&nbsp;&nbsp;点：</th>
                            <td>{#$item.area_name#}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="kppcld_b"></div>
        </div>

        <div class="kppcld">
            <div class="kppcld_t">
                <div class="kpic"><a href='{#url_reset("activity/detail","id_{#$item.id#}")#}'><img src="{#$item.logo#}" width="322" /></a></div>
                <div class="kname"><a href='{#url_reset("activity/detail","id_{#$item.id#}")#}'>{#$item.title#}</a></div>
                <div class="kinfor">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <th>时&nbsp;&nbsp;&nbsp;&nbsp;间：</th>
                            <td>{#$item.start_date#}-{#$item.end_date#}</td>
                        </tr>
                        <tr>
                            <th>地&nbsp;&nbsp;&nbsp;&nbsp;点：</th>
                            <td>{#$item.area_name#}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="kppcld_b"></div>
        </div>

        <div class="kppcld">
            <div class="kppcld_t">
                <div class="kpic"><a href='{#url_reset("activity/detail","id_{#$item.id#}")#}'><img src="{#$item.logo#}" width="322" /></a></div>
                <div class="kname"><a href='{#url_reset("activity/detail","id_{#$item.id#}")#}'>{#$item.title#}</a></div>
                <div class="kinfor">
                    <table width="100%" border="0" cellspacing="0" cellpadding="0">
                        <tr>
                            <th>时&nbsp;&nbsp;&nbsp;&nbsp;间：</th>
                            <td>{#$item.start_date#}-{#$item.end_date#}</td>
                        </tr>
                        <tr>
                            <th>地&nbsp;&nbsp;&nbsp;&nbsp;点：</th>
                            <td>{#$item.area_name#}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="kppcld_b"></div>
        </div>

    </div>

    <div id="page" style="display: none">
        <div class="pages"><b class="page_icon">上一页</b><b>1</b><a href="?p=2">2</a><a href="?p=2" class="nextprev" rel="2">下一页</a></div>
    </div>

</div>
<script src="/js/blocksit.min.js"></script>
<script language="javascript" type="text/javascript">
    $(window).load( function() {
        $('#kppcl').BlocksIt({
            numOfCol: 3,
            offsetX: 5,
            offsetY: 5
        });
    });

    var current_p = 0;
    //滚动
    $(window).scroll(function(){
        // 当滚动到最底部以上100像素时， 加载新内容
        if ($(document).height() - $(this).scrollTop() - $(this).height()<100) {
            ajax_load_data();
        }
    });
    function ajax_load_data(){
        var next_p = $('#page').find('.nextprev').attr('rel');
        if(next_p && next_p != current_p){
            console.log('nextpage = '+next_p);
            current_p = next_p;

            $.ajax({
                url:'{#url_reset("request/front/ajax","","php")#}',
                data:{'act':'ajax_forum','p':next_p},
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
                            $('#kppcl').append(data.html).BlocksIt('reload');
                        }

                        if(data.pages_str){
                            $('#page').html(data.pages_str);
                        }
                    }
                }
            });
        }
    }
</script>
```

参考文章：

http://my.oschina.net/Rayn/blog/123938


