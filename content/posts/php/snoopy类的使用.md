---
title: "snoopy类的使用"
date: "2025-06-20 11:07:54"
slug: "snoopy-lei-de-shi-yong"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/20/snoopy类的使用/"
  - "/2025/06/20/snoopy类的使用.html"
  - "/snoopy类的使用/"
  - "/snoopy类的使用.html"
  - "/2025/06/20/snoopy-lei-de-shi-yong/"
  - "/2025/06/20/snoopy-lei-de-shi-yong.html"
  - "/snoopy-lei-de-shi-yong.html"
---
Snoopy是一个php类，用来模拟浏览器的功能，可以获取网页内容，发送表单。  
  
Snoopy 正确运行需要你的服务器的 PHP 版本在 4 以上，并且支持 PCRE（Perl Compatible Regular Expressions），基本的 LAMP 服务都支持。  
下 载snoopy  
  
Snoopy的一些特点:  
  
1，抓取网页的内容 fetch  
2，抓取网页的文本内容 (去除HTML标签) fetchtext  
3，抓取网页的链接，表单 fetchlinks fetchform  
4，支持代理主机  
5，支持基本的用户名/密码验证  
6，支持设置 user_agent, referer(来路), cookies 和 header content(头文件)  
7，支持浏览器重定向，并能控制重定向深度  
8，能把网页中的链接扩展成高质量的url(默认)  
9，提交数据并 且获取返回值  
10，支持跟踪HTML框架  
11，支持重定向的时候传递cookies  
要求php4以上就可以了 由于本身是php一个类 无需扩支持 服务器不支持curl时候的最好选择，  
  
类方法:  
  
fetch($URI)  
———–  
  
这是为了抓取网页的内容而使用的方法。  
$URI参数是被抓取网页的URL地址。  
抓取的结果被存储在 $this->results 中。  
如果你正在抓取的是一个框架，Snoopy将会将每个框架追踪后存入数组中，然后存入 $this->results。  
  
fetchtext($URI)  
—————  
  
本方法类似于fetch()，唯一不同的就是本方法会去除HTML标签和其他的无关数据，只返回网页中的文字内容。  
  
fetchform($URI)  
—————  
  
本方法类似于fetch()，唯一不同的就是本方法会去除HTML标签和其他的无关数据，只返回网页中表单内容(form)。  
  
fetchlinks($URI)  
—————-  
  
本方法类似于fetch()，唯一不同的就是本方法会去除HTML标签和其他的无关数据，只返回网页中链接(link)。  
默认情况下，相对链接将自 动补全，转换成完整的URL。  
  
submit($URI,$formvars)  
———————-  
  
本方法向$URL 指定的链接地址发送确认表单。$formvars是一个存储表单参数的数组。  
  
submittext($URI,$formvars)  
————————–  
  
本方法类似于submit()，唯一不同的就是本方法会去除HTML标签和其他的无关数据，只返回登陆后网页中的文字内容。  
  
submitlinks($URI)  
—————-  
  
本方法类似于submit()，唯一不同的就是本方法会去除HTML标签和其他的无关数据，只返回网页中链接(link)。  
默认情况下，相对链接将 自动补全，转换成完整的URL。  
  
类属性: (缺省值在括号里)  
  
$host 连接的主机  
$port 连接的端口  
$proxy_host 使用的代理主机，如果有的话  
$proxy_port 使用的代理主机端口，如果有的话  
$agent 用户代理伪装 (Snoopy v0.1)  
$referer 来路信息，如果有的话  
$cookies cookies， 如果有的话  
$rawheaders 其他的头信息, 如果有的话  
$maxredirs 最大重定向次数， 0=不允许 (5)  
$offsiteok whether or not to allow redirects off-site. (true)  
$expandlinks 是否将链接都补全为完整地址 (true)  
$user 认证用户名, 如果有的话  
$pass 认证用户名, 如果有的话  
$accept http 接受类型 (image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, \*/\*)  
$error 哪里报错, 如果有的话  
$response_code 从服务器返回的响应代码  
$headers 从服务器返回的头信息  
$maxlength 最长返回数据长度  
$read_timeout 读取操作超时 (requires PHP 4 Beta 4+)  
设置为0为没有超时  
$timed_out 如果一次读取操作超时了，本属性返回 true (requires PHP 4 Beta 4+)  
$maxframes 允许追踪的框架最大数量  
$status 抓取的http的状态  
$temp_dir 网页服务器能够写入的临时文件目录 (/tmp)  
$curl_path cURL binary 的目录, 如果没有cURL binary就设置为 false  
  
以下是demo

```php
include "Snoopy.class.php";   
$snoopy = new Snoopy;   

$snoopy->proxy_host = "www.baidu.com";   
$snoopy->proxy_port = "8080";   

$snoopy->agent = "(compatible; MSIE 4.01; MSN 2.5; AOL 4.0; Windows 98)";   
$snoopy->referer = "http://www.baidu.com/";   

$snoopy->cookies["SessionID"] = 238472834723489l;   
$snoopy->cookies["favoriteColor"] = "RED";   

$snoopy->rawheaders["Pragma"] = "no-cache";   

$snoopy->maxredirs = 2;   
$snoopy->offsiteok = false;   
$snoopy->expandlinks = false;   

$snoopy->user = "joe";   
$snoopy->pass = "bloe";   

if($snoopy->fetchtext("http://www.baidu.com"))   
{   
    echo "<PRE>".htmlspecialchars($snoopy->results)."</PRE>\n";<BR>   
}else{  
    echo "error fetching document: ".$snoopy->error."\n";
}
```

snoopy采集phpchina示例

```php
<?php  
//采集phpchina  
set_time_limit(0);  
require_once("Snoopy.class.php");  
$snoopy=new Snoopy();  
//登陆论坛  
$submit_url = "http://www.phpchina.com/bbs/logging.php?action=login";  
$submit_vars["loginmode"] = "normal";  
$submit_vars["styleid"] = "1";  
$submit_vars["cookietime"] = "315360000";  
$submit_vars["loginfield"] = "username";  
$submit_vars["username"] = "***"; //你的用户名  
$submit_vars["password"] = "*****"; //你的密码  
$submit_vars["questionid"] = "0";  
$submit_vars["answer"] = "";  
$submit_vars["loginsubmit"] = "提 交";  
$snoopy->submit($submit_url,$submit_vars);  
if ($snoopy->results)  
{  
    //获取连接地址  
    $snoopy->fetchlinks("http://www.phpchina.com/bbs");  
    $url=array();  
    $url=$snoopy->results;  
 
    foreach ($url as $key=>$value)  
    {  
        //匹配http://www.phpchina.com/bbs/forumdisplay.php?fid=156&sid=VfcqTR地 址即论坛板块地址  
        if (!preg_match("/^(http:\/\/www\.phpchina\.com\/bbs\/forumdisplay\.php\?fid=)[0-9]*&sid=[a-zA-Z]{6}/i",$value)){
            unset($url[$key]);  
        }  
    }
    //获取到板块数组$url，循环访问，此处获取第一个模块第一页的数据  
    $i=0;  
    foreach ($url as $key=>$value)  
    {  
        if ($i>=1)  
        {  
            //测试限制  
            break;  
        }  
        else  
        {  
            //访问该模块，提取帖子的连接地址，正式访问里需要提取帖子分页的数据，然后根据分页数据提取帖子数据  
            $snoopy=new Snoopy();  
            $snoopy->fetchlinks($value);  
            $tie=array();  
            $tie[$i]=$snoopy->results;  
     
            //转换数组  
            foreach ($tie[$i] as $key=>$value)  
            {  
                //匹配http://www.phpchina.com/bbs/viewthread.php?tid=68127&amp; extra=page%3D1&amp;page=1&sid=iBLZfK  
               
 if 
(!preg_match("/^(http:\/\/www\.phpchina\.com\/bbs\/viewthread\.php\?tid=)[0-9]*&amp;extra=page\%3D1&amp;page=[0-9]*&sid=[a-zA-Z]{6}/i",$value))  
                {  
                    unset($tie[$i][$key]);  
                }  
            } 
            //归类数组，将同一个帖子不同页面的内容放一个数组里  
            $left='';//连接左边公用地址  
            $j=0;  
            $page=array();  
            foreach ($tie[$i] as $key=>$value)  
            {  
                $left=substr($value,0,52);  
                $m=0;  
                foreach ($tie[$i] as $pkey=>$pvalue)  
                {  
                    //重组数组  
                    if (substr($pvalue,0,52)==$left)  
                    {  
                        $page[$j][$m]=$pvalue;  
                        $m++;  
                    }  
                }  
                $j++;  
            }  
            //去除重复项开始  
            //$page=array_unique($page);只能用于一维数组  
            $paget[0]=$page[0];  
            $nums=count($page);  
            for ($n=1;$n<$nums;$n++)  
            {  
                $paget[$n]=array_diff($page[$n],$page[$n-1]);  
            }  
            //去除多维数组重复值结束  
            //去除数组空值  
            unset($page);  
            $page=array();//重新定义page数组  
            $page=array_filter($paget);  

            $u=0;  
            $title=array();  
            $content=array();  
            $temp='';  
            $tt=array();  
            foreach ($page as $key=>$value)  
            {  
                //外围循环，针对一个帖子  
                if (is_array($value))  
                {  
                    foreach ($value as $k1=>$v1)  
                    {  
                        //页内循环，针对一个帖子的N页  
                        $snoopy=new Snoopy();  
                        $snoopy->fetch($v1);  
                        $temp=$snoopy->results;  
                        //读取标题  
                        if (!preg_match_all("/<h2>(.*)<\/h2>/i",$temp,$tt))  
                        {  
                            echo "no title";  
                            exit;  
                        }  
                        else  
                        {  
                            $title[$u]=$tt[1][1];  
                        }  
                        unset($tt);  
                        //读取内容  
                       
 if (!preg_match_all("/<div id=\"postmessage_[0-9]{1,8}\" 
class=\"t_msgfont\">(.*)<\/div>/i",$temp,$tt))  
                        {  
                            print_r($tt);  
                            echo "no content1";  
                            exit;  
                        }  
                        else  
                        {  
                            foreach ($tt[1] as $c=>$c2)  
                            {  
                                $content[$u].=$c2;  
                            }  
                        }  
                    }  
                }  
                else  
                {  
                    //直接取页内容  
                    $snoopy=new Snoopy();  
                    $snoopy->fetch($value);  
                    $temp=$snoopy->results;  
                    //读取标题  
                    if (!preg_match_all("/<h2>(.*)<\/h2>/i",$temp,$tt))  
                    {  
                        echo "no title";  
                        exit;  
                    }  
                    else  
                    {  
                        $title[$u]=$tt[1][1];  
                    }  
                    unset($tt);  
                    //读取内容  
                   
 if (!preg_match_all("/<div id=\"postmessage_[0-9]*\" 
class=\"t_msgfont\">(.*)<\/div>/i",$temp,$tt))
                    {  
                        echo "no content2";  
                        exit;  
                    }  
                    else  
                    {  
                        foreach ($tt[1] as $c=>$c2)  
                        {  
                            $content[$u].=$c2;  
                        }  
                    }  
                }  
                $u++;  
            }  
            print_r($content);  
        } 
    $i++;  
    } 
}  
else  
{  
    echo "login failed";  
    exit;  
}  
?>
```
