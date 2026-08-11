---
title: "Go基础学习记录之SQL注入"
date: "2025-08-04 11:38:49"
slug: "go-ji-chu-xue-xi-ji-lu-zhi-sql-zhu-ru"
categories: ["技术"]
tags: ["Golang"]
aliases:
  - "/2025/08/04/Go基础学习记录之SQL注入/"
  - "/2025/08/04/Go基础学习记录之SQL注入.html"
  - "/Go基础学习记录之SQL注入/"
  - "/Go基础学习记录之SQL注入.html"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-sql-zhu-ru/"
  - "/2025/08/04/go-ji-chu-xue-xi-ji-lu-zhi-sql-zhu-ru.html"
  - "/go-ji-chu-xue-xi-ji-lu-zhi-sql-zhu-ru.html"
---
## SQL注入

### 什么是SQL注入

SQL注入攻击（正如其名称所示）是众多类型的脚本注入攻击之一。  
在Web开发中，这些是最常见的安全漏洞形式。  
攻击者可以使用它从数据库中获取敏感信息，攻击的各个方面可能涉及将用户添加到数据库，导出私有文件，甚至为自己的恶意目的获取最高系统权限。

当Web应用程序无法有效地过滤掉用户输入时，会发生SQL注入，从而使攻击者可以向服务器提交恶意SQL查询代码。  
应用程序通常会将注入的代码作为攻击者输入的一部分接收，这会以某种方式改变原始查询的逻辑。  
当应用程序尝试执行查询时，会执行攻击者的恶意代码。

### SQL注入示例

许多Web开发人员都没有意识到SQL查询是如何被篡改的，并且可能会误以为他们是可信命令。  
众所周知，SQL查询能够绕过访问控制，从而绕过标准的身份验证和授权检查。  
而且，可以通过主机系统级别的命令运行SQL查询。

让我们看一些真实的例子来详细解释SQL注入的过程。

请考虑以下简单登录表单：

```html
<form action="/login" method="POST">
    <p>Username: <input type="text" name="username" /></p>
    <p>Password: <input type="password" name="password" /></p>
    <p><input type="submit" value="Login" /></p>
</form>
```

我们的表单处理可能如下所示：

```go
username := r.Form.Get("username")
password := r.Form.Get("password")
sql := "SELECT * FROM user WHERE username='" + username + "' AND password='" + password + "'"
```

如果用户输入用户名或密码：

```go
myuser' or 'foo' = 'foo' --
```

然后我们的SQL变成以下内容：

```sql
SELECT * FROM user WHERE username='myuser' or 'foo' = 'foo' --'' AND password='xxx'
```

在SQL中，`--`后面的任何内容都是注释。  
因此，插入 `--` 如上面的攻击者所做的那样以致命的方式改变查询，允许攻击者以没有有效密码的用户成功登录。

MSSQL SQL注入存在更多危险的漏洞，有些甚至可以执行系统命令。  
以下示例将演示在某些版本的MSSQL数据库中SQL注入的可怕程度。

```go
sql := "SELECT * FROM products WHERE name LIKE '%" + prod + "%'"
Db.Exec(sql)
```

如果攻击者提交`a％'exec master..xp_cmdshell'net user test testpass / ADD' --` 作为"prod"变量，则sql将成为

```go
sql := "SELECT * FROM products WHERE name LIKE '%a%' exec master..xp_cmdshell 'net user test testpass /ADD'--%'"
```

MSSQL Server执行SQL语句，包括用户提供的“prod”变量中的命令，该变量将新用户添加到系统中。  
如果此程序按原样运行，并且MSSQLSERVER服务具有足够的权限，则攻击者可以注册系统帐户以访问此计算机。

> 虽然上面的示例与特定的数据库系统相关联，但这并不意味着其他数据库系统不会受到类似类型的攻击。SQL注入攻击背后的原理保持不变，尽管它们所采用的方法可能会有所不同。

### 如何防止SQL注入

您可能认为攻击者必须知道有关目标数据库结构的信息才能执行SQL注入攻击。  
虽然这是事实，但很难保证攻击者无法找到此信息，一旦获得此信息，数据库就会受到攻击。  
如果您使用开源软件访问数据库，例如论坛应用程序，入侵者可以轻松获取相关代码。  
显然，由于代码设计不当，安全风险更大。  
Discuz，phpwind和phpcms是流行的开源程序的一些例子，它们容易受到SQL注入攻击。

这些攻击发生在没有优先考虑安全预防措施的系统中。  
我们之前已经说过了，我们再说一遍：永远不要相信任何形式的输入，特别是用户数据。  
这包括来自选择框，隐藏输入字段或cookie的数据。  
正如我们上面的第一个例子所示，即使是普通的查询也可能导致灾难。

SQL注入攻击可能是毁灭性的 - 我们甚至可以开始防御它们？  
以下建议是防止SQL注入的良好起点：

1. 严格限制数据库操作的权限，以便用户只拥有完成其工作所需的最小权限集，从而最大限度地降低数据库注入攻击的风险。  
2. 检查输入数据是否具有预期的数据格式，并严格限制可以提交的变量类型。这可能涉及正则表达式匹配，或使用strconv包将字符串转换为其他基本类型以进行清理和评估。  
3. 在将它们持久存储到数据库之前，转码或转义成对特殊字符`( '"\&*;`等).Go的text/template包有一个HTMLEscapeString函数，可用于返回转义的HTML。  
4. 使用数据库的参数化查询界面。参数化语句使用参数而不是在嵌入式SQL语句中连接用户输入变量;换句话说，它们不直接拼接SQL语句。例如，使用Go的`database/sql`包中的Prepare函数，我们可以创建预准备语句，以便以后使用Query或Exec(query string, args... interface {})。  
5. 在发布应用程序之前，请使用专业工具对其进行彻底测试，以检测SQL注入漏洞并修复它们（如果存在）。有很多在线开源工具就是这样做的，比如sqlmap，SQLninja等等。  
6. 避免在公共网页上打印出SQL错误信息。攻击者可以使用这些错误消息来执行SQL注入攻击。此类错误的示例包括类型错误，不匹配错误的字段或包含SQL语句的任何错误。

### 小结

通过上面的例子，我们了解到SQL注入是一个非常真实且非常危险的Web安全漏洞。  
当我们编写Web应用程序时，我们应该注意每一个细节，并极其小心地处理安全问题。  
这样做将导致更好，更安全的Web应用程序，并最终成为您的应用程序是否成功的决定因素。
