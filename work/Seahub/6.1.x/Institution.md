You need update `settings.py` or '{seafile-project-dir}/conf/seahub_settings.py` file  if you want enable institution options.

example：
```
MULTI_INSTITUTION = True
EXTRA_MIDDLEWARE_CLASSES = (
'seahub.institutions.middleware.InstitutionMiddleware',
)    
```

**when restart service**, admin system interface will increase Institution options, user options will increase Institution info.

`add Institution`: at Institution options,when after click add button,input institution name then click submit button.

![](https://raw.githubusercontent.com/zMingGit/Picture/master/institution/addInst.png)

`update specified user institution`: The mouse moves to the row of the organization of that particular user's row，click button of edit icon, select institution then click blank place.

![](https://raw.githubusercontent.com/zMingGit/Picture/master/institution/userInst.png)

`multi-user modification institution`: when select multi-user, click button of set institution at interface,
then select institution and click blank place.

![](https://raw.githubusercontent.com/zMingGit/Picture/master/institution/usersInst.png)
