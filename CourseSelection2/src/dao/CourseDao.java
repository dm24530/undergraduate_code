package dao;
import entity.Course;

import entity.IEntity;
import entity.Student;

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class CourseDao implements IDao {

	//初始化课程信息
	private static CourseDao instance;
	private HashMap<String, Course> courses;
	private Course course;
	private CourseDao() {
		courses = new HashMap<String, Course>();
	    course = new Course();

		File file = new File("course.dat");
		String string = getTxt(file);
		String[] split = string.split("\r\n");

		for (int i=1;i<split.length;i++) {
			Course course = new Course();
			String[] split1 = split[i].split(",");
			course.setCourseNo(split1[0]);
			course.setCourseName(split1[1]);
			course.setCourseGrade(Integer.parseInt(split1[2]));
			courses.put(course.getCourseNo(),course);
		}

	}

	//读取txt文件内容
	public static String getTxt(File file){
		StringBuilder result = new StringBuilder();
		try{
			BufferedReader br = new BufferedReader(new FileReader(file));//构造一个BufferedReader类来读取文件
			String s = null;
			while((s = br.readLine())!=null){//使用readLine方法，一次读一行
				result.append(System.lineSeparator()+s);
			}
			br.close();
		}catch(Exception e){
			e.printStackTrace();
		}
		return result.toString();
	}


	private void getcoursesFromInputStream(String isName) {
		// TODO Auto-generated method stub
		try{
			FileInputStream fs = new FileInputStream(isName);
			byte[] content = new byte[1024];
			int i=0;
			int conInteger = 0;
			while(true){
			    try{
			        conInteger = fs.read();
			    } catch (Exception e){
			       e.printStackTrace();
			    }
			    if(-1 == conInteger){
			         break;
			    }else if('\r' == (char)conInteger || '\n' == (char)conInteger){
			        try{
			            this.processUserString(new String(content,"GBK").trim());
			            i=0;
			        } catch (Exception e){
			           e.printStackTrace();
			        }
			        continue;
			    } else{
			        content[i] = (byte)conInteger;
			        i++;
			    }   
			}
		}catch(Exception e){
			e.printStackTrace();
		}
	}
	private void processUserString(String userString) {
		// TODO Auto-generated method stub
		String [] userFields = userString.split(",");
		Course c = new Course();
		c.setCourseNo(userFields[0]);
		c.setCourseName(userFields[1]);
		c.setCourseGrade(Integer.parseInt(userFields[2]));
		courses.put(c.getCourseNo(),c);
	}
	public static CourseDao getInstance() {
		if(instance == null) {
			synchronized(CourseDao.class) {
				if(instance == null) {
					instance = new CourseDao();
					return instance;
				}
			}
		}
		return instance;
	}

	public Map<String,Course> show(){
		return courses;
	}


	
	@Override
	public void insert(IEntity entity) {
		// TODO Auto-generated method stub

	}

	@Override
	public void delete() {
		// TODO Auto-generated method stub

	}

	@Override
	public void update() {
		// TODO Auto-generated method stub

	}

	@Override
	public HashMap<String, entity.IEntity> getAllEntities() {
		// TODO Auto-generated method stub
		return null;
	}



	@Override
	public IEntity getEntity(String Id) {
		// TODO Auto-generated method stub
		return courses.get(Id);
	}
	@Override
	public IEntity getEntity(int s) {
		// TODO Auto-generated method stub
		return null;
	}

}
