---
title: "Create thumbnails for an ImageField in django(创建缩略图)"
date: "2025-06-20 14:13:17"
slug: "create-thumbnails-for-an-imagefield-in-django-chuang-jian-suo-lve-tu"
categories: ["技术"]
tags: ["Django"]
aliases:
  - "/2025/06/20/Create-thumbnails-for-an-ImageField-in-django(创建缩略图)/"
  - "/2025/06/20/Create-thumbnails-for-an-ImageField-in-django(创建缩略图).html"
  - "/Create-thumbnails-for-an-ImageField-in-django(创建缩略图)/"
  - "/Create-thumbnails-for-an-ImageField-in-django(创建缩略图).html"
  - "/2025/06/20/Create-thumbnails-for-an-ImageField-in-django-创建缩略图/"
  - "/2025/06/20/Create-thumbnails-for-an-ImageField-in-django-创建缩略图.html"
  - "/2025/06/20/create-thumbnails-for-an-imagefield-in-django-chuang-jian-suo-lve-tu/"
  - "/2025/06/20/create-thumbnails-for-an-imagefield-in-django-chuang-jian-suo-lve-tu.html"
  - "/create-thumbnails-for-an-imagefield-in-django-chuang-jian-suo-lve-tu.html"
---
Create thumbnails for an ImageField in django，在django中创建缩略图的过程其实有两种方法，第一种方法是比较传统的就是直接使用写入的方法，第二种方式就是使用PIL，我这里针对自己项目的需要，需要实现直接上传直接切图的功能。

功能实现：

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
        file_name = os.path.join('upload/'+type+'/small',name+'_small'+ext)
        path_name = os.path.join(MEDIA_ROOT, file_name)
        img.save(path_name)

        return(file_name)
    return(file_name)
```

因为是要传递三种不同尺寸的图片，并且图片的也不同，一个大的一个中等的一个小的。

创建的form是这样的 如下：

```python
class ManCreateForm(forms.Form):
    GENDER = (
       (0, u'展示'),
       (1, u'不展示'), 
       )

    title = forms.CharField(max_length=255, label='标题',widget=forms.TextInput(attrs={'placeholder':'标题','class':'input-block-level span8'}))
    url_address = forms.CharField(label='详情地址', widget=forms.TextInput(attrs={'placeholder':'详情地址','class':'input-block-level span8'}))
    description = forms.CharField(label='详情简介',widget=forms.Textarea(attrs={'placeholder':'详情简介','class':'input-block-level span8'}))
    large_image = forms.ImageField(label='大图',widget=forms.ClearableFileInput(attrs={'placeholder':'大图','class':'input-block-level span8'}))
    middle_image = forms.ImageField(label='中图',widget=forms.ClearableFileInput(attrs={'placeholder':'中图','class':'input-block-level span8'}))
    small_image = forms.ImageField(label='小图',widget=forms.ClearableFileInput(attrs={'placeholder':'小图','class':'input-block-level span8'}))
    show = forms.ChoiceField(label='是否展示',widget=forms.Select,choices=GENDER)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title is None:
            raise forms.ValidationError("标题不能为空")

        return title

    def clean_url_address(self):
        url = self.cleaned_data['url_address']
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError:
            raise forms.ValidationError("详情地址必须是标准的url地址")

        return url



class WomanCreateForm(forms.Form):
    GENDER = (
       (0, u'展示'),
       (1, u'不展示'), 
       )
    title = forms.CharField(max_length=255, label='标题',widget=forms.TextInput(attrs={'placeholder':'标题','class':'input-block-level span8'}))
    description = forms.CharField(label='详情简介',widget=forms.Textarea(attrs={'placeholder':'详情简介','class':'input-block-level span8'}))
    url_address = forms.CharField(label='详情地址',widget=forms.TextInput(attrs={'placeholder':'详情地址','class':'input-block-level span8'}))
    large_image = forms.ImageField(label='大图',widget=forms.ClearableFileInput(attrs={'placeholder':'大图','class':'input-block-level span8'}))
    middle_image = forms.ImageField(label='中图',widget=forms.ClearableFileInput(attrs={'placeholder':'中图','class':'input-block-level span8'}))
    small_image = forms.ImageField(label='小图',widget=forms.ClearableFileInput(attrs={'placeholder':'小图','class':'input-block-level span8'}))
    show = forms.ChoiceField(label='是否展示',widget=forms.Select,choices=GENDER)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title is None:
            raise forms.ValidationError("标题不能为空")

        return title

    def clean_url_address(self):
        url = self.cleaned_data['url_address']
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError:
            raise forms.ValidationError("详情地址必须是标准的url地址")

        return url

class GiftsCreateForm(forms.Form):
    GENDER = (
       (0, u'展示'),
       (1, u'不展示'), 
       )
    title = forms.CharField(max_length=255, label='标题',widget=forms.TextInput(attrs={'placeholder':'标题','class':'input-block-level span8'}))
    description = forms.CharField(label='详情简介',widget=forms.Textarea(attrs={'placeholder':'详情简介','class':'input-block-level span8'}))
    url_address = forms.CharField(label='详情地址',widget=forms.TextInput(attrs={'placeholder':'详情地址','class':'input-block-level span8'}))
    large_image = forms.ImageField(label='大图',widget=forms.ClearableFileInput(attrs={'placeholder':'大图','class':'input-block-level span8'}))
    middle_image = forms.ImageField(label='中图',widget=forms.ClearableFileInput(attrs={'placeholder':'中图','class':'input-block-level span8'}))
    small_image = forms.ImageField(label='小图',widget=forms.ClearableFileInput(attrs={'placeholder':'小图','class':'input-block-level span8'}))
    show = forms.ChoiceField(label='是否展示',widget=forms.Select,choices=GENDER)

    def clean_title(self):
        title = self.cleaned_data['title']
        if title is None:
            raise forms.ValidationError("标题不能为空")

        return title

    def clean_url_address(self):
        url = self.cleaned_data['url_address']
        validate = URLValidator()
        try:
            validate(url)
        except ValidationError:
            raise forms.ValidationError("详情地址必须是标准的url地址")

        return url
```

三个类里面的内容基本上是一样的，只不过我追求名称的区分，就写了三个

