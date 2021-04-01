package dao;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Set;

import entity.Course;
import entity.IEntity;
import entity.SC;
import entity.Student;

public class SCDao implements IDao{
	
	private static SCDao instance;
	private HashMap<String, IEntity> scs;
	private SC sc;
	private FileInputStream fs;
    private FileOutputStream fos;
    
    private SCDao() {
    	scs = new HashMap<String,IEntity>();
		sc = new SC();
    	getSCFormInputStream("sc.dat");
    }
    
    private void getSCFormInputStream(String isName){
   	 try {
			fs=new FileInputStream(isName);
			byte[] content=new byte[1024];
			int i=0;
			int conInteger=0;
			while(true) {
				try {
					conInteger=fs.read();
				} catch (IOException e) {
					e.printStackTrace();
				}
				if(-1==conInteger) {
					break;
				}else if('\r'==(char)conInteger||'\n'==(char)conInteger) {
					try {
						this.processSCString(new String(content,"GBK").trim());
					} catch (UnsupportedEncodingException e) {
						e.printStackTrace();
					}
					i=0;
				}else {
					content[i]=(byte)conInteger;
					i++;
				}
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		}
    }
    private void processSCString(String scString) {
    	ArrayList<String>  arrayList= new ArrayList<String>();
		String[] scFields=scString.split(";");
   	 	SC sc = new SC();
   	 	sc.setStudentNo(scFields[0]);
        String courseString=new String();
	 	courseString=scFields[1];
	 	arrayList.add(courseString);
	 	sc.setCourseInformation(arrayList);
	 	
	 	//sc.setGrade(Integer.parseInt(scFields[2]));
	 	scs.put(sc.getStudentNo(), sc);
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
   	
	public void update() {
	   	 Set<String> scSet=scs.keySet();
	   	 StringBuffer scStringBuffer=new StringBuffer();
	   	// System.out.println(sc.getCourseInformation());
	   	 for(String studentNo:scSet) {
	   		 SC sc=(SC)scs.get(studentNo);
				String uString = sc.getStudentNo()+";"
						+sc.getCourseInformation()+"\r\n";
						//";"+sc.getGrade()+
				scStringBuffer.append(uString);
	   	 }
	   	 putSCToFile(scStringBuffer.toString(),"sc.dat");
	}
	
    private void putSCToFile(String uString,String osName){
   	 	try {
   	 		fos=new FileOutputStream(osName);
   	 	} catch (FileNotFoundException e) {
   	 		e.printStackTrace();
   	 	}
   	 	try {
   	 		fos.write(uString.getBytes("GBK"));
   	 	} catch (UnsupportedEncodingException e) {
   	 		e.printStackTrace();
   	 	} catch (IOException e) {
   	 		e.printStackTrace();
   	 	}
    }
    
	public void insert(IEntity entity) {
		SC sc= (SC)entity;
   		scs.put(sc.getStudentNo(), sc);
	}
	
	public void delete() {
		
	}
	
	public HashMap<String,IEntity> getAllEntities(){
		return scs;
	}
	
	public IEntity getEntity(String Id) {
		return scs.get(Id);
	}
	
}
