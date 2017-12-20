## 重构

共享admin权限部分忧郁底层只记录r、rw权限，而seahub部分只记录admin权限，所以在seahub处理请求中会有将admin转为r、rw权限的过程。  
因为这个转换，导致有两个权限记录，有点混淆，所以在seahub处理请求中只保持seahub权限，将底层的处理封装一下，将admin转为r或者rw权限的过程也封装进去。

```
setSeafilePermission(request)
	seaserv.seafserv_threaded_rpc.org_add_share
	seafile_api.org_share_subdir_to_user
	seafile_api.share_repo
	seafile_api.share_subdir_to_user
	
	

updateSeafilePermission(request)
	seafile_api.org_set_share_permission
	seafile_api.org_update_share_subdir_perm_for_user
	seafile_api.set_share_permission
	seafile_api.update_share_subdir_perm_for_user
```