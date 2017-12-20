## Requirements

Quey the repo(all the repo you can access) that name contains specifiy keyword

Parameter not case sensitive.

	The return type is a list, return an empty list if this query is no result, Return all the repos you can access if Parameter is empty string.


##  API Request

### Note

data source: be shared repos + owned repos + group repos + public repos
 
### Repo Object

```
owned repo
{
	'type': 'repo',
	'id': '663d57b8-1602-4d6c-a8e3-1b237ca3a766',
	'owner': 'admin@admin.com',
	'name': 'admin',
	'mtime': '1992-03-21',
	'modifier_email': 'admin@admin.com',
	'modifier_contact_email': 'contart_email(admin@admin.com)',
	'modifer_name': 'name(admin@admin.com)',
	'size': 19,
	'size_formatted': filesizeformat(19),
	'encrypted': False,
	'permission': 'rw',
	'virtual': False,
	'root': '',
	'head_commit_id': commit_id,
	'version': 6.1.7
}
or be shared repo
{
	"type": "srepo",
	"id": r.repo_id,
	"owner": r.user,
	"name": r.repo_name,
	"owner_nickname": email2nickname(r.user),
	"mtime": r.last_modify,
	"mtime_relative": translate_seahub_time(r.last_modify),
	"size": r.size,
	"size_formatted": filesizeformat(r.size),
	"encrypted": r.encrypted,
	"permission": r.permission,
	"share_type": r.share_type,
	"root": '',
	"head_commit_id": r.head_cmmt_id,
	"version": r.version,
}
or group repo
{
	"type": "grepo",
	"id": r.id,
	"owner": r.group.group_name,
	"groupid": r.group.id,
	"name": r.name,
	"mtime": r.last_modify,
	"size": r.size,
	"encrypted": r.encrypted,
	"permission": check_permission(r.id, email),
	"root": '',
	"head_commit_id": r.head_cmmt_id,
	"version": r.version,
}
or public repo
{
	"type": "grepo",
	"id": r.repo_id,
	"name": r.repo_name,
	"owner": "Organization",
	"mtime": r.last_modified,
	"mtime_relative": translate_seahub_time(r.last_modified),
	"size": r.size,
	"size_formatted": filesizeformat(r.size),
	"encrypted": r.encrypted,
	"permission": r.permission,
	"share_from": r.user,
	"share_type": r.share_type,
	"root": '',
	"head_commit_id": r.head_cmmt_id,
	"version": r.version,
}
```

### url

----
GET api2/search-repos/nameContains=my

### Result

----
200 Response([repo_obj1, repo_obj2..])