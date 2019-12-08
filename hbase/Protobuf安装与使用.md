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