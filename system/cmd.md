### nohup

```
 nohup ./start.sh > start.log 2>&1 &
```

不接受hup的参数，再关闭shell，注销当前用户以后，不会关闭运行的脚本。

### setsid

```
 setsid ./start.sh
```

将运行的脚本放在1 pid下跑。

### 查询进程下的线程数量

```
cat /proc/{{process pid}}/status
```

可以看到进程的相关信息

或者 `ps hH p {{pid}} | wc -l`

