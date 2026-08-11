---
title: "session.save_path目录大量session临时文件带来的服务器效率问题"
date: "2025-06-19 10:29:09"
slug: "sessionsave-path-mu-lu-da-liang-session-lin-shi-wen-jian-dai-lai-de-fu-wu-qi-xiao-lv-wen-ti"
categories: ["技术"]
tags: ["PHP", "Session"]
aliases:
  - "/2025/06/19/session.save-path目录大量session临时文件带来的服务器效率问题/"
  - "/2025/06/19/session.save-path目录大量session临时文件带来的服务器效率问题.html"
  - "/session.save-path目录大量session临时文件带来的服务器效率问题/"
  - "/session.save-path目录大量session临时文件带来的服务器效率问题.html"
  - "/2025/06/19/Session-save-path目录大量session临时文件带来的服务器效率问题/"
  - "/2025/06/19/Session-save-path目录大量session临时文件带来的服务器效率问题.html"
  - "/2025/06/19/sessionsave-path-mu-lu-da-liang-session-lin-shi-wen-jian-dai-lai-de-fu-wu-qi-xiao-lv-we/"
  - "/2025/06/19/sessionsave-path-mu-lu-da-liang-session-lin-shi-wen-jian-dai-lai-de-fu-wu-qi-xiao-l.html"
  - "/sessionsave-path-mu-lu-da-liang-session-lin-shi-wen-jian-dai-lai-de-fu-wu-qi-xiao-lv-wen-ti.html"
---
如果访问量大，可能产生的 SESSION 文件会比较多，这时可以设置分级目录进行 SESSION 文件的保存，效率会提高很多，设置方法为：session.save_path="N;/save_path"，N 为分级的级数，save_path 为开始目录。当写入 SESSION 数据的时候，PHP 会获取到客户端的 SESSION_ID，然后根据这个 SESSION ID 到指定的 SESSION 文件保存目录中找到相应的 SESSION 文件，不存在则创建之，最后将数据序列化之后写入文件。     检查了下各web节点，所有web服务器的httpd线程均达到满负荷，很奇怪。因为所有web节点都通过nfs来共享session目录来达到 session的一致性，检查了下nfs文件服务器，IO读写比较大，检查了session_tmp目录，发现session目录临时文件达到 70000多个，初步判断也许是因为一级目录下文件过多带来的IO性能下降。  
   
以前没有想过session存放的效率问题，今天由此想到了session多级存放的问题，来解决一个目录下session文件过多带来的读写效率问题，查了下php.net其实php在配置中已经给出了有关选项。

php.net上的：http://www.php.net/manual/en/ref.session.php

`session.save_path` 定义了传递给存储处理器的参数。如果选择了默认的 files 文件处理器，则此值是创建文件的路径。默认为 `/tmp`。参见 `session_save_path()`。 此指令还有一个可选的 N 参数来决定会话文件分布的目录深度。例如，设定为 '5;/tmp' 将使创建的会话文件和路径类似于  
`/tmp/4/b/1/e/3/sess_4b1e384ad74619bd212e236e52a5a174If`。 要使用 N 参数，必须在使用前先创建好这些目录。在 ext/session 目录下有个小的 shell 脚本名叫 mod_files.sh 可以用来做这件事。此外注意如果使用了 N 参数并且 N 大于 0，那么将不会执行自动垃圾回收，更多信息见 php.ini。另外如果用了 N 参数，要确保将 session.save_path 的值用双引号 "quotes" 括起来，因为分隔符分号（ ;）在 php.ini 中也是注释符号。   
`session.save_path string`   
在定义session.save_path中可以定义多级存放的路径，修改php.ini   
`session.save_path = "3;/tmp/session"`   
将session文件分成两级存放，即`/tmp/session/c/m/d/0/o/sess_cmd0on71pr8kf1dogkesn59s30`，取前两位字符，但是php并不生成目录，需要自己手工生成，所以写了个脚本来生成初始的目录。   
附上一个创建四级文件夹包的代码。

```php
#!/usr/local/php/bin/php
<?php
$string = '0123456789abcdefghijklmnopqrstuvwxyz';
$length = strlen($string);
for($i=0;$i<$length;$i++){
    for($j=0;$j<$length;$j++){
        for($k=0;$k<$length;$k++){
            for($m=0;$m<$length;$m++){
                echo $path = '/tmp/session/'.$string[$i].'/'.$string[$j].'/'.$string[$k].'/'.$string[$m];
                createFolder($path);
                echo "\n";
            }
        }
    }
}

function createFolder($path){
    if(!file_exists($path)){
        createFolder(dirname($path));
        mkdir($path,0777);
    }
}
exit;
?>
```
