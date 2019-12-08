
### :Protobuf 安装
>
	1.    tar  -zxf protobuf-.......
	2. yum groupinstall "Development tools"
	3. ./config......   默认安安装在 usr/local
	4. make && make  install 

> 
	package com.bjsxt.hbase;
	message PhoneDetail
	{

		required string dnum = 1;
		required string length = 2;
		required string type = 3;
		required string date = 4;
	}
	message DayOfPhone
	{
		repeated PhoneDetail DayPhone = 1;
	}

		vi phone.proto 把上面的数据 放进去 

		/usr/local/bin/protoc phone.proto --java_out=/root/

		ftps 把java放到 eclipese


		insert3 放在 phone3中
		
### :Protobuf 使用   具体代码在 hbase/java/

- 一个电话 掉话率  检测

##### 先引入 那个Phone.java文件 
	
	在目录下


##### phoneCase 是对 数据插入 对象包装插入 多对象包装插入
> 
	注意。 put(rowKey)
			put.add("cf".getBytes(),"dnum".getBytes(),dnum.getBytes());
			get(rowkey);
			table.put(puts); 
			table.get(get);
	
	Scan scan = new Scan()
	scan.setStartrow("");   // 在 row中 查找  开始范围 
	scan.setStopRow("");   //   停止范围 
	
	
	/**
	 查询 指定 column中的数据 
	FiltersList lis  = new FiltersList(FiltersList.Operator.MUST_PASS_ALL);  ///  所有条件必须满足
	SingleColumnValueFilter filter= new SingleColumnValueFilter(familyName.getBytes(), 
	"type".getBytes(),  CompareOp.EQUAL, "0".getBytes());  // 只有 colum中的 type == 0才被取到
	PrefixFilter filter2 =new PrefixFilter("15894311313".getBytes());
	
	lis.addFilter(filter);  // 加入到 过滤器组中。
	lis.addFilter(filter);
	
	Scan scan = new Scan();
	scan.setFillter(filters);
	ResultScanner scanner = table.getScanner(scan);
	for（Result result: scanner） {
			System.out.print(Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell("cf".getBytes(), "dnum".getBytes()))));
			System.out.print("=="+Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell("cf".getBytes(), "type".getBytes()))));
			System.out.print("=="+Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell("cf".getBytes(), "length".getBytes()))));
			System.out.println("=="+Bytes.toString(CellUtil.cloneValue(result.getColumnLatestCell("cf".getBytes(), "date".getBytes()))));
	}
	scanner.close();


>   对象 插入 

	Phone.PhoneDetail.Builder phoneDetail = Phone.PhoneDetail.newBuilder();
	phoneDetail.setDate(date);
	phoneDetail.setDnum(dnum);
	phoneDetail.setLength(length);
	phoneDetail.setType(type);
	
	String rowkey = phoneNumber+"_"+String.valueOf(Long.MAX_VALUE-sdf.parse(date).getTime());
	Put put = new Put(rowkey.getBytes());
	put.add("cf".getBytes(),"phoneDetail".getBytes(),phoneDetail.build().toByteArray());
	puts.add(put);

>  把1000个 phoneDetail 包装到 一个 DayOfPhone中 
		插入 
	String rowkey = phoneNumber+"_"+String.valueOf(Long.MAX_VALUE-sdf.parse("20181225000000").getTime());
	Phone.DayOfPhone.Builder dayof = Phone.DayOfPhone.newBuilder();
	for(int j =0;j<1000;j++){
		// 属性 
		String dnum = getPhone("177");
		String length = String.valueOf(r.nextInt(99));// 通话时长
		String type = String.valueOf(r.nextInt(2));
		String date = getDate2("20181225");
		
		Phone.PhoneDetail.Builder phoneDetail = Phone.PhoneDetail.newBuilder();
		phoneDetail.setDate(date);
		phoneDetail.setDnum(dnum);
		phoneDetail.setLength(length);
		phoneDetail.setType(type);
		dayof.addDayPhone(phoneDetail);
	}
	Put put = new Put(rowkey.getBytes());
	put.add("cf".getBytes(), "day".getBytes(), dayof.build().toByteArray());
	puts.add(put);   //  10 只有10 条数据 rowkey 

	table.put(puts);
		
		
	获取数据 
		Get get = new Get("15893304049_9223370522077571807".getBytes());
	Result result = table.get(get);
	PhoneDetail phoneDetail = Phone.PhoneDetail.parseFrom(CellUtil.cloneValue(result.getColumnLatestCell("cf".getBytes(), 
			"phoneDetail".getBytes())));
	System.out.println(phoneDetail);	











