# Requirement

java-jdk


# Deploy

download es.gz.tar.

tar -zxvf es.gz.tar

# config/elasticsearch.yml

## cluster name

cluster.name: xx

## node name

node.name: node_xx

## data path

path.data: /path/data1, /path/data2

## log path

path.logs: /path/logs

## plugin path

path.plugins: /path/plugins

## minumum_master_nodes  

### .yml
discovery.zen.minumum_master_nodes: (master候选节点个数/2) + 1

### curl

PUT /_cluster/settings
{
    "persitent": {
        "discovery.zen.minimum_master_nodes": 2
    }
}

## Recover

### .yml

gateway.recover_after_nodes: 8
gateway.expected_nodes: 10
gateway.recover_after_time: 5m


## 单播配置

### .yml

可以使用三个master候选节点当作单播列表
discovery.zen.ping.unicast.hosts: ["host1", "host2:port"]


## 内存

export ES_HEAP_SIZE=10g

./bin/elasticsearch -Xmx10g -Xms10g

堆内存最大值和最小值需要相同，防止运行时改变堆内存大小。


## 关闭swap

sudo swapoff -a

`.yml`
vm.swappiness = 1
某些内核版本 swappiness为0会触发linux内核的out of memory killer机制


如果以上方法都不行，修改`.yml`文件

bootstrap.mlockall: true


## 修改进程默认文件描述符最大数量

`查看`
Get /_nodes/process
max_file_descriptor就是es进程可以访问的可用文件描述符数量


## 日志记录

`修改默认记录日志等级`
PUT /_cluster/settings
{
    "transient": {
        "logger.discovery": "DEBUGE"
    }
}


