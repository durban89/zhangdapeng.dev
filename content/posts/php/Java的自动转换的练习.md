---
title: "Java的自动转换的练习"
date: "2025-06-24 15:30:04"
slug: "java-de-zi-dong-zhuan-huan-de-lian-xi"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/24/Java的自动转换的练习/"
  - "/2025/06/24/Java的自动转换的练习.html"
  - "/Java的自动转换的练习/"
  - "/Java的自动转换的练习.html"
  - "/2025/06/24/java-de-zi-dong-zhuan-huan-de-lian-xi/"
  - "/2025/06/24/java-de-zi-dong-zhuan-huan-de-lian-xi.html"
  - "/java-de-zi-dong-zhuan-huan-de-lian-xi.html"
---
### [Example First](#1)

```java
public class ZiDongZhuanHuan {
	public static void main(String args[]){
		short s = 3;
		int i = 3;
		float f=1.0f;
		double d1= f;
		long l = 1234l;
		double d2 = l;
		
		System.out.println("short类型自动转换为int类型"+ i);
		System.out.println("float类型自动转换为double类型"+d1);
		System.out.println("long类型自动转换为double类型"+d2);
		
		
	}
}
```

得到的结果是：

```bash
short类型自动转换为int类型3
float类型自动转换为double类型1.0
long类型自动转换为double类型1234.0
```

---

### [Example Second](#2)

```java
public class ZiDongZhuanHuan2 {
	public static void main(String args[]){
		int l = 123123123;
		float d = l;
		System.out.println("int 自动转换为 float后的值为"+d);
	}
}
```

结果是：

```bash
int 自动转换为 float后的值为1.2312312E8
```

---

### [Example Third](#3)

```java
public class ZiDongZhuanHuan3 {
	public static void main(String args[]){
		char c1 = 'a';
		int i1 = c1;
		System.out.println("char 类型自动转换为 int 后的值等于"+i1);
		char c2 = 'A';
		int i2 = c2+1;
		System.out.println("char 类型和int类型计算后的值为"+i2);
		
	}
}
```

结果是：

```bash
char 类型自动转换为 int 后的值等于97
char 类型和int类型计算后的值为66
```
