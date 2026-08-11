---
title: "JavaScript jquery-form-validate 异步提交表单和进行后台验证的操作方式"
date: "2025-06-27 10:59:31"
slug: "javascript-jquery-form-validate-yi-bu-ti-jiao-biao-dan-he-jin-xing-hou-tai-yan-zheng-de-cao-zuo-fang-shi"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/JavaScript-jquery-form-validate-异步提交表单和进行后台验证的操作方式/"
  - "/2025/06/27/JavaScript-jquery-form-validate-异步提交表单和进行后台验证的操作方式.html"
  - "/JavaScript-jquery-form-validate-异步提交表单和进行后台验证的操作方式/"
  - "/JavaScript-jquery-form-validate-异步提交表单和进行后台验证的操作方式.html"
  - "/2025/06/27/javascript-jquery-form-validate-yi-bu-ti-jiao-biao-dan-he-jin-xing-hou-tai-yan-zheng-de/"
  - "/2025/06/27/javascript-jquery-form-validate-yi-bu-ti-jiao-biao-dan-he-jin-xing-hou-tai-yan-zhen.html"
  - "/javascript-jquery-form-validate-yi-bu-ti-jiao-biao-dan-he-jin-xing-hou-tai-yan-zheng-de-cao-zu.html"
---
一般来说，表单的异步验证，要不就自己写一个，这里使用jquery validation表单验证，实现起来很简单的

先看下样式表和js脚本

```html
<style>
    label.error{
        display: none;
        width: 0px;
    }
    .login .log input.error, .login .log select.error,.login .log textarea.error{
        border: 2px solid red;
        background-color: #FFFFD5;
        margin: 0px;
        color: red;
    }
</style>
<script src="/js/jquery-validation/dist/jquery.validate.js" type="text/javascript"></script>
<script src="/js/jquery-validation/lib/jquery.form.js" type="text/javascript"></script>
<script type="text/javascript">
    $(function(){
        //去掉提示
        jQuery.validator.messages.required = "";
        $('form#login').validate({
            borderColorOnError : '#FFF',
            invalidHandler: function(e, validator) {
                //错误个数
                var errors = validator.numberOfInvalids();
                if (errors) {
                    $("label.error").css('display',"none");
                } else {
                    $("label.error").hide();
                }
            },
            submitHandler: function(form) {
                $(form).ajaxSubmit({
                    beforeSend:function(){
                        show_loading_body();
                    },
                    complete:function(){
                        show_loading_body();
                    },
                    success:function(data){
                        data = JSON.parse(data);
                        if(data.url != undefined && data.status != undefined && data.status == 'ok'){
                            $('.jgCode').show();
                        }else{

                        }
                    }

                });
            }

        });
    });
</script>
```

跟ajax的使用方式基本上是一致的

```js
function show_loading_body() {
    if ($("#layer_loading").length > 0) {
        $("#layer_loading").css("display") == 'none' ? $("#layer_loading").css(
                'display', '') : $("#layer_loading").css('display', 'none');
    } else {
        var yScroll = document.documentElement.scrollTop;
        var screenheight = document.documentElement.clientHeight;
        var t = yScroll + screenheight - 240;
        //alert(t);
        //if (t > document.body.clientHeight) {
        //    t = document.body.clientHeight;
        //}
        $("body")
                .append(
                '<div id="layer_loading" style="position:absolute;z-index:1001;" id="layer_loading"><img src="/images/public/load.gif" title="loading……" alt="loading……"/> loading……</div>');
        $("#layer_loading").css("left",
                (($(document).width()) / 2 - (parseInt(200) / 2)) + "px").css(
                "top", t + "px");
        $("#layer_loading").show();
    }
}
```

后台的验证，我这里说一下我的验证方式。结合ajax和非ajax的一个整合操作（PHP）

```php
if(isset($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest'){
    echo json_encode(array('status'=>'dsd'));
    exit;
}else{
    if(!ckgdcode($checkcode)){
        redirect ( "您输入的验证码有误！请返回重新登陆！", url_reset('login')."?url=".$return_url );
        exit;

    }
}
```

这样子的话，就不需要在另外传递参数来判断了。

