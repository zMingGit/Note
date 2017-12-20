```
TaggedRevision {
    tag: tagname,
    tag_creator: username,
	revision: {
        repo_id: repo_id,
        commit_id: commit_id,
        email: email,
        name: email->name,
        contact_email: email->contact_email,
        time: time->isoformat(time),
        description: commit.desc,
	    link: web-link
	}
}
```

## 普通用户 API

## 给一个资料库的一个版本添加标签

**need read and write access**

POST api/v2.1/revision-tags/tagged-items/

参数

* repo_id
* commit_id
* tag_name

```
    200 Response({
	"revisionTags":[TaggedRevision1, TaggedRevision2...]
	})
    201 Response({
	"revisionTags":[TaggedRevision1, TaggedRevision2...]
	})
    400 repo can not be empty
        Tag can not be empty
        library not found.
		commit not found.
        Tag can only contain letters, numbers, dot,underscore.
    403 Permission denied.
```

## 删除所有旧标签，添加新标签
PUT api/v2.1/revision-tags/tagged-items/

参数

* repo_id
* commit_id
* tag_name
```
    200 Response({
	"revisionTags":[TaggedRevision1, TaggedRevision2...]
	})
    201 Response({
	"revisionTags":[TaggedRevision1, TaggedRevision2...]
	})
    400 repo can not be empty
        Tag can not be empty
        library not found.
		commit not found.
        Tag can only contain letters, numbers, dot,underscore.
    403 Permission denied.
```

## 给一个资料库下的一个版本删除标签

**need read and write access**
DELETE api/v2.1/revision-tags/tagged-items/

参数

* repo_id
* tag_name


```
    200 Response({})
    202 Response({})
    400 repo can not be empty
        Tag can not be empty
        library not found.
        Tag can only contain letters, numbers, dot,underscore.
    403 Permission denied.
```

## 列出该用户所有版本标签 (用于标签补全)

GET api/v2.1/revision-tags/tag-names/

```
  200 Response(
      [tag_name1, tag_name2 ....]
  )
  403 Permission denied.
```


## 管理员使用的 API


### 列出所有的资料库版本标签

GET api/v2.1/admin/revision-tags/tagged-items/

```
  200 Response(
       [ revision_obj1, revision_obj2 ....]
  )
  403 Permission denied.
```

注意返回的列表按照标签名称排序

### 列出某个用户的资料库版本标签

GET api/v2.1/admin/revision-tags/tagged-items/?user=xxx

### 列出某个资料库的所有版本标签

GET api/v2.1/admin/revision-tags/tagged-items/?repo_id=xxx

### 列出一个标签的所有资料库版本

GET api/v2.1/admin/revision-tags/tagged-items/?tag_name=xxx

```
  200 Response({
      [ revision_obj1, revision_obj2 ....]
  })
  400 tag does not exists
  403 Permission denied.
```

### 查找包含特定字符串的版本标签

GET api/v2.1/admin/revision-tags/tagged-items/?tag_contains=tag1.0

```
  200 Response(
      [ revision_obj1, revision_obj2 ....]
  )
  400 search key invalid.
  403 Permission denied.
```

注意返回的列表按照标签名称排序

