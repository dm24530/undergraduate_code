package biz;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

import dao.*;
import entity.*;
import view.MainUI;

public class CourseBiz {	
	
	static StudentDao studentDao;
	static CourseDao coursedao;
	static SCDao scDao;
	private SC sc;
	private static Student student;
	private ArrayList<String> al;
	/*
	 * 选课操作
	 */
	public static void selection(String studentNo){
		//选课开始
		CourseDao courseDao = CourseDao.getInstance();
		StudentDao studentDao = StudentDao.getInstance();
		SCDao scDao = SCDao.getInstance();
		Map<String, Course> courses = courseDao.show();
		System.out.println("--------------所有课程信息------------------");
		for (Course course : courses.values()) {
			System.out.println("课程编号:"+course.getCourseNo()+",课程名称:"+course.getCourseName()+",课程学分:"+course.getCourseGrade());
		}
		Scanner in = new Scanner(System.in);
		System.out.println("请输入所选课程编号");
	    String courseNo = in.next();
		Course entity = (Course)courseDao.getEntity(courseNo);
		if (entity == null){
			System.out.println("所选课程不存在");
			MainUI.show(studentNo);
		}else{
			int s = Integer.parseInt(courseNo);
			SC sc = (SC) scDao.getEntity(studentNo);
			Student student = (Student) studentDao.getEntity(studentNo);

			String[] ke={"C语言","数据结构","Java面向对象","Linux操作系统","数据库","网页设计"};  //文件中存储的课程名
			try{
				File file = new File("sc1.txt");    // 建立一个file对象，参数就是你想访问文件的路径
				BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file)));
				List list =new ArrayList();       //定义一个集合存放每一行的字符串
				while(true){
				    String str=br.readLine();  //读取文件当中的一行
				    if(str==null) 
				    	break;       //如果读取的是空，也就是文件读取结束 跳出循环
				    int index=str.indexOf(student.getStudentName());    //看此行的是否为用户信息
				    if(index != -1){
				    	int index1=str.indexOf(ke[s-1]);     //查找是否有所选课程 不包含返回值>=0		        
				    	//System.out.println(index1);
				    	if(index1>0){           //用index1判读是否有所选的课程
				    	    System.out.println("选课失败，该课程" + ke[s-1] + "已选!"); //如果包含就返回，选课失败
				    	   // return;
				    	    selection(studentNo);
				        }
				        else{
				        	System.out.println(ke[s-1] + "选课成功！");
				    	    str=str+","+ke[s-1];      //不包含则选课成功，将所选课程加入文件中                                               
				        }
				    }
				    list.add(str);     //把修改之后的str放到集合当中
				}
			br.close();
			PrintWriter pw=new PrintWriter(file);    //建立一个输出流，把东西写入文件
			for(int i=0;i<list.size();i++){
				String str =(String)list.get(i);     //从集合当中取出字符串
				pw.println(str);                     //把该字符串写入文件当中
				}
			pw.close();
			} catch (Exception e){
			       e.printStackTrace();
			   }
			SCBiz.judge(studentNo);
		}
	}

	/*
	 * 退选操作
	 */
	public static void exitRace(String studentNo) {
		//退选开始
				CourseDao courseDao = CourseDao.getInstance();
				StudentDao studentDao = StudentDao.getInstance();
				SCDao scDao = SCDao.getInstance();
				Map<String, Course> courses = courseDao.show();
				System.out.println("--------------所有课程信息------------------");   //输出所有课程信息
				for (Course course : courses.values()) {
					System.out.println("课程编号:"+course.getCourseNo()+",课程名称:"+course.getCourseName()+",课程学分:"+course.getCourseGrade());
				}
				Scanner in = new Scanner(System.in);      //所退选课程编号
				System.out.println("请输入退选课程编号");
			    String courseNo = in.next();
				Course entity = (Course)courseDao.getEntity(courseNo);
				if (entity == null){          //找不到这个课的信息
					System.out.println("所选课程不存在");
					MainUI.show(studentNo);
				}else{               
					int s = Integer.parseInt(courseNo);   
					SC sc = (SC) scDao.getEntity(studentNo);
					Student student = (Student) studentDao.getEntity(studentNo);
					
					String[] ke={"C语言","数据结构","Java面向对象","Linux操作系统","数据库","网页设计"};
					try{
						File file = new File("sc1.txt");      // 建立一个file对象，参数就是你想访问文件的路径
						BufferedReader br = new BufferedReader(new InputStreamReader(new FileInputStream(file)));
						List list =new ArrayList();           //定义一个集合存放每一行的字符串
						while(true){
						    String str=br.readLine();          //读取文件当中的一行
						    if(str==null) break;                //如果读取的是空，也就是文件读取结束 跳出循环
						    int index=str.indexOf(student.getStudentName());   //看此行的是否为用户信息
						    if(index == 0){
						    	int index1=str.indexOf(ke[s-1]);   //查找是否有所选课程 不包含返回值==0		        
						    	//System.out.println(index1);
						    	if(index1<0){  
						    	    System.out.println("退选失败，该课程" + ke[s-1] + "未选!");   //如果包含就返回，选课失败
						    	   // return;
						    	   selection(studentNo);
						        }
						        else{
						        	str=str.replace(","+ke[s-1],"");
						        	System.out.println(ke[s-1] + "退选成功！");
						    	      
						        	   
						        }
						    }
						    list.add(str);            //把修改之后的str放到集合当中
						}
					br.close();
					PrintWriter pw=new PrintWriter(file);      //建立一个输出流，把东西写入文件
					for(int i=0;i<list.size();i++){
						String str =(String)list.get(i);     //从集合当中取出字符串
						pw.println(str);                     //把该字符串写入文件当中
						}
					pw.close();
					} catch (Exception e){
					       e.printStackTrace();
					   }
					SCBiz.judge(studentNo);
				}
			}
	/*
	 * 课程情况查看
	 */
	private static void showAllCourse() {
	
	}
	public static String getTxt(File file,String studentNo){
		studentDao = StudentDao.getInstance();
		student = (Student) studentDao.getEntity(studentNo);
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
		SCBiz.judge(studentNo);
		return result.toString();
	}
	/*
	 * 已选课程情况查看
	 *//*
	private static void showSeleceCourse() {
		scDao = SCDao.getInstance();
		scb = scDao.getAllEntities();
		Set<String> keySet = scb.keySet();
		System.out.println("所有的已选课程信息：");
		Iterator it = keySet.iterator();
		while(it.hasNext()) {
			Object key = it.next();
			SC value = (SC)scb.get(key);
			System.out.println(value.getStudentNo()+","+value.getCourseNo()+","+value.getGrade());
		}
		judge(student.getStudentNo());
	}
	/*
	 * 判断课程是否存在
	 */
	/*
	public static boolean judgeCourse() {
		coursedao = CourseDao.getInstance();
		cs = coursedao.getAllEntities();
		Set<String> keySet = cs.keySet();
		System.out.println("请输入课程编号：");
		String courseNo = scanner.nextLine();
		 boolean blnExists = cs.containsKey(courseNo);
		 System.out.println(blnExists);
		return blnExists;
	}
	
	private void save() {
		StudentDao dbutil = StudentDao.getInstance();
		dbutil.update();
	}
	private void save2() {
		SCDao dbutil = SCDao.getInstance();
		dbutil.update();
	}
	*/
/*	
	public void addCourse(String studentNo,
			              String courseNo,
			              String courseName,  
			              int courseGrade) {
		course = new Course();
		course.setCourseNo(courseNo);     //将课程信息存入
		course.setCourseName(courseName);
		course.setCourseGrade(courseGrade);
		courseDao = CourseDao.getInstance();
		courseDao.insert(course);save();
		System.out.println(course.getCourseName()+"课程注册成功！");
		MainUI.show(studentNo);
	}
	*/
	private void save() {
		CourseDao dbutil = CourseDao.getInstance();
		dbutil.update();
	}
}
