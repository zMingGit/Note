python 提供 -m[mod] 选项， 来装作运行一个模块的样子.

比如:
    python -m test

不同点:

    会将这个文件的目录添加到sys.path中.
    sys.argv中的第一个参数(文件名)会改成绝对路径
    运行的时候不能添加最后的`.py`后缀