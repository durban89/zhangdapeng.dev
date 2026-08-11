---
title: "关于django的图片文件名称的问题"
date: "2025-06-20 14:13:26"
slug: "guan-yu-django-de-tu-pian-wen-jian-ming-cheng-de-wen-ti"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/关于django的图片文件名称的问题/"
  - "/2025/06/20/关于django的图片文件名称的问题.html"
  - "/关于django的图片文件名称的问题/"
  - "/关于django的图片文件名称的问题.html"
  - "/2025/06/20/guan-yu-django-de-tu-pian-wen-jian-ming-cheng-de-wen-ti/"
  - "/2025/06/20/guan-yu-django-de-tu-pian-wen-jian-ming-cheng-de-wen-ti.html"
  - "/guan-yu-django-de-tu-pian-wen-jian-ming-cheng-de-wen-ti.html"
---
最近在使用django做图片上传的时候，发现一个问题就是，有些在别处下载过来的图片，如果不修改名称就使用的话，导致的结果就是，有时候直接输出会出现显示不了图片的情况，经过检查才发现，是因为图片的名称有特殊字符，导致输出失败，于是决定一下图片的命名方式；

下面是是我对图片进行截切的函数代码;

```python
def upload_large_image_file(file, type='man'):
    '''文件上传函数,上传的文件夹一定要存在'''
    if file:
        size = 480
        #先移动文件，然后截取指定大小尺寸的文件
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
        file_name = os.path.join('upload/'+type+'/large',name+'_large'+ext)
        path_name = os.path.join(MEDIA_ROOT, file_name)
        img.save(path_name)

        return(file_name)
    return(file_name)


def upload_middle_image_file(file, type='man'):
    '''文件上传函数,上传的文件夹一定要存在'''
    if file:
        size = 320
        #先移动文件，然后截取指定大小尺寸的文件
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
        file_name = os.path.join('upload/'+type+'/middle',name+'_middle'+ext)
        path_name = os.path.join(MEDIA_ROOT, file_name)
        img.save(path_name)

        return(file_name)
    return(file_name)


def upload_small_image_file(file,type='man'):
    '''文件上传函数,上传的文件夹一定要存在'''
    if file:
        size = 100
        #先移动文件，然后截取指定大小尺寸的文件
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
        file_name = os.path.join('upload/'+type+'/small',name+'_small'+ext)
        path_name = os.path.join(MEDIA_ROOT, file_name)
        img.save(path_name)

        return(file_name)
    return(file_name)
```

