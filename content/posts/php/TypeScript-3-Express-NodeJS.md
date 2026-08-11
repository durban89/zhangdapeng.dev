---
title: "TypeScript 3 + Express + Node.js"
date: "2025-07-09 10:42:21"
slug: "typescript-3-express-nodejs"
categories: ["技术"]
tags: ["TypeScript", "NodeJS", "ExpressJS"]
aliases:
  - "/2025/07/09/TypeScript-3-+-Express-+-Node.js/"
  - "/2025/07/09/TypeScript-3-+-Express-+-Node.js.html"
  - "/TypeScript-3-+-Express-+-Node.js/"
  - "/TypeScript-3-+-Express-+-Node.js.html"
  - "/2025/07/09/TypeScript-3-Express-NodeJS/"
  - "/2025/07/09/TypeScript-3-Express-NodeJS.html"
  - "/2025/07/09/typescript-3-express-nodejs/"
  - "/2025/07/09/typescript-3-express-nodejs.html"
  - "/typescript-3-express-nodejs.html"
---
## 第一步、安装需要的配置

首先，我们将使用node包管理器（npm）来为我们的应用程序安装依赖项。  
Npm与Node.js一起安装。  
如果您还没有安装Node.js，可以通过homebrew程序完成。

安装Homebrew并更新它：

```javascript
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew update
$ brew doctor
```

然后使用`brew install`命令安装node

```javascript
brew install node
```

## 第二步、创建项目

接下来，让我们使用npm init命令创建一个新项目。

```javascript
$ mkdir ts_node_blog
$ cd ts_node_blog
$ npm init
```

在回答提示后，您将在项目文件夹中有一个新的package.json文件。  
我们也添加一些自定义脚本。

首先，添加开发脚本。  
这将使用nodemon模块来监视对快速Web应用程序的源文件的任何更改。  
如果文件更改，那么我们将重新启动服务器。  
接下来，添加grunt脚本。  
这只是调用grunt任务运行器。  
我们将在本教程后面安装它。  
最后，添加启动脚本。  
这将使用node来执行bin/www文件。  
如果您使用的是Linux或Mac，则package.json文件应如下所示：

```javascript
{
  "name": "ts_node_blog",
  "version": "1.0.0",
  "description": "The blog of typescript + nodejs + express",
  "main": "app.js",
  "scripts": {
    "dev": "NODE_ENV=development nodemon ./bin/www",
    "grunt": "grunt",
    "start": "node ./bin/www",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "typescript",
    "noejs",
    "blog"
  ],
  "author": "durban.zhang <[email protected]>",
  "license": "MIT"
}
```

如果您使用的是Windows，则package.json文件应如下所示：

```javascript
{
  "name": "ts_node_blog",
  "version": "1.0.0",
  "description": "The blog of typescript + nodejs + express",
  "main": "app.js",
  "scripts": {
    "dev": "SET NODE_ENV=development nodemon ./bin/www",
    "grunt": "grunt",
    "start": "node ./bin/www",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "typescript",
    "noejs",
    "blog"
  ],
  "author": "durban.zhang <[email protected]>",
  "license": "MIT"
}
```

请注意Windows用户对dev脚本的微小更改。

## 第三步、安装Express

下一步是安装Express依赖项。  
我在我的npm install命令中包含了--save标志，以便将依赖项保存在package.json文件中。

```javascript
$ npm install express --save
$ npm install @types/express --save-dev
```

请注意，这还会在项目中生成新的node\_modules文件夹。  
如果您使用Git，则应将此文件夹添加到.gitignore文件中。

## 第四步、启动脚本的配置

接下来我们需要创建我们的启动脚本。  
如果您还记得，我们在package.json文件的scripts配置中指定了一个start属性。  
我将其值设置为："node ./bin/www"。  
所以，让我们在：bin/www创建一个空文件

```javascript
$ mkdir bin
$ cd bin
$ touch www
```

以下是www文件的完整内容：

```javascript
#!/usr/bin/env node
"use strict";

const server = require("../dist/server");
const debug = require("debug")("express:server");
const http = require("http");

const httpPort = normalizePort(process.env.Port || 8080);
const app = server.Server.bootstrap().app;
app.set("port", httpPort);
const httpServer = http.createServer(app);

httpServer.listen(httpPort);

httpServer.on("error", onError);

httpServer.on("listening", onListening);

function normalizePort(val) {
  const port = parseInt(val, 10);

  if (isNaN(port)) {
    return val;
  }

  if (port >= 0) {
    return port;
  }

  return false;
}

function onError(error) {
  if (error.syscall !== "listen") {
    throw error;
  }

  const bind = typeof httpPort === 'string'
    ? "Pipe " + httpPort
    : "Port " + httpPort;

  switch(error.code) {
    case "EACCES":
      console.error(bind + " requires elevated privileges");
      process.exit(1);
      break;
    case "EADDRINUSE":
      console.error(bind + " alreay is use");
      process.exit(1);
      break;
    default:
      throw error;
  }
}

function onListening() {
  const addr = httpServer.address();
  const bind = typeof httpPort === 'string'
    ? "Pipe " + httpPort
    : "Port " + httpPort;
  debug("Listening on " + bind);
}
```

这有点长。所以，让我打破这一点并解释每个部分。

```javascript
#!/usr/bin/env node
"use strict";

const server = require("../dist/server");
const debug = require("debug")("express:server");
const http = require("http");
```

首先，我们有node shebang来执行这个脚本。如果您使用的是Windows，只需将此文件重命名为www.js，node将根据文件扩展名执行此操作。

然后我们通过“use strict”命令启用严格模式。

然后我需要一些依赖。首先，我将在：dist/server.js中有一个模块（文件）。我们还没有创建这个，所以不要担心。然后我们需要express和http模块。

```javascript
const httpPort = normalizePort(process.env.Port || 8080);
const app = server.Server.bootstrap().app;
app.set("port", httpPort);
const httpServer = http.createServer(app);
```

首先，我确定将http服务器绑定到的端口，并监听。这将首先检查PORT环境变量，然后默认为8080。

我还使用了由Google Cloud Platform团队提供的normalizePort()函数。我从他们的示例应用程序中借用了这些。

接下来，我将使用bootstrap()老启动我的应用程序。在创建Server类之后，这将更有意义。

然后我为HTTP服务器设置端口。

最后我们创建了http服务器，传入我们的express app。

```javascript
httpServer.listen(httpPort);

httpServer.on("error", onError);

httpServer.on("listening", onListening);
```

在这部分中，我将指定我们的http服务器将侦听的端口，然后我附加一些事件处理程序。  
我正在听error和listening事件。  
在创建应用程序期间发生错误时将触发错误事件。  
当http服务器启动并正在侦听指定端口时，将触发侦听事件。

## 第五步、安装TypeScript 和 Grunt

接下来，使用npm install命令安装TypeScript：

```javascript
$ npm install typescript --save-dev
```

我将使用Grunt任务运行器来编译TypeScript源代码。  
使用npm安装grunt：

```javascript
$ npm install grunt --save-dev
```

现在我们安装了grunt，让我们安装一些任务运行器：

```javascript
$ npm install grunt-contrib-copy --save-dev
$ npm install grunt-ts --save-dev
$ npm install grunt-contrib-watch --save-dev
```

grunt-contrib-copy任务运行器将./public和./views目录中的文件复制到./dist目录中  
我们将使用grunt-ts任务来编译TypeScript源代码。  
我们将使用grunt-contrib-watch来监视对TypeScript源文件的任何更改。  
当一个文件更新（或保存）文件后，我想重新编译我的应用程序。  
结合我们之前在package.json文件中创建的dev脚本，我们将能够轻松地对TypeScript源进行更改，然后立即在浏览器中查看更改。

## 第六步、创建gruntfile.js

下一步是配置Grunt来编译我们的TypeScript源代码。  
首先，在应用程序根目录中创建gruntfile.js文件。

```javascript
$ touch gruntfile.js
```

在您喜欢的编辑器中打开gruntfile.js文件。我使用Visual Studio Code。gruntfile.js文件内容如下

```javascript
module.exports = function(grunt) {
  "use strict";

  grunt.initConfig({
    copy: {
      build: {
        files: [
          {
            expand: true,
            cwd: './public',
            src: ["**"],
            dest: "./dist/public",
          },
          {
            expand: true,
            cwd: './views',
            src: ["**"],
            dest: "./dist/views",
          },
        ]
      }
    },
    ts: {
      app: {
        files: [
          {
            src: ["src/\*\*/\*.ts", "!src/.baseDir.ts"],
            dest: "./dist",
          }
        ],
        options: {
          module: "commonjs",
          target: "es6",
          sourceMap: false,
          rootDir: "src",
        }
      }
    },
    watch: {
      ts: {
        files: ["src/\*\*/\*.ts"],
        tasks: ["ts"],
      },
      views: {
        files: ["views/\*\*/\*.pug"],
        tasks: ["copy"],
      }
    }
  });

  grunt.loadNpmTasks("grunt-contrib-copy");
  grunt.loadNpmTasks("grunt-contrib-watch");
  grunt.loadNpmTasks("grunt-ts");

  grunt.registerTask("default", [
    "copy",
    "ts",
  ]);
};
```

以下是gruntfile.js的说明：

1. 使用exports对象，我们将导出一个将由grunt任务运行器调用的函数。这是非常标准的。它有一个名为grunt的参数。

2. 遵循最佳实践我正在启用严格模式。

3. 然后我们调用grunt.initConfig()方法并传入我们的配置对象。

4. 在我们的配置对象中，我们指定每个任务

5. 第一项任务是复制。此任务将复制./public和./views目录中的文件。

6. 接下来的任务是ts。此任务将TypeScript源代码编译为可由Node.js执行的JavaScript。已编译的JavaScript代码将输出到./dist目录。

7. 第三项任务是观察。此任务将监视对TypeScript源文件（\*.ts）以及视图模板文件（\*.pug）的任何更改。

如果一切正常，您应该能够执行grunt命令

```javascript
$ npm run grunt
```

你应该看到这样的事情：

```javascript
> [email protected] grunt /Users/durban/nodejs/ts_node_blog
> grunt

Running "copy:build" (copy) task

Running "ts:app" (ts) task
No files to compile

Done.
```

## 第七步、安装中间件

在我们创建server.ts模块之前，我们需要安装一些更多的依赖项。  
我在此示例Express应用程序中使用以下中间件：

1. body-parser[https://github.com/expressjs/body-parser]  
2. cookie-parser[https://github.com/expressjs/cookie-parser]  
3. morgan[https://github.com/expressjs/morgan]  
4. errorhandler[https://github.com/expressjs/errorhandler]  
5. method-override[https://github.com/expressjs/method-override]

您可以使用上面的链接阅读有关这些内容的更多信息。让我们继续，通过npm安装这些：

```javascript
$ npm install body-parser --save
$ npm install cookie-parser --save
$ npm install morgan --save
$ npm install errorhandler --save
$ npm install method-override --save
```

我们还需要为这些模块安装TypeScript声明文件。  
在TypeScript 3之前，您必须使用名为Typings的开源项目。  
现在不再是这种情况，因为TypeScript 3极大地改进了对第三方模块声明（或头文件）的支持。

让我们使用npmjs.org上的@ types/repository安装TypeScript声明文件：

```javascript
$ npm install @types/cookie-parser --save-dev
$ npm install @types/morgan --save-dev
$ npm install @types/errorhandler --save-dev
$ npm install @types/method-override --save-dev
```

## 第八步、创建Server类

首先，为TypeScript代码创建一个src目录，然后创建一个新的server.ts文件。

我们准备好在Node.js上使用Express启动我们的新HTTP服务器。  
在我们这样做之前，我们需要创建我们的Server类。  
这个类将配置我们的express Web application，会涉及到REST API和routes的类。下面是定义我们的Server类的server.ts文件的开头：

```javascript
import * as bodyParser from "body-parser";
import * as cookieParser from "cookie-parser";
import * as express from "express";
import * as logger from "morgan";
import * as path from "path";
import errorHandler = require("errorhandler");
import merhodOverride = require("method-override");

/**
 * The Server 
 * 
 * @class Server
 */
export class Server {
  public app: express.Application;

  /**
   * Bootstrap the application
   * 
   * @class Server
   * @method bootstrap
   * @static
   * @return Returns the newly created injector for this app. Returns the newly created injector for this app.
   */
  public static bootstrap(): Server {
    return new Server();
  }

  /**
   * Constructor
   * 
   * @class Server
   * @method constructor
   */
  constructor() {
    // create express application
    this.app = express();

    // configure application
    this.config();

    // add routes
    this.routes();

    // add api
    this.api();
  }

  /**
   * Create REST Api routes
   * 
   * @class Server
   * @method api
   */
  public api() {

  }

  /**
   * Configure application
   * 
   * @class Server
   * @method config
   */
  public config() {

  }

  /**
   * Create router
   * 
   * @class Server
   * @method router
   */
  public routes() {

  }
}
```

让我们深入研究Server.ts模块（文件）中的Server类。

### 导入

```javascript
import * as bodyParser from "body-parser";
import * as cookieParser from "cookie-parser";
import * as express from "express";
import * as logger from "morgan";
import * as path from "path";
import errorHandler = require("errorhandler");
import merhodOverride = require("method-override");
```

1. 首先，我们导入我们以前安装的中间件和必要的模块。  
2. body-parser中间件将JSON有效负载数据解析为可在我们的express应用程序中使用的req.body对象。  
3. cookie-parser中间件类似于body-parser，因为它解析用户的cookie数据并在req.cookies对象中使用它。  
4. 然后我们导入express模块。这是express框架。  
5. 我正在使用morgan HTTP logger 中间件。这应该只在开发期间使用。  
6. 然后我导入path模块。我将使用它来为config()方法中的public和views目录设置路径目录。  
7. errorhandler 中间件将在开发期间处理错误。同样，这不应该用于生产。相反，您需要记录错误，然后向用户显示错误指示。  
8. 最后，我使用method-override中间件。您可能不需要这个，但在REST API配置中使用"PUT"和"DELETE"HTTP谓词时需要这样做。

### Server类

```javascript
/**
 * The Server 
 * 
 * @class Server
 */
export class Server {
  public app: express.Application;

  /**
   * Bootstrap the application
   * 
   * @class Server
   * @method bootstrap
   * @static
   * @return Returns the newly created injector for this app. Returns the newly created injector for this app.
   */
  public static bootstrap(): Server {
    return new Server();
  }
}
```

接下来，我们创建一个名为Server的新类。  
我们的类有一个名为app的公共变量。  
请注意，我们的应用程序是express.Application类型。  
在Server类中，我有一个名为bootstrap()的静态方法。  
这在我们的www启动脚本中调用。  
它只是创建Server类的新实例并返回它。

### constructor函数

```javascript
/**
 * Constructor
 * 
 * @class Server
 * @method constructor
 */
constructor() {
  // create express application
  this.app = express();

  // configure application
  this.config();

  // add routes
  this.routes();

  // add api
  this.api();
}
```

在constructor()函数中，我通过创建一个新的express应用程序来设置app属性的值。  
然后我调用Server类中定义的一些方法来配置我的应用程序并创建我的应用程序的REST API和HTTP路由。  
现在这些都是空的。

此时您可能想要测试一下。  
虽然我们还没有配置HTTP服务器，但我们应该能够使用grunt编译我们的TypeScript：

```javascript
$ npm run grunt
```

您应该看到编译成功完成的指示：

```javascript
$ npm run grunt

> [email protected] grunt /Users/durban/nodejs/ts_node_blog
> grunt

Running "copy:build" (copy) task

Running "ts:app" (ts) task
Compiling...
Using tsc v3.0.3

TypeScript compilation complete: 2.65s for 1 TypeScript files.

Done.
```

## 第九步、配置Server

下一步是在我们的Server类中实现config()方法：

```javascript
public config() {
  // add static paths
  this.app.use(express.static(path.join(__dirname, 'public')));

  this.app.set('trust proxy', true);
  // configure pug
  this.app.set('views', path.join(__dirname, "views"));
  this.app.set("view engine", "pug");

  // use logger middleware
  this.app.use(logger("dev"));

  // use json form parse middleware
  this.app.use(bodyParser.json());

  // use query string parser middleware
  this.app.use(bodyParser.urlencoded({
    extended: true,
  }));

  // use cookie parser middleware
  this.app.use(cookieParser("SECRET_TS_NODE_BLOG"));

  // use override middleware
  this.app.use(methodOverride());

  // catch 404 and forward to error handler
  this.app.use(function(err: any, req: express.Request, res: express.Response, next: express.NextFunction) {
    err.status = 404;
    next(err);
  });

  // use handling
  this.app.use(errorHandler());
}
```

关于config()方法的一些注意事项：

1. 首先，我在/public设置静态路径。位于./public文件夹中的任何文件都可以公开访问（duh）。  
2. 接下来，我配置了pug模板引擎。我们将在一分钟内完成安装。我们所有的pug模板文件都位于./views目录中。  
3. 然后我们添加morgan logger中间件。  
4. 然后我们添加了body-parser中间件来解析JSON以及查询字符串。  
5. 然后我们添加cookie-parser中间件。  
6. 然后我们添加方法覆盖中间件。  
7. 最后，我们添加一些代码来捕获404错误以及任何应用程序异常。

如上所述，我们正在使用pug(哈巴狗)模板引擎。  
但是，在我们使用它之前，我们需要通过npm安装它：

```javascript
$ npm install pug --save
```

我们还应该创建public和views目录：

```javascript
$ mkdir public
$ mkdir views
```

这是我们的目录结构应该是这样的：

```javascript
.
├── bin
│   └── www
├── dist
│   └── server.js
├── gruntfile.js
├── package-lock.json
├── package.json
├── public
├── src
│   └── server.ts
└── views
```

现在我们的服务器已配置，我们应该能够编译我们的TypeScript源代码并启动node HTTP服务器：

```javascript
$ npm run grunt
$ npm start
```

然后，您应该看到该node正在运行：

```javascript
> [email protected] start /Users/durban/nodejs/ts_node_blog
> node ./bin/www
```

现在启动浏览器并转到http//localhost:8080。  
如果一切正常，您应该在浏览器中看到以下消息：

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1536811118/gowhich/t_1_1.png)

这是因为我们还没有定义任何route。  
让我们继续。

## 第十步、创建BaseRoute类

现在我们的服务器已配置并运行，我们已准备好开始构建我们的Web应用程序的路由。  
但是，你可能会问自己route是什么。  
好吧，根据Express文档：

> Routing refers to determining how an application responds to a client request to a particular endpoint, which is a URI (or path) and a specific HTTP request method (GET, POST, and so on).

首先，让我们创建一个带有两个新文件的./src/routes目录：route.ts和index.ts。

```javascript
$ cd ./src
$ mkdir routes
$ cd routes
$ touch route.ts
$ touch index.ts
```

route.ts模块将导出BaseRoute类。  
所有路由类都将扩展BaseRoute。  
让我们来看看route.ts的内容。

```javascript
import { NextFunction, Request, Response } from "express";

/**
 * BaseRoute
 * 
 * @class BaseRoute
 */
export class BaseRoute {
    protected title: string;

    private scripts: string[];

    /**
     * Constructor
     * 
     * @class BaseRoute
     * @method constructor
     */
    constructor() {
        this.title = "TS Blog";
        this.scripts = [];
    }

    /**
     * Add a JS external file to the request
     * 
     * @class BaseRoute
     * @method addScript
     * @param src {string} The src to the external JS file
     * @return {BaseRoute} The self for chaining
     */
    public addScript(src: string): BaseRoute {
        this.scripts.push(src);
        return this;
    }

    public render(req: Request, res: Response, view: string, options?: Object) {
        // add constants
        res.locals.BASE_URL = "/";

        // add scripts 
        res.locals.scripts = this.scripts;

        // add title
        res.locals.title = this.title;

        res.render(view, options);
    }
}
```

BaseRoute目前相当薄。但是，这将作为一种在我的应用程序中实现身份验证的方法，以及所有路由可能需要的许多其他功能。

我有一个标题字符串变量，它将保存路径的标题。

作为示例，BaseRoute当前存储特定路由所必需的脚本数组。可能还希望在BaseRoute中定义所有路径都需要的脚本。这只是一部分特性在BaseRoute中实现的一个示例，该功能将可用于所有路由。

此外，BaseRoute类有一个render()方法。这将在我们的扩展类中的每个路由方法中调用。这为我们提供了一种方法来渲染视图，并定义了常见的本地模板变量。

在此示例中，我将BASE\_URL，脚本和标题设置到每个视图中。

## 第十一步、创建IndexRoute类

路由定义通过以下方式定义：

```javascript
app.METHOD(PATH, HANDLER)
```

METHOD是适当的HTTP动词，例如get或post。该方法应为小写。PATH是请求的URI路径。并且，HANDLER是在路线匹配时执行的功能。index.ts模块将导出IndexRoute类。  
我们来看看index.ts的内容。

```javascript
import { NextFunction, Request, Response, Router } from "express";
import { BaseRoute } from "./route";

/**
 * IndexRoute
 * 
 * @class IndexRoute
 */
export class IndexRoute extends BaseRoute {
  /**
   * Constructor
   * 
   * @class IndexRoute
   * @method constructor
   */
  constructor() {
    super();
  }

  /**
   * Create the router
   * 
   * @class IndexRoute
   * @method create
   * @static
   * @param router 
   */
  public static create(router: Router) {
    console.log("[IndexRoute::create] Creating index route");

    // add home page route
    router.get("/", (req: Request, res: Response, next: NextFunction) => {
      new IndexRoute().index(req, res, next);
    })
  }

  /**
   * The home page route
   * 
   * @class IndexRoute
   * @method index
   * @param req {Request} The express Request Object.
   * @param res {Response} The express Response Object.
   * @param next {NextFunction} Execute the next method.
   */
  public index(req: Request, res: Response, next: NextFunction) {
    // set custom title
    this.title = "Home | TS Blog";

    let options: Object = {
      "message": "Welcome to the TS Blog",
    };

    // render template
    this.render(req, res, "index", options);
  }
}
```

我们来看看IndexRoute类：

1. 首先，我们从express模块​​导入NextFunction，Request，Response和Router类。  
2. 我还从routes模块导入BaseRoute类。  
3. create()静态方法创建所有将在类中定义的路由。在这个例子中，我只定义了一个路由。但是，您可能会为应用程序的部分定义多个路由。例如，UsersRoute类可能具有/users/signin/users/signup等的路由。  
4. constructor()函数只是调用BaseRoute的构造函数。  
5. index()函数将呈现我们的模板。在我们渲染模板之前，我们设置一个自定义标题，并定义一个名为options的对象，其中包含将在我们的模板中可用的属性和值。在这个例子中，我设置一个名为message的本地模板变量，其中包含一个简单的字符串。我将在index.pug模板中输出。

## 第十二步、定义routes

现在我们已经创建了第一个路由的shell，我们需要在Server类中定义它。  
但是，在我们定义路由之前，让我们首先通过以下方式在server.ts模块中导入我们的IndexRoute类：

```javascript
import { IndexRoute } from "./routes/index";
```

然后，让我们在server.ts模块中实现routes()方法：

```javascript
/**
 * Create router
 * 
 * @class Server
 * @method router
 */
public routes() {
  let router: express.Router;
  router = express.Router();

  // IndexRoute
  IndexRoute.create(router);

  // use router middleware
  this.app.use(router);
}
```

在routes()方法中，我们创建了express.Router()实例。  
然后，我们调用静态IndexRoute.create()方法并传入路由器实例。  
最后，我们将路由器中间件添加到我们的应用程序中。

## 第十三步、创建Template

现在我们已经创建并定义了路由，我们需要创建必要的模板。  
在这个例子中，我将在views目录中创建一个index.pug文件。

```javascript
$ cd ./views
$ touch index.pug
```

这是我的示例index.pug文件的样子：

```javascript
html
  head
    title= title
  body
    h1= message
```

## 第十四步、启动服务

我们完成了。我们为使用TypeScript源代码中的Express开发应用程序奠定了坚实的基础。下一步是编译并启动服务器。

```javascript
$ npm run grunt
$ npm start
```

现在启动浏览器并转到http://localhost:8080。  
如果一切正常，您应该在浏览器中看到以下消息：

![](https://res.cloudinary.com/dy5dvcuc1/image/upload/v1536811118/gowhich/t_1_2.png)

## 第十五步、安装nodemon

如果你想启动我的node服务器来监视源代码的任何变化（在开发中），那么我建议你使用nodemon

```javascript
$ npm install nodemon --save-dev
```

然后我们可以运行我们在package.json中定义的自定义开发脚本来启动我们的应用程序使用nodemon：

```javascript
$ npm run dev
```

参考资料

> https://brianflove.com/2016/11/11/typescript-2-express-mongoose-mocha-chai/
