---
title: "iOS存储方式"
date: "2025-06-05 11:06:45"
slug: "ios-cun-chu-fang-shi"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/05/iOS存储方式/"
  - "/2025/06/05/iOS存储方式.html"
  - "/iOS存储方式/"
  - "/iOS存储方式.html"
  - "/2025/06/05/ios-cun-chu-fang-shi/"
  - "/2025/06/05/ios-cun-chu-fang-shi.html"
  - "/ios-cun-chu-fang-shi.html"
---
### [第一种:NSKeyedArchiver（加密形式）](#1)

代码很简单就不多解释了直接上代码：

```c
//=================NSKeyedArchiver========================
NSString *saveStr1 = @ "我是" ;
NSString *saveStr2 = @ "数据" ;
NSArray *array = [NSArray arrayWithObjects:saveStr1, saveStr2, nil];
//----Save
//这一句是将路径和文件名合成文件完整路径
NSString *Path = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES) objectAtIndex:0];
NSString *filename = [Path stringByAppendingPathComponent:@ "saveDatatest" ];
[NSKeyedArchiver archiveRootObject:array toFile:filename];
//用于测试是否已经保存了数据
saveStr1 = @ "hhhhhhiiii" ;
saveStr2 =@ "mmmmmmiiii" ;
//----Load
array = [NSKeyedUnarchiver unarchiveObjectWithFile: filename];
saveStr1 = [array objectAtIndex:0];
saveStr2 = [array objectAtIndex:1];
NSLog(@ "str:%@" ,saveStr1);
NSLog(@ "astr:%@" ,saveStr2);
```

### [第二种:NSUserDefaults](#2)

举个简单的例子

```c
//=================NSUserDefaults========================
NSString *saveStr1 = @ "我是" ;
NSString *saveStr2 = @ "数据" ;
NSArray *array = [NSArray arrayWithObjects:saveStr1, saveStr2, nil];
//Save
NSUserDefaults *saveDefaults = [NSUserDefaults standardUserDefaults];
[saveDefaults setObject:array forKey:@ "SaveKey" ];
//用于测试是否已经保存了数据
saveStr1 = @ "hhhhhhiiii" ;
saveStr2 =@ "mmmmmmiiii" ;
//---Load
array = [saveDefaults objectForKey:@ "SaveKey" ];
saveStr1 = [array objectAtIndex:0];
saveStr2 = [array objectAtIndex:1];
NSLog(@ "str:%@" ,saveStr1);
NSLog(@ "astr:%@" ,saveStr2);

```

### [第三种:Write写入方式](#3)

举个例子，也很简单的

```c
//=================Write写入方式========================
NSString *saveStr1 = @ "我是" ;
NSString *saveStr2 = @ "数据" ;
NSArray *array = [NSArray arrayWithObjects:saveStr1, saveStr2, nil];
//----Save
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
NSString *documentsDirectory = [paths objectAtIndex:0];
if (!documentsDirectory) {
  NSLog(@ "没找到" );
}
NSMutableArray *saveDataArray=nil;
NSString *appFile = [documentsDirectory stringByAppendingPathComponent:@ "Savedatas.plist" ];
[[NSArray arrayWithObjects:array,nil] writeToFile:appFile atomically:NO];
//用于测试是否已经保存了数据
saveStr1 = @ "hhhhhhiiii" ;
saveStr2 =@ "mmmmmmiiii" ;
//----Load
if ([[NSFileManager defaultManager] fileExistsAtPath:appFile]){
  saveDataArray = [NSMutableArray arrayWithContentsOfFile:appFile];
}else{
  saveDataArray = [NSMutableArray arrayWithContentsOfFile:[[NSBundle mainBundle] pathForResource:@ "Savedatas" ofType:@ "plist" ]];
}
NSArray *strArray = [saveDataArray objectAtIndex:0];
saveStr1 = [strArray objectAtIndex:0];
saveStr2 = [strArray objectAtIndex:1];
NSLog(@ "str:%@" ,saveStr1);
NSLog(@ "astr:%@" ,saveStr2);
```

### [第四种:SQLite3](#4)

在使用sqlite3之前  你需要将libsqlite3.dylib这个类库加入到你的项目中

```c
- (NSString *)dataFilePath{

  NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
  NSString *documentsDirectory = [paths objectAtIndex:0];
  return [documentsDirectory stringByAppendingPathComponent:kFilename];
}
NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
NSString *documentsDirectory = [paths objectAtIndex:0]; //首先得到应用程序沙盒中Document文件夹的路径
return [documentsDirectory stringByAppendingPathComponent:kFilename]//返回你指定文件的路径
```

打开数据库

```c
sqlite3 *database;
if(sqlite3_open([filePath UTF8String], &database)) {
  sqlite3_close(database);
  NSAssert(0,@"Failed to open database");
}
```

创建数据库

```c
char *errorMsg;
NSString *createSQL = @"CREATE TABLE IF NOT EXISTS FIELDS (ROW INTEGER PRIMARY KEY,FIELD_DATA TEXT);";
if (sqlite3_exec(database, [createSQL UTF8String], NULL, NULL, &errorMsg)!=SQLITE_OK) {
  sqlite3_close(database);
  NSAssert1(0,@"Error creating table:%s",errorMsg);
}
```

数据查询

```c
NSString *query = @"SELECT ROW, FIELD_DATA FROM FIELDS ORDER BY ROW";
sqlite3_stmt *statement;
if (sqlite3_prepare_v2(database, [query UTF8String], -1, &statement, nil)==SQLITE_OK) {
  while (sqlite3_step(statement)==SQLITE_ROW) {
    int row = sqlite3_column_int(statement, 0);
    char *rowData = (char *)sqlite3_column_text(statement, 1);

    //NSString *fieldName = [[NSString alloc] initWithFormat:@"field&d",row];
    //NSString *fieldValue = [[NSString alloc] initWithUTF8String:rowData];

    //UITextField *field = [self valueForKey:fieldName];
    //field.text = fieldValue;
    //[fieldName release];
    //[fieldValue release];
  }
  sqlite3_finalize(statement);
}
sqlite3_close(database);
```

数据插入／更新

```c
sqlite3 *database;
if (sqlite3_open([[self dataFilePath] UTF8String], &database)) {
  sqlite3_close(database);
  NSAssert(0,@"Failed to open database");
}
 
for (int i=1; i<=4; i++) {
  NSString *fieldName = [[NSString alloc] initWithFormat:@"field%d",i];
  UITextField *field = [self valueForKey:fieldName];
  [fieldName release];

  char *errorMsg;
  char *update = "INSERT OR REPLACE INTO FIELDS (ROW,FIELD_DATA) VALUES(?,?);"; //这里插入的值可以用nsstring替换，但是最好的做法是使用绑定，如果遇到特殊字符 这是不二选择

  sqlite3_stmt *stmt;
  if (sqlite3_prepare_v2(database, update, -1, &stmt, nil)==SQLITE_OK) {
    sqlite3_bind_int(stmt, 1, i);
    sqlite3_bind_text(stmt, 2, [[field text] UTF8String], -1, NULL);
  }
  if (sqlite3_step(stmt)!=SQLITE_DONE) {
    NSAssert(0,@"Error updating table:%s",errorMsg);
  }
  sqlite3_finalize(stmt);
}
sqlite3_close(database);
```

#######################可爱分割线#############################

对Write写入方式保存数据和读取数据封装了两个方法：

封装的函数如下：

```c
//保存游戏数据  
//参数介绍：  
//   (NSMutableArray *)data ：保存的数据  
//   (NSString *)fileName ：存储的文件名  
-(BOOL) saveGameData:(NSMutableArray *)data  saveFileName:(NSString *)fileName  
{  
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);  
    NSString *documentsDirectory = [paths objectAtIndex:0];  
    if (!documentsDirectory) {  
        NSLog(@"Documents directory not found!");  
        return NO;  
    }  
    NSString *appFile = [documentsDirectory stringByAppendingPathComponent:fileName];  
    return ([data writeToFile:appFile atomically:YES]);  
}  
//读取游戏数据  
//参数介绍：  
//   (NSString *)fileName ：需要读取数据的文件名  
-(id) loadGameData:(NSString *)fileName  
{  
    NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);  
    NSString *documentsDirectory = [paths objectAtIndex:0];  
    NSString *appFile = [documentsDirectory stringByAppendingPathComponent:fileName];  
    NSMutableArray *myData = [[[NSMutableArray alloc] initWithContentsOfFile:appFile] autorelease];  
    return myData;  
}
```

可以使用类似下面的例子进行使用

```c
NSString *saveStr1 = @"测试保存读取";  
NSString *saveStr2 = @"两个函数";  
NSMutableArray *array = [NSMutableArray arrayWithObjects:saveStr1, saveStr2, nil];   
[self saveGameData:array saveFileName:@"Himi"];  
NSMutableArray*temp =(NSMutableArray*)[self loadGameData:@"Himi"];  
NSLog(@"%@--%@",[temp objectAtIndex:0],[temp objectAtIndex:1]);
```

有两点需要注意的地方：

1，取出数据的时候需要注意

```c
NSUserDefaults *saveDefaults = [NSUserDefaults standardUserDefaults];   NSMutableArray *arraySaveData =[saveDefaults objectForKey:@"OhSaveData"];  
//NSMutableArray *arraySaveData=[NSMutableArray arrayWithArray:[saveDefaults objectForKey:@"OhSaveData"]];
```

第二句代码是通过一个文件名获取你存储的数据，返回数据数组，但是！一定要注意这里返回的数据数组是不可修改的！及时你将读取的数据赋给一个可修改的数组中也一样无法修改其中的数据，所以如果你想将取出的数据进行修改那么这里需要要使用第三行代码来获取

2，修改已经的存储文件

```c
NSUserDefaults *saveDefaults = [NSUserDefaults standardUserDefaults];   
[saveDefaults setObject:arraySaveData forKey:@"已经存在的文件名"];
```
