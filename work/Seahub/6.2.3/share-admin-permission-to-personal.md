## 需求

共享的时候增加admin权限

1. admin

    被共享者可以共享资料库及其子目录(无法共享给repo的拥有者)，也可以修改、删除已有共享记录。

~~2. preview~~

 ~~使被共享者只能拥有移除这个共享纪录和预览文件的功能。~~

## 设计

### 新增数据库

此表作为底层权限控制的扩展

```
         ExtraSharePermission

repo_id     char(36)    db_index                被分享的repo
share_to    char(255)   db_index                被分享的人
permission  char(30)                            权限(admin, preview)

```


### api修改:

	api2/repos/repo_id/dir/shared_items/:
		介绍:
			用于资料库及其子目录的所有共享记录的显示、添加、更改和删除。
		更改: 
			权限判断的时候如果不是repo拥有者或者不是admin权限用户，则无法操作。
			PUT:
				添加admin和preview的权限处理。记录在ExtraSharePermission表,同时在底层添加r(preview)和rw(admin)权限记录。
          POST:
				同样会更新seahub端的共享记录。
          GET:
				查看的时候，会返回给前端seahub扩展的分享权限表和底层的分享权限表整合过的记录
          DELETE:
				添加preview和admin权限删除逻辑，删除ExtraSharePermission表数据，同时删除底层(seafile server)的r(preview)和rw(admin)权限。

    api2/beshared-repos/:
        介绍:
            用于取消共享
        改动:
            DELETE:
				删除操作中会删除seahub扩展的分享权限表的记录。

    api/v2.1/shared-repos/repo_id/
        介绍:
            用于更新share admin下repo的分享权限
        改动:
            GET:
                对所有用户，如果存在于ExtraSharePermission表中，那么往返回结果中添加记录。（对于repo拥有者，这api是正常的，因为之前都是以拥有者名义去分享，但是对于其它admin权限用户来说，就不正常了，所以需要将ExtraSharePermission表中的记录添加到每个admin用户的返回结果中。）  逻辑 -->  获得extra表中自己为admin权限的所有repo_id，调用seafile_api.list_repo_shared_to获得分享的所有记录，添加到结果中。
            PUT:
                增加admin判断，以及更新ExtraSharePermission表.
            DELETE:
                如果为admin权限，删除ExtraSharePermission对应的记录
             
    ajax/lib/repo_id/dir
    	改动:
    		GET：
    			添加admin权限

### 界面修改:

1. 在分享资料库或者子文件夹的界面，会增加admin~~和preview~~权限的选择，下方会显示资料库或者子文件夹分享出去的所有共享记录（包括其它admin分享出去的记录）。

2. 在Share with me 选项下，会显示所有被分享给自己的资料库，如果为admin权限，那么会多处来一个分享的图标，可以分享给其他人。在资料库内，admin权限用户可以做的操作与rw权限用户一样~~，preview权限用户什么都做不了，只能点击文件后预览。~~

3. share admin下的Library中会显示资料库分享给其它用户的所有记录。以及其中的权限编辑选项会添加admin~~、preview的~~权限。~~（其中分享给用户和组没有很好的区分，如果组名称和用户名称一样，会混淆）~~

~~3. shared with groups下的repo，如果分享的是admin权限，那么对于groups的所有管理员，也会额外显示一个分享的图标。资料库内可以做的操作与rw权限的用户一样。~~

## 实现

共享逻辑:

	共享的时候如果权限为admin或者preview，那么会记录到ExtraSharePermission 表。而由于文件的操作权限会检查repo和文件的父文件夹权限，所以在记录额外的admin以及preview权限的时候，在底层(seafile server)也需要添加对应的r(preview)，rw(admin)权限。
    因为共享是作为repo的一个属性，无关于share_from字段，谁分享的这类信息并没有很好的意义，所以在底层需要share_from字段的时候，替换成repo的拥有者交给底层。

## 功能实例介绍:

1. a 分享给b admin权限,b 能分享给c 任意权限， a就不能再次分享给c同一个repo(因为已经存在这次分享)，只能修改b分享给c的权限。a和b用户都能看到repo被分享给别人的所有记录，同时也能修改、取消共享已有共享记录。

~~2. a 分享给b preview权限，b只能取消这次共享和进入repo，预览支持预览格式的文件。~~

~~3. a 分享给b组 admin权限，b组内只有group管理员才能共享给其它组或者其它人。a和b组内的管理员都能看到repo被分享给别人的所有记录，同时也能修改、取消共享已有共享记录。~~



~~## 问题~~  
~~两个用户分享同一个repo到另外一个人，另外一个人这里只能看到一个repo，(需要看到多个repo吗),如果两个人分享的权限不同，是以权限最高的为准吗。~~



~~## 文件夹共享~~  
~~判断是否为repo的拥有者或者在seahub的共享权限表中权限是否为admin.~~  
~~判断是否已经共享过~~  
~~判断路径是否为／~~  
~~如果不为/ 代表共享的是个文件夹，底层会共享文件夹后，返回一个新的repo id~~  
~~否则代表共享一个repo，底层不返回数据。~~  
~~seahub判断，如果共享的是文件夹，则使用文件夹共享后的产生的repo的ip，否则使用原repo.~~  
~~(ps: 所以seahub数据库的path可以删除了)~~