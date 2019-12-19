



### 单词统计 

#### Runner

	package com.sxt.mr.wc;

	import java.io.IOException;

	import org.apache.hadoop.conf.Configuration;
	import org.apache.hadoop.fs.Path;
	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Job;
	import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
	import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
	import org.apache.hadoop.util.Tool;
	import org.apache.hadoop.util.ToolRunner;
	import org.apache.log4j.Logger;


	public class MyWC implements Tool{
		private static final Logger logger = Logger
				.getLogger(MyWC.class);
		private Configuration conf =null;
		public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
			
			try {
				ToolRunner.run(new Configuration(), new MyWC(),args);
			} catch (Exception e) {
				logger.error("执行日志解析job异常",e);
				throw new RuntimeException(e);
			}
		}

		@Override
		public void setConf(Configuration conf) {
			conf.set("fs.defaultFS", "hdfs://node06:8020");
			conf.set("mapreduce.framework.name", "yarn");
	//		conf.set("mapreduce.framework.name", "local");
			conf.set("yarn.resourcemanager.hostname", "node08");
			conf.set("ha.zookeeper.quorum", "node07,node08,node09");
			conf.set("mapreduce.app-submission.cross-platform", "true");
			this.conf = conf;
		}

		@Override
		public Configuration getConf() {
			return this.conf;
		}
			
		/**
		 * 集群上  运行时  必须 打jar包  然后 运行  这个类  
		 */
		@Override
		public int run(String[] args) throws Exception {
			Configuration conf = this.getConf();
			
	//		System.setProperty("HADOOP_USER_NAME", "root");
			Job job = Job.getInstance(conf);
			job.setJarByClass(MyWC.class);   // 本地就 可以  
			job.setJobName("myjob");
			job.setJar("data/dd.jar");       // 集群运行时   必须要整个项目的jar

			//		job.setInputPath();
	//		job.setOutputPath();
			Path inPath = new Path("/user/root/test.txt");
			FileInputFormat.addInputPath(job, inPath);
			
			Path outPath = new Path("/output/wordcount");
			// 如果 输出路径 有  则删除
			if (outPath.getFileSystem(conf).exists(outPath)){
				outPath.getFileSystem(conf).delete(outPath,true);
			}
			FileOutputFormat.setOutputPath(job, outPath );

			job.setMapperClass(MyMapper.class);
			job.setMapOutputKeyClass(Text.class);// 说明  mappper端的输出时自定义对象且序列化的
			job.setMapOutputValueClass(IntWritable.class);
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(IntWritable.class);
			job.setReducerClass(MyReduce.class);
			
			return job.waitForCompletion(true)?0:-1;  // 打印作业流程	
		}

	}

#### mapper

	package com.sxt.mr.wc;

	import java.io.IOException;
	import java.util.StringTokenizer;

	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.LongWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Mapper;

	public class MyMapper extends Mapper<LongWritable, Text, Text,IntWritable>{
		
	   private final static IntWritable one = new IntWritable(1);
	   private Text word = new Text();
	   
	   // StringTockenizer字符串单词的切分       Object 偏移量  Text是一行的东西（）
	   public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
		 StringTokenizer itr = new StringTokenizer(value.toString()); // hello sxrt1
		 while (itr.hasMoreTokens()) {
		   word.set(itr.nextToken());
		   context.write(word, one); // hello 1  sxt 1  
		 }
	   }
	}


##### reducer
	package com.sxt.mr.wc;

	import java.io.IOException;

	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Reducer;


	public class MyReduce extends Reducer<Text, IntWritable, Text, IntWritable>{
	   private IntWritable result = new IntWritable();
		 
	   public void reduce(Text key, Iterable<IntWritable> values,
						  Context context) throws IOException, InterruptedException {
		 int sum = 0;
		 for (IntWritable val : values) {
		   sum += val.get();
		 }
		 result.set(sum);
		 context.write(key, result); // hello 36 sxt 100
	   }

	}

















