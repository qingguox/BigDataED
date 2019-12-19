


#### 三个哨兵 监控一个master 

![Image text](https://github.com/1367379258/BigDataEd/blob/master/zookeeper_redis/redis/2.8/redis%E5%8D%95%E4%B8%AA%E5%93%A8%E5%85%B5.png)
	1.创建redis目录： mkdir redis

	2.在redis目录下分别创建3个端口目录： 6380,6381,6382
	（不在配置文件中写他的目录指定关系，直接在当前目录下执行，持久化目录）

	3.当前目录下分别启动３个实例：
		redis-server --port 6380
		redis-server --port 6381 --slaveof 127.0.0.1 6380
		redis-server --port 6382 --slaveof 127.0.0.1 6380
	　
	4. 主从演示 crud权限，高可用

		
	-----------------------------------------------

	伪分布哨兵集群搭建：

	1 拷贝src下的redis-sentinel至bin目录下：
	2 启动三个主从redis实例

	3 创建哨兵配置文件目录： mkdir sent
	4 目录下创建启动配置文件病拷贝： vi s1.conf cp s2.conf s3.conf
		
	  配置文件内容：
		port 26380,1,2
		sentinel monitor sxt 127.0.0.1 6380 2

	5 启动sentinel读取配置文件：  3 个窗口 redis-sentinel s1.conf ...
		 
	  redis-sentinel s1.conf s2.conf s3.conf
	  
	  相当于 m 挂断  三个哨兵进程对m状态进行投票 超过两个 就主从替换。 

 ##### 网状的sentinel  相当于多个节点启动 哨兵 监控
	一个几点监控 一个master 两个 slave

![Image text](https://github.com/1367379258/BigDataEd/blob/master/zookeeper_redis/redis/2.8/redis%E5%93%A8%E5%85%B5%E7%BD%91%E7%BB%9C%E6%9E%B6%E6%9E%84%E5%9B%BE.jpg)
	
	
  
  
  
  