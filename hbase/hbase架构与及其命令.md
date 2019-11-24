# hbase

## hbase是数据库

### 特点

-  高可靠性
- 高性能
- 面向列 
- 可伸缩
- 实时读写

### 数据量

- 十亿级别的行
- 百万级别的列

### 速度快的原因

- 充分利用内存
- 使用了LSM树
- 缓存机制
- 文件是顺序读

## 数据模型

![Image text](https://github.com/1367379258/BigDataEd/blob/master/hbase/photo/Hbase%E6%95%B0%E6%8D%AE%E6%A8%A1%E5%9E%8B.jpg)

### rowkey

- 相当于MySQL中的主键，唯一标识一行记录
- rowkeys是字典序
- rowkey的长度最长是64k，但是一般推荐10-100字节

### column family

- 一组列的集合
- 列族必须作为表的schema定义给出
- 列族是权限，存储的最小单元

### qulifier

- 列
- 可以动态的，随机的插入
- 表定义之后没有限制列，随着值的插入也把列插入
- 列必须归属于某一个列族

### timestamp

- 时间戳，64为整数，精度是毫秒
- 起版本号的作用，一个Cell中可以存在多版本的数据
- 时间戳可以自己定义，但是一般不推荐

### cell

- 存储数据的最小单元（逻辑概念）
- 存储的是KV格式的数据

	- K:	rowkey+column family+qulifier+timestamp
	- V：value

- hbase的cell存储数据的时候没有类型的区分，存放的都是字节数组

## 架构

### hbase是主从架构
![Image text](https://github.com/1367379258/BigDataEd/blob/master/hbase/photo/hbase%E6%9E%B6%E6%9E%84.jpg)

### 角色

- client

	- 操作hbase的接口，并维护客户端缓存

- zookeeper

	- 保证任何时刻集群中有且仅有一台avtive的master
	- 存储所有region的寻址入口

	- 所有region元数据存储在哪一台regionserver

	- 监控regionserver的上线和下线信息，并实时通知master
	- 存储相关的表的schema数据

- master

	- 分配region
	- 保证整个集群中的所有regionserver的负载均衡
	- 当发现某一台regionserver宕机之后，重新分配上面的region
	- 当region变大进行裂变的时候，master去分配region到哪一台regionserver

- regionserver

	- 负责接受客户端的读写请求，处理对于region的IO
	- 当某一个region变大之后，负责等分为两个region

- region

	- 相当于表的概念，一张表至少对应一个region
	- 当表的数据过大的时候，region会发生裂变

- store

	- 相当于列族
	- 角色

		- memstore

			- 位于内存
			- 每一个store有一个memstore

		- storefile

			- 磁盘存储空间，将数据持久化的存储位置
			- 每一个region有一个或者多个storefile
			- storefile可以进行合并操作

	- 存储结构：使用了LSM的数据模型

### 读写流程

- 读流程

	- 1、客户端向zk中发送请求
	- 2、从zk中拿到metadata的存储节点
	- 3、去存储metadata的节点获取对应region的所在位置
	- 4、访问对应的region获取数据
	- 5、先去memstore中查询数据，如果有结果，直接返回
	- 6、如果没有查询到结果，去blockcache查找数据，如果找到，直接返回
	- 7、如果没有找到，去storefile中查找数据，并将查询到的结果缓存会blockcache中，方便下一次查询
	- 8、将结果返回给客户端
	- 注意：blockcache是缓存，有大小限制，会有淘汰机制，默认将最早的数据淘汰

- 写流程

	- 1、client向zk发送请求
	- 2、从zk中拿到metadata的存储节点
	- 3、去存储matadata的节点获取对应region所在的位置
	- 4、访问对应的region写数据
	- 5、首先会向wal（HLog 预写日志）中写记录，写成功之后才会存储到memstore
		(万一写入 出错，就会根据hlog中日志回滚数据。)
	- 6、当memstore中的数据量达到阈值之后，进行溢写，溢写成storefile
	- 7、store file是一个个的小文件，会进行合并（minor,major）
	- 8、store file是对hfile的封装，hfile是实际存储再hdfs上的数据文件
	
	MemStore称为写缓存 ，blockcache是读缓存（存储在regionserver 只有一份）
	HLog 被一个server下所有region所共享 
### WAL

- write ahead log
- 放置数据丢失
- 先写内存，再向hdfs上溢写，但是是异步的方式

## JAVAAPI

### HBaseAdmin

- 管理表

	- createtable
	- disabletable
	- deletetable

### HTable

- 管理数据

	- put
	- get
	- scan
	- delete

*XMind: ZEN - Trial Version*