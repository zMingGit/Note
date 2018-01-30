
## 需求
系统管理员在系统管理的资料库选项中，可以用每个资料库后面的共享图标将资料库共享给其他用户或者组。

## 设计
使用已有的ExtraSharePermission和ExtraGroupSharePermission表，将共享关系记录下来，用于覆盖底层的r、rw权限，实现admin权限的增加.

## 改动
### API修改
- api-v2.1-admin-shares 增加admin权限对应的代码
- api2-dir-shared-items 共享通用函数修改后影响对应的代码
- api-v2.1-group-libraries 共享通用函数修改后影响对应的代码

### 共享功能通用函数

- 增加`unshare_dir_to_user`函数
- 增加`unshare_dir_to_group`函数
- 增加`has_shared_to_user`函数
- 增加`has_shared_to_group`函数
- `check_user_share_out_permission`, `check_user_share_in_permission`注释修改

### 前端
- 修改sysadmin下对应模板，支持admin的逻辑
- 修改`sysadmin-app/views/folder-share-item`增加`is_admin`字段处理逻辑
- 修改`sysadmin-app/views/share.js`添加`is_admin`字段

### 测试
- 修改`seahub/test_utils`文件，增加`share_repo_to_admin_with_admin_permission`和`share_repo_to_group_with_admin_permission`函数
- 修改`tests/api/end/admin/test_shares`文件，添加查询、共享、修改权限、删除等对应admin权限的测试函数.