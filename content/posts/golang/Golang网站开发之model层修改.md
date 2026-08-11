---
title: "Golang网站开发之model层修改"
date: "2025-08-04 18:08:04"
slug: "golang-wang-zhan-kai-fa-zhi-model-ceng-xiu-gai"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Golang网站开发之model层修改/"
  - "/2025/08/04/Golang网站开发之model层修改.html"
  - "/Golang网站开发之model层修改/"
  - "/Golang网站开发之model层修改.html"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-model-ceng-xiu-gai/"
  - "/2025/08/04/golang-wang-zhan-kai-fa-zhi-model-ceng-xiu-gai.html"
  - "/golang-wang-zhan-kai-fa-zhi-model-ceng-xiu-gai.html"
---
本次修改主要原因是为了避免SQL注入，也是在此对database/sql进行了深入的了解，以加深了对interface的使用

先说下之前的model中父类（这里之所以叫父类，是为了理解，有些golang开发者可能觉得不应该这样叫，其实语言学多了，大概都是一个抽象的名词，其中具体的实现逻辑或者叫法不太一致，这里的父类也可以更改为你自己的叫法）中方法的弊端，就是容易被注入。原因是：我的一些SQL是通过拼接的方式实现的，必然存在这个劣势，而且很危险，但是当时开始学也不知道如何解决，这次解决掉。

这里简单记录下，之前的错误做法，以MergeWhere函数为例，

```go
// MergeWhere 合并where条件
func (w WhereValues) MergeWhere() string {
	where := []string{}

	if len(w) == 0 {
		return "1=1"
	}

	for k, v := range w {
		if v.Operator == "" {
			s := fmt.Sprintf("%s = %s", k, v.Value)
			where = append(where, s)
		} else {
			s := fmt.Sprintf("%s %s %s", k, v.Operator, v.Value)
			where = append(where, s)
		}
	}

	return strings.Join(where, " AND ")
}
```

从这个函数可以看出来，最后返回一个拼接的sql，而且值也是已经拼接好的，问题就在这里，下面看下修复后的代码

```go
// SortedKeys WhereValues
func (w WhereValues) SortedKeys() []string {
	sortedKeys := make([]string, 0)
	for k := range w {
		sortedKeys = append(sortedKeys, k)
	}

	sort.Strings(sortedKeys)

	return sortedKeys
}

// MergeWhere 合并where条件
func (w WhereValues) MergeWhere() (string, []interface{}) {
	where := []string{}
	value := make([]interface{}, len(w))

	if len(w) == 0 {
		return "1=1", nil
	}

	sortedKeys := w.SortedKeys()

	var j = 0
	for _, k := range sortedKeys {

		v := w[k]
		if v.Operator == "" {
			s := fmt.Sprintf("%s = ?", k)
			where = append(where, s)
		} else {
			s := fmt.Sprintf("%s %s ?", k, v.Operator)
			where = append(where, s)
		}

		value[j] = v.Value
		j++
	}

	return strings.Join(where, " AND "), value
}
```

上面的代码多返回一个value值，这个value值是一个[]interface{}，之所以这样做是因为，官方接口定义了接口参数是一个`...interface{}`类型，所以必须要符合规范要求，以方便接口调用

参考 <https://golang.org/src/database/sql/sql.go>

> func (db \*DB) Exec(query string, args ...interface{}) (Result, error)

> func (db \*DB) Query(query string, args ...interface{}) (\*Rows, error)

除此之外加了一个SortedKeys函数，保证参数跟占位符的顺序一致

下面看下如何使用

```go
func (p *ModelProperty) Query(s SelectValues, where WhereValues, offset int64, limit int64) ([]SelectResult, error) {
	var selectString = s.MergeSelect()

	// 多返回一个参数whereValue
	whereString, whereValue := where.MergeWhere()

	sql := fmt.Sprintf("SELECT %s FROM %s WHERE %s LIMIT %d, %d",
		selectString, p.TableName, whereString, offset, limit)

	// 注意这里多加了一个whereValue的参数，其使用方式注意下，后面加了三个点号
	rows, err := Conn.Query(sql, whereValue...)

	result := []SelectResult{}

	if err != nil {
		return result, err
	}

	selectField := s.MergeSelectValue()

	for rows.Next() {
		err = rows.Scan(selectField...)

		if err != nil {
			return result, err
		}

		tmpResult := s.MergeResultValues()

		result = append(result, tmpResult)
	}

	return result, nil
}
```
