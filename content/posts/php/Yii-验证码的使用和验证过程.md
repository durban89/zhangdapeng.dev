---
title: "Yii 验证码的使用和验证过程"
date: "2025-06-17 17:20:48"
slug: "yii-yan-zheng-ma-de-shi-yong-he-yan-zheng-guo-cheng"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/17/Yii-验证码的使用和验证过程/"
  - "/2025/06/17/Yii-验证码的使用和验证过程.html"
  - "/Yii-验证码的使用和验证过程/"
  - "/Yii-验证码的使用和验证过程.html"
  - "/2025/06/17/yii-yan-zheng-ma-de-shi-yong-he-yan-zheng-guo-cheng/"
  - "/2025/06/17/yii-yan-zheng-ma-de-shi-yong-he-yan-zheng-guo-cheng.html"
  - "/yii-yan-zheng-ma-de-shi-yong-he-yan-zheng-guo-cheng.html"
---
如果要实现这个过程的话，需要几个步骤

### [第一步就是controller的操作](#1)

在要操作的控制器中添加如下代码：

```php
<?php
function actions()
{
    return [
        // captcha action renders the CAPTCHA image displayed on the contact page
        'captcha' => [
            'class' => 'CCaptchaAction',
            'backColor' => 0xFFFFFF,
            'maxLength' => '8', // 最多生成几个字符
            'minLength' => '7', // 最少生成几个字符
            'height' => '40',
            'width' => '230',
        ],
    ];

}

function accessRules()
{
    return [
        ['allow',
            'actions' => ['captcha'],
            'users' => ['*'],
        ],
    ];
}
```

### [第二步就是view的操作](#2)

在要显示验证码的地方添加如下代码：

```php
<div class="control-group">
    <?php $this->widget('CCaptcha',array(
        'showRefreshButton'=>true,
        'clickableImage'=>false,
        'buttonLabel'=>'刷新验证码',
        'imageOptions'=>array(
            'alt'=>'点击换图',
            'title'=>'点击换图',
            'style'=>'cursor:pointer',
            'padding'=>'10')
        )); ?>
</div>
```

### [第三步就是LoginForm的操作](#3)

```php
<?php

/**
 * LoginForm class.
 * LoginForm is the data structure for keeping
 * user login form data. It is used by the 'login' action of 'SiteController'.
 */
class LoginForm extends CFormModel
{
    public $username;
    public $password;
    public $rememberMe;
    public $verifyCode;
    private $_identity;

    /**
     * Declares the validation rules.
     * The rules state that username and password are required,
     * and password needs to be authenticated.
     */
    public function rules()
    {
        return [
            // username and password are required
            //            array('username, password', 'required'),
            ['username', 'required', 'message' => '登录帐号不能为空'],
            ['password', 'required', 'message' => '密码不能为空'],
            ['verifyCode', 'required', 'message' => '验证码不能为空'],
            ['verifyCode', 'captcha', 'on' => 'login', 'allowEmpty' => !Yii::app()->admin->isGuest],
            // rememberMe needs to be a boolean
            ['rememberMe', 'boolean'],
            // password needs to be authenticated
            ['password', 'authenticate'],
        ];
    }

    /**
     * Declares attribute labels.
     */
    public function attributeLabels()
    {
        return [
            'rememberMe' => '下次记住我',
            'verifyCode' => '验证码',
        ];
    }

    /**
     * Authenticates the password.
     * This is the 'authenticate' validator as declared in rules().
     */
    public function authenticate($attribute, $params)
    {
        if (!$this->hasErrors()) {
            $this->_identity = new UserIdentity($this->username, $this->password);
            if (!$this->_identity->authenticate()) {
                $this->addError('password', '帐号或密码错误.');
            }
        }
    }

    public function validateVerifyCode($verifyCode)
    {
        if (strtolower($this->verifyCode) === strtolower($verifyCode)) {
            return true;
        } else {
            $this->addError('verifyCode', '验证码错误.');
        }
    }

    /**
     * Logs in the user using the given username and password in the model.
     * @return boolean whether login is successful
     */
    public function login()
    {
        if (null === $this->_identity) {
            $this->_identity = new UserIdentity($this->username, $this->password);
            $this->_identity->authenticate();
        }
        if (UserIdentity::ERROR_NONE === $this->_identity->errorCode) {
            $duration = $this->rememberMe ? 3600 * 24 * 30 : 0; // 30 days
            Yii::app()->user->login($this->_identity, $duration);
            return true;
        } else {
            return false;
        }
    }
}
```

### [第四步，实现验证的过程，那么具体的查看我自己的写的一个方式，在第三部已经写好了](#4)

validateVerifyCode就是啦，可以在controller里面调用

我的调用如下：

```php
<?php
function actionLogin()
{
    $model = new LoginForm;
    if (isset($_POST['ajax']) && 'login-form' === $_POST['ajax']) {
        echo CActiveForm::validate($model);
        Yii::app()->end();
    }

    if (isset($_POST['LoginForm'])) {
        $model->attributes = $_POST['LoginForm'];
        // validate user input and redirect to the previous page if valid
        if ($model->validate() &&
            $model->validateVerifyCode($this->createAction('captcha')->getVerifyCode()) &&
            $model->login()) {
            $this->redirect(CController::createUrl('default/index'));
        }
    }
    $this->render('login', ['model' => $model]);
}
```
