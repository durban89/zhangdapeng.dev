---
title: "PHP 中文分词PSCWS4使用说明"
date: "2025-06-12 17:45:22"
slug: "php-zhong-wen-fen-ci-pscws4-shi-yong-shuo-ming"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/12/PHP-中文分词PSCWS4使用说明/"
  - "/2025/06/12/PHP-中文分词PSCWS4使用说明.html"
  - "/PHP-中文分词PSCWS4使用说明/"
  - "/PHP-中文分词PSCWS4使用说明.html"
  - "/2025/06/12/php-zhong-wen-fen-ci-pscws4-shi-yong-shuo-ming/"
  - "/2025/06/12/php-zhong-wen-fen-ci-pscws4-shi-yong-shuo-ming.html"
  - "/php-zhong-wen-fen-ci-pscws4-shi-yong-shuo-ming.html"
---
分词的这个技术，挺重要的，在有些方面起着非常重要的作用，这里摘自一博友的文章

PSCWS4 类对应的文件为 pscws4.class.php。在 PHP 代码中的调用方法如下：

```php
<?php
//加入头文件
require './pscws4/pscws4.class.php';

//建立分词类对像,参数为字符集,默认为gbk,
//可在后面调用set_charset改变
$pscws = new PSCWS4('utf8');

//接下来,设定一些分词参数或选项,set_dict 是必须的,
//若想智能识别人名等需要set_rule
//包括:set_charset,set_dict,set_rule,
//set_ignore,set_multi,set_debug,set_duality...等方法

$pscws->set_dict('./pscws4/etc/dict.xdb');
$pscws->set_rule('./pscws4/etc/rules.ini');

//分词调用send_text()将待分词的字符串传入,
//紧接着循环调用get_result()方法取回一系列分好的词
//直到get_result()返回false为止
//返回的词是一个关联数组,包含:word词本身,idf逆词率(重),
//off在text中的偏移,len长度,attr词性;
$pscws->send_text($text);
while($some = $pscws->get_result()) {
    foreach($some as $word) {
        print_r($word);
    }
}
```

— 类方法完全手册 —

(注: 构造函数可传入字符集作为参数, 这与另外调用 set_charset 效果是一样的)  
  
- void set_charset(string charset);  
说明：设定分词词典、规则集、欲分文本字符串的字符集，系统缺省是 gbk 字集。  
返回：无。  
参数：charset 是设定的字符集，目前只支持 utf8 和 gbk。（注：big5 也可作 gbk 处理）  
注意：输入要切分的文本，词典，规则文件这三者的字符集必须统一为该 charset 值。  
  
- bool set_dict(string dict_fpath);  
说明：设置分词引擎所采用的词典文件。  
参数：dict_path 是词典的路径，可以是相对路径或完全路径。  
返回：成功返回 true 失败返回 false。  
错误：若有错误会给出 WARNING 级的错误提示。  
  
- void set_rule(string rule_path);  
说明：设定分词所用的新词识别规则集（用于人名、地名、数字时间年代等识别）。  
返回：无。  
参数：rule_path 是规则集的路径，可以是相对路径或完全路径。  
  
- void set_ignore(bool yes)  
说明：设定分词返回结果时是否去除一些特殊的标点符号之类。  
返回：无。  
参数：yes 设定值，如果为 true 则结果中不返回标点符号，如果为 false 则会返回，缺省为 false。  
  
- void set_multi(int mode);  
说明：设定分词返回结果时是否复合分割，如“中国人”返回“中国＋人＋中国人”三个词。  
返回：无。  
参数：mode 设定值，1 ~ 15。  
按位与的 1 | 2 | 4 | 8 分别表示: 短词 | 二元 | 主要单字 | 所有单字  
  
- void set_duality(bool yes);  
说明：设定是否将闲散文字自动以二字分词法聚合。  
返回：无。  
参数：yes 设定值，如果为 true 则结果中多个单字会自动按二分法聚分，如果为 false 则不处理，缺省为 false。  
  
- void set_debug(bool yes);  
说明：设置分词过程是否输出N-Path分词过程的调试信息。  
参数：yes 设定值，如果为 true 则分词过程中对于多路径分法分给出提示信息。  
返回：无。  
  
- void send_text(string text)  
说明：发送设定分词所要切割的文本。  
返回：无。  
参数：text 是文本的内容。  
注意：执行本函数时，请先加载词典和规则集文件并设好相关选项。  
  
- mixed get_result(void)  
说明：根据 send_text 设定的文本内容，返回一系列切好的词汇。  
返回：成功返回切好的词汇组成的数组， 若无更多词汇，返回 false。  
参数：无。  
注意：每次切割后本函数应该循环调用，直到返回 false 为止，因为程序每次返回的词数是不确定的。  
返回的词汇包含的键值有：word (string, 词本身) idf (folat, 逆文本词频) off (int, 在文本中的位置) attr(string, 词性)  
  
- mixed get_tops( [int limit [, string attr]] )  
说明：根据 send_text 设定的文本内容，返回系统计算出来的最关键词汇列表。  
返回：成功返回切好的词汇组成的数组， 若无更多词汇，返回 false。  
参数：limit 可选参数，返回的词的最大数量，缺省是 10；  
attr 可选参数，是一系列词性组成的字符串，各词性之间以半角的逗号隔开，  
这表示返回的词性必须在列表中，如果以~开头，则表示取反，词性必须不在列表中，  
缺省为空，返回全部词性，不过滤。  
  
- string version(void);  
说明：返回本版号。  
返回：版本号（字符串）。  
参数：无。  
  
- void close(void);  
说明：关闭释放资源，使用结束后可以手工调用该函数或等系统自动回收。  
返回：无。  
参数：无。  


以下是相关资源的下载地址：  
PSCWS4: http://www.ftphp.com/scws/down/pscws4-20081221.tar.bz2  
规则集: http://www.ftphp.com/scws/down/scws-rules-all.zip  
词典系列:http://www.ftphp.com/scws/down/scws-dict-chs-gbk.tar.bz2  
http://www.ftphp.com/scws/down/scws-dict-chs-utf8.tar.bz2
