```
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make

sudo ./utils/install_server.sh

```


`quick start`

```
redis-server xxx.conf --requirepass hello123 --daemonize yes
```