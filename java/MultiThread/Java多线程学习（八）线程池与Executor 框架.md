

## Java多线程学习（八）线程池与Executor 框架


本节思维导图：


![](https://github.com/1367379258/BigDataEd/blob/master/java/photo/%E5%A4%9A%E7%BA%BF%E7%A8%8B%E5%85%AB%20%E7%BA%BF%E7%A8%8B%E6%B1%A0%E4%B8%8EExecutor%E6%A1%86%E6%9E%B6.jpg)

一 使用线程池的好处
线程池提供了一种限制和管理资源（包括执行一个任务）。 每个线程池还维护一些基本统计信息，例如已完成任务的数量。
这里借用《Java并发编程的艺术》提到的来说一下使用线程池的好处：

降低资源消耗。通过重复利用已创建的线程降低线程创建和销毁造成的消耗。
提高响应速度。当任务到达时，任务可以不需要的等到线程创建就能立即执行。
提高线程的可管理性。线程是稀缺资源，如果无限制的创建，不仅会消耗系统资源，还会降低系统的稳定性，使用线程池可以进行统一的分配，调优和监控。
##二 Executor 框架

2.1 简介
Executor 框架是Java5之后引进的，在Java 5之后，通过 Executor 来启动线程比使用 Thread 的 start 方法更好，除了更易管理，效率更好（用线程池实现，节约开销）外，还有关键的一点：有助于避免 this 逃逸问题。

补充：this逃逸是指在构造函数返回之前其他线程就持有该对象的引用. 调用尚未构造完全的对象的方法可能引发令人疑惑的错误。

2.2 Executor 框架结构(主要由三大部分组成)
1 任务。
执行任务需要实现的Runnable接口或Callable接口。
Runnable接口或Callable接口实现类都可以被ThreadPoolExecutor或ScheduledThreadPoolExecutor执行。

两者的区别：

Runnable接口不会返回结果但是Callable接口可以返回结果。后面介绍Executors类的一些方法的时候会介绍到两者的相互转换。

2 任务的执行
如下图所示，包括任务执行机制的核心接口Executor ，以及继承自Executor 接口的ExecutorService接口。ScheduledThreadPoolExecutor和ThreadPoolExecutor这两个关键类实现了ExecutorService接口。

注意： 通过查看ScheduledThreadPoolExecutor源代码我们发现ScheduledThreadPoolExecutor实际上是继承了ThreadPoolExecutor并实现了ScheduledExecutorService ，而ScheduledExecutorService又实现了ExecutorService，正如我们下面给出的类关系图显示的一样。

ThreadPoolExecutor类描述:

//AbstractExecutorService实现了ExecutorService接口
	public class ThreadPoolExecutor extends AbstractExecutorService	
	
ScheduledThreadPoolExecutor类描述:

//ScheduledExecutorService实现了ExecutorService接口
	public class ScheduledThreadPoolExecutor
			extends ThreadPoolExecutor
			implements ScheduledExecutorService 





3 异步计算的结果
Future接口以及Future接口的实现类FutureTask类。
当我们把Runnable接口或Callable接口的实现类提交（调用submit方法）给ThreadPoolExecutor或ScheduledThreadPoolExecutor时，会返回一个FutureTask对象。

我们以AbstractExecutorService接口中的一个submit方法为例子来看看源代码

    public Future<?> submit(Runnable task) {
        if (task == null) throw new NullPointerException();
        RunnableFuture<Void> ftask = newTaskFor(task, null);
        execute(ftask);
        return ftask;
    }
	
上面方法调用的newTaskFor方法返回了一个FutureTask对象。

    protected <T> RunnableFuture<T> newTaskFor(Runnable runnable, T value) {
        return new FutureTask<T>(runnable, value);
    }

2.3 Executor 框架的使用示意图




1.** 主线程首先要创建实现Runnable或者Callable接口的任务对象。** 
备注： 工具类Executors可以实现Runnable对象和Callable对象之间的相互转换。（Executors.callable（Runnable task）或Executors.callable（Runnable task，Object resule））。

2.** 然后可以把创建完成的Runnable对象直接交给ExecutorService执行** （ExecutorService.execute（Runnable command））；或者也可以把Runnable对象或Callable对象提交给ExecutorService执行（ExecutorService.submit（Runnable task）或ExecutorService.submit（Callable task））。

执行execute()方法和submit()方法的区别是什么呢？
1)execute()方法用于提交不需要返回值的任务，所以无法判断任务是否被线程池执行成功与否；
2)submit()方法用于提交需要返回值的任务。线程池会返回一个future类型的对象，通过这个future对象可以判断任务是否执行成功，并且可以通过future的get()方法来获取返回值，get()方法会阻塞当前线程直到任务完成，而使用get（long timeout，TimeUnit unit）方法则会阻塞当前线程一段时间后立即返回，这时候有可能任务没有执行完。

3. **如果执行ExecutorService.submit（…），ExecutorService将返回一个实现Future接口的对象** （我们刚刚也提到过了执行execute()方法和submit()方法的区别，到目前为止的JDK中，返回的是FutureTask对象）。由于FutureTask实现了Runnable，程序员也可以创建FutureTask，然后直接交给ExecutorService执行。

4. **最后，主线程可以执行FutureTask.get()方法来等待任务执行完成。主线程也可以执行FutureTask.cancel（boolean mayInterruptIfRunning）来取消此任务的执行。** 





————————————————
版权声明：本文为CSDN博主「SnailClimb在csdn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_34337272/article/details/79959271


————————————————
版权声明：本文为CSDN博主「SnailClimb在csdn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_34337272/article/details/79959271



			
			

			
			
————————————————
版权声明：本文为CSDN博主「SnailClimb在csdn」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_34337272/article/details/79959271














