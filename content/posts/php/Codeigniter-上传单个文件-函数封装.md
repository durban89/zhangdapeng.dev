---
title: "Codeigniter 上传单个文件 函数封装"
date: "2025-06-27 14:15:09"
slug: "codeigniter-shang-chuan-dan-ge-wen-jian-han-shu-feng-zhuang"
categories: ["技术"]
tags: ["PHP", "CodeIgniter"]
aliases:
  - "/2025/06/27/Codeigniter-上传单个文件-函数封装/"
  - "/2025/06/27/Codeigniter-上传单个文件-函数封装.html"
  - "/Codeigniter-上传单个文件-函数封装/"
  - "/Codeigniter-上传单个文件-函数封装.html"
  - "/2025/06/27/codeigniter-shang-chuan-dan-ge-wen-jian-han-shu-feng-zhuang/"
  - "/2025/06/27/codeigniter-shang-chuan-dan-ge-wen-jian-han-shu-feng-zhuang.html"
  - "/codeigniter-shang-chuan-dan-ge-wen-jian-han-shu-feng-zhuang.html"
---
Codeigniter 上传单个文件 函数封装，记录下，方便以后使用

```php
if(!function_exists('upload_file')){
  
    function upload_file($field,$filetype,$maxsize){
        $CI = & get_instance();
        $CI->load->library('upload');
        $CI->upload->initialize(array('encrypt_name'=>TRUE,'overwrite'=>TRUE));
        $CI->upload->set_upload_path('static/attachments');
        $CI->upload->set_allowed_types($filetype);
        $CI->upload->set_max_filesize($maxsize);
        $CI->upload->do_upload($field);
        $info = $CI->upload->data();
        if($info['client_name']){
            return '/static/attachments/'.$info['client_name'];
        }else{
            return '';
        }
    }
}
```

