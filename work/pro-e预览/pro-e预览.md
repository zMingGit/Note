## pro-e 预览

环境要求:
windows, linux, pro enginner/creo, java二次开发的服务

预计实现时间:
    四周

预览处理流程:

1. seahub将文件通过socket发送给java服务。
2. java服务接受到文件， 通过二次开发的功能代码， 将文件转成pdf
3. java服务通过socket发送给seahub服务
4. 通过seafevent进行转换成html
5. seahub获得html进行预览

开发难点:
seahub与java服务之间的文件传输.
java对pro engineer的二次开发，将pro e项目文件转为pdf.

##  dwg 预览

环境要求:
Linux, libredwg, svglib, reportlab

预计实现时间:
3天

预览处理流程:

1. 通过libredwg将dwg转为svg
2. 然后通过svglib将svg转为pdf
3. 通过seafevent进行转换成html
4. seahub获得html进行预览

## vsdx预览

环境要求:
Linux, visio2pdf

预计实现时间:
2天

预览处理流程:

1. 通过visio2pdf将vsdx转为pdf
2. 通过seafevent进行转换成html
3. seahub获得html进行预览


## ms project

环境要求:
Linux, olefile

预计实现实现:
2天

预览处理流程:

1. 通过olefile将mpp转为txt文件，直接显示在页面