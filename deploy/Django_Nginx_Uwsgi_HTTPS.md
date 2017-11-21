
## Centos7下 使用Certbot 获得https证书，以及nginx和uwsgi部署django服务。

### 前言 
 
完成django项目之后首先用manager 来运行，查看项目是否能正常奔跑

以及django的配置中DEBUG千万要改为False. Allowed_host 也需改为'*', 如果你需要所有ip可以访问的话。


### 用NGINX + UWSGI先部署django

先创建一个 uwsgi的配置文件 `uwsgi.ini`


```
[uwsgi]
socket = 0.0.0.0:9090 #端口可以改为任意你喜欢的端口
#http = 0.0.0.0:9090  #用来测试uwsgi是否正常

chdir=/root/blogDev/Blog/   #项目的绝对路径地址
wsgi-file=/root/blogDev/Blog/blog/wsgi.py  #项目的wsgi文件的绝对路径地址

master = true
workers = 2
pidfile = /root/uwsgi9090.pid
daemonize = /root/uwsgi9090.log 
```


使用`uwsgi --ini xxxx/uwsg.ini`启动uwsgi

如果使用的是http方式启动，可以直接用网页查看是否成功，这里也配置为https，具体就不细讲了。



然后就是配置nginx， 主要就是更改nginx的配置文件。

更改其中server的模块

```
 server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        # 改为你自己的域名
        server_name  www.zming.info; 
        root         /usr/share/nginx/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;
        location / {
            include uwsgi_params;
            uwsgi_pass 0.0.0.0:9090;
            uwsgi_param UWSGI_CHDIR /root/blogDev/Blog;
            uwsgi_param UWSGI_SCRIPT blog.wsgi;
            client_max_body_size 35m;
        }
        
        # 注意这里为项目的静态文件路径。
        location /static {
            alias /root/blog_static;
        }

        error_page 404 /404.html;
           location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
```

启动的时候如果发现如果大部分请求403的话，极大可能就是默认的nginx用户没权限访问资源。可以切为root用户或者提升nginx用户权限。


```
在配置的最前面 user后面改为root表示用root的权限执行。
user root;
```


到这里如果一切没意外，django项目可以正常跑动了。

如果为了以后的http2世代更快的速度，以及为了网站不被劫持，更安全，那么就继续，升级http到https。


### 申请https证书

#### centos7上利用certbot获得证书。

`[certbot doc](https://certbot.eff.org/#centosrhel7-nginx)`


安装依赖项
```
yum -y install yum-utils
yum-config-manager --enable rhui-REGION-rhel-server-extras rhui-REGION-rhel-server-optional
sudo yum install certbot-nginx
```

尝试获得证书

```
sudo certbot --nginx certonly
```

在这里我获得了一个错误。

`NameError: name 'sys_platform' is not defined`


然后去网上寻找答案，就有了下面的安装。

```
pip uninstall distribute
pip install setuptools
```

但是还是报错。

```
No module named 'requests.packages.urllib3'pip install request
```

跳过找答案的过程，下面是我的所有操作。

```
pip install requests
pip install lxml
pip install cssselect
pip install requests urllib3 pyOpenSSL --force --upgrade
pip install --upgrade --force-reinstall 'requests==2.6.0'
```

最后终于可以运行了

```
sudo certbot --nginx certonly
sudo certbot renew --dry-run
certbot renew  #自动续订
```






#### 参考

https://github.com/certbot/certbot/issues/5104
https://github.com/certbot/certbot/issues/4514
https://serverfault.com/questions/830284/certbot-for-letsencrypt-missing-pyopenssl-module




### 申请好证书后，就开始简单了，直接配置nginx就好了

更改nginx配置文件, 让http直接跳转到https。

```

    server {
        listen       80 default_server;
        listen       [::]:80 default_server;
        server_name  www.zming.info;
        rewrite ^(.*)$  https://$host$1 permanent;
    }



    server {
        listen       443 ssl http2 default_server;
        listen       [::]:443 ssl http2 default_server;
        # !!! 注意这里改为你自己的域名
        server_name  www.zming.info; 
        root         /usr/share/nginx/html;

        # !!! 注意这里改为你之前获得的证书的fullchain地址
        ssl_certificate "/etc/letsencrypt/live/www.zming.info/fullchain.pem";
        # !!! 注意这里改为你之前获得的证书的key的地址
        ssl_certificate_key "/etc/letsencrypt/live/www.zming.info/privkey.pem";
        ssl_session_cache shared:SSL:1m;
        ssl_session_timeout  10m;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;

       # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            include uwsgi_params;
            uwsgi_pass 0.0.0.0:9090;
            uwsgi_param UWSGI_CHDIR /root/blogDev/Blog;
            uwsgi_param UWSGI_SCRIPT blog.wsgi;
            client_max_body_size 35m;
        }

        location /static {
            alias /root/blog_static;
        }

        error_page 404 /404.html;
           location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }
```


到这里https就配置完成了。只需要重启nginx就OK了。


希望你能够拥有美好的阅读体验。
