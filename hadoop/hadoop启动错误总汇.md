

hdfs ->[node06 (node07 namenode] (node08 node09 datanode)-<zookeeper
### 集群出现错误: 
>
	1. node06  node07处于  standly状态 
		解决 1： 在会话下 执行jps,查看各个节点的状态,发现没有zkfc(DFSZKFailoverController)
				原因是 zookeeper集群启动起来之后 没有格式化zkfc ，从而没有控制hdfs 
				导致 两个主节点都处于standly状态，集群属于不可用状态
			办法： stop-all.sh  结束所有 dfs 和 yarn js在此查看 jps	
				 会话下执行 zkServer.sh start node07 node08 node09 启动QuorumPeerMain
				 node06主节点下执行 start-dfs.sh start-yarn.sh node08 node09下yarn-daemon.sh start resourcemanager
>	
	2. node06 是standly node07 是active 状态：
		解决 1： 会话下，执行 jsp发现 zkfc启动 正常 
				原因是：node06 在某段时间让zkfc认为挂掉了 ，所以把namenode的控制权交给了备用节点node07
			解决 ： 在node07下执行 hadoop-daemon.sh stop namenode 停掉管理
			在浏览器中 访问 node06:60070 状态 从standly准变为 active，如果没有则，多刷新几次。
				如果实在不行，就把hdfs yarn重启一遍  记住要保持 date 一致 否 ：date -s "2019-08-19 31:36"

>				
	会话zookeeper.sh 			
	node06 start-dfs.sh start-yarn.sh 
	node08 9  yarn-daemon.sh start resourcemanager
	
	node06 start-hbase.sh 
	node06 hbase shell