---
title: "Java的强制转换的练习"
date: "2025-06-24 15:30:00"
slug: "java-de-qiang-zhi-zhuan-huan-de-lian-xi"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/24/Java的强制转换的练习/"
  - "/2025/06/24/Java的强制转换的练习.html"
  - "/Java的强制转换的练习/"
  - "/Java的强制转换的练习.html"
  - "/2025/06/24/java-de-qiang-zhi-zhuan-huan-de-lian-xi/"
  - "/2025/06/24/java-de-qiang-zhi-zhuan-huan-de-lian-xi.html"
  - "/java-de-qiang-zhi-zhuan-huan-de-lian-xi.html"
---
### [第一个练习](#1)

```java
public class QiangZhiZhuanHuan {
	public static void main(String args[]){
		int i1 = 123;
		byte b = (byte)i1;
		System.out.println("int 强制类型转换为 byte 后值等于"+b);
	}
}
```

输出的结果是：

```bash
int 强制类型转换为 byte 后值等于123
```

---

### [第二个练习](#2)

```java
public class QiangZhiZhuanHuan2 {
	public static void main(String args[]){
		int i1 = 128;
		byte b = (byte)i1;
		System.out.println("int 强制类型转换 byte 后的值等于"+b);
		double d = 123.456;
		int i2 = (int)d;
		System.out.println("double 强制类型转换为 int 后的值等于"+i2);
	}
}
```

输出的结果是：

```bash
int 强制类型转换 byte 后的值等于-128
double 强制类型转换为 int 后的值等于123
```

---

### [第三个练习](#3)

```java
public class QiangZhiZhuanHuan3 {
	public static void main(String args[]){
		char c1 = 'A';
		int i = c1 + 1;
		char c2 = (char) i;
		System.out.println("int 类型强制转换为char 类型的值为"+c2);
	}
}
```

输出的结果是：

```bash
int 类型强制转换为char 类型的值为B
```

