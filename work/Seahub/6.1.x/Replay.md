获得所有用户的snapshot label:  
`GET api/v2.1/admin/revision-tags/tagged-items/`
所有用户的snapshot label就等于所有的snapshot label了

获得某一个资料库的snapshot label:  
`GET api/v2.1/admin/revision-tags/tagged-items/?repo_id=xxx`  
这个api他在issue里说有问题， 但是本地测试没问题


Get the snapshot of a label  
`GET api/v2.1/admin/revision-tags/tagged-items/?tag_contains=xxx`  
他在issue里面说这个只能admin使用！！！ 但是咱当时看的文档的设计就是admin使用的。  


Delete method:
`DELETE api/v2.1/admin/revision-tags/tagged-items/`  
的确没实现，当时用的put去修改，为空就全部删除。 测试完6.2.3之后写好文档就添加。

资料库删除revision还在  
`待定`