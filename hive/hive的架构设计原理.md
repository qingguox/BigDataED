
### hive架构 

![Image text](https://github.com/1367379258/BigDataEd/blob/master/hive/photo/hive%E7%9A%84%E6%9E%B6%E6%9E%84%E8%AE%BE%E8%AE%A1.png)

>
	如图:Hive通过用户提供的一系列交互接口,接收到用户的指令(SQL),使用自己的Driver,结合元数据(MetaStore),将这些指令翻译成MapReduce,提交到Hadoop中执行,
	最后,将执行返回的结果输出到用户交互接口

######	具体详细
	用户接口:Client CLI(hive shell 命令行),JDBC/ODBC(java访问hive),WEBUI(浏览器访问hive)
	元数据:Metastore:元数据包括:表名,表所属数据库(默认是default) ,表的拥有者,列/分区字段,表的类型(是否是外部表),表的数据所在目录等
	默认存储在自带的derby数据库中,推荐使用MySQL存储Metastore
	hive 使用HDFS进行存储,使用MapReduce进行计算
	
  
	驱动器:Driver
	(1)解析器(SQL Parser):将SQL字符转换成抽象语法树AST,这一步一般使用都是第三方工具库完成,比如antlr,
		对AST进行语法分析,比如表是否存在,字段是否存在,SQL语句是否有误
	(2)编译器(Physical Plan):将AST编译生成逻辑执行计划
	(3)优化器(Query Optimizer):对逻辑执行计划进行优化
	(4)执行器(Execution):把逻辑执行计划转换成可以运行的物理计划,对于Hive来说,就是MR/Spark
	
##### 运行流程	
	
![Image text](https://github.com/1367379258/BigDataEd/blob/master/hive/photo/hive的运行流程.jpg) 	
	
	Hive通过给用户提供的一系列交互接口，接收到用户的指令(SQL)，使用自己的Driver，结合元数据(MetaStore)，将这些指令翻译成MapReduce，提交到Hadoop中执行，最后，将执行返回的结果输出到用户交互接口。
	
	
	
	
	
	
	