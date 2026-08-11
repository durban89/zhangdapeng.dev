---
title: "jQuery validate 实例 remote操作 自定义错误提示"
date: "2025-06-20 11:07:37"
slug: "jquery-validate-shi-li-remote-cao-zuo-zi-ding-yi-cuo-wu-ti-shi"
categories: ["技术"]
tags: ["jQuery", "JavaScript"]
aliases:
  - "/2025/06/20/jQuery-validate-实例-remote操作-自定义错误提示/"
  - "/2025/06/20/jQuery-validate-实例-remote操作-自定义错误提示.html"
  - "/jQuery-validate-实例-remote操作-自定义错误提示/"
  - "/jQuery-validate-实例-remote操作-自定义错误提示.html"
  - "/2025/06/20/jquery-validate-shi-li-remote-cao-zuo-zi-ding-yi-cuo-wu-ti-shi/"
  - "/2025/06/20/jquery-validate-shi-li-remote-cao-zuo-zi-ding-yi-cuo-wu-ti-shi.html"
  - "/jquery-validate-shi-li-remote-cao-zuo-zi-ding-yi-cuo-wu-ti-shi.html"
---
**jquery validate 实例 remote操作 自定义错误提示**

关于这个网站上好多的示例，但是为看到过有关于remote的操作，还有关于自定义错误提示的示例，自己google一下，自己又测试了一下来个PHP版本的，此项目方案更适合于QEEPHP框架，或者其他的框架。

html代码

```html
<form id='complete-form' action="" method="post">
  	<li class="input">
        <span class="title">邮箱</span>
        <input id='email' name='email' type="email" />
        <span class="back"></span>
    </li>
    <li class="input">
        <span class="title">登录密码</span>
        <input id='password' name='password' type="password" />
        <span class="back"></span></li>
    <li class="input">
        <span class="title">确认密码</span>
        <input id='repassword' name='repassword' type="password" />
        <span class="back"></span>
    </li>
    <li class="submit">
        <span>完成注册</span>
    </li>
  </form>
```

js代码

```javascript
<script language="javascript">
    $(function(){
        $('form#complete-form').validate({
            rules: {
                email:{
                    required:true,
                    email:true,
                    remote:{
                        url:'/default/isemail/type/validate',
                        type:'post'
                    },
                },
                password:{
                    required:true,
                    minlength:6,
                },
                repassword:{
                    required:true,
                    equalTo:password,
                    minlength:6,
                }
            },
            messages:{
                email:{
                    required:'邮箱地址不能为空',
                    email:'邮箱格式错误',
                    remote:'该邮箱已经被注册 <a href="/default/bind">绑定账号</a>'
                },
                password:{
                    required:'登录密码不能为空',
                    minlength:'密码长度不能少于6个字符'
                },
                repassword:{
                    required:'确认密码不能为空',
                    minlength:'密码长度不能少于6个字符',
                    equalTo:'确认密码与输入的密码不一致'
                }
            },
            errorElement:'em',
            errorPlacement: function(error, element) {
                error.appendTo( element.parent().find('.back'));       
                
            },
        });
        
        $("#complete .submit span").click(function(){
            $("#complete form").submit();	
        })
    });
</script>
```

php后台操作代码：

```php
/**
 * Email是否存在
 */
public function actionIsEmail(){
    $email = $this->_context->post('email','');
    $ajaxType = $this->_context->get('type','');

    $email = $this->filter($email);
    $obj = User_Star::find('email=?',$email)->query();
    
    if(empty($obj->id)){
        if($ajaxType != 'validate'){
            $message['error'] = 1;//可以注册
            $message['email'] = false;
            echo json_encode($message);
            exit;
        }else{
            echo 'true';
            exit;
        }
    }else{
        if($ajaxType != 'validate'){
            $message['error'] = 0;//不可以注册
            $message['email'] = true;
            echo json_encode($message);
            exit;
        }else{
            echo 'false';
            exit;
        }
    }
}
```

这里提示几点，

1，记载jquery框架库

2，加载jauery.validate插件

3，php后台输出操作，一定是字符串型的
