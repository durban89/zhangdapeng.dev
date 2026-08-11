---
title: "JavaScript jquery-form-validate html标签中实现 验证信息的修改  messages"
date: "2025-06-27 10:59:28"
slug: "javascript-jquery-form-validate-html-biao-qian-zhong-shi-xian-yan-zheng-xin-xi-de-xiu-gai-messages"
categories: ["技术"]
tags: ["JavaScript"]
aliases:
  - "/2025/06/27/JavaScript-jquery-form-validate-html标签中实现-验证信息的修改-messages/"
  - "/2025/06/27/JavaScript-jquery-form-validate-html标签中实现-验证信息的修改-messages.html"
  - "/JavaScript-jquery-form-validate-html标签中实现-验证信息的修改-messages/"
  - "/JavaScript-jquery-form-validate-html标签中实现-验证信息的修改-messages.html"
  - "/2025/06/27/javascript-jquery-form-validate-html-biao-qian-zhong-shi-xian-yan-zheng-xin-xi-de-xiu-g/"
  - "/2025/06/27/javascript-jquery-form-validate-html-biao-qian-zhong-shi-xian-yan-zheng-xin-xi-de-x.html"
  - "/javascript-jquery-form-validate-html-biao-qian-zhong-shi-xian-yan-zheng-xin-xi-de-xiu-gai-mess.html"
---
示例代码：

```html
<dl class="element">
    <dt>E-mail：</dt>
    <dd><input type="text" name="info[email]" class="text required email" data-validation="required" data-msg-email="请输入有效的Email地址"/></dd>
</dl>
```

实例二：

```html
<input id="inputSignupEmail" class="span10" name="email" type="text" placeholder="Email" 
 data-rule-required="true" 
 data-rule-email="true" 
 data-msg-required="请输入Email地址" 
 data-msg-email="请输入有效的Email地址"/>
```

从中可以看出规则的使用，不在需要单独写js来定义了，除非你要remote

调用jquery-validate

```html
<script src="/js/jquery-validation/dist/jquery.validate.js" type="text/javascript"></script>
<script src="/js/jquery-validation/lib/jquery.form.js" type="text/javascript"></script>
<script type="text/javascript">
    $(function(){
        //去掉提示
        jQuery.validator.messages.required = "";
        $('form#yuyue').validate({
            borderColorOnError : '#FFF',
            invalidHandler: function(e, validator) {
                //错误个数
                var errors = validator.numberOfInvalids();
                if (errors) {
                    $("label.error").css('display',"none");
                } else {
                    $("label.error").hide();
                }
            }
        });
    });
</script>
```

