---
title: "Eclipse总Maven Dependencies消失的解决办法"
date: "2025-07-04 11:48:07"
slug: "eclipse-zong-maven-dependencies-xiao-shi-de-jie-jue-ban-fa"
categories: ["技术"]
tags: ["Eclipse"]
aliases:
  - "/2025/07/04/Eclipse总Maven-Dependencies消失的解决办法/"
  - "/2025/07/04/Eclipse总Maven-Dependencies消失的解决办法.html"
  - "/Eclipse总Maven-Dependencies消失的解决办法/"
  - "/Eclipse总Maven-Dependencies消失的解决办法.html"
  - "/2025/07/04/eclipse-zong-maven-dependencies-xiao-shi-de-jie-jue-ban-fa/"
  - "/2025/07/04/eclipse-zong-maven-dependencies-xiao-shi-de-jie-jue-ban-fa.html"
  - "/eclipse-zong-maven-dependencies-xiao-shi-de-jie-jue-ban-fa.html"
---
首先检查一下条件是否符合

> 1、右键项目根本找不到Maven  
> 2、右键项目属性(Properties)也找不到Maven

**1】第一个文件.project的修改**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
    <name>simple_custom_error_pages</name>
    <comment></comment>
    <projects></projects>
    <buildSpec>
        <buildCommand>
            <name>org.eclipse.jdt.core.javabuilder</name>
            <arguments></arguments>
        </buildCommand>
    </buildSpec>
    <natures>
        <nature>org.eclipse.jdt.core.javanature</nature>
    </natures>
</projectDescription>
```

改为如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<projectDescription>
    <name>simple_custom_error_pages</name>
    <comment></comment>
    <projects></projects>
    <buildSpec>
        <buildCommand>
            <name>org.eclipse.jdt.core.javabuilder</name>
            <arguments></arguments>
        </buildCommand>
        <buildCommand>
            <name>org.eclipse.m2e.core.maven2Builder</name>
            <arguments></arguments>
        </buildCommand>
    </buildSpec>
    <natures>
        <nature>org.eclipse.jdt.core.javanature</nature>
        <nature>org.eclipse.m2e.core.maven2Nature</nature>
    </natures>
</projectDescription>
```

**2】第二个文件.classpath的修改**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<classpath>
    <classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER"/>
    <classpathentry kind="src" path="src/main/java"/>
    <classpathentry kind="output" path="target/classes"/>
</classpath>
```

改为如下

```xml
<?xml version="1.0" encoding="UTF-8"?>
<classpath>
    <classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER"/>
    <classpathentry kind="con" path="org.eclipse.m2e.MAVEN2_CLASSPATH_CONTAINER">
        <attributes>
            <attribute name="maven.pomderived" value="true"/>
        </attributes>
    </classpathentry>
    <classpathentry kind="src" path="src/main/java"/>
    <classpathentry kind="output" path="target/classes"/>
</classpath>
```
