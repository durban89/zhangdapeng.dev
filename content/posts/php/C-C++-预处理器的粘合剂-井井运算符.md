---
title: "C/C++ 预处理器的粘合剂：##运算符"
date: "2025-06-11 11:00:03"
slug: "cc-yu-chu-li-qi-de-nian-he-ji-yun-suan-fu"
categories: ["技术"]
tags: ["C/C++"]
aliases:
  - "/2025/06/11/C-C++-预处理器的粘合剂-井井运算符/"
  - "/2025/06/11/C-C++-预处理器的粘合剂-井井运算符.html"
  - "/2025/06/11/cc-yu-chu-li-qi-de-nian-he-ji-yun-suan-fu/"
  - "/2025/06/11/cc-yu-chu-li-qi-de-nian-he-ji-yun-suan-fu.html"
  - "/cc-yu-chu-li-qi-de-nian-he-ji-yun-suan-fu.html"
---
实例代码:

```c
/* glue.c -- 使用##运算符 */
#include <stdio.h>
#define XNAME(n) x ## n
#define PRINT_XN(n) printf("x" #n " = %d\n", x ## n)

int main(void)
{
	int XNAME(1) = 14;
	int XNAME(2) = 20;
	PRINT_XN(1);
	PRINT_XN(2);
	return 0;
}
```

运行结果如下：

```shell
x1 = 14
x2 = 20
```
