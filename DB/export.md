
## Start or Stop
sudo /etc/init.d/mysql start|stop


## Monitor
```
write user and pwd to /etc/mysql/mysql.con  
mysqldump --compact  --skip-add-locks --skip-add-drop-table --skip-comments seahub  > sql/mysql_new.sql
```


## Export
```
sqlite3 seahub/seahub_d.db .dump > sql/sqlite3_new.sql
```
sudo tail -f /var/lib/mysql/zming-virtual-machine.log 

mysqldump --single-transaction --quick --compact  --skip-add-locks --skip-add-drop-table --skip-comments 
-K seahub > alldb.sql



mysqldump --single-transaction --quick --compact  --skip-add-locks --skip-add-drop-table --skip-comments --skip-set-charset -K --dump-date seahub > alldb.sql

mysqldump --opt seahub > alldb.sql



mysqldump  --create-options --disable-keys --skip-add-drop-table --skip-add-locks --skip-comments  --extended-insert --lock-tables --quick --set-charset  seahub_export > alldb.sql



into sqlite3


sqlite3 some.db .schema > schema.sql
sqlite3 seahub_export.db .dump > dump.sql