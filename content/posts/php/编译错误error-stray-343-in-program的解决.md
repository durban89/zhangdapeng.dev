---
title: "编译错误error: stray ‘343’ in program的解决"
date: "2025-06-11 11:39:33"
slug: "bian-yi-cuo-wu-error-stray-343-in-program-de-jie-jue"
categories: ["技术"]
tags: ["C"]
aliases:
  - "/2025/06/11/编译错误error:-stray-‘343’-in-program的解决/"
  - "/2025/06/11/编译错误error:-stray-‘343’-in-program的解决.html"
  - "/编译错误error:-stray-‘343’-in-program的解决/"
  - "/编译错误error:-stray-‘343’-in-program的解决.html"
  - "/2025/06/11/编译错误error-stray-343-in-program的解决/"
  - "/2025/06/11/编译错误error-stray-343-in-program的解决.html"
  - "/2025/06/11/bian-yi-cuo-wu-error-stray-343-in-program-de-jie-jue/"
  - "/2025/06/11/bian-yi-cuo-wu-error-stray-343-in-program-de-jie-jue.html"
  - "/bian-yi-cuo-wu-error-stray-343-in-program-de-jie-jue.html"
---
c代码编译的错误提示：

```c
films1.c:15: error: stray ‘\200’ in program
films1.c:15: error: stray ‘\343’ in program
films1.c:15: error: stray ‘\200’ in program
```

代码如下：

```c
/* films1.c-- 使用结构数组 */
#include <stdio.h>
#define TSIZE 45 	/*存放片名的数组大小*/
#define FMAX 5		/* 对多的影片数 */
struct film{
	char title[TSIZE];
	int rating;
};
int main(void)
{
	struct film movies[FMAX];
	int i =0;
	int j;
	puts("Enter first movie title: ");
	while(i < FMAX && gets(movies[i].title) != NULL && movies[i].title != '\0')
	{
		puts("Enter your rating <0-10>");
		scanf("%d",&movies[i++].rating);
		while(getchar() != '\n')
		{
			continue;
		}
		puts("Enter next movie title (empty line to stop)");
	}
	
	if(i == 0)
	{
		printf("No data entered.");
	}
	else
	{
		printf("Here is the movie list: \n");
	}
	for(j=0;j<i;j++)
	{
		printf("Movie: %s Rating: %d \n", movies[j].title, movies[i].rating);
	}
	printf("Bye!\n");
	
	return 0;
}
```

经过搜索，找出了问题的所在：

这个错误是由于使用了中文引号或其他全角符号，还有一种就是有中文的空格（这个不容易观察），需调到顶格处，再用tab即可。  
通过 cat -A可以看到捣乱的字符。  
解决方案可以编写脚本过滤字符，看到有人说可以用gedit的替换功能，替换为标准空格。这个方法比较省力一点。尤其是代码较多时。一行一行改的想法还是放弃吧。

