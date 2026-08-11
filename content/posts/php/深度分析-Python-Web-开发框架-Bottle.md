---
title: "[深度分析] Python Web 开发框架 Bottle"
date: "2025-06-24 11:24:13"
slug: "shen-du-fen-xi-python-web-kai-fa-kuang-jia-bottle"
categories: ["技术"]
tags: ["Python", "Bottle"]
aliases:
  - "/2025/06/24/[深度分析]-Python-Web-开发框架-Bottle/"
  - "/2025/06/24/[深度分析]-Python-Web-开发框架-Bottle.html"
  - "/[深度分析]-Python-Web-开发框架-Bottle/"
  - "/[深度分析]-Python-Web-开发框架-Bottle.html"
  - "/2025/06/24/深度分析-Python-Web-开发框架-Bottle/"
  - "/2025/06/24/深度分析-Python-Web-开发框架-Bottle.html"
  - "/2025/06/24/shen-du-fen-xi-python-web-kai-fa-kuang-jia-bottle/"
  - "/2025/06/24/shen-du-fen-xi-python-web-kai-fa-kuang-jia-bottle.html"
  - "/shen-du-fen-xi-python-web-kai-fa-kuang-jia-bottle.html"
---
[Bottle](http://bottlepy.org/docs/dev-cn/)是一个非常精致的WSGI框架，它提供了 Python Web开发中需要的基本支持：URL路由，Request/Response对象封装，模板支持，与WSGI服务器集成支持。整个框架的全部代码约有 2000行，它的核心部分没有其他任何依赖，只要有Python环境就可以运行。

Bottle适用于小型的Web开发，在应用程序规模比较小的情况下可以实现快速开发。但是由于自身功能所限，对于大型的Web程序，Bottle的功能略显不足，程序员需要手动管理模块、数据库、配置等等，与Pylons等框架相比Bottle的优势就难以体现出来了。

## [快速入门](#1)

通过一个简单的、典型的例子描述Bottle的使用：

```python
from bottle import Bottle, run, mako_view, request

myapp = Bottle()

@myapp.get('/hello/:name/:count#\\d+#')
@mako_view('hello')
def hello(name, count):
    ip = request.environ.get('REMOTE_ADDR')
    return dict(n=name, c=int(count), ip=ip)

run(app=myapp)
```

我们创建一个Bottle对象，通过decorator配置一条路由记录。Bottle的url映射支持具名参数，“/hello/:name/:count#\\d+#” 格式的参数，可以匹配/hello/(.+?)/(\d+?)的 URL。在方法体中，通过environ字典获得客户端IP，这个操作和其他WSGI框架是一致的。接着通过一个字典类型将Model数据传递给 View。View模板通过decorator定义，采用mako模板引擎实现，模板名为hello，他表示在当前目录下一个名叫hello.tpl的文 件。

## [剖析](#2)

Bottle主要可以分成4个模块：

***Router和WSGI Application***

***Request和Response, Web helpers***

***Template Adapters***

***WSGI Server Adapters***

## [Router和WSGI Application](#3)

一个Bottle对象是一个标准的WSGI App，这使他可以与很多WSGI Server集成。每个app下管理一个Router用于针对URL映射到handler方法。根据Python decorator的特性，路由规则是在程序启动时自动执行的。

Bottle的route方法用于注册handler到router中。除此以外，还有很多function currying帮助您简单地路由GET / POST 等特定HTTP方法。

Bottle最近以来支持了hook，可以注册一些方法在每个请求之前、或之后执行。

当接受一个HTTP请求时，WSGI Server会调用WSGI App的wsgi方法。它的流程是：

1. 根据标准的WSGI接口规范，从WSGI environ中生成一个Request对象，初始化一个response对象。
2. 在寻找方法之前，实际上Bottle会自动执行您注册的`before_hook`。（`Bottle._add_hook_wrapper`）
3. 根据request.path的URL在router中寻找对应的handler方法（Bottle.match_url, Router.match）。这一步中除了找到合适的handler方法，还要负责提取url中的具名参数，将结果以tuple的形式返回。
4. 以返回的方法和参数，执行handler，获得返回值。
5. 执行所有的after_hooks。
6. 根据返回的不同类型，写入Response的头部。在这一步，Bottle还会应用一些filter，在Bottle中，filter是用于处理 handler返回类型的。例如，一个典型的filter即内置的dict2json，他将handler返回的dict类型自动换成 json。（`Bottle._cast`）
7. 根据返回的HTTP状态码，对handler返回对象进行处理。调用WSGI Server的start_response方法将返回对象写给客户端。

## [Request和Response, Web helpers](#4)

Bottle对HTTP的请求和响应封装了Request和Response对象。它采用threadlocal的方式，由Bottle app管理生命周期。您可以在声明handler方法时不必像Java Servlet那样将他们以参数传入，这样增加了方法设计的灵活性，也使得单元测试变得相对轻松。

Request对象是对WSGI environ属性的封装，可以从中取得的属性取决于WSGI Server对[PEP333](https://www.python.org/dev/peps/pep-0333/#environ-variables)的实现。

关于Request API，可以参考[文档](http://bottle.paws.de/docs/dev/api.html#bottle.Request)

类似的，可以参考[Response API](http://bottle.paws.de/docs/dev/api.html#bottle.Response)了解如何对HTTP响应进行操作

和很多Web框架一样，你不必手动去设置HTTP重定向，helper方法会简化这些操作：`abort`, `redirect`, `static_file`。当然，你也可以自己创建一些helper。

## [Template Adapters](#5)

template方法用于渲染视图，您可以使用不同的模板实现：`mako`, `jinja2`, `cheetah`, `simpletal`以及Bottle自己的简单实现。

view作为一个decorator可以简化模板的选择。与route类似，作者也提供了一些function currying来支持mako_view这样简便的写法。

## [Server Adapters](#6)

Bottle的Server Adapters简直可以说是WSGI Server的博览会，从这里您可以了解目前比较流行的WSGI实现：

* flup
* wsgiref
* cherrypy
* paste
* fapws3
* tornado
* Google Appengine
* twisted
* diesel
* meinheld
* gunicorn
* eventlet
* gevent
* rocket

当然，这些不是全部，如果要使用不在其中的WSGI Server，您只需实现一个ServerAdapter的run方法即可，需要做的就是将Bottle app传给server并启动它。

内置的run方法用于启动服务，您还可以指定一个reloader参数使Bottle在后台检查源文件的修改情况，实现热加载。

除了run方式的启动，由于Bottle app本身就是一个符合标准的WSGI app，所以也可以通过一些服务器特有的方式启动服务，例如gunicorn：

```bash
gunicorn -w 2 -D -b 127.0.0.1:18080 module:app
```

## [实战Middlewares](#7)

Middleware是WSGI的重要概念http://www.python.org/dev/peps/pep-0333 /#middleware-components-that-play-both-sides 借助一些成熟的middleware可以添加一些Bottle目前不具备的功能：没错，Session。

Session Middleware最著名的选择叫做Beaker，要其用Beaker，只需要一个装饰器模式的App声明即可，您可以参考Beaker的[文档](http://beaker.groovie.org/configuration.html).

Pylons以使用Middleware著称，而除了Routing这样核心的Middleware，包括Beaker和Authkit都可以应用在Bottle程序上。

## [App Mounting](#8)

Bottle的App提供一个很有用的mount方法帮助你将Web应用模块化。您可以将一个Bottle App挂载到一个父App上的某个路径，以父App启动后，父App可以为子App在一个路径下提供路由。

不过你会遇到这样的问题：

```python
child = Bottle()
@child.get("/")
def hello():
    return "hello world"

parent = Bottle()
parent.mount(child, "/child")
```

很自然的，您希望打开浏览器访问http://localhost:8000/child可能看到hello world，然后却得到404.这个问题不难察觉，于是访问http://localhost:8000/child/，工作正常。

我曾给作者提过这个问题http://github.com/defnull/bottle/issues#issue/88，（补一 句，Bottle的作者少有的Nice，对你提出的问题他通常都会认真解答），作者提了一个重定向的方式，不过还是没有决定把它直接加进mount方法 里。

那么，我们需要一个新的mount来支持http://localhost:8000/child

```python
def mount(parent, child, path):
    parent.mount(child, path)
    @parent.get(path)
    def redir():
        redirect(path+"/")
```

## [Google AppEngine](#9)

因为有WSGI标准，你可以用Bottle开发Google AppEngine程序。您只需要在handler文件中加入这样的代码即可：

```python
from google.appengine.ext.webapp.util import run_wsgi_app
def main():
    run_wsgi_app(my_bottle_app)
if __name__ == '__main__':
    main()
```

依赖？Bottle本身是self-contained，不过你可能还需要一个强大一些的模板引擎来完成你的应用，比如Mako。这样，你需要把依赖和自己的程序一起上传到GAE。对于Mako来说，除了它自己，还依赖marksave，别忘了它。

以上就是我对Bottle的理解和使用心得，希望您在合适的场景下使用Bottle，只有这样，才能感受到这个框架所带来的乐趣。

