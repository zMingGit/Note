actualData {
    'keey_days': xx
}

##  修改某个repo的history设置
PUT  -d "keepdays=4"   api2/admin/repos/(?P<repo_id>)/history-limit/
```
200 Response({actualData1, actualData2....})
403 Response    if not is repo owner,repo is virtual, ENABLE_REPO_HISTORY_SETTING is False
404 Response    if repo does not exists
400 Response    if keeydays is not number or does not exists.
```


