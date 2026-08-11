---
title: "Java Web开发Tomcat中三种部署项目的方法"
date: "2025-06-27 09:45:54"
slug: "java-web-kai-fa-tomcat-zhong-san-zhong-bu-shu-xiang-mu-di-fang-fa"
categories: ["技术"]
tags: ["Java", "Tomcat"]
aliases:
  - "/2025/06/27/Java-Web开发Tomcat中三种部署项目的方法/"
  - "/2025/06/27/Java-Web开发Tomcat中三种部署项目的方法.html"
  - "/Java-Web开发Tomcat中三种部署项目的方法/"
  - "/Java-Web开发Tomcat中三种部署项目的方法.html"
  - "/2025/06/27/java-web-kai-fa-tomcat-zhong-san-zhong-bu-shu-xiang-mu-di-fang-fa/"
  - "/2025/06/27/java-web-kai-fa-tomcat-zhong-san-zhong-bu-shu-xiang-mu-di-fang-fa.html"
  - "/java-web-kai-fa-tomcat-zhong-san-zhong-bu-shu-xiang-mu-di-fang-fa.html"
---
Java Web开发Tomcat中三种部署项目的方法,开始java web开发必不可少的步骤，经过查找，觉得有篇文章介绍的不错

第一种方法：在tomcat中的conf目录中，在server.xml中的，<host/>节点中添加： 

```bash
<Context path="/hello" docBase="D:\eclipse3.2.2forwebtools\workspace\hello\WebRoot" debug="0" privileged="true"> 
</Context>
```

至于Context 节点属性，可详细见相关文档。   
  
第二种方法：将web项目文件件拷贝到webapps 目录中。   
  
第三种方法：很灵活，在conf目录中，新建 Catalina（注意大小写）＼localhost目录，在该目录中新建一个xml文件，名字可以随意取，只要和当前文件中的文件名不重复就行了，该xml文件的内容为： 

```bash
<Context path="/hello" docBase="D:\eclipse3.2.2forwebtools\workspace\hello\WebRoot" debug="0" privileged="true"> 
</Context>
```

第3个方法有个优点，可以定义别名。服务器端运行的项目名称为path，外部访问的URL则使用XML的文件名。这个方法很方便的隐藏了项目的名称，对一些项目名称被固定不能更换，但外部访问时又想换个路径，非常有效。   
  
第2、3还有优点，可以定义一些个性配置，如数据源的配置等。   
  
还有一篇 详细的 

1、直接放到Webapps目录下  

Tomcat的Webapps目录是Tomcat默认的应用目录，当服务器启动时，会加载所有这个目录下的应用。也可以将JSP程序打包成一个war包放在目录下，服务器会自动解开这个war包，并在这个目录下生成一个同名的文件夹。一个war包就是有特性格式的jar包，它是将一个Web程序的所有内容进行压缩得到。具体如何打包，可以使用许多开发工具的IDE环境，如Eclipse、NetBeans、ant、JBuilder等。也可以用cmd 命令：`jar -cvf applicationname.war package.*`；  

甚至可以在程序执行中打包：

```java
try{     
  string strjavahome = system.getproperty("java.home");
  strjavahome = strjavahome.substring(0, strjavahome.lastindexof(\\))+"\\bin\\";
  runtime.getruntime().exec("cmd /c start "+strjavahome+"jar cvf hello.war c:\\tomcat5.0\\webapps\\root\\*");
} catch(exception e) {
  system.out.println(e);
}
```

webapps这个默认的应用目录也是可以改变。打开Tomcat的conf目录下的server.xml文件，找到下面内容：

```bash
<Host name="localhost" debug="0" appBase="webapps" unpackWARs="true" autoDeloy="true" xmlValidation="falase" xmlNamespaceAware="false">
```

2、在server.xml中指定  

在Tomcat的配置文件中，一个Web应用就是一个特定的Context，可以通过在server.xml中新建Context里部署一个JSP应用程序。打开server.xml文件，在Host标签内建一个Context，内容如下。

```bash
<Context path="/myapp" reloadable="true" docBase="D:\myapp" workDir="D:\myapp\work"/>
```

其中path是虚拟路径，docBase是JSP应用程序的物理路径，workDir是这个应用的工作目录，存放运行是生成的于这个应用相关的文件。

3、创建一个Context文件  
    
以上两种方法，Web应用被服务器加载后都会在Tomcat的conf\catalina\localhost目录下生成一个XML文件，其内容如下：

```bash
<Context path="/admin" docBase="${catalina.home}/server/webapps/admin" debug="0" privileged="true"></Context>
```

可以看出，文件中描述一个应用程序的Context信息，其内容和server.xml中的Context信息格式是一致的，文件名便是虚拟目录名。您可以直接建立这样的一个xml文件，放在Tomcat的`conf\catalina\localhost`目录下。例子如下：  
注意：删除一个Web应用同时也要删除webapps下相应的文件夹祸server.xml中相应的Context，还要将Tomcat的`conf  
\catalina\localhost`目录下相应的xml文件删除。否则Tomcat仍会岸配置去加载。。。 

tomcat部署web应用主要有以下几种方式：

1．拷贝你的WAR文件或者你的web应用文件夹（包括该web的所有内容）到$CATALINA_BASE/webapps目录下。  
2．为你的web服务建立一个只包括context内容的XML片断文件，并把该文件放到$CATALINA_BASE/webapps目录下。这个web应用本身可以存储在硬盘上的任何地方。这种context片断提供了一种便利的方法来部署web应用，你不需要编辑server.xml，除非你想改变缺省的部署特性，安装一个新的web应用时不需要重启动Tomcat。  
3． 同方法2,只是将context片断放在CATALINA_BASE\conf\Catalina\localhost目录下.这种方法比方法2>要有效,笔者经过多次实验发现方法2不如后面这种方法好用.前者多次出现系统打不开的情况.  
4．直接在server.xml中</Host>前加上Context片断,使用这种方法时,tomcat会自动在CATALINA_BASE\conf\Catalina\localhost目录下生成一个文件片断.方法同方法3具有同样效果.这种方式需要将ROOT目录删除才行.

另外，为了让tomcat只运行`conf/server.xml`中指定的web应用，可以有以下几种办法：  
实现一:  
     1)将要部署的WEB应用放在webapps以外的路径, 并在server.xml相应的context中的docBase指定.  
     2)删除webapps中的所有文件夹, 以及conf/catalina/localhost下所有xml文件.  
     注: webapps是server.xml中的Host元素的appBase属性的值.   
实现二:  
     1) 修改server.xml中Host元素的属性, 添加或修改: `deployXML="false"` `deployOnStartup="false"` `autoDeploy="false"`  
     2) 含义:  
     `deployXML="false"`: 不部署conf/catalina/localhost下的xml相应的WEB应用     
     `deployOnStartup="false"` : tomcat启动时, 不部署webapps下的所有web应用     
     `autoDeploy="false"`: 避免tomcat在扫描改动时, 再次把webapps下的web应用给部署进来.

---

参看文章：

http://shuyangyang.blog.51cto.com/1685768/1040127

