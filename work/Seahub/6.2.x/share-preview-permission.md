## Add perview permission when share repo to groups or personal

### Requiements

if you are perviewing permissions, you can only preview files that support preview operations.


### Seahub Changed

The both repo and list_lib_dir related information returned by the seahub will append the extra_permission field.This field means to record the user's extended permissions。this field value can only is either `admin` or `preview`.

```
Model Used:
	path: seahub/share/models.py
	name: ExtraSharePermission, ExtraGroupsSharePermission
	It won't change model schema.
```


```
Api Changes:
	api/v2.1/groups/:
	groups/(?P<group_id>\d+)/repos/:
	api2/beshared-repos/:
	ajax/lib/(?P<repo_id>[-0-9a-f]{36})/dir/:
	api2/repos/(?P<repo_id>[-0-9a-f]{36})/dir/shared_items/:
```

