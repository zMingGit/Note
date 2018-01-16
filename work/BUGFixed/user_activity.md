由于原来的表结构为id, username, timstamp
现在改为了name_time_md5, username, timestamp

所以需要更改表结构.


```
ALTER TABLE UserActivityStat MODIFY id name_time_md5 varchar(32) primary key

ALTER TABLE UserActivityStat CHANGE id new_col_name name_time_md5 varchar(32) primary key;
```