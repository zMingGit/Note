## 现在文件夹或者repo分享给某个组的流程

```
select获得当前用户的所有group->选择group->提交->
->后台调用底层完成->发送send通知model去更新。
```


## 逻辑步骤

seahub配置setting添加  ENABLE_SHARE_TO_ALL_GROUPS

前端通过libraries视图将 seahub的ENABLE_SHARE_TO_ALL_GROUPS 设置到 前端的 app.pageOptions上


前端根据配置决定是直接调用自己维护的groups还是ajax请求all_groups的API。然后拿到结果后对结果硬编码到groups select标签的option里面




## api

### struct
```
groups_obj {
    'id': group.id,
    'name': group.name,
    'owner': group.owner,
    'create_at': isoformat_timestr,
    'avatar_url': request.build_absolute_uri(avatar_url),
    'admins': get_group_admins(group.id),
    'wiki_enabled': is_wiki_mod_enabled_for_group(group_id)
}
```
### GET
```
get api/v2.1/groups/all/

200 Response({'repos': [groups_obj1, groups_obj2....]})
```



[
(dt(2017,5,16,0,0,0), 'Added', 1),
(dt(2017,5,16,0,0,0), 'Deleted', 2),
(dt(2017,5,16,0,0,0), 'Visited', 3),

(dt(2017,5,17,0,0,0), 'Added', 11),
(dt(2017,5,17,0,0,0), 'Deleted', 22),

(dt(2017,5,19,0,0,0), 'Deleted', 22),

]



```
fill_data

res_list
[
    1,1,1,1
]



res_list
[
    2,2,1,2
]
temp_list 
[
    (dt(2017,5,16,0,0,0), 'Added', 1),
    (dt(2017,5,16,0,0,0), 'Deleted', 2),
    (dt(2017,5,16,0,0,0), 'Visited', 3),
    (dt(2017,5,17,0,0,0), 'Added', 11),
    (dt(2017,5,17,0,0,0), 'Deleted', 22),
    (dt(2017,5,19,0,0,0), 'Deleted', 22),
]


res_list
[
    2,2,1,2, 
    (dt(2017,5,18,0,0,0), 'Added', 0),
    (dt(2017,5,18,0,0,0), 'Deleted', 0),
    (dt(2017,5,18,0,0,0), 'Visited', 0),
]



res_list
[
    (dt(2017,5,18,0,0,0), 'Added', 0),
    (dt(2017,5,18,0,0,0), 'Deleted', 0),
    (dt(2017,5,18,0,0,0), 'Visited', 0),
    (dt(2017,5,16,0,0,0), 'Added', 1),
    (dt(2017,5,16,0,0,0), 'Deleted', 2),
    (dt(2017,5,16,0,0,0), 'Visited', 3),
    (dt(2017,5,17,0,0,0), 'Added', 11),
    (dt(2017,5,17,0,0,0), 'Deleted', 22),
    (dt(2017,5,19,0,0,0), 'Deleted', 22),
]



change struct


[
{'datetime': '2017-5-16T0:0:0', 'Added': 1, 'Deleted': 2, 'Visited': 3},
{'datetime': '2017-5-17T0:0:0', 'Added': 11, 'Deleted': 22, 'Visited': 0},
{'datetime': '2017-5-18T0:0:0', 'Added': 0, 'Deleted': 0, 'Visited': 0},
{'datetime': '2017-5-19T0:0:0', 'Added': 0, 'Deleted': 22, 'Visited': 0},
]

```

(datetime.datetime(2017, 8, 9, 3, 3), 'Added', 1)
(datetime.datetime(2017, 8, 9, 3, 3), 'Deleted', 1)
(datetime.datetime(2017, 8, 9, 3, 3), 'Visited', 1)


(datetime.datetime(2017, 8, 9, 3, 4), 'Added', 1)
(datetime.datetime(2017, 8, 9, 3, 4), 'Deleted', 1)
(datetime.datetime(2017, 8, 9, 3, 4), 'Visited', 1)
(datetime.datetime(2017, 8, 9, 3, 5), 'Added', 1)
(datetime.datetime(2017, 8, 9, 3, 5), 'Deleted', 1)
(datetime.datetime(2017, 8, 9, 3, 5), 'Visited', 1)

