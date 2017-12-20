## 批量从Excel导入用户(.xlsx文件)

## 第三方库选择

#### 因为只要读excel数据，所以只选取侧重读的第三方库
* openpyxl  (读写Excel的xlsx/xlsm格式文件的库)
* xlrd  (支持xls以及xlsx格式的excel，官方说明如果不需要xls格式支持的话用openpyxl去代替)
* pandas (底层还是用的xlrd第三方库，不过现在做数据处理这个用的比较多)

## 第三方库测试

xlrd 加载1w行的xlsx文件需要1.6秒左右， 而且没看到文档中有优化

openpyxl 正常加载1w行的xlsx文件需要7秒左右

openpyxl 添加只读模式进行加载1w行的xlsx文件需要10毫秒左右的时间。

pandas 底层使用xlrd对于excel进行解析，所以就不进行测试了。

## View
```

post -F file=excel.xlsx useradmin/batchadduser/
    
	Failed:
			invalid file format.
			invalid file data.
			number of users exceeds the limit.
			encrypt file.
			compressed file.

get useradmin/batchadduser_help/?type=xlsx
	The type can be XLSX format.
	return the xlsx file.
```

## Remove

remove csv feature