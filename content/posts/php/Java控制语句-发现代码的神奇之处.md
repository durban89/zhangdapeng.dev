---
title: "Java控制语句 发现代码的神奇之处"
date: "2025-06-25 10:10:00"
slug: "java-kong-zhi-yu-ju-fa-xian-dai-ma-de-shen-qi-zhi-chu"
categories: ["技术"]
tags: ["Java"]
aliases:
  - "/2025/06/25/Java控制语句-发现代码的神奇之处/"
  - "/2025/06/25/Java控制语句-发现代码的神奇之处.html"
  - "/Java控制语句-发现代码的神奇之处/"
  - "/Java控制语句-发现代码的神奇之处.html"
  - "/2025/06/25/java-kong-zhi-yu-ju-fa-xian-dai-ma-de-shen-qi-zhi-chu/"
  - "/2025/06/25/java-kong-zhi-yu-ju-fa-xian-dai-ma-de-shen-qi-zhi-chu.html"
  - "/java-kong-zhi-yu-ju-fa-xian-dai-ma-de-shen-qi-zhi-chu.html"
---
神奇之旅一：九九乘法表

虽然循环的有点晕，但是一步一步来的话还是蛮清晰的

```java
public class Print99 {
	public static void main(String args[]){
		System.out.println("99乘法表");
		System.out.print("\t");
		for(int i = 1; i <= 9; i++){
			System.out.print(i+"\t");
		}
		System.out.println();
		for(int i=1;i<=9;i++){
			System.out.print(i+"\t");
			for(int j = 1;j<=9;j++){
				if(j<=i){
					System.out.print(i*j+"\t");
				}
			}
			System.out.println();
		}
	}
	
}
```

结果如下：

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529458276/gowhich/Print99_WX20180620-092730.png)

神奇之旅二：螺旋型数组。

仔细看哦，会转圈的哦

这个比上一个还要晕

```java
import java.io.*;
public class RingDemo {
	public static void main(String args[]){
		String strln = "";
		System.out.println("请输入矩阵的列数");
		InputStreamReader input = new InputStreamReader(System.in);
		BufferedReader buff = new BufferedReader(input);
		try{
			strln = buff.readLine();
			
		}catch(IOException e){
			System.out.println(e.toString());
		}
		int int1 = Integer.parseInt(strln);
		int n = int1;
		System.out.println("这是行列数为"+n+"的螺旋型数组");
		int intA = 1;
		int[][] array = new int[n][n];
		//初始化行数
		int intB;
		if(n%2 == 0){
			intB = n / 2;
		}else{
			intB = n/2 + 1;
		}
		for(int i=0;i<=intB;i++){
			//从左到右
			for(int j=i;j<n-i;j++){
				array[i][j] = intA;
				intA++;
			}
			//从上到下
			for(int k = i;k<n-i;k++){
				array[k][n -i - 1] = intA;
				intA++;
			}
			//从右到左
			for(int l = n-i-2;l>=i;l--){
				array[n -i -1][l] = intA;
				intA++;
			}
			//从下到上
			for(int m = n-i-2;m > i;m--){
				array[m][i] = intA;
				intA++;
			}
		}
		//输出数组
		for(int i=0;i<n;i++){
			for(int j = 0;j<n;j++){
				System.out.print(array[i][j]+"\t");
			}
			System.out.println();
		}
		
	}
}
```

结果如下：

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1529458276/gowhich/RingDemo_WX20180620-092911.png)

