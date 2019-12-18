

### hbase 从 hdfs 读取数据 分析后 ，写入 hbase


> 

	package com.bjsxt.hbase_2;

	import org.apache.hadoop.conf.Configuration;
	import org.apache.hadoop.fs.Path;
	import org.apache.hadoop.hbase.client.Put;
	import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.NullWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Job;
	import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
	import org.apache.hadoop.util.Tool;
	import org.apache.hadoop.util.ToolRunner;
	import org.apache.log4j.Logger;


	/**
	 *  从   hdfs 读取数据 ，， 处理后 ， 写入 hbase
	 * @author asus
	 *
	 */
	public class WCRunner implements Tool{
		
		private static final Logger logger = Logger
				.getLogger(WCRunner.class);
		private Configuration conf = null;
		public static void main(String[] args) {
			
			try {
				ToolRunner.run(new Configuration(), new WCRunner(), args);
			} catch (Exception e) {
				logger.error("执行日志解析job异常",e);
				e.printStackTrace();
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
			conf.set("hbase.zookeeper.quorum", "node07,node08,node09");
			this.conf = conf;
		}

		@Override
		public Configuration getConf() {
			return this.conf;
		}

		@Override
		public int run(String[] args) throws Exception {
			
			
			Configuration conf = this.getConf();
			
			Job job = Job.getInstance(conf);
			job.setJarByClass(WCRunner.class);
			job.setJar("date/wc_tool.jar");   //整个项目的 jar 包
			
			job.setMapperClass(WCMapper.class);
			job.setMapOutputKeyClass(Text.class);
			job.setMapOutputValueClass(IntWritable.class);
			
			TableMapReduceUtil.initTableReducerJob("wc", WCReducer.class, job, 
					null, null, null, null,false);;
			FileInputFormat.addInputPath(job, new Path("/usr/wc.txt"));
			job.setOutputKeyClass(NullWritable.class);
			job.setOutputValueClass(Put.class);
			
			return job.waitForCompletion(true) ? 0 : -1;
		}
	}
	
> 
			package com.bjsxt.hbase_2;

	import java.io.IOException;

	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.LongWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Mapper;

	public class WCMapper  extends Mapper<LongWritable, Text, Text, IntWritable>{
		
		@Override
		protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, IntWritable>.Context context)
				throws IOException, InterruptedException {
			String[] split = value.toString().split("\\s+");
			for (String str: split) {
				context.write(new Text(str), new IntWritable(1));
			}
		}
	}
	
>

	package com.bjsxt.hbase_2;

	import java.io.IOException;

	import org.apache.hadoop.hbase.client.Mutation;
	import org.apache.hadoop.hbase.client.Put;
	import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
	import org.apache.hadoop.hbase.mapreduce.TableReducer;
	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Reducer;

	public class WCReducer extends TableReducer<Text, IntWritable, ImmutableBytesWritable>{
		
		@Override
		protected void reduce(Text key, Iterable<IntWritable> value,
				Reducer<Text, IntWritable, ImmutableBytesWritable, Mutation>.Context context)
				throws IOException, InterruptedException {
			if (key != null || key.toString() != "") {
				int sum = 0;
				for (IntWritable intWritable: value) {
					sum += intWritable.get();
				}
				Put put = new Put(key.toString().getBytes());
				put.add("cf".getBytes(), "name".getBytes(), String.valueOf(sum).getBytes());
				context.write(null, put);
			}
		}
	}

### 从 hbase 中读取数据 ， 写入到 hdfs
	
>
	package com.bjsxt.hbase_3;

	import org.apache.hadoop.conf.Configuration;
	import org.apache.hadoop.fs.Path;
	import org.apache.hadoop.hbase.client.Scan;
	import org.apache.hadoop.hbase.mapreduce.TableMapReduceUtil;
	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Job;
	import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
	import org.apache.hadoop.util.Tool;
	import org.apache.hadoop.util.ToolRunner;
	import org.apache.log4j.Logger;


	/**
	 *  从   hdfs 读取数据 ，， 处理后 ， 写入 hbase
	 * @author asus
	 *
	 */
	public class WCRunner2 implements Tool{
		
		private static final Logger logger = Logger
				.getLogger(WCRunner2.class);
		private Configuration conf = null;
		public static void main(String[] args) {
			
			try {
				ToolRunner.run(new Configuration(), new WCRunner2(), args);
			} catch (Exception e) {
				logger.error("执行日志解析job异常",e);
				e.printStackTrace();
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
			conf.set("hbase.zookeeper.quorum", "node07,node08,node09");
			this.conf = conf;
		}

		@Override
		public Configuration getConf() {
			return this.conf;
		}

		@Override
		public int run(String[] args) throws Exception {
			
			
			Configuration conf = this.getConf();
			
			Job job = Job.getInstance(conf);
			job.setJarByClass(WCRunner2.class);
			job.setJar("date/wc_tool2.jar");   //整个项目的 jar 包

			Scan scans = new Scan();
			scans.setCaching(500);   
			scans.setCacheBlocks(false);
			TableMapReduceUtil.initTableMapperJob("wc", scans, WCMapper2.class, Text.class, IntWritable.class, job);
		
			job.setReducerClass(WCReducer2.class);
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(IntWritable.class);
			FileOutputFormat.setOutputPath(job, new Path("/usr/wc2"));

			return job.waitForCompletion(true) ? 0 : -1;
		}
	}




>
	package com.bjsxt.hbase_3;

	import java.io.IOException;

	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Reducer;

	public class WCReducer2 extends Reducer<Text, IntWritable, Text, IntWritable>{
		
		
		@Override
		protected void reduce(Text key, Iterable<IntWritable> value,
				Reducer<Text, IntWritable, Text, IntWritable>.Context context) throws IOException, InterruptedException {
			
			int sum = 0;
			for (IntWritable intWritable: value) {
				sum += intWritable.get();
			}
			context.write(key, new IntWritable(sum));
		}
	}

>

	package com.bjsxt.hbase_3;

	import java.io.IOException;

	import org.apache.hadoop.hbase.CellUtil;
	import org.apache.hadoop.hbase.client.Result;
	import org.apache.hadoop.hbase.io.ImmutableBytesWritable;
	import org.apache.hadoop.hbase.mapreduce.TableMapper;
	import org.apache.hadoop.hbase.util.Bytes;
	import org.apache.hadoop.io.IntWritable;
	import org.apache.hadoop.io.Text;
	import org.apache.hadoop.mapreduce.Mapper;

	public class WCMapper2 extends TableMapper<Text, IntWritable>{
		
		private Text text = new Text();
		@Override
		protected void map(ImmutableBytesWritable key, Result value,
				Mapper<ImmutableBytesWritable, Result, Text, IntWritable>.Context context)
				throws IOException, InterruptedException {
			String str = Bytes.toString(CellUtil.cloneValue(value.getColumnLatestCell("cf".getBytes(), "name".getBytes())));
			text.set(Bytes.toString(key.get()));
			context.write(text, new IntWritable(Integer.valueOf(str)));
		}
	}


	
