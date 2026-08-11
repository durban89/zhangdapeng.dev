---
title: "PHP下载远程图片的方法"
date: "2025-06-09 11:56:59"
slug: "php-xia-zai-yuan-cheng-tu-pian-de-fang-fa"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/09/PHP下载远程图片的方法/"
  - "/2025/06/09/PHP下载远程图片的方法.html"
  - "/PHP下载远程图片的方法/"
  - "/PHP下载远程图片的方法.html"
  - "/2025/06/09/php-xia-zai-yuan-cheng-tu-pian-de-fang-fa/"
  - "/2025/06/09/php-xia-zai-yuan-cheng-tu-pian-de-fang-fa.html"
  - "/php-xia-zai-yuan-cheng-tu-pian-de-fang-fa.html"
---
### [获取远程文件大小及信息的函数](#1)

```php
<?php
function getFileSize($url)
{
    $url = parse_url($url);
    if ($fp = @fsockopen($url[’host’], empty($url[’port’]) ? 80 : $url[’port’], $error)) {
        fputs($fp, "GET " . (empty($url[’path’]) ? ’ / ’ : $url[’path’]) . " HTTP/1.1\r\n");
        fputs($fp, "Host:$url[host]\r\n\r\n");
        while (!feof($fp)) {
            $tmp = fgets($fp);
            if (trim($tmp) == ’’) {
                break;
            } else if (preg_match(’ / Content - Length:( . * ) / si’, $tmp, $arr)) {
                return trim($arr[1]);
            }
        }
        return null;
    } else {
        return null;
    }
}

echo getFileSize("http://www.dianpub.com/download/xml.rar");
```

### [图片](#2)

```php
<?php
//记录程序开始的时间
$BeginTime = getmicrotime();

function GrabImage($url, $filename = "")
{
    if ("" == $url): return false;
    if ("" == $filename) {
        $ext = strrchr($url, ".");
        if (".gif" != $ext && ".jpg" != $ext): return false;
        $filename = date("dMYHis") . $ext;
    }
    ob_start();
    readfile($url);
    $img = ob_get_contents();
    ob_end_clean();
    $size = strlen($img);
    $fp2 = @fopen($filename, "a");
    fwrite($fp2, $img);
    fclose($fp2);
    return $filename;
}

$img = GrabImage("http://www.dianpub.com/images/_1978837_detector_ap100.jpg", "");
if ($img): echo '<pre><img src="' . $img . '"></pre>';else:echo "false";

//记录程序运行结束的时间
$EndTime = getmicrotime();

//返回运行时间
exit($EndTime - $BeginTime);
```

### [全文下载图片](#3)

```php
<?php
if (!empty($saveremoteimg)) {
    $body = stripslashes($body);
    $img_array = [];
    preg_match_all("/(src|SRC)=[\"|'| ]{0,}(http:\/\/(.*)\.(gif|jpg|jpeg|bmp|png))/isU", $body, $img_array);
    $img_array = array_unique($img_array[2]);
    set_time_limit(0);
    $imgUrl = $img_dir . "/" . strftime("%Y%m%d", time());
    $imgPath = $base_dir . $imgUrl;
    $milliSecond = strftime("%H%M%S", time());
    if (!is_dir($imgPath)) {
        @mkdir($imgPath, 0777);
    }

    foreach ($img_array as $key => $value) {
        $value = trim($value);
        $get_file = @file_get_contents($value);
        $rndFileName = $imgPath . "/" . $milliSecond . $key . "." . substr($value, -3, 3);
        $fileurl = $imgUrl . "/" . $milliSecond . $key . "." . substr($value, -3, 3);
        if ($get_file) {
            $fp = @fopen($rndFileName, "w");
            @fwrite($fp, $get_file);
            @fclose($fp);
        }
        $body = ereg_replace($value, $fileurl, $body);
    }
    $body = addslashes($body);
}
```

### [PHP远程文件下载类（支持断点续传）](#4)

1）功能:支持断点续传的下载,能计算传输率,能控制传输率

简易使用方法:

```php
<?php
$object = new httpdownload();
$object->set_byfile($file);//服务器文件名,包括路径
$object->filename = $filename;//下载另存为的文件名
$object->download();
```

类文件：

```php
<?php
class httpdownload
{
    public $data = null;
    public $data_len = 0;
    public $data_mod = 0;
    public $data_type = 0;
    public $data_section = 0; //section download
    public $sentSize = 0;
    public $handler = ['auth' => null];
    public $use_resume = true;
    public $use_autoexit = false;
    public $use_auth = false;
    public $filename = null;
    public $mime = null;
    public $bufsize = 2048;
    public $seek_start = 0;
    public $seek_end = -1;
    public $totalsizeref = 0;
    public $bandwidth = 0;
    public $speed = 0;
    public function initialize()
    {
        global $HTTP_SERVER_VARS;
        if ($this->use_auth) {
            if (!$this->_auth()) {
                header('WWW-Authenticate: Basic realm="Please enter your username and password"');
                header('HTTP/1.0 401 Unauthorized');
                header('status: 401 Unauthorized');
                if ($this->use_autoexit) {
                    exit();
                }

                return false;
            }
        }
        if (null == $this->mime) {
            $this->mime = "application/octet-stream";
        }
        //default mime
        if (isset($_SERVER['HTTP_RANGE']) || isset($HTTP_SERVER_VARS['HTTP_RANGE'])) {
            if (isset($HTTP_SERVER_VARS['HTTP_RANGE'])) {
                $seek_range = substr($HTTP_SERVER_VARS['HTTP_RANGE'], strlen('bytes='));
            } else {
                $seek_range = substr($_SERVER['HTTP_RANGE'], strlen('bytes='));
            }

            $range = explode('-', $seek_range);
            if ($range[0] > 0) {
                $this->seek_start = intval($range[0]);
            }
            if ($range[1] > 0) {
                $this->seek_end = intval($range[1]);
            } else {
                $this->seek_end = -1;
            }

            if (!$this->use_resume) {
                $this->seek_start = 0;
                //header("HTTP/1.0 404 Bad Request");
                //header("Status: 400 Bad Request");
                //exit;
                //return false;
            } else {
                $this->data_section = 1;
            }
        } else {
            $this->seek_start = 0;
            $this->seek_end = -1;
        }
        $this->sentSize = 0;
        return true;
    }

    public function header($size, $seek_start = null, $seek_end = null)
    {
        header('Content-type: ' . $this->mime);
        header('Content-Disposition: attachment; filename="' . $this->filename . '"');
        header('Last-Modified: ' . date('D, d M Y H:i:s \G\M\T', $this->data_mod));
        if ($this->data_section && $this->use_resume) {
            header("HTTP/1.0 206 Partial Content");
            header("Status: 206 Partial Content");
            header('Accept-Ranges: bytes');
            header("Content-Range: bytes $seek_start-$seek_end/$size");
            header("Content-Length: " . ($seek_end - $seek_start + 1));
        } else {
            header("Content-Length: $size");
        }
    }

    public function download_ex($size)
    {
        if (!$this->initialize()) {
            return false;
        }

        ignore_user_abort(true);
        //Use seek end here
        if ($this->seek_start > ($size - 1)) {
            $this->seek_start = 0;
        }

        if ($this->seek_end <= 0) {
            $this->seek_end = $size - 1;
        }

        $this->header($size, $seek, $this->seek_end);
        $this->data_mod = time();
        return true;
    }

    public function download()
    {
        if (!$this->initialize()) {
            return false;
        }

        try {
            error_log("begin download\n", 3, "/usr/local/www/apache22/LOGS/apache22_php.err");
            $seek = $this->seek_start;
            $speed = $this->speed;
            $bufsize = $this->bufsize;
            $packet = 1;
            //do some clean up
            @ob_end_clean();
            $old_status = ignore_user_abort(true);
            @set_time_limit(0);
            $this->bandwidth = 0;
            $size = $this->data_len;
            if (0 == $this->data_type) //download from a file {
            {
                $size = filesize($this->data);
            }

            if ($seek > ($size - 1)) {
                $seek = 0;
            }

            if (null == $this->filename) {
                $this->filename = basename($this->data);
            }

            $res = fopen($this->data, 'rb');
            if ($seek) {
                fseek($res, $seek);
            }

            if ($this->seek_end < $seek) {
                $this->seek_end = $size - 1;
            }

            $this->header($size, $seek, $this->seek_end); //always use the last seek
            $size = $this->seek_end - $seek + 1;
            while (!(connection_aborted() || connection_status() == 1) && $size > 0) {
                if ($size < $bufsize) {
                    echo fread($res, $size);
                    $this->bandwidth += $size;
                    $this->sentSize += $size;
                } else {
                    echo fread($res, $bufsize);
                    $this->bandwidth += $bufsize;
                    $this->sentSize += $bufsize;
                }
                $size -= $bufsize;
                flush();
                if ($speed > 0 && ($this->bandwidth > $speed * $packet * 1024)) {
                    sleep(1);
                    $packet++;
                }
            }
            fclose($res);

            if (1 == $this->data_type) //download from a string
            {
                if ($seek > ($size - 1)) {
                    $seek = 0;
                }

                if ($this->seek_end < $seek) {
                    $this->seek_end = $this->data_len - 1;
                }

                $this->data = substr($this->data, $seek, $this->seek_end - $seek + 1);
                if (null == $this->filename) {
                    $this->filename = time();
                }

                $size = strlen($this->data);
                $this->header($this->data_len, $seek, $this->seek_end);
                while (!connection_aborted() && $size > 0) {
                    if ($size < $bufsize) {
                        $this->bandwidth += $size;
                        $this->sentSize += $size;
                    } else {
                        $this->bandwidth += $bufsize;
                        $this->sentSize += $bufsize;
                    }
                    echo substr($this->data, 0, $bufsize);
                    $this->data = substr($this->data, $bufsize);
                    $size -= $bufsize;
                    flush();
                    if ($speed > 0 && ($this->bandwidth > $speed * $packet * 1024)) {
                        sleep(1);
                        $packet++;
                    }
                }
            } else if (2 == $this->data_type) {
                //just send a redirect header
                header('location: ' . $this->data);
            }
            if ($this->totalsizeref == $this->sentSize) {
                error_log("end download\n", 3, "/usr/local/www/apache22/LOGS/apache22_php.err");
            } else {
                error_log("download is canceled\n", 3, "/usr/local/www/apache22/LOGS/apache22_php.err");
            }

            if ($this->use_autoexit) {
                exit();
            }

            //restore old status
            ignore_user_abort($old_status);
            set_time_limit(ini_get("max_execution_time"));
        } catch (Exception $e) {
            error_log("cancel download\n" . $e, 3, "/usr/local/www/apache22/LOGS/apache22_php.err");
        }
        return true;
    }

    public function set_byfile($dir)
    {
        if (is_readable($dir) && is_file($dir)) {
            $this->data_len = 0;
            $this->data = $dir;
            $this->data_type = 0;
            $this->data_mod = filemtime($dir);
            $this->totalsizeref = filesize($dir);
            return true;
        } else {
            return false;
        }
    }

    public function set_bydata($data)
    {
        if ('' == $data) {
            return false;
        }

        $this->data = $data;
        $this->data_len = strlen($data);
        $this->data_type = 1;
        $this->data_mod = time();
        return true;
    }

    public function set_byurl($data)
    {
        $this->data = $data;
        $this->data_len = 0;
        $this->data_type = 2;
        return true;
    }

    public function set_lastmodtime($time)
    {
        $time = intval($time);
        if ($time <= 0) {
            $time = time();
        }

        $this->data_mod = $time;
    }

    public function _auth()
    {
        if (!isset($_SERVER['PHP_AUTH_USER'])) {
            return false;
        }

        if (isset($this->handler['auth']) && function_exists($this->handler['auth'])) {
            return $this->handler['auth']('auth', $_SERVER['PHP_AUTH_USER'], $_SERVER['PHP_AUTH_PW']);
        } else {
            return true;
        }
        //you must use a handler
    }
}
```

### [PHP使用GD库下载远程图片](#5)

```php
<?php
$imgname = "http://imgdujia.kuxun.cn/newpic/929/812929/4.jpg";
$src_im = imagecreatefromjpeg($imgname);
$srcW = ImageSX($src_im); //获得图像的宽
$srcH = ImageSY($src_im); //获得图像的高

$dst_im = ImageCreateTrueColor($srcW, $srcH); //创建新的图像对象

imagecopy($dst_im, $src_im, 0, 0, 0, 0, $srcW, $srcH);
imagejpeg($dst_im, "newpic.jpg"); //创建缩略图文件

echo "<img src="newpic . jpg" mce_src="newpic . jpg"></img>";
```

```php
<?php
header("Content-type: image/png");
$im = imagecreatefromjpeg("http://postimg.mop.com/200602/02/74/122374/200602022335325121.JPG");
$white = imagecolorallocate($im, 0xF9, 0xD7, 0xCD);
imagefill($im, 0, 0, $white);
$text_color = imagecolorallocate($im, 233, 14, 91);
imagestring($im, 1, 5, 5, "A Simple Text String", $text_color);
imagepng($im);
imagedestroy($im);
``` 
