package 改造;
import user.*;
import factory.*;
import utility.*;

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Random;

public class TelcomUser {
	private String phoneNumber;
	//被叫号码
	private String callTo;
	//用来存储通讯记录
	private StringBuffer commiuncationRecords;
	//创建一个User用户feifei
	User feifei;
	public  TelcomUser (String phoneNumber) {
		this.phoneNumber = phoneNumber;
		this.commiuncationRecords = new StringBuffer();
		//使用工厂方法
		Factory userFactory = (Factory) XMLUtil.getBean();	
		feifei=userFactory.produceuser();
	}
	
	//模拟通话记录的形成
	public void generateCommunicateRecord() {
		//随机生成通话记录数目
		int recordNum = new Random().nextInt(10);
		for(int i=0;i<=recordNum;i++) {
			//开始时间，当前时间前的某个随机时间
			long timeStart = System.currentTimeMillis() - new Random().nextInt(36000000);
			//结束时间，开始后的十分钟内随机一个时间，至少一分钟
			long timeEnd = timeStart + 60000 + new Random().nextInt(600000);
			//被叫号码
			callTo = getCallToStringPhoneNumber();
			//插入通话记录
			 this.commiuncationRecords.append(this.phoneNumber +
					 ","+ timeStart +
					 "," +timeEnd +
					 "," +this.callTo +
					 ";"); 
		}
	}
	
	//随机生成被叫号码（后四位）并返回
	public String getCallToStringPhoneNumber() {
		// TODO Auto-generated method stub
		return "1380372" + String.valueOf(new Random().nextInt(10))
		+ String.valueOf(new Random().nextInt(10))
		+ String.valueOf(new Random().nextInt(10))
		+ String.valueOf(new Random().nextInt(10));
	}
	
	//模拟计费方法，以字符串的形式返回保留的4位小数的计费结果
	public String accountFee(long timeStart, long timeEnd) {
		// TODO Auto-generated method stub
		//每分钟收费不同营业商不同价钱,按当前营业商的费率为准
				double feePerMinute = feifei.feilv();
				//通话分钟数按四舍五入计算
				int minutes = Math.round((timeEnd - timeStart)/60000);
				//计算话费
				double feeTotal = feePerMinute * minutes;
				return String.format("%.4f", feeTotal);
	}
	
/*    //打印通话记录
	public void printDetails() {
		获取全部通话记录
		String allRecords = this.commiuncationRecords.toString();
		分割通话记录
		String [] recordArray = allRecords.split(";");
		循环将分割通话记录的每一项输出
		for(int i=0;i<recordArray.length;i++) {
			String[] recordField = recordArray[i].split(",");
			System.out.println(feifei.name());
			System.out.println("主叫：" + recordField[0]);
			System.out.println("呼叫：" + recordField[3]);
			System.out.println("通话开始时间：" + new Date(Long.parseLong(recordField[1])));
			System.out.println("通话结束时间：" + new Date(Long.parseLong(recordField[2])));
			System.out.println("计费费率："+feifei.feilv()+"元");
			System.out.println("计费："
			+accountFee(Long.parseLong(recordField[1]),Long.parseLong(recordField[2]))
					+ "元。");
		}
	}           */
//	打印通话记录
	public void printDetails() {
		//获取全部通话记录
				String allRecords = this.commiuncationRecords.toString();
				//分割通话记录
				String [] recordArray = allRecords.split(";");
				//循环分割记录内的每一项并输出
				for(int i = 0; i < recordArray.length; i++) {
//					System.out.println("---------通话记录分割线---------");
					//通讯公司名称
					System.out.println("---------"+feifei.name()+"---------");
					String [] recordField = recordArray[i].split(",");
					System.out.println("主叫：" + recordField[0]);
					System.out.println("被叫：" + recordField[3]);
					//通话开始时间
					Date timeStart = new Date(Long.parseLong(recordField[1]));
					//通话结束时间
					Date timeEnd = new Date(Long.parseLong(recordField[2]));
					//通话时长
					Date timeminus = new Date(Long.parseLong(recordField[2])-Long.parseLong(recordField[1]));
					
					DateFormat mediumFormat = DateFormat.getDateTimeInstance(DateFormat.MEDIUM, DateFormat.MEDIUM);
					//以年月日时分秒的形式记录通话的开始结束时间
					SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy年MM月dd日 hh时mm分ss秒");
					//以分秒形式记录通话时长,让顾客看的更清晰
					SimpleDateFormat simpleDateFormat2 = new SimpleDateFormat("mm分ss秒");
					//DateFormat
					/*
					System.out.println("通话开始时间：" + mediumFormat.format(timeStart));
					System.out.println("通话结束时间：" + mediumFormat.format(timeEnd));
					*/
					
					//将所需要的各项输出		
					System.out.println("通话开始时间：" + simpleDateFormat.format(timeStart));
					System.out.println("通话结束时间：" + simpleDateFormat.format(timeEnd));
					System.out.println("通话时长："+simpleDateFormat2.format(timeminus));
					System.out.println("计费费率："+feifei.feilv());
					System.out.println("计费：" 
							+ accountFee(Long.parseLong(recordField[1]), Long.parseLong(recordField[2]))
							+ " 元。");
				}
			}
	}
