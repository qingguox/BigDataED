package com.bjsxt.hbase;

import java.io.IOException;
import java.io.InterruptedIOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.hbase.CellUtil;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.MasterNotRunningException;
import org.apache.hadoop.hbase.TableName;
import org.apache.hadoop.hbase.ZooKeeperConnectionException;
import org.apache.hadoop.hbase.client.Get;
import org.apache.hadoop.hbase.client.HBaseAdmin;
import org.apache.hadoop.hbase.client.HTable;
import org.apache.hadoop.hbase.client.Put;
import org.apache.hadoop.hbase.client.Result;
import org.apache.hadoop.hbase.client.ResultScanner;
import org.apache.hadoop.hbase.client.RetriesExhaustedWithDetailsException;
import org.apache.hadoop.hbase.client.Scan;
import org.apache.hadoop.hbase.filter.CompareFilter.CompareOp;
import org.apache.hadoop.hbase.filter.FilterList;
import org.apache.hadoop.hbase.filter.PrefixFilter;
import org.apache.hadoop.hbase.filter.SingleColumnValueFilter;
import org.apache.hadoop.hbase.util.Bytes;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import com.bjsxt.hbase.Phone.DayOfPhone;
import com.bjsxt.hbase.Phone.PhoneDetail;

/**
 *  电话    小区电话案例 ，   包装对象的 使用。
 * @author asus
 *
 */
public class PhoneCase_practice {
	
	// 表的 管理对象，负责表的 创建，和删除
	HBaseAdmin admin = null;
	// 数据的 管理类
	HTable table = null;
	// 表名
	String tm = "phone2";
	// 列族 
	String familyName = "cf";
	
	@Before 
	public void init() throws MasterNotRunningException, ZooKeeperConnectionException, IOException {
		
		Configuration conf = new Configuration();
		conf.set("hbase.zookeeper.quorum", "node07,node08,node09");
//		conf.set("fs.defaultFs", "hdfs://node06:8020");
//		conf.set("mapreduce.framework.name", "yarn");
//		conf.set("ha.zookeeper.yuorum", "node07,node08,node09");
//		conf.set("yarn.resourcemanager.hostname", "node08");
		admin = new HBaseAdmin(conf);
		table = new HTable(conf, tm.getBytes());
	}
	
	/*
	 *  创建表 phone2
	 */
	@Test
	public void createTable() throws IOException {
		// 表的描述  和 列的 描述
		HTableDescriptor desc = new HTableDescriptor(TableName.valueOf(tm));
		HColumnDescriptor family = new HColumnDescriptor(familyName);
		desc.addFamily(family);
		if (admin.tableExists(tm)) {
			admin.disableTable(tm);
			admin.deleteTable(tm);
		}
		admin.createTable(desc);
	}
	
	Random r = new Random();
	SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddhhmmss");
	
	/**
	 * 10个用户 ，每一个用户 每年产生1000个通话记录
	 * dnum : 对放手机号
	 * type : 0主叫    1被叫
	 * length : 长度 
	 * date ：时间 
	 * @throws InterruptedIOException 
	 * @throws RetriesExhaustedWithDetailsException 
	 * @throws ParseException 
	 * @throws Exception 
	 */
	@Test
	public void insert() throws RetriesExhaustedWithDetailsException, InterruptedIOException, ParseException {
		List<Put> list = new ArrayList<>();
		for (int i = 0; i < 10; i++) {
			String phoneNumber = getPhone("158");
			for (int j = 0; j < 1000; j++) {
				// 属性
				String dnum = getPhone("177");
				String length = String.valueOf(r.nextInt(99)); // 通话时长
				String type = String.valueOf(r.nextInt(2));
				String date = getDate("2018");
				
				String rowKey = phoneNumber+"_"+String.valueOf(Long.MAX_VALUE-sdf.parse(date).getTime());
				Put put = new Put(rowKey .getBytes());
				put.add(familyName.getBytes(), "dnum".getBytes(), dnum.getBytes());
				put.add(familyName.getBytes(), "length".getBytes(), length.getBytes());
				put.add(familyName.getBytes(), "type".getBytes(), type.getBytes());
				put.add(familyName.getBytes(), "date".getBytes(), date.getBytes());
				list.add(put);
			}
		}
		table.put(list);
	}
	
	/**
	 * 查询 某一个用户 3 月份的 所有用户记录 
	 *  startRow
	 *  stopRow 
	 * @throws ParseException 
	 * @throws IOException 
	 */
	@Test
	public void scan() throws Exception {
		
		String phoneNum = "15894908883";
		String startRow = phoneNum+"_"+String.valueOf(Long.MAX_VALUE-sdf.parse("20180401000000").getTime());
		String stopRow = phoneNum+"_"+String.valueOf(Long.MAX_VALUE-sdf.parse("20180301000000").getTime());;
		
		Scan scan = new Scan();
		scan.setStartRow(startRow.getBytes());
		scan.setStopRow(stopRow.getBytes());
		ResultScanner scanner = table.getScanner(scan);
		for (org.apache.hadoop.hbase.client.Result result : scanner) {
			String dnum = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "dnum".getBytes())));
			String length = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "length".getBytes())));
			String type = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "type".getBytes())));
			String date = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "date".getBytes())));
			System.out.println(dnum+ " == "+length+" == "+type+" = "+date);
		}
		scanner.close();
	}
	
	/**
	 * 查看 一个用户  所有的 主叫电话 
	 * 条件 ：
	 *     电话号码 
	 *     type  = 0
	 * @throws IOException 
	 */
	@Test
	public void scan2() throws Exception {
		
		FilterList filters = new FilterList(FilterList.Operator.MUST_PASS_ALL);
		SingleColumnValueFilter filter1 = new SingleColumnValueFilter(familyName.getBytes(), "type".getBytes(), CompareOp.EQUAL, "0".getBytes());
		PrefixFilter filter2 = new PrefixFilter("15894908883".getBytes());
		filters.addFilter(filter1);
		filters.addFilter(filter2);
		
		Scan scan = new Scan();
		scan.setFilter(filters);
		ResultScanner scanner = table.getScanner(scan);
		int i = 0;
		for (org.apache.hadoop.hbase.client.Result result : scanner) {
			String dnum = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "dnum".getBytes())));
			String length = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "length".getBytes())));
			String type = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "type".getBytes())));
			String date = Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "date".getBytes())));
			System.out.println(dnum+ " == "+length+" == "+type+" = "+date);
			i++;
		}
		System.out.println("共有 "+i);
		scanner.close();
	}
	
	
	
	
	private String getPhone(String string) {
		return string+String.format("%08d", r.nextInt(99999999));
	}
	private String getDate(String string) {
		return string+String.format("%02d%02d%02d%02d%02d", r.nextInt(12)+1,r.nextInt(31),
				r.nextInt(24),r.nextInt(60),r.nextInt(60));
	}
	
	
	

	/**
	 * 10个用户  1000条  每一个记录当做一个对对象
	 * @throws ParseException 
	 * @throws InterruptedIOException 
	 * @throws RetriesExhaustedWithDetailsException 
	 */
	@Test
	public void insert2() throws ParseException, RetriesExhaustedWithDetailsException, InterruptedIOException{
		List<Put> puts = new ArrayList<>();
		for(int i = 0;i < 10;i++){
			String phoneNumber = getPhone("158");
			for(int j = 0;j<1000;j++){
				// 属性 
				String dnum = getPhone("177");
				String length = String.valueOf(r.nextInt(99));// 通话时长
				String type = String.valueOf(r.nextInt(2));
				String date = getDate("2018");
				
				// 保存在一个对象中    cf:phoneDail value: phoneDAil
				Phone.PhoneDetail.Builder phoneDetail = Phone.PhoneDetail.newBuilder();
				phoneDetail.setDate(date);
				phoneDetail.setDnum(dnum);
				phoneDetail.setLength(length);
				phoneDetail.setType(type);
				
				
				String rowkey = phoneNumber+"_"+String.valueOf(Long.MAX_VALUE-sdf.parse(date).getTime());
				Put put = new Put(rowkey .getBytes());
				put.add(familyName.getBytes(), "phoneDetail".getBytes(),phoneDetail.build().toByteArray());
				puts.add(put);
			}
		}
		table.put(puts);
	}
	
	@Test
	public void get2() throws IOException {
		Get get = new Get("15814840952_9223370519726076807".getBytes());
		Result result = table.get(get);
		PhoneDetail phoneDetail = Phone.PhoneDetail.parseFrom(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "phoneDetail".getBytes())));
		System.out.println(phoneDetail);
	}
	
	
	
	/**
	 * 10 个用户   ，20181225产生 1000条记录  每一天的记录放在一个rowkey中
	 * 
	 * 把 多个同一个对象1装入 另一个对象2中
	 * @throws Exception 
	 */
	@Test
	public void insert3() throws ParseException, RetriesExhaustedWithDetailsException, InterruptedIOException{
		List<Put> puts = new ArrayList<>();
		for(int i = 0;i < 10;i++){
			String phoneNumber = getPhone("133");
			String rowkey = phoneNumber+"_"+String.valueOf(Long.MAX_VALUE-sdf.parse("20181225000000").getTime());
			Phone.DayOfPhone.Builder dayOfPhone = Phone.DayOfPhone.newBuilder();
			for(int j = 0;j<1000;j++){
				// 属性 
				String dnum = getPhone("177");
				String length = String.valueOf(r.nextInt(99));// 通话时长
				String type = String.valueOf(r.nextInt(2));
				String date = getDate2("20181225");
				
				// 保存在一个对象中    cf:phoneDail value: phoneDAil
				Phone.PhoneDetail.Builder phoneDetail = Phone.PhoneDetail.newBuilder();
				phoneDetail.setDate(date);
				phoneDetail.setDnum(dnum);
				phoneDetail.setLength(length);
				phoneDetail.setType(type);
				dayOfPhone.addDayPhone(phoneDetail);
				
			}
			Put put = new Put(rowkey.getBytes());
			put.add(familyName.getBytes(), "dayOfPhone".getBytes(),dayOfPhone.build().toByteArray());
			puts.add(put);    // 10 条数据
		}
		table.put(puts);
	}
	
	@Test
	public void get3() throws IOException {
		Get get = new Get("13324399746_9223370491187575807".getBytes());  // 获取row
		Result result = table.get(get);
		DayOfPhone dayOfPhone = Phone.DayOfPhone.parseFrom(CellUtil.cloneValue(result.getColumnLatestCell(familyName.getBytes(), "dayOfPhone".getBytes())));
		
		List<PhoneDetail> dayPhoneList = dayOfPhone.getDayPhoneList();
		for (PhoneDetail phoneDetail : dayPhoneList) {
			System.out.println(phoneDetail);
		}
	}
	
	@SuppressWarnings("unused")
	private String getDate2(String string) {
		return string+String.format("%02d%02d%02d", r.nextInt(24),r.nextInt(60),r.nextInt(60));
	}

	/**
	 * 
	 * @throws IOException
	 */
	@After
	public void destory() throws IOException{
		if (admin!=null){
			admin.close();
		}
	}
	
	
}
