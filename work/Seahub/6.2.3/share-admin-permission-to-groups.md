## 需求

把repo共享给组的时候增加admin权限。


## 设计

```
         ExtraGroupsSharePermission

repo_id     char(36)    db_index                be shared repo
group_id    char(255)   db_index                be shared group id
permission  char(30)                            permission(admin)

```



## 改动

### 界面修改:
	分享弹窗中添加admin权限选择。
	share with groups/All groups中添加分享图标(如果分享的是admin权限，才能看得到).
	分享给组的modal下的记录会有admin权限显示，编辑的时候也增加admin权限选项。


### API修改:
	
	api2/repos/(?P<repo_id>[-0-9a-f]{36})/dir/shared_items/:
		GET:
			返回带有admin权限的记录
		PUT:
			添加记录，如果为adim权限，底层记录rw权限，额外记录在ExtraGroupsSharePermission表中。
		Delete:
			添加删除ExtraGroupsSharePermission表中记录的操作
		POST：
			添加更行ExtraGroupsSharePermission表中记录的操作


	groups/(?P<group_id>\d+)/repos/:
		GET:
			返回带admin权限的记录
			获得指定组中分享给admin权限的所有资料库，然后判断资料库是否在列表中。


	groups/(?P<group_id>\d+)/repos/(?P<repo_id>[-0-9a-f]{36})／
		DELETE:
			添加删除ExtraGroupsSharePermission表的操作
			
			
	api/v2.1/groups/(?P<group_id>\d+)/
		Delete:
			将被删除的组的记录从ExtraGroupsSharePermission表中移除。
			
	ajax/lib/(?P<repo_id>[-0-9a-f]{36})/dir/:
		添加is_admin字段，前端需要。
		获得资料库名称，判断用户是否拥有admin权限，然后is_admin字段。
		
	api/v2.1/groups/:
		Get:
		获得组信息的时候，会填充是否为管理员的信息进去。
		
		将用户所在的组和组内的每个资料库做一个元祖，然后组合成集合，数据库中查询记录，判断这个组是否拥有admin权限。


### 信号

	seahub.share.models下repo被移除的信号的处理函数中删除ExtraGroupsSharePermission表的记录
	seahub/group/views.py文件下remove_group_common函数:
	删除组的时候会删除ExtraGroupsSharePermission表中的记录
		
	