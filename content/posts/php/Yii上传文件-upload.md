---
title: "Yii上传文件 upload"
date: "2025-06-20 14:33:39"
slug: "yii-shang-chuan-wen-jian-upload"
categories: ["技术"]
tags: ["PHP", "Yii"]
aliases:
  - "/2025/06/20/Yii上传文件-upload/"
  - "/2025/06/20/Yii上传文件-upload.html"
  - "/Yii上传文件-upload/"
  - "/Yii上传文件-upload.html"
  - "/2025/06/20/yii-shang-chuan-wen-jian-upload/"
  - "/2025/06/20/yii-shang-chuan-wen-jian-upload.html"
  - "/yii-shang-chuan-wen-jian-upload.html"
---
yii常规post方式提交表单方式请参考：

<http://www.yiichina.com/forum/topic/45/>

除了常规post提交方式外，还有异步提交方式。  
原理是使用iframe代替原来的页面跳转，大大提升用户体验。

1，前端html代码

```html
<form id="upForm" action="<?php echo $this->createUrl('repairUpload'); ?>" method="post" enctype    ="multipart/form-data" target="upload_target">  
    <input type="file" name="repair_attached_file" id="repair_attached_file" /><input type="subm    it" name="submitBtn" value="立即上传" />  
    <iframe id="upload_target" name="upload_target" src="#" style="width:0;height:0;border:0px solid #fff;"></iframe>  
</form>  
<span id="upload_repairinfo_success" style="color:blue;"></span>  

<script type="text/javascript">  
function startUpload() {  
    var spanObj = document.getElementById("upload_repairinfo_success");  
    spanObj.innerHTML = " 开始上传";  
    document.getElementById("upForm").sumbit();  
}  
function stopUpload(responseText){  
    var spanObj = document.getElementById("upload_repairinfo_success");  
    //spanObj.innerHTML = "上传成功";  
    spanObj.innerHTML = responseText;  
}  
</script>
```

2、后端php代码

```php
public function actionRepairUpload(){  
    $attach = CUploadedFile::getInstanceByName('repair_attached_file');  
    $retValue = "";  
    if($attach->size > 3*1024*1024){  
        $retValue = "提示：文件大小不能超过3M";  
    }else{  
        $f = file_get_contents($attach->tempName);  
        $a = new Attachment();  
        $a->ref_type = "failParts";  
        $a->data = $f;  
        $a->file_path = $attach->name;  
        $a->save();  
        $retValue = $a->id;  
    }  
    echo "<script type='text/javascript'>window.top.window.stopUpload('{$retValue}')</script>";  
}
```
