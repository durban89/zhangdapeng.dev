---
title: "Yii2 如何在modules中添加验证码"
date: "2025-07-03 17:11:43"
slug: "yii2-ru-he-zai-modules-zhong-tian-jia-yan-zheng-ma"
categories: ["技术"]
tags: ["Yii", "PHP"]
aliases:
  - "/2025/07/03/Yii2-如何在modules中添加验证码/"
  - "/2025/07/03/Yii2-如何在modules中添加验证码.html"
  - "/Yii2-如何在modules中添加验证码/"
  - "/Yii2-如何在modules中添加验证码.html"
  - "/2025/07/03/yii2-ru-he-zai-modules-zhong-tian-jia-yan-zheng-ma/"
  - "/2025/07/03/yii2-ru-he-zai-modules-zhong-tian-jia-yan-zheng-ma.html"
  - "/yii2-ru-he-zai-modules-zhong-tian-jia-yan-zheng-ma.html"
---
最近玩了下Yii2的验证码部分，正常的逻辑都可以走通的，网上的例子也是没有问题的，关键有问题的部分是在module中使用的时候，分享给大家，往下看之前可以去看看正常情况下是如何使用的。

> controller部分的代码，这里的跟网上的都类似

```php
public function actions()
{
    return [
        'captcha' => [
            'class' => 'yii\captcha\CaptchaAction',
            'fixedVerifyCode' => null,
            'backColor' => 0x000000, //背景颜色
            'maxLength' => 6, //最大显示个数
            'minLength' => 5, //最少显示个数
            'padding' => 5, //间距
            'height' => 40, //高度
            'width' => 130, //宽度
            'foreColor' => 0xffffff, //字体颜色
            'offset' => 4, //设置字符偏移量 有效果
        ],
    ];
}
```

> model 部分的代码【这里是需要注意的】

```php
public function rules()
{
    return [
        ['username', 'required', 'message' => '登录账号不能为空'],
        ['password', 'required', 'message' => '登录密码不能为空'],
        ['verifyCode', 'required', 'message' => '验证码不能为空'],
        ['verifyCode', 'captcha', 'captchaAction' => 'admin/default/captcha', 'message' => '验证码输入错误'],
        ['rememberMe', 'boolean'],
        ['password', 'validatePassword'],
    ];
}
```

rules中的verifyCode,需要加一个captchaAction对应的值，不然会出现验证码验证不通过，而且验证码的的数字也不会变化，原因应该是默认使用了site/captcha导致的

> view部分的代码【由于php跟html的混排导致我无法忍受页面样式的混乱排版，所以尽量将参数配置部分拿出来】

```php
$captchaConfig = [
    'name' => 'captchaimg',
    'captchaAction' => ['/admin/default/captcha'],
    'template' => '<div class="form-group"><div>{image}</div></div>',
    'imageOptions' => [
        'id' => 'captchaimg',
        'title' => '换一个',
        'alt' => '换一个',
        'style' => 'cursor:pointer;margin-left:25px;',
    ],
];
```

```bash
<?=Captcha::widget($captchaConfig);?>
```
