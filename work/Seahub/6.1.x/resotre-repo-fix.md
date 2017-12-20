## restore repo

问题:在恢复未删除的repo以后底层会返回511

### 需求api

获得repo的拥有者（已删除repo的情况下）
```
function(repo_id){
    ...
    return repo_owner
}
```