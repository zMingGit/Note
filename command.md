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



### ES单节点信息监控 

```
curl http://localhost:9200/_nodes/stats
```

### ES简单查询

```
curl -XGET http://127.0.0.1:9200/repofiles/_search? -d '
{
"query": {
}}
'

curl -XGET http://127.0.0.1:9200/repofiles/_search? -d '
{
"query": {
 "bool": {
  "filter": [
   {"term": {"repo": "abfb2b79-78c2-48a4-836a-27e642831b0f"}}
  ]
 }
}}
'
```


## NET
```
dotnet new console -o hwapp
cd hwapp
dotnet restore
dotnet run
```



%3rDM21].j#_V?S*

 python /usr/local/shadowsocks/server.py -c /etc/shadowsocks.json -d start



 https://raw.githubusercontent.com/zMingGit/Picture/master/



curl -d "username=foo@foo.com&password=foo" http://192.168.1.227/api2/auth-token/

curl -H "Authorization: Token 391d0cb4009dfecd5c9d55eaf241e486cde6b6cc" http://192.168.1.227/api2/repos/08320006-46d8-4128-8f16-fff48470b752/dir/


api/v2.1/deleted-repos/

curl -d "repo_id=08320006-46d8-4128-8f16-fff48470b752" -H "Authorization: Token 391d0cb4009dfecd5c9d55eaf241e486cde6b6cc" http://192.168.1.227/api/v2.1/deleted-repos/




share_admin Library -> shared_repos



