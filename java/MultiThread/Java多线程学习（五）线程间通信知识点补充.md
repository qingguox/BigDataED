Java多线程学习（五）线程间通信知识点补充

本节思维导图：


思维导图源文件+思维导图软件关注微信公众号：“Java面试通关手册” 回复关键字：“Java多线程” 免费领取。

我们通过之前几章的学习已经知道在线程间通信用到的synchronized关键字、volatile关键字以及等待/通知（wait/notify）机制。今天我们就来讲一下线程间通信的其他知识点：管道输入/输出流、Thread.join()的使用、ThreadLocal的使用。

一 管道输入/输出流
管道输入/输出流和普通文件的输入/输出流或者网络输入、输出流不同之处在于管道输入/输出流主要用于线程之间的数据传输，而且传输的媒介为内存。

管道输入/输出流主要包括下列两类的实现：

面向字节： PipedOutputStream、 PipedInputStream

面向字符: PipedWriter、 PipedReader

1.1 第一个管道输入/输出流实例
完整代码：https://github.com/Snailclimb/threadDemo/tree/master/src/pipedInputOutput

writeMethod方法
————————————————
版权声明：本文为CSDN博主「SnailClimb在csdn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_34337272/article/details/79694226