---
title: "Yii2语言国际化自动配置"
date: "2025-07-08 16:02:05"
slug: "yii2-yu-yan-guo-ji-hua-zi-dong-pei-zhi"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/07/08/Yii2语言国际化自动配置/"
  - "/2025/07/08/Yii2语言国际化自动配置.html"
  - "/Yii2语言国际化自动配置/"
  - "/Yii2语言国际化自动配置.html"
  - "/2025/07/08/yii2-yu-yan-guo-ji-hua-zi-dong-pei-zhi/"
  - "/2025/07/08/yii2-yu-yan-guo-ji-hua-zi-dong-pei-zhi.html"
  - "/yii2-yu-yan-guo-ji-hua-zi-dong-pei-zhi.html"
---
如何实现语言国际自动化，大家可能觉得自动化，是不是不需要配置就自动切换，这个思路我之前也想过，能不能根据IP来判断地理位置然后确定其语言，网上找过一个"IpToCountry"相关的，有兴趣的可以搜索出来看看，他会提供一个ip对照的表，每隔一段时间会更新一次，不过这个暂时没做，后面考虑尝试下

这里我们说下Yii2如何实现，因为我们上面的一篇文章分享做了语言国际化的配置，也将对应的语言翻译了出来，下面就是需要根据条件来做切换  
从配置文件我们知道只需要更改language这个配置值就可以了，但是要在哪里更改呢。这里我的操作步骤如下

我想整体对项目的所有内容进行语言国际化，唯一我能想到的是修改控制器，有的说是修改 入口文件，我觉得修改入口文件有点破坏框架结构了。

## 第一步 创建一个AppController

继承yii/web/Controller，实现如下

```php
<?php

namespace app\controllers;

use Yii;
use yii\web\Controller;

class AppController extends Controller
{
    public function init()
    {
        if (isset(Yii::$app->session['_lang'])) {
            Yii::$app->language = Yii::$app->session['_lang'];
        }

        parent::init();
    }
}
```

## 第二步 将所有自己的控制器都继承AppController

做类似如下操作，我这里只是举了一个BlogController的例子

```php
class BlogController extends AppController
```

## 第三步 实现设置多语言的处理

我这里在我的控制器SiteController加了如下Action

```php
public function actionLanguage($language)
{
    Yii::$app->session['_lang'] = $language;
    $redirectUrl = Yii::$app->request->headers['Referer'];
    if (!$redirectUrl) {
        $redirectUrl = Yii::$app->homeUrl;
    }
    return $this->redirect($redirectUrl);
}
```

每次需要修改语言的话，只要将语言传入actionLanguage，就会更改session中\_lang的值，然后每个控制器在调用的时候都会先去更改项目的language

## 第四步 前端UI修改

通过在前端加个修改的逻辑，方便前端访问者进行更改语言设置

```html
<ul class="nav navbar-nav navbar-right">
  <li class="dropdown">
    <a href="j#" data-target="#" class="dropdown-toggle" data-toggle="dropdown">
      {{ Yii.t('app', 'Language') }}
      <b class="caret"></b>  
    </a>
    <ul class="dropdown-menu">
      <li
        class="{% if app.session['_lang'] == 'zh-CN' %}active{% endif %}"
      >
        <a
          href="{{ url(['site/language'], { 'language': 'zh-CN' })}}"
        >{{ Yii.t('app', 'Chinese') }}</a>
      </li>
      <li
        class="{% if app.session['_lang'] == 'en-US' %}active{% endif %}"
      >
        <a 
          href="{{ url(['site/language'], { 'language': 'en-US' })}}"
        >{{ Yii.t('app', 'English') }}</a>
      </li>
    </ul>
  </li>
</ul>
```

我这里使用的Twig模板。

到这里就都设置完了，可以正常切换语言了。后面如果又加了新的内容进去的话，可以直接执行上文中提到的命令

```bash
./yii message/extract @app/config/i18n.php
```

如有不理解的地方可以加群详细了解
