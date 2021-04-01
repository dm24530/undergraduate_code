package 模拟电信计费系统;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.*;

public class TelcomUser {
	private String phoneNumber;
	private String callTo;
	
	private ArrayList <TreeMap>commiuncationRecords;
	private TreeMap singleRecord;
	
	public TelcomUser (String phoneNumber) {
		this.phoneNumber = phoneNumber;
		this.commiuncationRecords = new ArrayList<TreeMap>();
//		this.callToNumbers = new TreeSet();
	}
	//模拟通话记录的形成
	void generateCommunicateRecord() {
		//随机生成通话记录数目
		int recordNum = new Random().nextInt(10);
		for(int i=0;i<=recordNum;i++) {
			//开始时间，当前时间前的某个随机时间
			long timeStart = System.currentTimeMillis() - new Random().nextInt(36000000);
			//结束时间，开始后的十分钟内随机一个时间，至少一分钟
			long timeEnd = timeStart + 60000 + new Random().nextInt(600000);
			//被叫号码
			this.callTo = getCallToPhoneNumber();
//			this.callToNumbers.add(this.callTo);
			//插入通话记录
			this.singleRecord = new TreeMap();
			this.singleRecord.put("主叫",this.phoneNumber);
			this.singleRecord.put("开始时间",new Date(timeStart));
			this.singleRecord.put("结束时间",new Date(timeEnd));
			this.singleRecord.put("被叫号码", this.callTo);
			this.singleRecord.put("计费",this.accountFee(timeStart, timeEnd));
			this.commiuncationRecords.add(this.singleRecord);
		}
	}
    
	//随机生成被叫号码（后四位）并返回
	private String getCallToPhoneNumber() {
		return "1380372" + String.valueOf(new Random().nextInt(10))
		+ String.valueOf(new Random().nextInt(10))
		+ String.valueOf(new Random().nextInt(10))
		+ String.valueOf(new Random().nextInt(10));
	}
	//模拟计费方法，以字符串的形式返回保留的4位小数的计费结果
	private String accountFee(long timeStart,long timeEnd) {
		//每分钟收费0.2元
		double feePerMinute = 0.2;
		//通话分钟数按四舍五入计算
		int minutes = Math.round((timeEnd - timeStart)/60000);
		double feeTotal = feePerMinute * minutes;
		return String.format("%.4f", feeTotal);
	}
	//打印通话记录
	void printDetails() {
		/*
		 * 打印通话记录方法二
		 */
		Iterator itRecords = this.commiuncationRecords.iterator();
		while(itRecords.hasNext()) {
			System.out.println("---------通话记录分割线---------");
			this.singleRecord = ((TreeMap)itRecords.next());
			Set entrySet = this.singleRecord.entrySet();
			Iterator itEntry = entrySet.iterator();
			while(itEntry.hasNext()) {
				Map.Entry entry = (Map.Entry)itEntry.next();
				Object key = entry.getKey();
				Object value = entry.getValue();
				System.out.println(key + ":" + value);
			}
		}
		
		/*打印通话记录方法一
	    Iterator itRecords = this.commiuncationRecords.iterator();
	
		while(itRecords.hasNext()) {
			System.out.println("---------通话记录分割线---------");
			this.singleRecord = ((HashMap)itRecords.next());
			Set keySet = this.singleRecord.keySet();
			Iterator itkey = keySet.iterator();
			while(itkey.hasNext()) {
				Object key = itkey.next();
				Object value = this.singleRecord.get(key);
				System.out.println(key + ":" + value);
			}
		}
		*/
	}
}
