curl -X PUT -d "email=admin@admin.com&login_id="  -H "Authorization: Token aced9fb76a7a1a4d6e232fceebebcf2b8aab6ff4" http://172.16.3.165:8000/api/v2.1/admin/users/admin@admin.com/

curl -d "username=admin@admin.com&password=admin" http://172.16.3.128:8000/api2/auth-token/

c020216a3e640d3958ca96e590ff2360db6b9934



curl -H "Authorization: Token c020216a3e640d3958ca96e590ff2360db6b9934" http://172.16.3.128:8000/

36bd077379403664f1445d6bba7a6a23235c8d04



# test

curl -d "username=foo@foo.com&password=foo" http://192.168.1.173:8000/api2/auth-token/

4616f69f08ca5a30d7050244e07ba91779a04903

curl -H "Authorization: Token 4616f69f08ca5a30d7050244e07ba91779a04903" http://192.168.1.173:8000/




curl -X PUT -d "email=q@q.com&login_id="  -H "Authorization: Token 6394c2ebb70aa170bb723a4a5a89d88c9173a58c" http://172.16.3.165:8000/api/v2.1/admin/users/q@q.com




### curl get multi parameter

    curl -sS  "www.baidu.com/?q=2&b=2"