##  功能流程

```
客户端发出请求 -> 到达django中间件 -> 中间件执行 -> 如果正常继续访问url对应的视图，否则返回403错误.
```

### 中间件逻辑

```
判断ENABILE_LIMIT_IPADDRESS是否开启，开启则判断当前访问ip是否存在于数据库中可以的ip表或者settings下的默认可以登录的IP列表中。若存在，则返回None表示继续其他中间件执行。否则根据是api请求还是页面请求抛出403错误或者返回403页面。
```


###  页面功能
```
用于向数据库信任ip表中添加或者删除ip。 ps: 不显示settings下可访问的ip列表
```



### 配置
```
settings下:

ENABLE_LIMIT_IPADDRESS控制是否开启限制ip的功能

TRUSTED_IP_LIST为默认可以登录的IP

```


### ip匹配算法

生成所有可以让指定ip通过的ip，利用django的Q查询去查询数据库中是否存在这些生成的ip中的任意一个，存在则ip符合入站规则，否则ip为不可访问的ip。

e.g.
```
匹配ip: 172.13.45.233

生成所有可以通过的ip列表:
172.13.45.233
172.13.45.*
172.13.*.*
172.*.*.*
```


## API


```
ip_obj {
    'ip': ipaddress
}
```




### GET

**结果使用快排进行排序**
```

GET api/v2.1/admin/device-trusted-ip

200 Response([ip_obj1, ip_obj2 ...])
403 ip不在信任ip列表中或者不是pro版本
```

### POST

```
POST -d 'ipaddress=172.1.1.1' api/v2.1/admin/device-trusted-ip

201 Response({'ip': 172.1.1.1})
200 Response({'ip': 172.1.1.1})

403 ip不在信任ip列表中或者不是pro版本
400 ip不符合规范
```


### DELETE
```
DELETE api/v2.1/admin/device-trusted-ip?ipaddress=172.1.1.1

200 Response()

403 ip不在信任ip列表中或者不是pro版本
400 ip不符合规范
```

