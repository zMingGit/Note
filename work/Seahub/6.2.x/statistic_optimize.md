将十分钟内的用户记录在字典中。

每十分钟将这个字典中的数据，分次批量replace(insert or  delete then insert)到数据库。

对于分布式也无所谓，因为mysql操作有自身的锁。


锁

10 -> 30分钟

去掉最后登陆时间.

retry

log 多少条信息被记录

timer