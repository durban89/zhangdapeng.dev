---
title: "Django简单实现创建，更新，删除的功能，外加图片的简单处理"
date: "2025-06-24 15:04:40"
slug: "django-jian-dan-shi-xian-chuang-jian-geng-xin-shan-chu-de-gong-neng-wai-jia-tu-pian-de-jian-dan-chu-li"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/24/Django简单实现创建，更新，删除的功能，外加图片的简单处理/"
  - "/2025/06/24/Django简单实现创建，更新，删除的功能，外加图片的简单处理.html"
  - "/Django简单实现创建，更新，删除的功能，外加图片的简单处理/"
  - "/Django简单实现创建，更新，删除的功能，外加图片的简单处理.html"
  - "/2025/06/24/Django简单实现创建-更新-删除的功能-外加图片的简单处理/"
  - "/2025/06/24/Django简单实现创建-更新-删除的功能-外加图片的简单处理.html"
  - "/2025/06/24/django-jian-dan-shi-xian-chuang-jian-geng-xin-shan-chu-de-gong-neng-wai-jia-tu-pian-de-/"
  - "/2025/06/24/django-jian-dan-shi-xian-chuang-jian-geng-xin-shan-chu-de-gong-neng-wai-jia-tu-pian.html"
  - "/django-jian-dan-shi-xian-chuang-jian-geng-xin-shan-chu-de-gong-neng-wai-jia-tu-pian-de-jian-da.html"
---
在开发walkerfree的过程中，我用到了Django这个框架，说实话，我用了使用了，都是滥用，喜欢自己写一些东西，于是有些Django写好的，比较方便的功能，没有去体会。好了长话短说，嘿嘿，看代码

第一个：添加条目的代码如下

```python
@login_required
def gifts_add(request):
    '''
    Feeling的添加
    '''
    if request.user.is_authenticated():
        user = request.user
    else:
        user = request.user
    if request.method == 'POST':
        form = GiftsCreateForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            url_address = form.cleaned_data['url_address']
            description = form.cleaned_data['description']
            show = form.cleaned_data['show']
            category = form.cleaned_data['category']
            large_image = upload_image_file(request.FILES['large_image'], type='gifts',size_type='large',image_size=480)
            middle_image = upload_image_file(request.FILES['middle_image'], type='gifts',size_type='middle',image_size=320)
            small_image = upload_image_file(request.FILES['small_image'], type='gifts',size_type='small',image_size=200)
            obj = Gifts(
title=title,
description = description,
url_address = url_address,
large_image = large_image,
middle_image = middle_image,
small_image = small_image,
is_show = show,
                category_id = category,
user_id = user.id,
create_date = datetime.now().strftime("%Y-%m-%d %H:%I:%S"),
update_date = datetime.now().strftime("%Y-%m-%d %H:%I:%S"),
)
            try:
                obj.save()
                return HttpResponseRedirect(reverse('accounts_gifts'))
            except:
                return HttpResponseRedirect(reverse('accounts_gifts'))
    else:
        form = GiftsCreateForm()
    return render_to_response('accounts/gifts_add.html',{'user':user,'action':'gifts', 'form':form},context_instance=RequestContext(request))
```

第二个：更新条目的代码

```python
@login_required
def gifts_update(request,id):
    '''
    Feeling的更新
    '''
    if request.user.is_authenticated():
        user = request.user
        obj = Gifts.objects.filter(id=id,user_id=user.id).get()
        if request.method == 'POST':
            if request.POST['title']:
                obj.title = request.POST['title']
            if request.POST['url_address']:
                obj.url_address = request.POST['url_address']
            if request.POST['show']:
                obj.is_show = request.POST['show']
            if request.POST['category']:
                obj.category_id = request.POST['category']
            if 'large_image' in request.FILES:
                #删除文件
                delete_image_file("%s" % obj.large_image)
                #存储文件
                large_image = upload_image_file(request.FILES['large_image'], type='gifts',size_type='large',image_size=480)
                obj.large_image = large_image
            if 'middle_image' in request.FILES:
                #删除文件
                delete_image_file("%s" % obj.middle_image)
                #存储文件
                middle_image = upload_image_file(request.FILES['middle_image'], type='gifts',size_type='middle',image_size=320)
                obj.middle_image = middle_image
            if 'small_image' in request.FILES:
                #删除文件
                delete_image_file("%s" % obj.small_image)
                #存储文件
                small_image = upload_image_file(request.FILES['small_image'], type='gifts',size_type='small',image_size=200)
                obj.small_image = small_image
            obj.save()
            return HttpResponseRedirect(reverse('accounts_gifts'))
        else:
            show = {}
            show[0] = u'显示'
            show[1] = u'不显示'
            category = {0:u'时尚女装',1:u'帅气男装',2:u'精品箱包'}
        return render_to_response('accounts/gifts_update.html',{'user':user,'action':'gifts','obj':obj,'show':show,'category':category},context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect(reverse('home'))
```

第三个：删除条目的代码：

```python
@login_required
def gifts_delete(request,id):
    '''
    Feeling的删除
    '''
    if request.user.is_authenticated() and request.method == 'POST':
        user = request.user
        try:
            #查找需要的Item
            obj = Gifts.objects.filter(id=id, user_id=user.id).get()
            delete_image_file("%s" % obj.large_image)
            delete_image_file("%s" % obj.middle_image)
            delete_image_file("%s" % obj.small_image)
            Gifts.objects.filter(id=id,user_id=user.id).delete()
            json_data = simplejson.dumps({'message':u'操作成功','status_code':1})
            return HttpResponse(json_data,mimetype='application/json')
        except Exception, data:
            json_data = simplejson.dumps({'message':u'操作失败','status_code':0,'data':data})
            return HttpResponse(json_data,mimetype='application/json')
    else:
        json_data = simplejson.dumps({'message':u'操作失败','status_code':0})
        return HttpResponse(json_data,mimetype='application/json')
```

第四个:添加图片的代码

```python
def upload_image_file(file, type='gifts',size_type='large',image_size = 480):
    '''文件上传函数,上传的文件夹一定要存在'''
    if file:
        size = image_size
        parser = ImageFile.Parser()
        for content in file.chunks():
            parser.feed(content)
        img = parser.close()
        width, height = img.size
        if width > size:
            delta = width / size
            height = int(height / delta)
            img.thumbnail((size, height), Image.ANTIALIAS)
        name, ext = os.path.splitext(os.path.basename(file.name))
        name = uuid.uuid4().hex
        now = datetime.now()
        datetime_path = '/%s/%s/%s' % (now.year, now.month, now.day)
        file_dir_path = 'upload/'+type+ '/' +size_type + datetime_path + '/'
        full_file_dir_path = os.path.join(MEDIA_ROOT, file_dir_path)
        #要存储的文件的名字
        file_name = name + '_' + size_type +ext
        #如果目录不存在则创建
        if os.path.exists(full_file_dir_path) == False:
            os.makedirs(full_file_dir_path,0777)
        #保存到数据库的名字
        save_file_name = os.path.join(file_dir_path ,file_name)
        #存储到服务器的文件名字
        path_name = os.path.join(full_file_dir_path, file_name)
        img.save(path_name)
        return(save_file_name)
```

第五个：删除图片的代码：

```python
def delete_image_file(file_path, type='gifts',size_type='large',image_size = 480):
    '''
    删除文件
    '''
    #/home/xx/T2DdJiXlXOXXXXXXXX_499983611_large_large_large_large_large.jpg
    file_full_path = os.path.join(MEDIA_ROOT, file_path)
    if os.path.exists(file_full_path):
        if os.path.isfile(file_full_path):
            #return file_full_path
            os.remove(file_full_path)
```
