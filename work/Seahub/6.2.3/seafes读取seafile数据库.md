## 需求
seafes不依赖与seafile，如果需要获得对应数据，通过数据库直接获取

## 设计
添加`seafes_data`目录，用于获取seafes需要的数据。

`seafes_data`下添加`db.py`文件, 用于读取seafile配置并连接到需要的数据库。
`seafes_data`下添加`seafile_methods.py`文件，用于查询数据库数据。