`demo.seafile.top`日志 :

```
[2017-11-07 14:06:21,865] [WARNING] error when invoking libreoffice: Traceback (most recent call last):
  File "/opt/seafile/seafile-pro-server-6.1.10/pro/python/seafevents/office_converter/unoconv.py", line 19, in <module>
    from distutils.version import LooseVersion
  File "/usr/lib/python3.4/distutils/version.py", line 29, in <module>
    import re
  File "/usr/lib/python3.4/re.py", line 324, in <module>
    import copyreg
  File "/opt/seafile/seafile-pro-server-6.1.10/seahub/thirdpart/future-0.16.0-py2.7.egg/copyreg/__init__.py", line 7, in <module>
    raise ImportError('This package should not be accessible on Python 3. '
ImportError: This package should not be accessible on Python 3. Either you are trying to run from the python-future src folder or your installation of python-future is corrupted.
```

转换ppt、xlsx的时候出问题， seafevents使用python3调用unoconv.py， 当导入copyreg的时候，检查PYTHONPATH，发现seahub/thirdpart/future-0.16.0-py2.7.egg／下有这个模块，但是这个包的代码限定了只能python3以下的python版本才能运行，所以报错。

检查打包机器上的对应包的内容，发现thirpart下没有这个文件夹，于是移动demo站点上的copyreg到PYTHONPATH路径外。恢复正常



