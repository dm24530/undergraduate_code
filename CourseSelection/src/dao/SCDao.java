package dao;
import entity.SC;
import entity.Course;
import entity.IEntity;
import entity.Student;

import java.io.*;
import java.util.HashMap;
import java.util.Set;

public class SCDao implements IDao {
	 static StudentDao studentDao;
	private static SCDao instance;
	private HashMap<String, SC> scs;
	private SC sc;
	private SCDao() {
		scs = new HashMap<String, SC>();
	    sc = new SC();

	}

	public static void show(String id){
		File file = new File("sc1.txt");
		System.out.println(getTxt(file,id));
	}


	//读取dat文件内容
	public static String getTxt(File file,String id){
	studentDao = StudentDao.getInstance();
		Student student = (Student) studentDao.getEntity(id);
	//	System.out.println(student.getStudentName());
		StringBuilder result = new StringBuilder();
		try{
			BufferedReader br = new BufferedReader(new FileReader(file));//构造一个BufferedReader类来读取文件
			String s = null;
			while((s = br.readLine())!=null){//使用readLine方法，一次读一行 
				int index=s.indexOf(student.getStudentName());  
				if(index==0) {
					System.out.println(s); 
				}
			
			}
			br.close();
		}catch(Exception e){
			e.printStackTrace();
		}
		return result.toString();
	}
	
	@Override
	public void insert(IEntity entity) {
		// TODO Auto-generated method stub
		SC st = (SC)entity;
		scs.put(st.getCourseNo(), st);
	}

	@Override
	public void delete() {
		// TODO Auto-generated method stub

	}

	@Override
	public void update() {
		// TODO Auto-generated method stub
		Set<String> userSet=scs.keySet();
		StringBuffer uStringBuffer=new StringBuffer();
		for(String StudentNo:userSet) {
			SC u=(SC)scs.get(StudentNo);
			String uString=u.getStudentNo()+","
					+u.getCourseNo()+","
					+u.getGrade()+"\r\n";
			uStringBuffer.append(uString);
		}
		putscsToFile(uStringBuffer.toString(),"sc1.txt");
	}
	
	private void putscsToFile(String uString,String osName) {
		try {
			FileOutputStream fos = new FileOutputStream(osName);
			try {
				fos.write(uString.getBytes("GBK"));
			}catch(UnsupportedEncodingException e) {
				e.printStackTrace();
			}
		}catch(Exception e) {
			e.printStackTrace();
		}
	}
	public static SCDao getInstance() {
		if(instance == null) {
			synchronized(SCDao.class) {
				if(instance == null) {
					instance = new SCDao();
					return instance;
				}
			}
		}
		return instance;
	}
	@Override
	public HashMap<String, IEntity> getAllEntities() {
		// TODO Auto-generated method stub
		return null;
	}

	public IEntity getEntity(String Id) {
		// TODO Auto-generated method stub
		return scs.get(Id);
	}

	@Override
	public IEntity getEntity(int s) {
		// TODO Auto-generated method stub
		return null;
	}
	


}
