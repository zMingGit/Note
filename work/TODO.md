

python-seafile renam file测试，不加reloaddir的话第二次会报错.

3. 这两个做完了再分析下 seafevents 算 diff 为什么比较耗内存吧

上周让他们把内存加大就好了，计算完后内存会下降回去。

订阅测试机器的redis数据，然后测试.不能有修改数据的操作.