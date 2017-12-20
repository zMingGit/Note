## 需求
使用分布式来解决索引实时化的问题以及索引任务分配。

## 记时
N/N

## 流程

![SeafEvents Redis](https://dev.seafile.com/seahub/f/0b7757a6cbb447b9bb06/?raw=1)

## 设计

### 架构

* 采用一个事件队列发布节点， 一个事件处理master节点，以及数个事件处理节点的架构。
* seafevents作为事件队列的发布节点。
* 会将一台机器的seafes作为master节点启动，订阅事件队列，以及分发任务。
* 其余的seafes节点会自动去请求master节点分发的任务，并处理。

### 发布和订阅

* 当seafevents发布消息的时候，如果没有任何节点订阅这个channel[名称:repo-update]，则会把这期间发送的事件记录在日志中，以便日后排查.
* redis的消息发布，必须先要有人订阅，所以seafes的master节点需要先启动，否则订阅之前发布的消息只能接收到一条。

### Index Worker 任务竞争

在单机上处理索引的时候，会对对应的资料库进行锁的操作，其他的Index Worker机器获得这个被锁的资料库消息后，无法对这个资料库执行更新索引操作，会将任务保存在本地数组，然后去执行其他资料库的任务。 在每次任务执行完成后，会去遍历本地数组，尝试执行任务。

## REDIS

* 使用redis内部的retry_on_timeout，当超时时，会自动重试一次，以保证是redis服务的问题。
* 当redis连接的时候，会发送一个ping请求，如果失败，会记录在日志中。

## seafevent节点

### 配置
`events.conf`:

```
[EVENTS PUBLISH]
enabled = true
mq_type = redis

[REDIS]
server = x.x.x.x
port = xx
password = xxxx
```

### 改动
* 直接向ccnet的mq注册回调函数，然后将事件发布到`repo-udpate`的channel上.
* 如果EVENTS PUBLISH下的enabled为True，当收到mq的消息的时候，会将消息发布到名称为repo-update的channel上。如果这个channel没有人订阅，则会记录事件到log中.
* message_handler文件合并到mq_listener
* 去掉app文件中的EventsListener类.

### 运行
seafevents目录下执行`./run.sh` 或者 `python main.py`.

## seafes的master节点

### 配置

`index-master.conf`:

```
[DEFAULT]
db_type=redis

[REDIS]
server = x.x.x.x
port = xx
password = xxxx
```

###  处理逻辑

会订阅名称为repo-update的channel消息，将消息lpush到名称为index-task的处理队列中

### 运行

在seafes目录下执行`./run_index_master.sh`

## seafes的处理节点

### 配置

`index-slave.conf`

```
[DEFAULT]
mq_type = redis
index_works = 2

[REDIS]
server = x.x.x.x
port = xx
password = xxxx
```

### 处理逻辑

会去brpop名称为index-task的处理队列中的消息，然后更新或者创建索引。

### 执行

在seafes目录下执行`./run_index_worker.py`