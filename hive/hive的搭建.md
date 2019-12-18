

### Hive 的搭建 

	Hive中metastore（元数据存储）的三种方式：
	a)内嵌Derby方式
	b)Local方式
	c)Remote方式

	我们使用 Remote server 和 client分离  也就是在不同机器上。

#### 一。先安装mysql

> 	安装mysql  
	Yum install mysql-server -y
	
	
>	启动服务   service  mysqld start 
	修改mysql权限：
	GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123' WITH GRANT OPTION;
	flush privileges;             
	删除多余会对权限造成影响的数据
	刷新权限            重启服务 service mysqld restart

#### 二。安装hive 配置环境，

	1.Node06 安装 mysql  （上面 ）  ndoe07 安装 hive
	2.解压  配置环境变量进入 conf目录 
	3.cp hive-default.xml.template hive-site.xml
	4.vi hive-site.xml  把下面的加上
	5. 用mysql的方式，需要将mysql的jar包拷贝到$HIVE_HOME/lib目录下）。 
	6. hive 进入
	Hive是通过=环境变量链接上hdfs
	
#####  3. 多用户模式  我们用的是server client分开下面那个

###### 1.Remote一体
	这种存储方式需要在远端服务器运行一个mysql服务器，并且需要在Hive服务器启动meta服务。
	这里用mysql的测试服务器，ip位192.168.1.214，新建hive_remote数据库，字符集位latine1
	hive-site.xml
	
	<?xml version="1.0"?>  
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>  
	   
	<configuration>  
	  
	<property>  
	  <name>hive.metastore.warehouse.dir</name>  
	  <value>/user/hive/warehouse</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionURL</name>  
	  <value>jdbc:mysql://192.168.25.35:3306/hive?createDatabaseIfNotExist=true</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionDriverName</name>  
	  <value>com.mysql.jdbc.Driver</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionUserName</name>  
	  <value>hive</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionPassword</name>  
	  <value>password</value>  
	</property>  
	  
	<property>  
	  <name>hive.metastore.local</name>  
	  <value>false</value>  
	</property>  
	  
	<property>  
	  <name>hive.metastore.uris</name>  
	  <value>thrift://192.168.1.188:9083</value>  
	</property>  
	  
	</configuration>  

	注：这里把hive的服务端和客户端都放在同一台服务器上了。服务端和客户端可以拆开，
	
######	2.Remote分开
	Node08 做server      node09做client
	Scp -r hive node09:`pwd`  分发node08上的东即可  然配环境 修改配置文件 启动server和client
	将hive-site.xml配置文件拆为如下两部分
	
>	1）、服务端配置文件
	<?xml version="1.0"?>  
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>  
	   
	<configuration>  
	<property>  
	  <name>hive.metastore.warehouse.dir</name>  
	  <value>/user/hive/warehouse</value>  
	</property>  
	<property>  
	  <name>javax.jdo.option.ConnectionURL</name>  
	  <value>jdbc:mysql://node06:3306/hive?createDatabaseIfNotExist=true</value>  
	</property>  
	<property>  
	  <name>javax.jdo.option.ConnectionDriverName</name>  
	  <value>com.mysql.jdbc.Driver</value>  
	</property>     
	<property>  
	  <name>javax.jdo.option.ConnectionUserName</name>  
	  <value>root</value>  
	</property>  
	<property>  
	  <name>javax.jdo.option.ConnectionPassword</name>  
	  <value>123456</value>  
	</property>  
	</configuration>  
	
>	2）、客户端配置文件

	<?xml version="1.0"?>  
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>  
	   
	<configuration>  
	  
	<property>  
	  <name>hive.metastore.warehouse.dir</name>  
	  <value>/user/hive/warehouse</value>  
	</property>  
	   
	<property>  
	  <name>hive.metastore.local</name>  
	  <value>false</value>  
	</property>  
	  
	<property>  
	  <name>hive.metastore.uris</name>  
	  <value>thrift://node08:9083</value>  
	</property>  
	  
	</configuration>  

>  3>启动

	启动hive服务端程序
	 hive --service metastore   

	客户端直接使用hive命令即可
	root@my188:~$ hive   
	Hive history file=/tmp/root/hive_job_log_root_201301301416_955801255.txt  
	hive> show tables;  
	OK  
	test_hive  
	Time taken: 0.736 seconds  
	hive>  

> 	客户端启动的时候要注意：

	[ERROR] Terminal initialization failed; falling back to unsupported
	java.lang.IncompatibleClassChangeError: Found class jline.Terminal, but interface was expected
		at jline.TerminalFactory.create(TerminalFactory.java:101)
	错误的原因： Hadoop jline版本和hive的jline不一致
	[hadoop@mina0 lib]$ rm   /home/hadoop/soft/hadoop-2.6.4/share/hadoop/yarn/lib/jline-0.9.94.jar 
	[hadoop@mina0 lib]$ cp jline-2.12.jar   /home/hadoop/soft/hadoop-2.6.4/share/hadoop/yarn/lib/


##### 1.本地模式（derby）
	
	这种方式是最简单的存储方式，只需要在hive-site.xml做如下配置便可
	
	<?xml version="1.0"?>  
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>  
	  
	<configuration>  
	<property>  
	  <name>javax.jdo.option.ConnectionURL</name>  
	  <value>jdbc:derby:;databaseName=metastore_db;create=true</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionDriverName</name>  
	  <value>org.apache.derby.jdbc.EmbeddedDriver</value>  
	</property>  
	   
	<property>  
	  <name>hive.metastore.local</name>  
	  <value>true</value>  
	</property>  
	   
	<property>  
	  <name>hive.metastore.warehouse.dir</name>  
	  <value>/user/hive/warehouse</value>  
	</property>  
	   
	  
	</configuration>  

	注：使用derby存储方式时，运行hive会在当前目录生成一个derby文件和一个metastore_db目录。这种存储方式的弊端是在同一个目录下同时只能有一个hive客户端能使用数据库，否则会提示如下错误
	[html] view plaincopyprint?
	hive> show tables;  
	FAILED: Error in metadata: javax.jdo.JDOFatalDataStoreException: Failed to start database 'metastore_db', see the next exception for details.  
	NestedThrowables:  
	java.sql.SQLException: Failed to start database 'metastore_db', see the next exception for details.  
	FAILED: Execution Error, return code 1 from org.apache.hadoop.hive.ql.exec.DDLTask  
	hive> show tables;
	FAILED: Error in metadata: javax.jdo.JDOFatalDataStoreException: Failed to start database 'metastore_db', see the next exception for details.
	NestedThrowables:
	java.sql.SQLException: Failed to start database 'metastore_db', see the next exception for details.
	FAILED: Execution Error, return code 1 from org.apache.hadoop.hive.ql.exec.DDLTask

##### 2.单用户模式（mysql）
	这种存储方式需要在本地运行一个mysql服务器，并作如下配置（下面两种使用mysql的方式，需要将mysql的jar包拷贝到$HIVE_HOME/lib目录下）。 
	
	<?xml version="1.0"?>  
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>  
	  
	<configuration>  
	<property>  
	  <name>hive.metastore.warehouse.dir</name>  
	  <value>/user/hive_remote/warehouse</value>  
	</property>  

	<property>  
	  <name>javax.jdo.option.ConnectionURL</name>  
	  <value>jdbc:mysql://node06/hive_remote?createDatabaseIfNotExist=true</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionDriverName</name>  
	  <value>com.mysql.jdbc.Driver</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionUserName</name>  
	  <value>root</value>  
	</property>  
	   
	<property>  
	  <name>javax.jdo.option.ConnectionPassword</name>  
	  <value>123</value>  
	</property>  
	</configuration>  

>	附：
	安装mysql  
	Yum install mysql-server -y

	启动服务   service  mysqld start 
	修改mysql权限：
	GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '123' WITH GRANT OPTION;
	flush privileges;             
	删除多余会对权限造成影响的数据
	刷新权限            重启服务 service mysqld restart

	[ERROR] Terminal initialization failed; falling back to unsupported
	java.lang.IncompatibleClassChangeError: Found class jline.Terminal, but interface was expected
		at jline.TerminalFactory.create(TerminalFactory.java:101)
	错误的原因： Hadoop jline版本和hive的jline不一致
	[hadoop@mina0 lib]$ rm   /home/hadoop/soft/hadoop-2.6.4/share/hadoop/yarn/lib/jline-0.9.94.jar 
	[hadoop@mina0 lib]$ cp jline-2.12.jar   /home/hadoop/soft/hadoop-2.6.4/share/hadoop/yarn/lib/


	

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		

