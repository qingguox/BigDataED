



### hive 的相关 操作 分区 建表 函数 系列化 


#### hive 的 建表
	
	1. 内部表 
		
		create table psn1(
			id int,
			name string,
			likes array<string>,
			address map<string, string>
		)
		row format delimited
		fileds terminated by','
		collection items terminated by'-'
		map keys terminated by':';
		
		load data local inpath '/root/data/data' into table psn1;
		// 导入本地数据 复制  不加local 是hdfs数据 上 是移动
		desc formatted psn1; 查看建表语句 及其存储位置
		
		hdfs dfs -cat /user/hive/warehource/psn1/date 
		
		datenode下 /var/sxt/hadoop/ 中存储的是就是  分块数据
		
		address struct<street:string，city:string, state:string,zip:int> 
		lines terminated by '\n'

	2. 外部表
	
		create external table psn2 (
			
			id int,
			name string,
			likes array<string>,
			address map<string,string>
		)
		row format delimited
		fileds terminated by','
		collection items terminated by'-'
		map keys terminated by':'
		location '/externalTable/';            hdfs上的一个目录  不属于hive的管理
	
		load data local inpath '/root/data/data' into table psn2;
		
>  
	内部外部表的区别 ：
	1、创建表的时候，内部表直接存储再默认的hdfs路径，外部表需要自己指定路径直接把指定路径下的数据插入
	2、删除表的时候，内部表会将数据mysql和元数据（节点server指定的）全部删除，外部表只删除元数据mysql  但是hdfs的数据还在（），hdfs   '/externalTable/';数据不删除
			因为表指定到了'/externalTable/';  而不是user/hive/warehouse 就不归 hive管理    还有即使在hive下  但也不归hive管理 
			删除的也只是元数据
	load data local inpath '/dog' into table dog; //加载hdfs数据会将数据移动到/user/hive/warehouse/目录下
		外部表  不指定 location 那就就在默认 user/hive/warehouse 下   然后 load data 本地 的数据 是 复制  
			指定location     那就在 /externaltable/
	====hive 只管理外部表的元数据 在mysql中拿去的， externalTable 也即是hdfs管理外部表
	注意：hive：读时检查（实现解耦，提高数据记载的效率）
		  关系型数据库：写时检查
		
#### hive下的 分区建表

##### 单分区 内部表

	create table psn3(
	
	id int,
	name string,
	likes array<string>,
	address map<string,string>
	)
	partationed by(age int)
	row format delimited
	fileds terminated by','
	collection items terminated by'-'
	map keys terminated by':'
	
	load data local inpath '/root/data/data' into table psn3 partation(age=10)

##### 双分区 内部表

	create table ps4
	(
	id int,
	name string,
	likes array<string>,
	address map<string,string>
	)
	partitioned by(age int,sex string)
	row format delimited 
	fields terminated by','
	collection items terminated by'-'
	map keys terminated by ':';

	load data local inpath 'data/data' into table ps4 partition(age=10,sex="man");
	
###### 外部表 双分区

	create table psn5
	(
	id int,
	name string,
	likes array<string>,
	address map<string,string>
	) 
	partitioned by(age int，sex string)
	row format delimited
	fields terminated by','
	collection items terminated by'-'
	map keys terminated by':'；
	location '/externalTable/';

	 //数据在  /externalTable/age=10/date 中 提前用hdfs dfs -put data /externalTable/age=10   s
	hive下 ： msck repair table psn7;   // 刷新mysql数据库中 分区 信息    如果不刷新 select * from psn7; 是没有数据的  因为 找不到age=60分区信息  
	
	
	
	
	
	
	
	
	
	
	