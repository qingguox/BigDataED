



### hive 的相关 操作 分区 建表 函数 系列化 


#### 1. hive 的 内部外部表
	
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
		
#### 2. hive下的 分区建表

##### 2.1单分区 内部表

	create table psn3(
	
	id int,
	name string,
	likes array<string>,
	address map<string,string>
	)
	partitioned by(age int)
	row format delimited
	fileds terminated by','
	collection items terminated by'-'
	map keys terminated by':'
	
	load data local inpath '/root/data/data' into table psn3 partition(age=10)

##### 2.2双分区 内部表

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
	
##### 2.3 外部表 双分区

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
	
##### 2.4 分区操作 
	alter table ps5 add partition(sex="hh",age=60);
	alter table ps5 drop partition(sex="hh");
	
	
##### 2.5 建表 修改表


######	2.5.1 创建表
	create table ps6 as select * from psn5;
	create table ps7 like ps5;  // 只复制表的结构



######	2.5.2 重命名表
	alter table old_table rename to new_table;


######	2.5.3 增加列 替换列
	alter table log_ss add columns (
		app_name string comment 'application name',
		session_id Long comment 'The current session id '
	);

	replace 是删除   并添加   删除 原有 到 add2_column 在添加 replace        eid int ekid int 用ekid 代替eid 是在原有数据库下(by)
	alter table ps1 replace columns ( 
		id int,
		name string,
		likes array<string>,
		address map<string,string>,
		add_column string,
		replace_column string
	);

######	2.5.4修改表的属性
	alter table log_message set tblproperties('notes'='sfa adf a a')

###### 2.6	
	
	FROM psn        
	INSERT OVERWRITE TABLE psn10              // 和insert into psn10作用一样
	SELECT id,name
	insert into psn11
	select id,likes

	把表的数据 导入到外部文件  用
	insert overwrite local directory '/root/result'   // 慎重  overwrite是覆盖 
	selet * from psn;

	where  kk > 0.2  为了避免错误 
                 >  cast (0.2 as float )  :先转为 float
	

	因为 delete 和 update用不了 因为hive不支持事务  但是实际上 人家是支持事务的  用一下的东西
	truncate table psn;          // 删除表

	select kk ll from tnale 
	distribute by kk      // 相同kk 发送到一个 reducer
	sort by ll asc;	// 进行排序· 

	比 group by 好用
	两个 查询语句  用 union all 拼接

	
#### 3. 	beeline  和 hiveserver2 有关
	hiveserver2 是和 hive --service metastore  一样 都是使用同一套 元数据服务 

	 一般 我们在 两个节点·开启   一个hiveserver2   一个hive --service metastore   08下  （开发人员）
	 hiveserver2   两种链接方式 ：（非开发人员）
		1. beeline 链接   （命令行 ）
			Beeline 要与HiveServer2配合使用
			服务端启动hiveserver2  node09 下      
			客户的通过beeline两种方式连接到hive
			1、beeline -u jdbc:hive2://node09:10000/default -n root
			2、beeline
			beeline> !connect jdbc:hive2://<host>:<port>/<db>;auth=noSasl root 123
				!connect jdbc:hive2://node09:10000/default  root 123
			默认 用户名、密码不验证
		2. JDBC 接口链接   就是java客户端链接  

#### 4.  自定义 函数 (两种饭是钢后)

>
  	1. 外部 eclipse 开发的jar  把hivedemo达成jar  然后 上传到 node09   /root/data下 
	 hive 下 运行  add jar /root/data/tuomain.jar;
	// 创建 会话下的函数   quit 之后 就没用了 没有了 自定义函数
 	create temporary function tm as 'cn.laolian.TuoMin'
	select tm(name) from psn;
	
	2.    hdfs dfs -put tuomain.jar /ccc
	create temporary function tm as 'cn.laolian.TuoMin' using jar 'hdfs://node06:8020/ccc/tuomain.jar';

	create temporary function tm ad 'cn.laolian.TuoMin' using jar 'hdfs://node06:8020/ccc/tuoamin.jar'

	
	
	
	
	
	
	
	