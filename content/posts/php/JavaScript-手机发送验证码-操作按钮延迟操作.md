---
title: "JavaScript 手机发送验证码 操作按钮延迟操作"
date: "2025-06-27 10:59:54"
slug: "javascript-shou-ji-fa-song-yan-zheng-ma-cao-zuo-an-niu-yan-chi-cao-zuo"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/JavaScript-手机发送验证码-操作按钮延迟操作/"
  - "/2025/06/27/JavaScript-手机发送验证码-操作按钮延迟操作.html"
  - "/JavaScript-手机发送验证码-操作按钮延迟操作/"
  - "/JavaScript-手机发送验证码-操作按钮延迟操作.html"
  - "/2025/06/27/javascript-shou-ji-fa-song-yan-zheng-ma-cao-zuo-an-niu-yan-chi-cao-zuo/"
  - "/2025/06/27/javascript-shou-ji-fa-song-yan-zheng-ma-cao-zuo-an-niu-yan-chi-cao-zuo.html"
  - "/javascript-shou-ji-fa-song-yan-zheng-ma-cao-zuo-an-niu-yan-chi-cao-zuo.html"
---
Js 手机发送验证码 操作按钮延迟操作

实例代码记录：

```javascript
<script type="text/javascript">
    function start_sms_button(obj){
        var count = 1 ;
        var sum = 30;
        var i = setInterval(function(){
            if(count > 10){
                obj.attr('disabled',false);
                obj.val('发送验证码');
                clearInterval(i);
            }else{
                obj.val('剩余'+parseInt(sum - count)+'秒');
            }
            count++;
        },1000);
    }

    $(function(){
        //发送验证码
        $('#send_sms').click(function(){
            var phone_obj = $('input[name="phone"]');
            var send_obj = $('input#send_sms');
            var val = phone_obj.val();
            if(val){
                if(IsMobile(val)){
                    send_obj.attr('disabled',"disabled");
                    //30秒后重新启动发送按钮
                    start_sms_button(send_obj);
                    $.ajax({
                        url:'{#url_reset("index/sms")#}',
                        data:{'mobile':val},
                        dataType:'json',
                        type:'post',
                        beforeSend:function(){
                            show_loading_body();
                        },
                        complete:function(){
                            show_loading_body();
                        },
                        success:function(data){
                            if(data.status!=undefined && (data.status == 'ok' || data.status == 'error')){
                                showMsg(data.msg);
                            }
                        }
                    });
                }else{
                    showMsg("手机号的格式错误");
                }
            }else{
                showMsg('手机号不能为空');
            }
        });
    });
</script>
```

