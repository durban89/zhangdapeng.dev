---
title: "百度分享插件-分享按钮自定义，bShare分享插件-分享按钮自定义"
date: "2025-06-27 11:00:05"
slug: "bai-du-fen-xiang-cha-jian-fen-xiang-an-niu-zi-ding-yi-bshare-fen-xiang-cha-jian-fen-xiang-an-niu-zi-ding-yi"
categories: ["技术"]
tags: ["插件"]
aliases:
  - "/2025/06/27/百度分享插件-分享按钮自定义，bShare分享插件-分享按钮自定义/"
  - "/2025/06/27/百度分享插件-分享按钮自定义，bShare分享插件-分享按钮自定义.html"
  - "/百度分享插件-分享按钮自定义，bShare分享插件-分享按钮自定义/"
  - "/百度分享插件-分享按钮自定义，bShare分享插件-分享按钮自定义.html"
  - "/2025/06/27/百度分享插件-分享按钮自定义-bShare分享插件-分享按钮自定义/"
  - "/2025/06/27/百度分享插件-分享按钮自定义-bShare分享插件-分享按钮自定义.html"
  - "/2025/06/27/bai-du-fen-xiang-cha-jian-fen-xiang-an-niu-zi-ding-yi-bshare-fen-xiang-cha-jian-fen-xia/"
  - "/2025/06/27/bai-du-fen-xiang-cha-jian-fen-xiang-an-niu-zi-ding-yi-bshare-fen-xiang-cha-jian-fen.html"
  - "/bai-du-fen-xiang-cha-jian-fen-xiang-an-niu-zi-ding-yi-bshare-fen-xiang-cha-jian-fen-xiang-an-n.html"
---
百度分享插件-分享按钮自定义

```html
<div class="bsync-custom icon-medium-blue">
    <a title="一键分享到各大微博和社交网络" class="bshare-bsync" onclick="javascript:bShare.more(event);return false;"></a>
</div>
<a class="bshareDiv" href="http://www.bshare.cn/share">分享按钮</a>
<script 
        type="text/javascript" 
        charset="utf-8" 
        src="http://static.bshare.cn/b/buttonLite.js#uuid=773faa5d-cee1-4696-9c99-d400a5d7a1c1&amp;style=999&amp;img=http%3A%2F%2Fjingguan.365use.com%2Fwap%2Fimages%2Frfhui1.jpg&amp;h=20&amp;w=23&amp;mdiv=0&amp;pop=-1&amp;bp=qqmb,bsharesync,sinaminiblog,qzone,189share,sohuminiblog,renren,xinhuamb,tianya,shouji,ifengmb,neteasemb,qqxiaoyou,kaixin001,weixin,douban,qqim">
</script>
```

bShare分享插件-分享按钮自定义

```css
<style>
    .userStyle{
        width:100%;
        height:30px;
        display:block;
    }
    .userStyle span.bds_more{
        background:url("/wap/images/rfhui1.jpg") no-repeat scroll 0 5px rgba(0, 0, 0, 0) !important;
    }
</style>
<div class="userStyle">
    <!-- Baidu Button BEGIN -->
    <div id="bdshare" class="bdshare_t bds_tools get-codes-bdshare">
        <span class="bds_more"></span>
    </div>
    <script type="text/javascript" id="bdshare_js" data="type=tools" ></script>
    <script type="text/javascript" id="bdshell_js"></script>
    <script type="text/javascript">
        document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000);
    </script>
    <!-- Baidu Button END -->
</div>
```
