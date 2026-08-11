---
title: "Yii2压缩PHP中模板代码的输出"
date: "2025-07-09 09:59:31"
slug: "yii2-ya-suo-php-zhong-mu-ban-dai-ma-de-shu-chu"
categories: ["技术"]
tags: ["Yii"]
aliases:
  - "/2025/07/09/Yii2压缩PHP中模板代码的输出/"
  - "/2025/07/09/Yii2压缩PHP中模板代码的输出.html"
  - "/Yii2压缩PHP中模板代码的输出/"
  - "/Yii2压缩PHP中模板代码的输出.html"
  - "/2025/07/09/yii2-ya-suo-php-zhong-mu-ban-dai-ma-de-shu-chu/"
  - "/2025/07/09/yii2-ya-suo-php-zhong-mu-ban-dai-ma-de-shu-chu.html"
  - "/yii2-ya-suo-php-zhong-mu-ban-dai-ma-de-shu-chu.html"
---
在Web开发中，无论是PHP的框架还是Python的框架，都会遇到使用模板的时候  
在使用模板的时候就会遇到一个问题，就是使用模板编写的代码通过查看源代码的时候，会发现代码混乱不堪，对于代码格式又嫉妒追求的我来说我因受不了，但是目前也没有找到什么好的格式化输出的办法  
但是格式化输出的话，也会需要处理一个压缩的问题，最终还是选择一个方案，开发的时候为了查看代码修改代码，就不做处理，但是上线的时候还是要做下压缩的处理，就是将无用的空格或者换行之类的全部删除掉。

问题前提已经抛出，现在看看如何解决这个问题，为了防止重复早轮子网上也查了一遍，结果也找到了，但是用composer安装的时候又是各种的不兼容，于是看了下源代码，其实很简单。这里我就简答的说下如何使用  
具体的逻辑我就不多说了，其实自己理解了下面的使用流程，自己改写也不是太难的事情

## **第一步 功能开发**

创建两个文件一个是components/HtmlMinify.php，代码逻辑如下

```php
<?php

namespace app\components;

use app\helpers\HtmlMinifyHelper;
use Yii;
use yii\base\Component;
use yii\base\Event;
use yii\web\Response;
use yii\web\View;

class HtmlMinify extends Component
{
    /**
     * Minify html. Process before response send
     * @var bool
     */
    public $html = false;
    /**
     * Minify css on page, added by registerCss. Process before render page in view component
     * @var bool
     */
    public $css = false;
    /**
     * Minify css on page. Process before render page in view component
     * @var bool
     */
    public $js = false;
    /**
     * Response formats list, where enable minify html
     * @var array
     */
    public $formats = [
        Response::FORMAT_HTML,
    ];

    public function init()
    {
        /** @var $this View */
        Yii::$app->view->on(View::EVENT_END_PAGE, [$this, 'onEventEndPage']);
        Yii::$app->response->on(Response::EVENT_BEFORE_SEND, [$this, 'onEventBeforeSend']);
    }

    public function onEventEndPage(Event $event)
    {
        $view = $event->sender;
        if ($this->css && !empty($view->css)) {
            foreach ($view->css as &$css) {
                $css = HtmlMinifyHelper::css($css);
            }
        }
        if ($this->js && !empty($view->js)) {
            foreach ($view->js as &$list) {
                foreach ($list as &$js) {
                    $js = HtmlMinifyHelper::js($js);
                }
            }
        }
    }

    public function onEventBeforeSend(Event $event)
    {
        $response = $event->sender;
        if ($this->html & in_array($response->format, $this->formats)) {
            if (!empty($response->data)) {
                $response->data = HtmlMinifyHelper::html($response->data);
            }
            if (!empty($response->content)) {
                $response->content = HtmlMinifyHelper::html($response->content);
            }
        }
    }
}
```

另外一个文件上是helpers/HtmlMinifyHelper.php，代码逻辑如下

```php
<?php
namespace app\helpers;

class HtmlMinifyHelper
{
    public static function html($input)
    {
        if (trim($input) === "") {
            return $input;
        }
        // Remove extra white-space(s) between HTML attribute(s)
        $input = preg_replace_callback('#<([^\/\s<>!]+)(?:\s+([^<>]*?)\s*|\s*)(\/?)>#s', function ($matches) {
            return '<' . $matches[1] . preg_replace('#([^\s=]+)(\=([\'"]?)(.*?)\3)?(\s+|$)#s', ' $1$2', $matches[2]) . $matches[3] . '>';
        }, str_replace("\r", "", $input));
        // Minify inline CSS declaration(s)
        if (strpos($input, ' style=') !==false){            $input=preg_replace_callback('#<([^<]+?)\s+style=([\'"])(.*?)\2(?=[\/\s>])#s',function ($matches){                return '<' . $matches[1] . ' style=' . $matches[2] . self::css($matches[3]) . $matches[2];
            }, $input);
        }
        return preg_replace(
            [
                // t = text
                // o = tag open
                // c = tag close
                // Keep important white-space(s) after self-closing HTML tag(s)
                '#<(img|input)(>| .*?>)#s',
                // Remove a line break and two or more white-space(s) between tag(s)
                '#(<!--.*?-->)|(>)(?:\n*|\s{2,})(<)|^\s*|\s*$#s',
                '#(<!--.*?-->)|(?<!\>)\s+(<\/.*?>)|(<[^\/]*?>)\s+(?!\<)#s', // t+c || o+t
                '#(<!--.*?-->)|(<[^\/]*?>)\s+(<[^\/]*?>)|(<\/.*?>)\s+(<\/.*?>)#s', // o+o || c+c
                '#(<!--.*?-->)|(<\/.*?>)\s+(\s)(?!\<)|(?<!\>)\s+(\s)(<[^\/]*?\/?>)|(<[^\/]*?\/?>)\s+(\s)(?!\<)#s', // c+t || t+o || o+t -- separated by long white-space(s)
                '#(<!--.*?-->)|(<[^\/]*?>)\s+(<\/.*?>)#s', // empty tag
                '#<(img|input)(>| .*?>)<\/\1>#s', // reset previous fix
                '#(&nbsp;)&nbsp;(?![<\s])#', // clean up ...
                '#(?<=\>)(&nbsp;)(?=\<)#', // --ibid
                // Remove HTML comment(s) except IE comment(s)
                '#\s*<!--(?!\[if\s).*?-->\s*|(?<!\>)\n+(?=\<[^!])#s',
            ],
            [
                '<$1$2</$1>',
                '$1$2$3',
                '$1$2$3',
                '$1$2$3$4$5',
                '$1$2$3$4$5$6$7',
                '$1$2$3',
                '<$1$2',
                '$1 ',
                '$1',
                "",
            ],
            $input);
    }

    public static function css($input)
    {
        if (trim($input) === "") {
            return $input;
        }
        return preg_replace(
            [
                // Remove comment(s)
                '#("(?:[^"\\\]++|\\\.)*+"|\'(?:[^\'\\\\]++|\\\.)*+\')|\/\*(?!\!)(?>.*?\*\/)|^\s*|\s*$#s',
                // Remove unused white-space(s)
                '#("(?:[^"\\\]++|\\\.)*+"|\'(?:[^\'\\\\]++|\\\.)*+\'|\/\*(?>.*?\*\/))|\s*+;\s*+(})\s*+|\s*+([*$~^|]?+=|[{};,>~+]|\s*+-(?![0-9\.])|!important\b)\s*+|([[(:])\s++|\s++([])])|\s++(:)\s*+(?!(?>[^{}"\']++|"(?:[^"\\\]++|\\\.)*+"|\'(?:[^\'\\\\]++|\\\.)*+\')*+{)|^\s++|\s++\z|(\s)\s+#si',
                // Replace `0(cm|em|ex|in|mm|pc|pt|px|vh|vw|%)` with `0`
                '#(?<=[\s:])(0)(cm|em|ex|in|mm|pc|pt|px|vh|vw|%)#si',
                // Replace `:0 0 0 0` with `:0`
                '#:(0\s+0|0\s+0\s+0\s+0)(?=[;\}]|\!important)#i',
                // Replace `background-position:0` with `background-position:0 0`
                '#(background-position):0(?=[;\}])#si',
                // Replace `0.6` with `.6`, but only when preceded by `:`, `,`, `-` or a white-space
                '#(?<=[\s:,\-])0+\.(\d+)#s',
                // Minify string value
                '#(\/\*(?>.*?\*\/))|(?<!content\:)([\'"])([a-z_][a-z0-9\-_]*?)\2(?=[\s\{\}\];,])#si',
                '#(\/\*(?>.*?\*\/))|(\burl\()([\'"])([^\s]+?)\3(\))#si',
                // Minify HEX color code
                '#(?<=[\s:,\-]\#)([a-f0-6]+)\1([a-f0-6]+)\2([a-f0-6]+)\3#i',
                // Replace `(border|outline):none` with `(border|outline):0`
                '#(?<=[\{;])(border|outline):none(?=[;\}\!])#',
                // Remove empty selector(s)
                '#(\/\*(?>.*?\*\/))|(^|[\{\}])(?:[^\s\{\}]+)\{\}#s',
            ],
            [
                '$1',
                '$1$2$3$4$5$6$7',
                '$1',
                ':0',
                '$1:0 0',
                '.$1',
                '$1$3',
                '$1$2$4$5',
                '$1$2$3',
                '$1:0',
                '$1$2',
            ],
            $input);
    }

    public static function js($input)
    {
        if (trim($input) === "") {
            return $input;
        }
        return preg_replace(
            [
                // Remove comment(s)
                '#\s*("(?:[^"\\\]++|\\\.)*+"|\'(?:[^\'\\\\]++|\\\.)*+\')\s*|\s*\/\*(?!\!|@cc_on)(?>[\s\S]*?\*\/)\s*|\s*(?<![\:\=])\/\/.*(?=[\n\r]|$)|^\s*|\s*$#',
                // Remove white-space(s) outside the string and regex
                '#("(?:[^"\\\]++|\\\.)*+"|\'(?:[^\'\\\\]++|\\\.)*+\'|\/\*(?>.*?\*\/)|\/(?!\/)[^\n\r]*?\/(?=[\s.,;]|[gimuy]|$))|\s*([!%&*\(\)\-=+\[\]\{\}|;:,.<>?\/])\s*#s',
                // Remove the last semicolon
                '#;+\}#',
                // Minify object attribute(s) except JSON attribute(s). From `{'foo':'bar'}` to `{foo:'bar'}`
                '#([\{,])([\'])(\d+|[a-z_][a-z0-9_]*)\2(?=\:)#i',
                // --ibid. From `foo['bar']` to `foo.bar`
                '#([a-z0-9_\)\]])\[([\'"])([a-z_][a-z0-9_]*)\2\]#i',
            ],
            [
                '$1',
                '$1$2',
                '}',
                '$1$3',
                '$1.$3',
            ],
            $input);
    }
}
```

## **第二步 功能配置**

修改配置文件文件，这里修改config/web.php  
components中加入如下代码

```php
'htmlMinify' => [
    'class' => 'app\components\HtmlMinify',
    'html' => !YII_ENV_DEV, // 这里只开启了html的
],
```

在bootstrap中加入如下代码

```php
'bootstrap' => ['log', 'htmlMinify'], // log是默认加的， htmlMinify是我们自己加的
```

到这里就结束了配置可以试着在生产环境试下

如有问题请加群沟通交流或下面留言
