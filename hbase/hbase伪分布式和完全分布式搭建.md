

# 搭建 伪分布式

#####  一个几点就可以了  我们选择没有zk的那个节点那就是 ndoe06
> 
	1. 上传 hbase-0.98.23-bin 和 protobuf到node06上
	2. mv hbase-sssssss  hbase
	4. vi /etc/profile    
		export HBASE_HOME=/root/hbase    Path  后面 :$HBASE_HOME/bin  . /etc/profile
	3. cd hbase/conf  vi hbase-env.sh             export JAVA=/usr/java/jdk1.7.......
			  vi hbase-site.sh          加上下面的东西
> 			  
		  <property>     
			<name>hbase.rootdir</name>   
		  	<value>file:///home/testuser/hbase</value>  
		 </property>  
		 <property>   
		   <name>hbase.zookeeper.property.dataDir</name>    
		  <value>/home/testuser/zookeeper</value> 
		  
		 </property>
>
	5. start-hbase.sh   jps查看  浏览器  node06:60010
   
# 搭建完全分布式 ： 
	
### hbase完全分布式安装：

#### 1、准备工作
	1、网络
	2、hosts
	3、ssh     node09是备机  要ssh
		ssh-keygen
		ssh-copy-id -i .ssh/id_dsa.pub node1
	4、时间：各个节点的时间必须一致
		date -s '2018-12-24 16:23:11'
		时间服务器
		yum install ntpdate
		ntpdate ntp1.aliyun.com
	5、jdk版本
####  2、解压配置  node06

	1、hbase-env.sh 
		JAVA_HOME	
		HBASE_MANAGES_ZK=false		//不启动 hbanse自身的zookeeper管理
>
	2、hbase-site.xml
		<property>
			<name>hbase.rootdir</name>
			<value>hdfs://mycluster/hbase</value>
		</property>
		<property>
			<name>hbase.cluster.distributed</name>
			<value>true</value>
		</property>
		<property>
			<name>hbase.zookeeper.quorum</name>
			<value>node07,node08,node09</value>
		</property>
>
	3、regionservers
		node07
		node08
		node09
	4、backup-masters
		node09 是备机
	5、拷贝hdfs-site.xml到conf目录

|	删除  hbase下的  docs  太大了  scp困难

	scp -r  hbase node09:/root/
	scp -r  hbase node08:/root/
	scp -r  hbase node07:/root/
	配置三个的环境变量  hbase	
	export HBASE_HOME=/root/hbase
	Path   ... :$HBASE_HOME/bin
####  3、start-hbase.sh 在·node06上
	启动其中某一个  hbase-daemon.sh start master  node09上 待机
