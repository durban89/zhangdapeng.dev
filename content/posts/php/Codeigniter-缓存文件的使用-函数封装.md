---
title: "Codeigniter 缓存文件的使用 函数封装"
date: "2025-06-27 14:15:12"
slug: "codeigniter-huan-cun-wen-jian-de-shi-yong-han-shu-feng-zhuang"
categories: ["技术"]
tags: ["PHP", "CodeIgniter"]
aliases:
  - "/2025/06/27/Codeigniter-缓存文件的使用-函数封装/"
  - "/2025/06/27/Codeigniter-缓存文件的使用-函数封装.html"
  - "/Codeigniter-缓存文件的使用-函数封装/"
  - "/Codeigniter-缓存文件的使用-函数封装.html"
  - "/2025/06/27/codeigniter-huan-cun-wen-jian-de-shi-yong-han-shu-feng-zhuang/"
  - "/2025/06/27/codeigniter-huan-cun-wen-jian-de-shi-yong-han-shu-feng-zhuang.html"
  - "/codeigniter-huan-cun-wen-jian-de-shi-yong-han-shu-feng-zhuang.html"
---
Codeigniter 缓存文件的使用 函数封装

```php
if(!function_exists('cache_read')){
    function cache_read($file, $dir = '', $mode = '') {
        $file = _get_cache_file($file, $dir);
        if(!is_file($file)) return NULL;
        return $mode ? read_file($file) : include $file;
    }
}
  
if(!function_exists('cache_write')){
    function cache_write($file, $string, $dir = '') {
        if(is_array($string)) {
            $string = "<?php return ".var_export($string, true)."; ?>";
            $string =  str_replace(array(chr(13), chr(10), "\n", "\r", "\t", '  '),array('', '', '', '', '', ''), $string);
        }
        $file = _get_cache_file($file, $dir);
        return write_file($file, $string);
    }
}
  
  
if(!function_exists('cache_delete')){
    function cache_delete($file, $dir = '') {
        $file = _get_cache_file($file, $dir);
        return unlink($file);
    }
}
  
  
if(!function_exists('_get_cache_file')){
    function _get_cache_file($file, $dir) {
        $path = config_item('cache_path') ? config_item('cache_path') : APPPATH . 'cache/';
        return ($dir ? $path.$dir.'/'.$file : $path.$file);
    }
}
```

