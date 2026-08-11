---
title: "golang创建Excel表格"
date: "2025-08-05 11:36:52"
slug: "golang-chuang-jian-excel-biao-ge"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/05/golang创建Excel表格/"
  - "/2025/08/05/golang创建Excel表格.html"
  - "/golang创建Excel表格/"
  - "/golang创建Excel表格.html"
  - "/2025/08/05/golang-chuang-jian-excel-biao-ge/"
  - "/2025/08/05/golang-chuang-jian-excel-biao-ge.html"
  - "/golang-chuang-jian-excel-biao-ge.html"
---
golang创建Excel表格

使用的库是excelize

地址：https://github.com/360EntSecGroup-Skylar/excelize

代码演示

```go
package main

import (
	"fmt"
	"github.com/360EntSecGroup-Skylar/excelize/v2"
)

func main() {
	f := excelize.NewFile()

	// 选择默认表 Sheet1
	streamWriter, err := f.NewStreamWriter("Sheet1")
	if err != nil {
		fmt.Println(err)
		return
	}

	// 表头
	excelHeader := []interface{}{
		excelize.Cell{Value: "年龄"},
		excelize.Cell{Value: "名字"},
		excelize.Cell{Value: "生日"},
		excelize.Cell{Value: "国籍"},
	}

	// 生成CellName 比如 A1
	headerCellName, err := excelize.CoordinatesToCellName(1, 1)
	if err != nil {
		fmt.Println(err)
		return
	}

	// 写表头
	if err := streamWriter.SetRow(headerCellName, excelHeader); err != nil {
		fmt.Println(err)
		return
	}

	row := []interface{}{
		"45",
		"名字1",
		"2023-12-12",
		"中国",
	}

	//生成CellName 比如 A2
	cell, err := excelize.CoordinatesToCellName(1, 2)
	if err != nil {
		fmt.Println(err)
		return
	}

	if err := streamWriter.SetRow(cell, row); err != nil {
		fmt.Println(err)
		return
	}

	//
	if err := streamWriter.Flush(); err != nil {
		fmt.Println(err)
		return
	}

	// 保存文件
	if err := f.SaveAs("sheet1.xlsx"); err != nil {
		fmt.Println(err)
		return
	}

	fmt.Println("保存成功")

}
```
