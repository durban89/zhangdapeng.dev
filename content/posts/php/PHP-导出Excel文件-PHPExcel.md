---
title: "PHP 导出Excel文件 -- PHPExcel"
date: "2025-06-27 10:59:52"
slug: "php-dao-chu-excel-wen-jian-phpexcel"
categories: ["技术"]
tags: ["PHP"]
aliases:
  - "/2025/06/27/PHP-导出Excel文件-PHPExcel/"
  - "/2025/06/27/PHP-导出Excel文件-PHPExcel.html"
  - "/PHP-导出Excel文件-PHPExcel/"
  - "/PHP-导出Excel文件-PHPExcel.html"
  - "/2025/06/27/php-dao-chu-excel-wen-jian-phpexcel/"
  - "/2025/06/27/php-dao-chu-excel-wen-jian-phpexcel.html"
  - "/php-dao-chu-excel-wen-jian-phpexcel.html"
---
PHP 导出Excel文件 -- PHPExcel

PHPExcel是个很好用的，也是自己最近使用的，觉得不错。

PHPExcel的官网地址：<https://phpexcel.codeplex.com/>

下面举个如何使用的例子。

```php
//读取记录
$w_str = implode("and ", $wherestr);
$rcount = $DB->countRecords('zhiyuan_baoming', $w_str); //总记录数
$pcount = ceil($rcount / $pagesize);  //总页数
$startPage = ($page - 1) * $pagesize;
$condition = $w_str . $orderstr . $limitstr;
$list = $DB->getFiledValues('', 'zhiyuan_baoming', $condition);
foreach ($list as $k => & $v) {
    $v['catename'] = $_zhiyuan_baomingcate[$v['cid']]['name'];
}
$smarty->assign('list', $list);

//导出数据
require_once(PATH_ROOT.'includes/phpexcel/PHPExcel.php');

$objPHPExcel = new PHPExcel();

$s1 = $objPHPExcel->setActiveSheetIndex(0)->setTitle('志愿服务报名列表');
$s1 ->setCellValue('A1', '姓名')
    ->setCellValue('B1', '性别')
    ->setCellValue('C1', '班级')
    ->setCellValue('D1', '邮箱')
    ->setCellValue('E1', '电话')
    ->setCellValue('F1', '学号')
    ->setCellValue('G1', '报名时间');
$s1->getColumnDimension('A')->setWidth(22);

$line = 2;
foreach($list as $d)
{

    $s1->setCellValue('A'.$line, $d['name'])
        ->setCellValue('B'.$line, $d['sex']==1 ? '男' : '女')
        ->setCellValue('C'.$line, $d['banji'])
        ->setCellValue('D'.$line, $d['email'])
        ->setCellValue('E'.$line, $d['phone'])
        ->setCellValue('F'.$line, $d['xuehao'])
        ->setCellValue('G'.$line, date('Y-m-d H:i:s',$d['createtime']));
    $line++;
}

$objPHPExcel->setActiveSheetIndex(0);

header('Content-Type: application/vnd.ms-excel');
header('Content-Disposition: attachment;filename="'.'注册用户列表'.'.xls"');
header('Cache-Control: max-age=0');
header('Cache-Control: max-age=1');
$objWriter = PHPExcel_IOFactory::createWriter($objPHPExcel, 'Excel5');
$objWriter->save('php://output');
```

这个是我的实战实例，可以参考下，具体的可以去官网查看。

