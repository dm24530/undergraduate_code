package dao;
import entity.IEntity;
import entity.Student;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.HashMap;
import java.util.Set;

public class StudentDao implements IDao {

	private static StudentDao instance;
	private HashMap<String, Student> students;
	private Student student;
	private  FileInputStream fs;
	public FileOutputStream fos;
	
	private StudentDao() {
			
		students = new HashMap<String, Student>();
		student = new Student();
		getUsersFromInputStream("user.dat");
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
	
	public void processUserString(String userString) {
		String [] userFields = userString.split(",");
		Student stu = new Student();
		stu.setStudentNo(userFields[0]);
		stu.setStudentPassword(userFields[1]);
		stu.setStudentName(userFields[2]);
		stu.setStudentGender(userFields[3]);
		stu.setStudentAge(Integer.parseInt(userFields[4]));
		stu.setStudentDepartment(userFields[5]);
		
		students.put(stu.getStudentNo(), stu);
	}
	
	public static StudentDao getInstance() {
		if(instance == null) {
			synchronized(StudentDao.class) {
				if(instance == null) {
					instance = new StudentDao();
					return instance;
				}
			}
		}
		return instance;
	}
	
	public void update() {
		// TODO Auto-generated method stub
		Set<String> stuSet = students.keySet();
		StringBuffer uStringBuffer = new StringBuffer();
		for(String studentNo:stuSet) {
			Student stu = (Student)students.get(studentNo);
			
			String uString = stu.getStudentNo() + ","
					+ stu.getStudentPassword() + ","
					+ stu.getStudentName() + ","
					+ stu.getStudentGender() + ","
					+ stu.getStudentAge() + ","
					+ stu.getStudentDepartment() + "\r\n";
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
	
	@Override
	public void insert(IEntity entity) {
		// TODO Auto-generated method stub
		Student st = (Student)entity;
		students.put(st.getStudentNo(), st);
	}

	@Override
	public void delete() {
		// TODO Auto-generated method stub

	}
/*
	@Override
	public void update() {
		// TODO Auto-generated method stub

	}
*/
	@Override
	public HashMap<String, IEntity> getAllEntities() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public IEntity getEntity(String Id) {
		// TODO Auto-generated method stub		
		return students.get(Id);
	}

}
