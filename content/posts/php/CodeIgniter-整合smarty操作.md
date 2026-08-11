---
title: "CodeIgniter 整合smarty操作"
date: "2025-06-27 14:15:06"
slug: "codeigniter-zheng-he-smarty-cao-zuo"
categories: ["技术"]
tags: ["PHP", "CodeIgniter"]
aliases:
  - "/2025/06/27/CodeIgniter-整合smarty操作/"
  - "/2025/06/27/CodeIgniter-整合smarty操作.html"
  - "/CodeIgniter-整合smarty操作/"
  - "/CodeIgniter-整合smarty操作.html"
  - "/2025/06/27/codeigniter-zheng-he-smarty-cao-zuo/"
  - "/2025/06/27/codeigniter-zheng-he-smarty-cao-zuo.html"
  - "/codeigniter-zheng-he-smarty-cao-zuo.html"
---
先在根目录下(和index.php同等级)建立几个文件夹:templates(放smarty模板文件),templates_c(放smarty编译文件),

config,cache(这些文件夹的作用,请参考smarty).注:这些文件夹你可以随意放在你想要的地方,

不过我觉得方便和安全找平衡是最重要,还有就是在引入smarty时,要注意路径的设置.

在index.php入口文件加入一句define('ROOT', dirname(__FILE__);

这样做的目的是在smarty初始化时,可以根据这个网站的根路径来方便设置

templete_dir,compile_dir等,这在下面Cismarty.php这个文件中用到.

再把smarty整个文件夹COPY到system/application/libraries/

system/application/libraries/smarty/下有Smarty.class.php等smarty的系统文件

在system/application/libraries/下建立一个Ci_Smarty.php文件,这个文件是一个扩展smarty类,作用是

默认初始化smarty的一化路径配置.如templete_dir,compile_die这两个必须有配置.方便日后在controller中引入和应用,

在controller中使用方法：

```php
$this->load->library('cismarty');
$this->ci_smarty->assign('title', $title);
//……
$this->ci_smarty->display('xx.tpl');
```

Ci_Smarty类的代码:

```php
<?php defined('BASEPATH') or die('Access restricted!');
 
require(APPPATH.'libraries/smarty/Smarty.class.php');//APPPATH是入口文件定义的application的目录
class Ci_Smarty extends Smarty
{
// {{{ constructor
   
 
public function __construct($template_dir = '', $compile_dir = '', $config_dir = '', $cache_dir = ''){
    parent::__construct();
    if(is_array($template_dir)){
      foreach ($template_dir as $key => $value) {
        $this->$key = $value;
      }
    }else {
      //ROOT是Codeigniter在入口文件index.php定义的本web应用的根目录
      //在入口文件中加入define('ROOT', dirname(__FILE__);
      $this->template_dir = $template_dir ? $template_dir : ROOT . '/templates';
      $this->compile_dir  = $compile_dir  ? $compile_dir  : ROOT . '/templates_c';
      $this->config_dir   = $config_dir   ? $config_dir   : ROOT . '/config';
      $this->cache_dir    = $cache_dir    ? $cache_dir    : ROOT . '/cache';
     }
} // end func constructor
    
// }}}
}
```

//一个controler的例子：

```php
<?php defined('BASEPATH') or die('Access restricted!');
 
class Demo extends Controller
{
  public function __construct(){
    parent::__construct();
    $this->load->library('CI_Smarty');
  }
  public function index()
  {
    $this->load->helper('text');
    $config = array();
    $this->ci_smarty->assign('title', '这是我第一个smarty在CI中的应用!');
    $this->ci_smarty->assign('content', 'smarty和Codeigniter的结合使用:');
    $code = file_get_contents(APPPATH.'libraries/Ci_Smarty.php');
    $this->ci_smarty->assign('code', highlight_string($code));
    $this->ci_smarty->display('demo.tpl');
  }
}
```

在ROOT/templates/demo.tpl代码：

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" c>
<title>{$title}</title>
{literal}
<style type="text/css">
li{
  margin:10px 0 10px 0;
}
</style>
{/literal}
</head>
<body>
<h5>Begin use the smarty view OBJ:</h5>
{$content}
{$code}
</body>
</html>
```

