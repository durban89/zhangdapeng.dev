---
title: "iOS7 中 通过UIImagePickerController选择图片后 UIImagePickerControllerDelegate方法的调用"
date: "2025-06-27 09:45:37"
slug: "ios7-zhong-tong-guo-uiimagepickercontroller-xuan-ze-tu-pian-hou-uiimagepickercontrollerdelegate-fang-fa-de-diao-yong"
categories: ["技术"]
tags: ["iOS"]
aliases:
  - "/2025/06/27/iOS7-中-通过UIImagePickerController选择图片后-UIImagePickerControllerDelegate方法的调用/"
  - "/2025/06/27/iOS7-中-通过UIImagePickerController选择图片后-UIImagePickerControllerDelegate方法的调用.html"
  - "/iOS7-中-通过UIImagePickerController选择图片后-UIImagePickerControllerDelegate方法的调用/"
  - "/iOS7-中-通过UIImagePickerController选择图片后-UIImagePickerControllerDelegate方法的调用.html"
  - "/2025/06/27/ios7-zhong-tong-guo-uiimagepickercontroller-xuan-ze-tu-pian-hou-uiimagepickercontroller/"
  - "/2025/06/27/ios7-zhong-tong-guo-uiimagepickercontroller-xuan-ze-tu-pian-hou-uiimagepickercontro.html"
  - "/ios7-zhong-tong-guo-uiimagepickercontroller-xuan-ze-tu-pian-hou-uiimagepickercontrollerdelegat.html"
---
图片选择完后的两个重要的方法

```objectivec
-(void) imagePickerController:(UIImagePickerController *)picker didFinishPickingMediaWithInfo:(NSDictionary *)info{
    [picker dismissViewControllerAnimated:YES completion:^{}];
    
    
    UIImage *image = [info objectForKey:UIImagePickerControllerEditedImage];
    /* 此处info 有六个值
     * UIImagePickerControllerMediaType; // an NSString UTTypeImage)
     * UIImagePickerControllerOriginalImage;  // a UIImage 原始图片
     * UIImagePickerControllerEditedImage;    // a UIImage 裁剪后图片
     * UIImagePickerControllerCropRect;       // an NSValue (CGRect)
     * UIImagePickerControllerMediaURL;       // an NSURL
     * UIImagePickerControllerReferenceURL    // an NSURL that references an asset in the AssetsLibrary framework
     * UIImagePickerControllerMediaMetadata    // an NSDictionary containing metadata from a captured photo
     */
    //获取图片后的操作
}

-(void) imagePickerControllerDidCancel:(UIImagePickerController *)picker{
    [picker dismissViewControllerAnimated:YES completion:^{}];
}
```

记录下，这个方法很重要，要不然找不到选择的图片就完蛋了

