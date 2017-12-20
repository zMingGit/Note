
## Start or Stop
sudo /etc/init.d/mysql start|stop


## Monitor

mysql配置文件`my.cnf`中添加配置

```
general_log = 1

log=/var/log/mysqld_query.log
```

或者在命令里使用:
```
SET GLOBAL general_log = 'ON';
SET GLOBAL general_log_file = '/var/log/mysql.log';
```
文件需要提前创建，而且保证访问权限。

### 日志文件权限
1. 保证linux中拥有权限
2. mysql设置(如果linux中已经是777权限，还报错，那么需要修改这个文件，添加路径和权限)
```
    sudo vi /etc/apparmor.d/usr.sbin.mysqld
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