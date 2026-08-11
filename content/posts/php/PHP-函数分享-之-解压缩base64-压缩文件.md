---
title: "PHP 函数分享 之 解压缩base64 压缩文件"
date: "2025-07-03 11:58:16"
slug: "php-han-shu-fen-xiang-zhi-jie-ya-suo-base64-ya-suo-wen-jian"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/07/03/PHP-函数分享-之-解压缩base64-压缩文件/"
  - "/2025/07/03/PHP-函数分享-之-解压缩base64-压缩文件.html"
  - "/PHP-函数分享-之-解压缩base64-压缩文件/"
  - "/PHP-函数分享-之-解压缩base64-压缩文件.html"
  - "/2025/07/03/php-han-shu-fen-xiang-zhi-jie-ya-suo-base64-ya-suo-wen-jian/"
  - "/2025/07/03/php-han-shu-fen-xiang-zhi-jie-ya-suo-base64-ya-suo-wen-jian.html"
  - "/php-han-shu-fen-xiang-zhi-jie-ya-suo-base64-ya-suo-wen-jian.html"
---
解压缩base64 压缩文件，稍微解释一下，比如你有一个pdf文件，使用软件压缩成了.gz格式的文件，然后再把这个文件做成了basa64 String 传输给某个人，比如这个人就是我，好吧，问题来了，我们要实现一个过程，就是反解这个文件，将base64 string 转成 .gz文件，然后再把.gz文件解压。

```php
function actionPdf(){
    $pdf_base64 = BASE64_DATA_PATH;
    //Get File content from txt file
    $pdf_base64_handler = fopen($pdf_base64,'r');
    $pdf_content = fread ($pdf_base64_handler,filesize($pdf_base64));
    fclose ($pdf_base64_handler);
    //Decode pdf content
    $pdf_decoded = base64_decode ($pdf_content);
    //Write data back to pdf file
    $pdf = fopen (PDF_FILE_PATH,'w');
    fwrite ($pdf,$pdf_decoded);
    //close output file
    fclose ($pdf);

    // This input should be from somewhere else, hard-coded in this example
    $file_name = PDF_FILE_PATH;

    // Raising this value may increase performance
    $buffer_size = 4096; // read 4kb at a time
    $out_file_name = str_replace('.gz', '', $file_name);

    // Open our files (in binary mode)
    $file = gzopen($file_name, 'rb');
    $out_file = fopen($out_file_name, 'wb');

    // Keep repeating until the end of the input file
    while(!gzeof($file)) {
        // Read buffer-size bytes
        // Both fwrite and gzread and binary-safe
        fwrite($out_file, gzread($file, $buffer_size));
    }

    // Files are done, close files
    fclose($out_file);
    gzclose($file);


    // $base64Data = file_get_contents(BASE64_DATA_PATH);
    // $data = base64_decode($base64Data);
    // file_put_contents(PDF_FILE_PATH,$data);
}
```

哈哈，参考java版本重写，还有node版本的。

PS：

每个人都是从生到死，但是活法不一样，就比如这个方法，从开始到最后做完了自己改做的事情。选择一个语言走下去吧【选择一个活法，直到死去】。

我们都想在自己的一生过好多种不同的活法，但是事实上，不可能呀。来来学点编程，体会一下，不同的人生【语言】带给你的不同体验。


