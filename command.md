## command

### kill process
```
PROCESS=`ps -ef|grep ccnet-server|grep -v grep|grep -v PPID|awk '{ print $2 }'`
for i in $PROCESS
do
	  echo "Kill the $1 process [ $i  ]"
	    kill -9 $i
done
```

