# KeePass With Nginx

## 背景

一个正常的周末，在写一个Chrome的插件，想做一个可以将本地书签保存到服务器上，以及可以导入服务器的书签到本地， 在退出google账号重新登录的时候，发现cookie都没了，Trello上不去，而且密码忘记了 ~~(绝对是那个密码，我不会错的)~~ . 这种小事天天见， 邮件找回密码就是了, 就在我信心满满看到Trello提示的希望正在路上的时候，我觉得没啥问题。 可是等了几分钟，没！有！邮！件！ 随后无线请求发送邮件，结果也是预料中的没收到， 折腾了一下， 邮箱服务没问题，就是trello的邮件收不到，发了个support就不管了。 但是这个引发了我的想法，自己记密码，忘记不说，还来以为自己是对的 ~~(我没错，我不认，绝对不可能是我错了)~~. 

## 挑选

看了一下常用的一些密码相关的服务以及软件。 说实话我不太放心这些密码的web服务，虽然每个服务写的他们的实现原理都是肯定安全的，但是内心始终不相信，没办法，只能找那种本地搭建的服务了. 随后想起来kiri之前说的KeepAss， 就去看了一下，发现正和我意. 随后就用nginx 的webdav将 KeepAss 的数据库部署起来，让多设备可以一起用， 还有chrome的插件，美滋滋的.

## 正文

下文的部署是在Centos的机器部署，其他机器其实大概是差不多的.

## 打开任督二脉

```bash
systemctl start firewalld
firewall-cmd --get-active-zones
firewall-cmd --zone=public --add-port=80/tcp --permanent
firewall-cmd --zone=public --add-port=443/tcp --permanent
firewall-cmd --reload
```

### 安装软件

首先本地安装一个KeepAss的客户端先，用于生成放在服务器上的数据库. 

​	File -> New -> Ok -> 选择数据库文件保存在哪里 -> *输入Master密码* -> 配置没啥关系 -> 完成

​	`此处的Master请务必记好，这是数据库的密码，忘记了的话emmmm没事，密码可以通过邮件找回，不要担心`

移动*xx.kdbx*数据库文件至*/root/webdav*目录下,此处需要注意一下webdav文件的权限

然后在服务器上安装Nginx、 Openssl、 htpasswd.

```bash
yum update
yum install nginx openssl
# 安装keepass
wget http://dl.fedoraproject.org/pub/epel/7/x86_64/Pa                                                                                             ckages/k/keepass-2.34-1.el7.x86_64.rpm
rpm -Uvh keepass-2.34-1.el7.x86_64.rpm
yum install keepass
# 安装htpasswd
yum provides *bin/htpasswd
yum install httpd-tools-2.4.6-67.el7.centos.6.x86_64
```

## 配置软件

首先用htpasswd生成webdav的访问账号密码.

```bash
#在/etc/nginx/htpasswd路径生成账号密码,按照提示输入密码即可
sudo htpasswd -c /etc/nginx/htpasswd superadmin
```

使用Openssl生成自注册证书, 让ngixn用https的方式提供webdav服务.

```bash
sudo htpasswd -c /etc/nginx/htpasswd superadmin
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/nginx.key -out /etc/nginx/ssl/nginx.crt
```

然后输入类似如下的信息

```console
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:New York
Locality Name (eg, city) []:New York City
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Bouncy Castles, Inc.
Organizational Unit Name (eg, section) []:Ministry of Water Slides
Common Name (e.g. server FQDN or YOUR name) []:your_domain.com
Email Address []:admin@your_domain.com
```

使用正向加密(Forward secrecy)保证加密通信以及会话不能被检索和解密,详情请看[wiki](https://en.wikipedia.org/wiki/Forward_secrecy)

```bash
sudo openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048
```

大功告成， 就剩下调戏nginx了， 在`/etc/nginx/conf.d/`目录下添加webdav.conf文件.

然后写入以下配置

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    access_log off;
    return 302 https://$http_host$request_uri;
}

server {
    listen 443 ssl;
    listen [::]:443 ssl;

    server_name 140.143.167.23;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log debug;
    root /root/webdav;

    ssl_certificate /etc/nginx/ssl/nginx.crt;
    ssl_certificate_key /etc/nginx/ssl/nginx.key;
    ssl_dhparam /etc/nginx/ssl/dhparam.pem;

    location / {
        auth_basic_user_file "/etc/nginx/htpasswd";

        dav_methods PUT DELETE MKCOL MOVE COPY;
        dav_access all:r;
    }
}
```

重启nginx

```bash
systemctl restart nginx
```

记得客户端连接之前，在工具->选项->高级中允许使用自检证书哦.然后就使用htpasswd设置的账号密码登录，以及使用mater密码连接数据库.

享用你的KeepAss吧! 