---
title: "Yii 控制器的action的访问限制中的 post提交限制的简单方法"
date: "2025-06-18 11:28:16"
slug: "yii-kong-zhi-qi-de-action-de-fang-wen-xian-zhi-zhong-de-post-ti-jiao-xian-zhi-de-jian-dan-fang-fa"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/18/Yii-控制器的action的访问限制中的-post提交限制的简单方法/"
  - "/2025/06/18/Yii-控制器的action的访问限制中的-post提交限制的简单方法.html"
  - "/Yii-控制器的action的访问限制中的-post提交限制的简单方法/"
  - "/Yii-控制器的action的访问限制中的-post提交限制的简单方法.html"
  - "/2025/06/18/yii-kong-zhi-qi-de-action-de-fang-wen-xian-zhi-zhong-de-post-ti-jiao-xian-zhi-de-jian-d/"
  - "/2025/06/18/yii-kong-zhi-qi-de-action-de-fang-wen-xian-zhi-zhong-de-post-ti-jiao-xian-zhi-de-ji.html"
  - "/yii-kong-zhi-qi-de-action-de-fang-wen-xian-zhi-zhong-de-post-ti-jiao-xian-zhi-de-jian-dan-fang.html"
---
对于我跟人来说，关于在一个控制器的中做action的post限制，一般的话我是这样做的

```php
public function actionDownload()
{
    if (Yii::app()->request->isPOSTRequest) {
        $message = [];
        if (isset($_POST['id']) && isset($_POST['url'])) {}
        if ($this->fileClick($_POST['id'], $_POST['url'])) {
            $message['code'] = 1;
        } else {
            $message['code'] = 0;
        }
        echo json_encode($message);
    }
    throw new CHttpException(400, '请求的页面不存在.');
}
```

感觉还不错，但是今天通过设置权限总是遇到错误，结果我发现了一个小角落的问题被我忽视了

```php
public function filters()
{
    return [
        'accessControl', // perform access control for CRUD operations
        'postOnly + delete', // we only allow deletion via POST request
    ];
}
```

postOnly + delete就是这里

yii的控制还是不错的，继续感悟
