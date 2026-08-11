---
title: "C/C++ 利用宏参数创建字符串"
date: "2025-06-11 10:59:10"
slug: "cc-li-yong-hong-can-shu-chuang-jian-zi-fu-chuan"
categories: ["技术"]
tags: ["C/C++"]
aliases:
  - "/2025/06/11/C/C++-利用宏参数创建字符串/"
  - "/2025/06/11/C/C++-利用宏参数创建字符串.html"
  - "/C/C++-利用宏参数创建字符串/"
  - "/C/C++-利用宏参数创建字符串.html"
  - "/2025/06/11/C-C++-利用宏参数创建字符串/"
  - "/2025/06/11/C-C++-利用宏参数创建字符串.html"
  - "/2025/06/11/cc-li-yong-hong-can-shu-chuang-jian-zi-fu-chuan/"
  - "/2025/06/11/cc-li-yong-hong-can-shu-chuang-jian-zi-fu-chuan.html"
  - "/cc-li-yong-hong-can-shu-chuang-jian-zi-fu-chuan.html"
---
代码示例：

```c
/* subst.c -- 在字符串中进行替换 */
#include <stdio.h>
#define PSOR(x) printf("The square of " #x " is %d\n", ((x)*(x)))

int main(void){
	int y = 5;
	PSOR(y);
	PSOR(2 + 4);
	return 0;
}
```

运行结果为：

```shell
The square of y is 25
The square of 2 + 4 is 36
```

