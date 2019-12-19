1.3节点 java 安装 

2.所有集群节点创建目录: mkdir opt/sxt  

3.zk压缩包解压在其他路径下:：
	#	tar xf zookeeper-3.4.6.tar.gz -C /opt/sxt/

4.进入conf目录，拷贝zoo_sample.cfg zoo.cfg 并配置
   dataDir，集群节点。
server.1=node07:2888:3888
server.2=node08:2888:3888
server.3=node08:2888:3888
5.单节点配置环境变量、并分发 ZOOKEEPER_PREFIX，共享模式读取profile 

6. 共享创建 /var/sxt/zk目录，进入各自目录 分别输出1,2，3 至文件 myid
	echo 1 > /var/sxt/zk/myid
	...

7. 共享启动zkServer.sh start 集群


8.启动客户端 help命令查看














