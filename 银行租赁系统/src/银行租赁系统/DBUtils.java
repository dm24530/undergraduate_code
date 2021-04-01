package 银行租赁系统;
import java.*;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Set;

public class DBUtils {
	
	private static DBUtils instance = null;
	private HashMap<String,User> users = new HashMap<String,User>();
	public StringBuffer  line;
	private  FileInputStream fs;
	public FileOutputStream fos;
	
	private DBUtils(){
		
		getUsersFromInputStream("user.dat");
	}
	
	
	public void processUserString(String userString) {
		String [] userFields = userString.split(",");
		User u = new User();
		u.setCardId(userFields[0]);
		u.setCardPwd(userFields[1]);
		u.setUserName(userFields[2]);
		u.setCall(userFields[3]);
		u.setSex(userFields[4]);
		u.setAccount(Integer.parseInt(userFields[5]));
		
		users.put(u.getCardId(), u);
	}
	
	private void getUsersFromInputStream(String isName) {
		try {
		    fs = new FileInputStream(isName);
			byte[] content = new byte[1024];
			int i=0;
			int conInteger = 0;
			while(true) {
				try {
					conInteger = fs.read();
				} catch(IOException e) {
					e.printStackTrace();
				}
				if(-1 == conInteger) {
					break;
				}else if('\r' == (char)conInteger || '\n' == (char)conInteger) {
					try {
						this.processUserString(new String(content,"GBK").trim());
						i=0;
					} catch(UnsupportedEncodingException e) {
						e.printStackTrace();
					}
					continue;
				}else {
					content[i] = (byte)conInteger;
					i++;
				  }
			     }
		     } catch(Exception e) {
				e.printStackTrace();
		 }
      }
	public void update() {
		// TODO Auto-generated method stub
		Set<String> userSet = users.keySet();
		StringBuffer uStringBuffer = new StringBuffer();
		for(String cardId:userSet) {
			User u = (User)users.get(cardId);
			
			String uString = u.getCardId() + ","
					+ u.getCardPwd() + ","
					+ u.getUserName() + ","
					+ u.getCall() + ","
					+ u.getSex() + ","
					+ u.getAccount() + "\r\n";
			uStringBuffer.append(uString);
		}
		putUsersToFile(uStringBuffer.toString(),"user.dat");
	}
	private void putUsersToFile(String uString,String osName) {
		try {
			fos = new FileOutputStream(osName);
			try {
				fos.write(uString.getBytes("GBK"));
			}catch(UnsupportedEncodingException e) {
				e.printStackTrace();
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	//懒汉单例模式
	public static DBUtils getInstance(){
		if(instance == null){
			synchronized (DBUtils.class){
				if(instance == null){
					instance = new DBUtils();
				}
			}
		}
		return instance;
	}
	//获取单一用户
	public User getUser(String cardId){
		User user = (User) users.get(cardId);
		return user;
	}
	//获取全部用户
	public HashMap<String,User> getUsers(){
//		 HashMap<String,User> userss =  (HashMap<String,User>) users;
		 return users;
	}
	public void addUser(User u) {
		users.put(u.getCardId(), u);
	}


}
