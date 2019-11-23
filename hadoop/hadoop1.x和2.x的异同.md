
adoop框架适用于离线批量处理大文件，主要分为三部分：

分布式存储：由HDFS负责；
分布式计算：由MapReduce负责；
资源（内存等）管理调度： 1.X 版本中由MapReduce负责，2.X 之后的版本中由新引入的YARN负责。
Hadoop 2.X 版本是用来解决1.X 版本存在的一些问题，虽说内部的架构发生了改变，但是对于使用者来说则是透明的，client API 的调用方法没有做什么改变，方便了使用者。

一、hadoop 1.X版本的 MapReduce


![Image text](https://github.com/1367379258/BigDataEd/blob/master/hadoop/photo/Hadoop%201.x-mr1.x.jpg)

hadoop 1.X 版本的MapReduce架构
1.1 主从架构：JobTracker 和 TaskTracker
Master：全局唯一的 JobTracker：

提供 client API：用户程序 (JobClient) 提交一个 Job，该 Job 的信息会发送到 JobTracker 中；JobTracker通过 heartbeat 与集群中的机器保持通信；
任务调度：哪些 Job 应该分配给哪些机器，监控所有的TaskTracker 和 Job的执行状态、完成 failed Job 的重试；一旦 TaskTracker挂了，则需要将任务移动到其他TaskTracker中重新执行；
资源管理：当有新的Job被提交，TaskTracker需要根据当前内存等资源情况分配任务到TaskTracker。
Slaves：多个TaskTracker：

任务执行：执行JobTracker分配的任务；
任务监控和汇报：监控各任务执行的状态；
汇报任务状态：将任务状态汇报给JobTracker。
二、hadoop 1.X 版本的MapReduce存在的问题
JobTracker存在单点故障的问题，一旦JobTracker所在的机器宕机，那么集群就无法正常工作；
JobTracker 同时负责任务调度和资源管理分配，当提交的Job数量很大时，会造成很大的内存开销，这也是导致JobTracker故障的诱因之一，对此业界普遍总结出1.X版本 Hadoop 的 MapReduce 只能支持 4000 节点主机的上限。
三、hadoop 2.X 版本之后的MapReduce和YARN
3.1 引入资源管理器YARN
为了解决上述问题，开发人员对MapReduce的架构进行了改进。弃用了1.X 版本中的“JobTracker + TaskTracker模式，在2.X版本中：

YARN：负责全部资源管理分配；
MapReduce：只负责分布式计算本身。
3.2 YARN的组成
![Image text](https://github.com/1367379258/BigDataEd/blob/master/hadoop/photo/Hadoop_MRV2.jpg)

hadoop 2.X 之后版本的MapReduce架构
YARN，全称为Yet Another Resource Negotiator，即一款通用的第三方的资源管理器，其不仅可以作为Hadoop集群的资源管理器，也可以作为其他集群的资源管理器，比如Spark集群（就是我们通常所说的Spark on YARN，可以参考：https://blog.csdn.net/liweihope/article/details/91358144）。
YARN总体上仍然是主从结构，其中：

Master： ResourceManager，负责对所有NodeManager上的资源进行统一管理和调度；
Slave：NodeManager，负责单个节点上的资源管理和任务调度；
当用户提交一个application时，需要提供一个用以跟踪和管理这个程序的ApplicationMaster，它负责向ResourceManager申请资源，并要求NodeManger启动可以占用一定资源的任务。由于不同的ApplicationMaster被分布到不同的节点上，因此它们之间不会相互影响。

YARN主要由4个部分组成：
1. ResourceManger:

全局唯一，管理整个集群的资源；包含：scheduler + ApplicationManager；
scheduler:负责向application分配资源；
ApplicationManager： 接收新application、监控application执行状态、重试failed application；
2. ApplicationMaster:

一个application对应一个ApplicationMaster；
.向ResourceManager的scheduler申请资源（用Container表示）；
将得到的application进一步分配给内部任务；
与NodeManager通信以启动/停止任务；
监控任务的状态；
3. NodeManager:

每个节点都有一个NodeManager；
负责该节点的任务调度和资源分配；
向ResourceManager汇报该节点的资源使用情况、container的运行状态，处理来自ApplicationMaster的container启动和停止请求；
4. Container:

与MapReduce 1.x 中的slot 类似，container是YARN中的资源抽象，对节点的资源，如cpu、内存、磁盘等进行封装；
YARN为每一个任务分配一个container去进行执行；
container与slot的区别在于，container是可以进行资源的动态划分的，而slot不能改变自身所包含资源的多少。

作者：alexlee666
链接：https://www.jianshu.com/p/c2cd0ddf770b
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。