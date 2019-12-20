
转载请备注地址：https://blog.csdn.net/qq_34337272/article/details/79640870

### 文章目录
#### 一 进程和多线程简介
		1.1 进程和线程
		1.2 何为进程？
		1.3 何为线程？
		1.4 何为多线程？
		1.5 为什么多线程是必要的？
		1.6 为什么提倡多线程而不是多进程？
#### 二 几个重要的概念
	2.1 同步和异步
	2.2 并发(Concurrency)和并行(Parallelism)
	2.3 高并发
	2.4 临界区
	2.5 阻塞和非阻塞
#### 三 使用多线程常见的三种方式
	①继承Thread类
	②实现Runnable接口
	③使用线程池
#### 四 实例变量和线程安全
	4.1 不共享数据的情况
	4.2 共享数据的情况
#### 五 一些常用方法
	5.1 currentThread()
	5.2 getId()
	5.3 getName()
	5.4 getPriority()
	5.5 isAlive()
	5.6 sleep(long millis)
	5.7 interrupt()
	5.8 interrupted() 和isInterrupted()
	5.9 setName(String name)
	5.10 isDaemon()
	5.11 setDaemon(boolean on)
	5.12 join()
	5.13 yield()
	5.14 setPriority(int newPriority)
#### 六 如何停止一个线程呢？
	6.1 使用interrupt()方法
	6.2 使用return停止线程
#### 七 线程的优先级
#### 八 Java多线程分类
	8.1 多线程分类
	8.2 如何设置守护线程？
	Java 并发的基础知识，可能会在笔试中遇到，技术面试中也可能以并发知识环节提问的第一个问题出现。比如面试官可能会问你：“谈谈自己对于进程和线程的理解，两者的区别是什么？”
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	————————————————
	版权声明：本文为CSDN博主「SnailClimb在csdn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
	原文链接：https://blog.csdn.net/qq_34337272/article/details/79640870





