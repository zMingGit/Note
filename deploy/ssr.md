### Install Requirement

```
yum install -y git python-setuptools && easy_install pip
yum install -y epel-release libsodium
pip install requests
```

### Open firewall

`
centos 7
`
```
systemctl enable firewalld
systemctl start firewalld
```

```
firewall-cmd --permanent --zone=public --add-port=7788/tcp
firewall-cmd --permanent --zone=public --add-port=7788/udp

firewall-cmd --reload
```

### Update the config of multi port 

```
mv shadowsocksr
vi config.json
```

```
{
    "server":"0.0.0.0",
    "server_ipv6":"::",
    "local_address":"127.0.0.1",
    "local_port":1080,
    "port_password":{
        "2788":{"protocol":"auth_aes128_sha1", "password":"password", "obfs":"tls1.2_ticket_auth_compatible", "obfs_param":""},
        "3789":{"protocol":"auth_aes128_sha1", "password":"qasd", "obfs":"tls1.2_ticket_auth_compatible", "obfs_param":""},
        "4888":{"protocol":"origin", "password":"8888"},
        "5889":{"protocol":"origin", "password":"8889"}
    },
    "timeout":300,
    "method":"chacha20",
    "protocol": "auth_sha1_compatible",
    "protocol_param": "",
    "obfs": "http_simple_compatible",
    "obfs_param": "",
    "redirect": "",
    "dns_ipv6": false,
    "fast_open": false,
    "workers": 1
}
```


```
 {
      "server": "45.77.122.243",
      "server_ipv6": "::",
      "server_port": 7788,
      "local_address": "127.0.0.1",
      "local_port": 1080,
    
      "password": "zm7788",
      "method": "chacha20",
      "protocol": "auth_chain_a",
      "protocol_param": "",                                                                                                                               
      "obfs": "tls1.2_ticket_auth",
      "obfs_param": "",
      "speed_limit_per_con": 0,
      "speed_limit_per_user": 0,
   
      "timeout": 120,
      "udp_timeout": 60,
      "dns_ipv6": false,
      "connect_verbose_info": 0,
      "redirect": "",
      "fast_open": false
 }
```


### Run

```
mv shadowsocksr/shadowsocksr/
nohup python server.py -c ../config.json start > ssr.log 2>&1 &
```
