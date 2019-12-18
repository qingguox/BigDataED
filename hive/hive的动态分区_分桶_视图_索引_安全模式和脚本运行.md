


#### 一，hive的动态分区

###### 1. 先定义一个 基本表 
	create table ps11 (
	id int,
	name string,
	likes array<string>,
	address map<string,string>,
	age int,
	gender string
	)
	row format delimited
	fields terminated by','
	collection items terminated by'-'
	map keys terminated by':';

	load data local inpath '/root/data/data4' into table ps11;


	// 动态分区·   静态分区和 动态分区 hive是离线数据  而不是动态数据 
	// set hive.exec.dynamic.partition.mode=nonstrict 先设置为 不严格检查 严格是 必须要有一个静态分区
	
###### 2. 定义 具有分区定义的表
	create table ps22(
	id int,
	name string,
	likes array<string>,
	address map<string,string>
	)
	partitioned by(age int, gender string)
	row format delimited
	fields terminated by','
	collection items terminated by'-'
	map keys terminated  by':';

###### 3.利用基本表 来插入数据 
	from ps11
	insert into ps22 partition(age, gender)
	select id, name, likes, address, age, gender;

#### 二，hive的分桶分桶 

###### 1. 先设置 hive 中的参数
	set hive.enforce.bucketing=true;

###### 2. 定义基本表
	create table bucket_basic (
	id int,
	name string,
	age int
	)
	row format delimited
	fields terminated by',';

	load data local inpath '/root/data/data3' into table bucket_basic;
	1,tom,11
	2,cat,22
	3,dog,33
	4,hive,44
	5,hbase,55
	6,mr,66
	7,alice,77
	8,scala,88
	
###### 2.  建立分桶表 

	create table psn_buckets (
	id int,
	name string,
	age int
	)
	clustered by(age) into 4  buckets           // 根据 年龄分桶  除以4 取余数 0 1 2 3
	row format delimited
	fields terminated by',';
	
	// 插入2数据 
	from bucket_basic
	insert into psn_buckets 
	select id, name, age;
	
	// 查询 分桶 
	select * from psn_buckets tablesample(bucket 2 out of 4 on age);   // 0  1 2 3

	在 hadfs    hdfs dfs -cat /user/hive/warehouse/psn_buckets/000002_0
	7	alice	77
	3	dog	33

#### 三，hive的视图

##### 1. 创建视图：

	CREATE VIEW [IF NOT EXISTS] [db_name.]view_name 
	  [(column_name [COMMENT column_comment], ...) ]
	  [COMMENT view_comment]
	  [TBLPROPERTIES (property_name = property_value, ...)]
	  AS SELECT ... ;
	查询视图：
	select colums from view;
	删除视图：
	DROP VIEW [IF EXISTS] [db_name.]view_name;




#### 四，hive的索引 目的：优化查询以及检索性能

###### 1.创建索引

	create index ps1_index on table ps1(name)
	as 'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler' with deferred rebuild
	in table ps1_index_table;

	as：指定索引器；
	in table：指定索引表，若不指定默认生成在default__psn2_t1_index__表中

	create index ps5_index on table ps5(name) 
	as 'org.apache.hadoop.hive.ql.index.compact.CompactIndexHandler' with deferred rebuild;

	// 重建索引 （建立索引之后 必须重建索引才能生效）
	alter index ps5_index on ps5 rebuild;
		
	// 查询索引
	show index on ps5;
	// 删除索引 
	drop index id exists ps5_index on ps5;
	

#### 五，hive的安全模式和 脚本运行

	hive -e  "select * from ps1"
	hive -e “” > aaa   结果输入到文件中
	hive -S -e "" > aaa ;不输出 ok啥的 只输出结果
	hive -f file   :把sql语句弄到文件.h  .hql文件中   运行
	hive -i /home/my/hive-init.sql  :初始化
	hive > source file (在hive cli中运行)
	
	hive -e "select * from ps1" ; 写入到文件中， chmod +x .sh 运行即可








