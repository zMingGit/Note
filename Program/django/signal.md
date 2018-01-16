## Signal

### 初始化
如要传入调用回调函数的参数，以及是否使用缓存. 其实感觉这个参数传入没啥意义，反正不会检查.

### 绑定回调函数

使用receive这个装饰器去讲函数放入signal内部的receivers里面，然后清除所有缓存。


### 调用
当调用send以后，会去遍历receiver里面的所有函数，然后放入缓存，在调用、返回结果。

如果不添加新的回调函数，那么下次发送信号的时候，会直接返回缓存中receivers的值。