---
title: "Java 算数运算 简单练习"
date: "2025-06-24 16:17:31"
slug: "java-suan-shu-yun-suan-jian-dan-lian-xi"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/24/Java-算数运算-简单练习/"
  - "/2025/06/24/Java-算数运算-简单练习.html"
  - "/Java-算数运算-简单练习/"
  - "/Java-算数运算-简单练习.html"
  - "/2025/06/24/java-suan-shu-yun-suan-jian-dan-lian-xi/"
  - "/2025/06/24/java-suan-shu-yun-suan-jian-dan-lian-xi.html"
  - "/java-suan-shu-yun-suan-jian-dan-lian-xi.html"
---
### [练习一](#1)

```java
public class SuanSu{
	public static void main(String args[]){
		int i1 = 7;
		int i2 = 3;
		int jia = i1 + i2;
		int jian = i1 - i2;
		int cheng = i1 * i2;
		int chu = i1 / i2;
		int yu = i1 % i2;
		
		System.out.println("进行加法运算得到的结果:"+jia);
		System.out.println("进行减法运算得到的结果:"+jian);
		System.out.println("进行乘法运算得到的结果:"+cheng);
		System.out.println("进行除法运算得到的结果:"+chu);
		System.out.println("进行余数运算得到的结果:"+yu);
	}
}
```

gowhich得到的结果是：

```bash
进行加法运算得到的结果:10
进行减法运算得到的结果:4
进行乘法运算得到的结果:21
进行除法运算得到的结果:2
进行余数运算得到的结果:1
```

### [练习二](#2)

```java
public class SuanSu2{
	public static void main(String args[]){
		int i1 = 7;
		int i2 = 0;
		int chu = i1 / i2;
		int yu = i1 % i2;
		
		System.out.println("进行除法运算的结果是:"+chu);
		System.out.println("进行余数运算的结果是:"+yu);
	}
	
}
```

gowhich得到的结果是：

```java
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at SuanSu2.main(SuanSu2.java:5)
```

### [练习三](#3)

```java
public class SuanSu3{
	public static void main(String args[]){
		String s1 = "Hello";
		String s2 = "World";
		
		String s3 = s1 + " " + s2;
		System.out.println(s3);
	}
}
```

gowhich得到的结果是：

```bash
Hello World
```

