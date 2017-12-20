## Update filecomment model schema

### Old Model:

```
    repo_id = models.CharField(max_length=36, db_index=True)  
    parent_path = models.TextField()  
    repo_id_parent_path_md5 = models.CharField(max_length=100, db_index=True)  
    item_name = models.TextField()  
    author = LowerCaseCharField(max_length=255, db_index=True)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    objects = FileCommentManager()
```

### New Model:

```
    uuid = models.ForeignKey(FileUUIDMap, on_delete=models.CASCADE)
    author = LowerCaseCharField(max_length=255, db_index=True)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    objects = FileCommentManager()
```

Encapsulation `repo_id`, `parent_path`, `repo_id_parent_path_md5` and `item_name` field to fileuuidmap table.


No FileCommentManager method name is modified.And add to the logic of the fileuuidmap made up of the repo_id,parent_paht, item_name, within the filecommentmanager method