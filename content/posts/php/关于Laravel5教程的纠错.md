---
title: "关于Laravel5教程的纠错"
date: "2025-07-02 16:00:55"
slug: "guan-yu-laravel5-jiao-cheng-de-jiu-cuo"
categories: ["技术"]
tags: ["PHP", "Laravel"]
aliases:
  - "/2025/07/02/关于Laravel5教程的纠错/"
  - "/2025/07/02/关于Laravel5教程的纠错.html"
  - "/关于Laravel5教程的纠错/"
  - "/关于Laravel5教程的纠错.html"
  - "/2025/07/02/guan-yu-laravel5-jiao-cheng-de-jiu-cuo/"
  - "/2025/07/02/guan-yu-laravel5-jiao-cheng-de-jiu-cuo.html"
  - "/guan-yu-laravel5-jiao-cheng-de-jiu-cuo.html"
---
教程地址：http://www.golaravel.com/laravel/docs/5.1/quickstart/#validation

有兴趣的自己的可以去看下。

没事自己，也看了下，这个最近比较火的PHP框架，总体先不做评价，给那些入门后看了这个教程很困惑的人吧，包括我在内。

这个教程里面说的Validation，也不知道是哪个版本的，从链接地址上看出来是5.1这个版本的，但是我用的是5.2的版本，应该不是那种不兼容的问题。

只是在添加路由的过程中，只给除了如何添加路由但是没有说明白，如何去放置这些路由，由于这个是直接在routes.php中直接添加路由的，可能需要其他一切设置吧，毕竟这里的全局errors不应该就只是一个routes能解决的，我觉得。

先说下问题吧，说了这么多。

遇到的问题是：

Undefined variable: errors

不知道问题的，可以先试下对应链接里面的教程，走一遍就应该知道问题所在了，在提交错误的时候，会出现这个错误，当然还有另外一个错误，估计都是一个问题导致的。

解决办法是在stackoverflow找到的，唉，其实这个也是一个国外的框架，先不管看法的人是不是国内的，知道在国内还没有发现有人遇到这个问题，估计遇到的也不是很多。

解决问题的连接地址放在这里：

http://stackoverflow.com/questions/34420590/laravel-5-2-validation-errors

这里展示一下我修改后的代码：

```php
Route::group(['middleware' => ['web']], function () {

    Route::get('/', function () {
        $tasks = Task::orderBy('created_at', 'asc')->get();
        return view('tasks', [
            'tasks' => $tasks
        ]);
    });

    Route::post('/task', function (Request $request) {

        $validator = Validator::make($request->all(), [
            'name' => 'required|max:255'
        ]);

        if ($validator->fails()) {
            return redirect('/')
                ->withInput()
                ->withErrors($validator);
        }

        $task = new Task;
        $task->name = $request->name;
        $task->save();

        return redirect('/');
    });

    Route::delete('/task/{id}', function ($id) {
        Task::findOrFail($id)->delete();

        return redirect('/');
    });
});
```

主要是把我们的Router放在

```php
Route::group(['middleware' => ['web']], function () {

});
```


