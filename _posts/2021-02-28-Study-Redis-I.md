---
title: 如何学习 Redis (I)
published: true
categories: [program]
tags: [redis]
---

Redis 简述
> Redis 作为高性能缓存数据库的代表，本质上是一个K-V类型的内存数据库，整个数据库系统加载在内存中进行操作，定期通过异步操作将数据写入到硬盘上。因为内存上操作，Redis的性能是非常出色，每秒可以处理超过10万读写操作。此外，Redis 提供多种数据结构，且单个 value 最大限制是1GB，由于受到机器的物理内存的限制，不能用海量数据的高性能读写。因此 Redis 适用于少量数据的高性能和高并发的场景。

Redis 特点
> 完全基于内存，绝大部分请求是纯粹的内存操作，非常快速。数据存在内存中，类似于 HashMap，HashMap 的优势就是查找和操作的时间复杂度都是O(1)
> 数据结构简单，对数据操作也简单，Redis 中的数据结构是专门进行设计的；
> 采用单线程，避免了不必要的上下文切换和竞争条件，也不存在多进程或者多线程导致的切换而消耗 CPU，不用去考虑各种锁的问题，不存在加锁释放锁操作，没有因为可能出现死锁而导致的性能消耗；
> 使用多路 I/O 复用模型，非阻塞 IO；
> 支持事务，Redis的所有操作都是原子性的，同时Redis还支持对几个操作合并后的原子性执行。
> 支持数据持久化，支持AOF和RDB两种持久化方式。

Redis 的数据类型
> String、 List、 Set、 Hash、 ZSet
> ![](/images/redis-datatype.png)   

Redis 的持久化机制
> Redis 提供2种持久化机制 RDB(默认) 和 AOF。   
> RDB是默认的持久化方式, 如果两种方式同时开启时，数据恢复Redis会优先选择AOF恢复。
> 1. RDB(Redis DataBase) 按照一定时间将内存的数据以快照的形式保存到硬盘中，对应产生的数据文件是dump.rdb。通过配置文件中的save参数定义快照周期。  
> * 只有一个 dump.rdb 文件，方便持久化
> * 容灾性好，一个文件可以比较容易安全保存
> * 性能最大化，fork子进程完成写操作，让主进程继续处理请求，IO最大化
> * 数据量比较大是，比 AOF 的启动效率更高
> * 数据安全性低，RDB 是间隔一段时间进行持久化，如果间隔间，Redis 发生故障，会发生数据丢失，数据不准确。  
> 2. AOF(Append-only file) 是指每次将写命令记录到单独的日志文件中，当重启Redis是，会依据持久化的日志文件恢复数据。  
> * 数据安全，AOF 持久化可以配置 appendfsync 属性为 always，每进行一次命令操作就记录到 AOF 文件中一次。
> * 通过 append 模式写文件，即使中途服务器宕机，可以通过 redis-check-aof 工具解决数据一致性问题。
> * AOF 机制的 rewrite 模式。 AOF 文件没被 rewrite 之前（文件过大时会对命令 进行合并重写），可以删除其中的某些命令（比如误操作的 flushall）)
> * AOF 文件比 RDB 文件大，且恢复速度慢。
> * 数据集大的时候，比 RDB 启动效率低。

缓存穿透
> 说明: 请求大量在缓存中不存在的Key，对后端服务造成压力，导致系统崩溃。
> 解决:
> 1. 对异常的 key 的查询结果缓存
> 2. 对大量的 key 的查询前进行过滤，限流

缓存雪崩
> 说明: 当缓存服务器重启或者大量缓存集中在某一个时间段失效，大量请求会给后端系统带来很大压力，导致系统崩溃。  
> 解决:  
> 1. 在缓存失效后，通过限流的方式控制请求
> 2. 做缓存备份，对原始缓存做一个拷贝，失效时间设置的比原始缓存要长  
> 3. 设置不同的 key 的缓存失效时间是均匀的

缓存并发竞争
> 说明: 多个客户端同时写一个 key，但顺序我们无法控制，数据就可能不对了。
> 解决: 
> 1. 使用分布式锁，同时加入数据的时间戳。同一时刻，只有抢到锁的客户端才能写入，写入时，需要比较当前数据的时间戳和缓存中数据的时间戳