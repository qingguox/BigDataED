


#### hive的权限控制

##### 1. 介绍

	三种授权模型：
	1、Storage Based Authorization in the Metastore Server
	基于存储的授权 - 可以对Metastore中的元数据进行保护，但是没有提供更加细粒度的访问控制（例如：列级别、行级别）。
	2、SQL Standards Based Authorization in HiveServer2
	基于SQL标准的Hive授权 - 完全兼容SQL的授权模型，推荐使用该模式。
	3、Default Hive Authorization (Legacy Mode)
	hive默认授权 - 设计目的仅仅只是为了防止用户产生误操作，而不是防止恶意用户访问未经授权的数据。

	Hive - SQL Standards Based Authorization in HiveServer2
		完全兼容SQL的授权模型
			除支持对于用户的授权认证，还支持角色role的授权认证
			role可理解为是一组权限的集合，通过role为用户授权
			一个用户可以具有一个或多个角色
			默认包含另种角色：public、admin
	Hive - SQL Standards Based Authorization in HiveServer2
		限制：
		1、启用当前认证方式之后，dfs, add, delete, compile, and reset等命令被禁用。
		2、通过set命令设置hive configuration的方式被限制某些用户使用。
		（可通过修改配置文件hive-site.xml中hive.security.authorization.sqlstd.confwhitelist进行配置）
		3、添加、删除函数以及宏的操作，仅为具有admin的用户开放。
		4、用户自定义函数（开放支持永久的自定义函数），可通过具有admin角色的用户创建，其他用户都可以使用。
		5、Transform功能被禁用。
		
	Hive - SQL Standards Based Authorization in HiveServer2  node08 尚在执行hive --serivce hiveserver2
		在hive服务端修改配置文件hive-site.xml添加以下配置内容：
		
	<property>
	  <name>hive.security.authorization.enabled</name>
	  <value>true</value>
	</property>
	<property>
	  <name>hive.server2.enable.doAs</name>
	  <value>false</value>
	</property>
	<property>
	  <name>hive.users.in.admin.role</name>
	  <value>root</value>
	</property>
	<property>
	  <name>hive.security.authorization.manager</name>
	  <value>org.apache.hadoop.hive.ql.security.authorization.plugin.sqlstd.SQLStdHiveAuthorizerFactory</value>
	</property>
	<property>
	  <name>hive.security.authenticator.manager</name>
	  <value>org.apache.hadoop.hive.ql.security.SessionStateUserAuthenticator</value>
	</property>
		服务端启动hiveserver2；客户端通过beeline进行连接   node07上 执 beeline
		
	Hive权限管理        beeline  
	！connect jdbc:hive2://node08:10000/default abc abc 普通用户是无法执行下面这些语句
	角色的添加、删除、查看、设置：

###### 2. 创建角色  授权，等

	1. create role role_name;                   ---创建角色
	2. drop role role_name;                     ---删除角色
	3. set role (role_name | ALL|NONE);         ---设置角色
		必须以root 密码为空进入，set role admin: 给当前用户设置角色admin，就能create 角色和查询了
		
	4. show  current roles;                     ---查看当前具有的角色
	5. show roles;                              ---查看所有角色
	
	1.1 给角色授权：   grant admin to role sxt with admin option;
	1.2 查看属于某种角色的用户、角色列表：  show principals role_name; 
	1.3 查看授予某个用户、角色的角色列表  show role grant (user|role) role principal_name;
	1.4 移除某个用户、角色的角色： revoke admin from role sxt;
	
	1.5 删除角色 ：drop role sxt;	
	
>	
	创建 用户   hive 的用户 和 hdfs 和 linux 一样 
	// 在  hive clie 也即时  node09  上创建。
	在 linux 上创建    useradd sxt01      passwd sxt01     groupadd sxtshare   
	usermod -a -G sxtshare sxt01 
	usermod -a -G sxtshare root 
	
	chown -R root:sxtshare   
	chmod 771 hive/              
	相当于是 linux的上用户 拥有对hive这个文件的修改 

	beeline -u jdbc:hive2://node08:10000/default -n sxt01 123
	
	注意  先以 root 进入 
		create role role_sxt;
		grant admin to role role_sxt with admin option;
		grant role role_sxt to user sxt01;
		
	其实 以  sxt01 进入  select 还是会报错 
	直接 set role admin === 直接把角色的权限提升至 admin超级

>   网友操作
	
	CREATE ROLE pbdd;(创建数据库角色)

	GRANT ROLE pbdd TO USER pbdd;(将数据库角色赋予用户)

	GRANT CREATE ON DATABASE test TO role pbdd;(给角色test库的建表权限)

	GRANT SELECT ON DATABASE test TO role pbdd;(给查询权限)

	GRANT ALL TO user root;(给root用户所有权限)

	REVOKE ALL on database test from user pbdd;(收回权限)

	show roles;(查看已经有的角色)

	SHOW GRANT user pbdd;(产看用户已有权限)

	SHOW GRANT user pbdd ON database test;(查看用户在test数据库的已有权限)

	SHOW GRANT user pbdd ON c_vip;(查看用户在表的权限


#### hive的参数配置 及其优化
	vi  ~/hiverc    进入这个文件 
	   进行 hive之前的配置
		
	set hive.cli.print.header=true                           // 打印表的 字段
	set hive.exec.dynamic.partition.mode=nonstrict 先设置为 不严格检查 严格是 必须要有一个静态分区
	set hive.enforce.bucketing=true  
	默认：false；设置为true之后，mr运行时会根据bucket的个数自动分配reduce task个数。（用户也可以通过	mapred.reduce.tasks自己设置reduce任务个数，但分桶时不推荐使用）
	注意：一次作业产生的桶（文件数量）和reduce task个数一致。
	Set hive.fetch.task.conversion=none/more;    // Hive中对某些情况的查询不需要使用MapReduce计算
	set hive.exec.mode.local.auto=true;        //  默认为集群模式 这时本地模快一些 
		注意：
		hive.exec.mode.local.auto.inputbytes.max //默认值为128M	
		表示加载文件的最大值，若大于该配置仍会以集群方式来运行！
	set hive.exec.parallel=true;        //  并行模式 
	set hive.mapred.mode=strict;       // 严格模式（默认为：nonstrict非严格模式）
		查询限制：
		1、对于分区表，必须添加where对于分区字段的条件过滤；
		2、order by语句必须包含limit输出限制；
		3、限制执行笛卡尔积的查询。
	Hive排序
		Order By - 对于查询结果做全排序，只允许有一个reduce处理
		（当数据量较大时，应慎用。严格模式下，必须结合limit来使用）
		Sort By - 对于单个reduce的数据进行排序
		Distribute By - 分区排序，经常和Sort By结合使用
		Cluster By - 相当于 Sort By + Distribute By
		（Cluster By不能通过asc、desc的方式指定排序规则；
		可通过 distribute by column sort by column asc|desc 的方式）
	Hive Join
		Join计算时，将小表（驱动表）放在join的左边
		Map Join：在Map端完成Join
		两种实现方式：
			1、SQL方式，在SQL语句中添加MapJoin标记（mapjoin hint）
			语法：
			SELECT  /*+ MAPJOIN(smallTable) */  smallTable.key,  bigTable.value 
			FROM  smallTable  JOIN  bigTable  ON  smallTable.key  =  bigTable.key;
			2、开启自动的MapJoin
	Map-Side聚合
		通过设置以下参数开启在Map端的聚合：
		set hive.map.aggr=true;
	合并小文件
		文件数目小，容易在文件存储端造成压力，给hdfs造成压力，影响效率

		设置合并属性

		是否合并map输出文件：hive.merge.mapfiles=true
		是否合并reduce输出文件：hive.merge.mapredfiles=true;
		合并文件的大小：hive.merge.size.per.task=256*1000*1000

		去重统计

		数据量小的时候无所谓，数据量大的情况下，由于COUNT DISTINCT操作需要用一个Reduce Task来完成，这一个Reduce需要处理的数据量太大，就会导致整个Job很难完成，一般COUNT DISTINCT使用先GROUP BY再COUNT的方式替换


>
	set hive.cli.print.header=true                          
	set hive.exec.dynamic.partition.mode=nonstrict 
	set hive.enforce.bucketing=true  
	Set hive.fetch.task.conversion=none/more;    
	set hive.exec.mode.local.auto=true;        
	set hive.exec.parallel=true;       
	set hive.mapred.mode=strict;      
	set hive.map.aggr=true;



