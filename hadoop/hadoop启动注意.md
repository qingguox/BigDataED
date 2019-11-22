 
 
#### 启动： 第一次启动集群（初始化）

#### 1. 会话下 ，    zkServer.sh start	
#### 2. node06下  执行   start-dfs.sh

> 
	配置文件:集群中要同步！！！
	zookeepr配置
	启动zookeeper集群
	zkServer.sh start   ||   zkServer.sh status
	
	hadoop-daemon.sh start journalnode
	第一台NN：
	hdfs namenode –format
	start-dfs.sh
	hdfs zkfc -formatZK
	另一台NN：
	hdfs namenode  -bootstrapStandby
	hadoop-daemon.sh start namenode
	$ZOOKEEPER/bin/zkCli.sh 
	ls /
	stop-dfs.sh && start-dfs.sh  ||  hadoop-daemon.sh start zkfc
 
 
#### 第二次启动 ：
		具体的配置在   资料下 的第三个  后面
	  1.  会话下  zkServer.sh start   
	  2. 启动  hdfs    在  node06下·  启动 start-dfs.sh 
	  3. 启动 map-reduce计算框架  在node06下  start-yarn.sh 
	  4. node08 09执行  yarn-daemon.sh start resourcemanager   3. 4 启动了 ResourceManager   node08:8088查看状态


> 
	 在  eclipse上打包 jar 用jdk1.7 因为linux上面是 jdk1.7  
	 否则会出现  Could not find com.sxt.s.xw.xMyWC 找不到类 之类的问题·

	 namenode 挂掉  就执行hadoop-daemon.sh start namenode

	在 eclipse 中·1 新建 hadoop  new  取消 user   node06 8020 finish 
	node06:50070 查看·存活状态namenode 

	我主节点namenode配置到了node06下     active，07是standly
	所以我的关闭 集群  是在 node06下 stop-dfs.sh  
	再次关闭 zookeeper·        在会话下  执行  zkServer.sh stop


