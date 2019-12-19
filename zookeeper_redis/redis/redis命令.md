NoSQL   是非关系行数据库
   1.1  解决大规模数据集合多重数据类型带来的挑战，，尤其是大数据应用难题
     为什么有NoSQL 一般为互联网项目 ：特点：数据高并发读写，海量数据高效率存储。可扩展
      NoSQL 主流：
	键值对：Redis    
	列式存储
	文档类型：
	图形数据库：
       

	1.2  Redis   1.只是nosql中的一个 
		2.直接操作内存  key-value   操作数据快  
		3.相当于 秒杀 抢票功能
		  而mysql 表数据库数据都在硬盘上   操作数据慢 
		
	1.3  linux  下启动 redis  
		先修改 redis.conf   vim  进入修改   ：demo : yes
		先以后台方式    
		启动server ./bin/redis-server   ./redis.conf  
		运行 ./bin/redis-cli
		启动客户端  在 ./usr/local/redis下 
			简单的方式:
			./bin/redis-cli    #连接本地端口号为 6379的服务器
			推荐的方式
			./bin/redis-cli -h 连接ip -p 端口号
				
	1.4 redis的停止
			方式1:通过kill -9 进程号(不推荐)
			方式2:通过客户端发送命令
				./redis-cli -h ip -p port shutdown
				
	1.2 mysql记录转化为 redis
		set it_user:id:1:username kk
		set it_user:id:1:email  56161@163.com
		
		set it_user:id:45:username
		set it_user:id:45:email
		
		获取 1号用户字段信息
		keys it_user：id：1*
	1.5  注意 命令+++++? * 操作
	keys ???? :key是4位
	keys *name* : 查找 key 中有name的记录
	
	del key1 key2 ...:删除多个key

	exists key :判断 key是否存在
	
	rename key newkey  :重命名key
	
	expire key  :设置key的生存时间  单位：秒  (默认是永久的)
	ttl key   :查看key还有多少寿命 
	
	type key :获取指定key的值类型 ： string ， hash ，list ，set ，zset（有序集合）
		
数据类型：  flushdb 删除全部数据
	key : String  value :五种数据类型
	
	String(★)：   "小，阿斯顿发顺丰"
	1.1 简单命令 :
		获取所有key           
		keys * ;
		set  key  value  ；
		get  key ；
		del key  删除key:
		
		getset key value : 先获取值  后设置值
		
		incr key:  incr:使key对应的value+1；
		decr key   : 使key对应的value-1；
		incrby key 数字 ：  给key对应value+数字
			eg: incrby age 13   - >value= value +13
		decrby key 数字 ：
		
		append key value111: 拼凑字符串，如果key存在，
					则在原有的value后面追加value1，
					如果 key不存在，则创建一个新的key/value111

		set key value ex 5
		setnx key 15 : 只有 key不存在时  才可以 覆盖哦 not exists
		set key 161 xx;  只允许修改	
		strlen key :长度
		getrange key 1 5  1到5 下标的 字符串

		setbit k1 1 1 ：给k1上的1出设置为1  则k1为  64   ASCII码  0 1 2 3 ..7 第7位是  2^0
		setbit k1  7  1 : 第7位 设置为1       则k1为65  A    1 + 64    8 位一个字   

	hash(理解) {uanem:"asdf",age:"15"} javaBean
	
	1.设置
		hset hash1 uname 张三  只能设置一个字段
		hmset key uname shn age 45 email 4555@163.com 设置多个字段
	2. 取值
		hget key :字段名/uname 
		hmget key uname age :多个字段
		hgetall key :key中 所有key-value
	3.删除
		hdel key uname  age 删除一个/多个字段    没有了字段  就没有了这条记录
		del key 删除所有
	4. 增加
		hincrby key 字段/age 数字： 增加字段-值
		
	5. hexists key 字段： 查看某个字段是否存在
	   hlen key : 查看key 的vakue中 字段的数量
	   hkeys key : 获取value中的所有字段
	   hvals key:获取value中字段的value值
		
		
	list         [1,2,3,4,5]  LinkedList
	
	1.设置值  list       
		lpush key 1 2 3 4  ：（头插法）相当于是链式存储，取出顺序为 4 3 2 1 
				a b c d   ：插入为 d c b a 
		rpush list2 a b c d : （尾插法）从右边开始  插入为a b c d
	2.取值：
		lrange key start end :获取链表中从start到 end元素的值，start end 从0开始
		                      也可是   -1最后一位元素， -2倒数第二个
						0 -1 默认输出list中全部数据
		获取指定下标的·1元素
		lindex key index
	3. 移除头尾元素
		lpop key： 返回并弹出指定key关联的链表中的第一个元素， 即头部元素
		          如果该key不存在，，返回nil ，若存在，返回链表头部元素
		rpop key : 返回连表尾部元素
				   如果该key不存在，，返回nil ，若存在，返回链表尾部元素
		rpoplpush list1 list2:  把list1的尾部元素弹出，添加到list2的头部
				   list2 不存在时，就会自动创建
		循环列表 ：
		rpoplpush  list1 list1； 从尾部弹出 又从头部插入
				   
	4. 扩展命令
		llen key  ：返回指定key关联的链表中的元素的数量
		
		删除 元素
		lrem key 0 hhhh : hhhh是指定元素  删除所有重复hhhh元素
		lrem key 2 hh : 顺序删除2个hh元素
		         -2     ： 逆向删除2个hh元素
				 
		替换 
		lset key index value;
		插入
		linsert key before/after piovt value  : pivot:被插元素 value:插入元素
		
	set           ['a','b'] HashSet 无序，，不重复
	redis 操作中，涉及到两个大数据集合的并集，交集，差集的运算
	
	1.赋值
	sadd key value[val1,val2.....] 向set集合中添加数据，
	 key  1 2 3 4  无序
							如果key的值已有，则不会重复添加
	
	2.取值
	smembers key ：获取set中所有元素
	sismember key member: 判断参数中指定的成员是否在该set中， 1 表示在 0：不造
						或者key本身就不存在。（无论集合中有多少元素都可以以极速返回）
	3.删除
	srem key 1 2 :删除 1 2
	
	4.扩展命令********
		1.差集的运算
		sdiff key1 key2  ....: 返回k1 - k2属于k1但不属于k2  与k的顺序有关
		
		2.集合的交集
		sinter key1 key2 key3 ....:返回交集元素
		
		3. 集合的并集
		sunion key1 key2 key3 ....:返回并集元素
		
		4. scard key :获取set中成员的数量
		 srandmember  key :随机返回set中的一个元素
		
		sdiffstore destination set1 set2... ：将set1 和 set2差集元素放在destination中
									与set的顺序有关	  在前就放回前面的数
								如果set3 存在，会覆盖掉set3的内容
			sdiffstore set3 set1 set2
		sinterstore  set3 set1 set2 ....   :将set1 和 set2..交集元素放在set3中
		
		sunionstore  set3 set1 set2 .....: 将set1 和 set2..并集元素放在set3中
		
		
	sortedSet(zset) [5000 'a',1000 'b',10 'c'] 有序set集合,不重复
		
		集合中 ： 500 小明
				 1000 小红 
				 5000 小张
		集合倒叙：
				5000
				1000
				 500
		有序set集合 ，，， 专门用来做排行榜
	
	1.赋值 set1 [5000 ‘xiaoming’, 1000 ‘xiaohong’, 500 'lili' ]
	zadd  set1 5000 xiaoming 1000 xiaohong 500 lili
	
	
	
	2.查看
	zscore key member : 返回指定成员的分数
		        zscore set1 lili : 500
	zcard key :获取集合中的成员人数 
		
	zrange key start end ：返回多个成员  0 -1 是全部成员
	zrange key start end withscores  成员和成绩   0 -1 是全部成员
							返回的成绩：从小到大
	zrevrange kye start end withscores :成绩从大到小
	
	3. 删除
	zrem key member.....: 删除多个成员

	zremrangebyrank key start stop :按照排名范围删除元素  0 1
	
	zremrangebyscore key start stop  :按照分数范围删除元素  500 1500

	4. zincrby key 500 member : 给指定成员的成绩+500
    zcount key min max   :获取成绩 200 500之间的人数
	zrank key member : 返回成员在集合中的排名 。索引（从小到大）
	zrevrank key member ：  返回成员在集合中的排名 。索引（从大到小）
	
	zunionstore st3 2 st1 st2  ; 1 2的并集放进st3中 但是要指定并集集合的数量

消息订阅与发布
	subscribe channel :订阅消息 频道是channel：
	psubscribe channel*  :批量订阅消息   
				eg ; psubscribe my*   定于所有 my1  , my2 .....多个
	
	publish channel 内容  ：在指定的频道中发送消息

redis 有16个数据库
		0-15
	默认在0号数据库上进行操作。。。
	数据库和数据库之间，不能共享键值对的。
	
	切换数据库 ：
		select 数据库名 （0-15）： 
	把某个键值对 进行数据库移植：
		move newkey 1:把 当前数据库中的newkey键值对移植到1号数据库
	
	清空当前数据库： flushdb
	和redis 服务器数据的清空：flushall
	
	dbsize: 返回当前数据库中key的数目
	info： 查看redis 服务器的配置信息
	
	
	
事务：	
		批量化执行命令：
	multi :                 begin transaction 
		开始命令：
		批量化命令：
	exec: 提交事务 ===队列中语句 对数据库进行操作   commmit
	
	discard :事务回滚：        不执行事务   rollback
	
		eg : multi :
		      set name 555
			  get name 
			exec :
				ok
				55
			multi  :
			   set name 6666
			  get name
			discard :
				
##### Rdis有两种持久化策略
	redis的持久化方式有俩种，持久化策略有4种：

	1. RDB（数据快照模式），定期存储，保存的是数据本身，存储文件是紧凑的
	2. AOF（追加模式），每次修改数据时，同步到硬盘(写操作日志)，保存的是数据的变更记录
	如果只希望数据保存在内存中的话，俩种策略都可以关闭
	也可以同时开启俩种策略，当Redis重启时，AOF文件会用于重建原始数据
	
##### RDB
	RDB定时备份内存中的数据集。服务器启动的时候，可以从 RDB 文件中恢复数据集。

优点

- 存储的文件是紧凑的
- 适合用于备份，方便恢复不同版本的数据
* 适合于容灾恢复，备份文件可以在其他服务器恢复
* 最大化了Redis的性能，备份的时候启动的是子线程，父进程不需要执行IO操作
* 数据保存比AOF要快

缺点

* 如果Redis因为没有正确关闭而停止工作是，到上个保存点之间的数据将会丢失
* 由于需要经常fork子线程来进行备份操作，如果数据量很大的话，fork比较耗时，如果cpu性能不够，服务器可能是卡顿。
	属于数据量大的时候，一个服务器不要部署多个Redis服务。
	
创建快照有以下5种形式：

1. 户端发送BGSAVE指令，服务端会fork一条子线程将快照写入磁盘
2. 客户端发送SAVE指令，服务端在主线程进行写入动作。一般不常使用，一般在内存不够去执行BGSVAE的时候才用
3. 设置了SAVE配置项，如SAVE 300 100，那么当“300秒内有100次写入”时，Redus会自动触发BGSAVE命令。如果有多个配置项，任意一个满足，都会触发备份
4. Redis通过SHUTDOWN命令接收到关闭服务器的请求、或者TERM信号时，会执行SAVE命令，这时候会阻塞所有客户端，不在执行客户端发送的任何命令
5. 当一个Redis服务器连接另外一个Redis服务器，并像对方发送SYNC命令开始一次复制操作时，如果主服务器目前没有在执行BGSAVE操作，
或者主服务器刚刚执行完，那么主服务器就会执行GBSAVE

###### AOF(append only file)
	AOF记录服务器的所有写操作。在服务器重新启动的时候，会把所有的写操作重新执行
	一遍，从而实现数据备份。当写操作集过大（比原有的数据集还大），Redis 会重写写操作集。

优点
- 使用AOF模式更加的灵活，因为可以有不同的fsync策略
- AOF是一个日志追加文件，所有不需要定位，就算断电也没有损坏问题，哪怕文件末尾是一个写到一半的命令，
	redus-check-aof工具也可以很轻易的修复
- 当AOF文件很大的，Redis会自动在后台进行重写。重写是决对安全的，因为Redis是继续往旧的文件里面追加，
	使用创建当前数据集所需的最小操作集合来创建一个全新的文件，一旦创建完成，Redis就会切换到新文件，开始往新文件进行追加操作
- AOF包含一个又一个的操作命令，易于理解和解析

缺点

- 对于同样的数据集，AOF文件通常要大于RDB文件
- AOF可能比RDB要慢，这取决于fsync策略。通常fsync设置为每秒一次的话性能仍然很高，如果关闭sfync，即使在很高的负载下也和RDB一样快。
	不过，即使在很大的写负载情况下，RDB还是能提供很好的最大延迟保证
- AOF1通过递增的方式更新数据，而RDB快照是从头开始创建，RDB会更健壮和稳定（所以适用于备份），

