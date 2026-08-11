---
title: "Yii简单的基于角色的访问控制"
date: "2025-05-29 15:28:14"
slug: "yii-jian-dan-de-ji-yu-jue-se-de-fang-wen-kong-zhi"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/05/29/Yii简单的基于角色的访问控制/"
  - "/2025/05/29/Yii简单的基于角色的访问控制.html"
  - "/Yii简单的基于角色的访问控制/"
  - "/Yii简单的基于角色的访问控制.html"
  - "/2025/05/29/yii-jian-dan-de-ji-yu-jue-se-de-fang-wen-kong-zhi/"
  - "/2025/05/29/yii-jian-dan-de-ji-yu-jue-se-de-fang-wen-kong-zhi.html"
  - "/yii-jian-dan-de-ji-yu-jue-se-de-fang-wen-kong-zhi.html"
---
```php
function filters()
{
    return [
        'accessControl', // perform access control for CRUD operations
    ];
}

function accessRules()
{
    return [
        [
            'allow',
            'action' => ['admin'],
            'roles' => ['staff', 'devel'],
        ],
        [
            'deny', // deny all users
            'users' => ['*'],
        ],
    ];
}
```


## [用户模型](#user-model)


在用户表中新增一列，列名 roles。建立相应的模型。在这里它将被命名为 “User”。

当添加用户可以给他们分配角色 “管理员”，“用户”，“员工”等等。


## [验证](#yanzheng)

在文件 protected/components/UserIdentity.php 添加如下内容：

```php
class UserIdentity extends CUserIdentity
{
    private $id;

    public function authenticate()
    {
        $record = User::model()->findByAttributes(['email' => $this->username]);
        if (null === $record) {
            $this->errorCode = self::ERROR_USERNAME_INVALID;
        } else if (md5($this->password) !== $record->password) {
            $this->errorCode = self::ERROR_PASSWORD_INVALID;
        } else {
            $this->id = $record->id;
            $this->setState('roles', $record->roles);
            $this->errorCode = self::ERROR_NONE;
        }
        return !$this->errorCode;
    }

    public function getId()
    {
        return $this->id;
    }
}
```

重要的一行是

```php
$this->setState('roles', $record->roles);
```

他给会话增加了用户角色。你可以使用如下代码获取用户角色。

```php
Yii:app()->user->getState("roles")
```

或

```php
Yii::app()->user->roles
```

## [检查权限:结构](#quanxianjiancha)


在 protected/components 文件夹下修改并创建文件 WebUser.php ,然后重写 checkAccess() 方法。

```php
<?php
class WebUser extends CWebUser
{
    /**
     * Overrides a Yii method that is used for roles in controllers (accessRules).
     *
     * @param string $operation Name of the operation required (here, a role).
     * @param mixed $params (opt) Parameters for this operation, usually the object to access.
     * @return bool Permission granted?
     */
    public function checkAccess($operation, $params = [])
    {
        if (empty($this->id)) {
            // Not identified => no rights
            return false;
        }
        $role = $this->getState("roles");
        if ('admin' === $role) {
            return true; // admin role has access to everything
        }
        // allow access if the operation request is the current user's role
        return ($operation === $role);
    }
}
```

在 checkAccess() 方法中你可以定义自己的逻辑。
确保类可以被yii使用配置文件 "protected/config/main.php" 必须包含以下内容:

```php
'components' => [
    // ...
    'user' => [
        'class' => 'WebUser',
    ],
]
```

{% blockquote %}
旁注:
[CWebUser::checkAccess()] 通常连接yii的验证系统。这里我们使用一个简单的处理角色的系统来替换[CAuthManager] 定义的分级系统。详细教程参加 Role-Based Access Control
{% endblockquote %}

## [检查权限: 使用](#quanxianjianchashiyong)

在你的 PHP 代码中使用 `Yii::app()->user->checkAccess('admin')` 来检查当前用户是否有 ‘admin’ 角色。

当用户拥有 "staff" 或 "admin" 角色时，调用 `Yii::app()->user->checkAccess("staff")` 将会返回 true。

在控制器中你可以使用 accessRules() 中的 "roles" 属性进行过滤。

见下面的例子。 怎样过滤动作 控制器必须包含以下代码：

```php
function filters()
{
    return [
        'accessControl', // perform access control for CRUD operations
    ];
}

function accessRules()
{
    return [
        [
            'allow',
            'action' => ['admin'],
            'roles' => ['staff', 'devel'],
        ],
        [
            'deny', // deny all users
            'users' => ['*'],
        ],
    ];
}
```

这里对控制器中的 "admin" 动作进行了限制访问: 只有拥有 "staff" 或 “devel” 角色才可以访问。 像API文档中描述的那样 CAccessRule, “roles” 属性实际上调用的是 `Yii::app()->user->checkAccess()` 方法。 怎样根据角色显示不同菜单 你只需使用一个基于用户角色的菜单。例如


```php
<?php
$user = Yii::app()->user; // just a convenience to shorten expressions
$this->widget('zii.widgets.CMenu', [
    'items' => [
        ['label' => 'Users', 'url' => ['/manageUser/admin'], 'visible' => $user->checkAcces('staff')],
        ['label' => 'Your Ideas', 'url' => ['/userarea/ideaList'], 'visible' => $user->checkAcces('normal')],
        ['label' => 'Login', 'url' => ['/site/login'], 'visible' => $user->isGuest],
        ['label' => 'Logout (' . Yii::app()->user->name . ')', 'url' => ['/site/logout'], 'visible' => !$user->isGuest],
    ],
]);
```

## [更进一步: 访问上下文](#more-context)

一个通常的需求，用户只能够修改自己的数据。在这种情况下，用户的角色是没有任何意义的：将要修改的数据。 这就是为什么 [CWebUser::checkAccess()] 有一个可选的参数 "$param" 。现在假设我们要检查的是一个用户是否有权更新Post记录的权限。我们可以这样写：

```php
if (Yii::app()->user->checkAccess('normal', $post)) {
    // .....
}
```
当然 `WebUser::checkAccess()` 必须被扩展来使用 "$params" 参数。这将取决于你的应用程序的逻辑。比如, 这可能是非常简单的 `$post->userId == $this->id`。
