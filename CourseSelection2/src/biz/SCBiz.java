package biz;

import view.CourseSelection;
import view.MainUI;
import dao.*;
import entity.*;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.util.*;
import dao.*;

public class SCBiz {
	StudentDao studentDao;
	CourseDao coursedao;
	SCDao scDao;
	Course course;
	private SC sc;
	private Student student;
	private HashMap<String, IEntity> cs;
	private HashMap<String, IEntity> scb;
	private ArrayList<Course> selectedCourses;
	private HashMap<String,ArrayList> scs;
	Scanner scanner = new Scanner(System.in);
	
	public void judge(String studentNo){
		studentDao = StudentDao.getInstance();
		student = (Student) studentDao.getEntity(studentNo);

		
			System.out.println("1-选课；2-退选；3-个人已选课程情况查看；4-全部已选课程情况查看；0-返回主界面");
			System.out.println("请输入你的选择：");
			Scanner in = new Scanner(System.in);
			String s = in.nextLine();
			if("1".equals(s) || "2".equals(s)) {
			switch (s) {
			case "1": //选课操作
			   addCourse(studentNo);
			   break;
			case "2": //退选操作
				/*
				Scanner scanner1 = new Scanner(System.in);
				System.out.println("请输入课程编号：");
				String courseNo1 = scanner1.nextLine();
			    exitRace(studentNo,courseNo1);
			    break;
			    */
			}
		  }else if("3".equals(s)) {
			  selfShowSeleceCourse(studentNo); 
		  }else if("4".equals(s)) {
			  showSeleceCourse(); 
		  }else if("0".equals(s)) {
			  MainUI.show(studentNo); 
		  } else {
			System.out.println("请注意，学院填写错误！");
			CourseSelection.show(studentNo);
		}
	}
	/*
	 * 选课操作
	 */
	private void addCourse(String studentNo) {
		selectedCourses= new ArrayList();
		scDao=SCDao.getInstance();
		showAllCourse();
		coursedao=CourseDao.getInstance();
		
		Scanner ins = new Scanner(System.in);
		System.out.println("请输入课程编号：");
		String courseNo = ins.nextLine();
		if(judgeCourse(courseNo)==true) {
			
		
		course=new Course();
		sc = new SC();
		course = (Course) coursedao.getEntity(courseNo);
		sc=(SC) SCDao.getInstance().getEntity(studentNo);
		sc.getCourseInformation().add(course);
		//selectedCourses.add(course);
//          sc.setStudentNo(studentNo);     //将课程信息存入
//          sc.setCourseInformation(selectedCourses);
          
         // scDao = SCDao.getInstance();
          scDao.insert(sc);
            save2();
          System.out.println(course.getCourseName()+"选择成功！");
          judge(student.getStudentNo());
          }else {
        	  System.out.println("所选科目不存在，请重新输入");
        	  addCourse(studentNo);
          }
}
	/*
	 * 退选操作
	 */
	private void exitRace(String studentNo,
            String courseNo) {
		scDao = SCDao.getInstance();
		scb = scDao.getAllEntities();
		Set<String> keySet = scb.keySet();
		scb.remove(courseNo);
		System.out.println(sc.getCourseNo()+"课程退选成功！");
		save2();
		MainUI.show(studentNo);
		/*
		Scanner in = new Scanner(System.in);
		String id = in.next();	
		if(!id.equals("end")) {			
			Course cr = map2.get(id);	
			courses.remove(cr);		
			map2.remove(id);		
			System.out.println("移除成功");
		}
*/

	}
	/*
	 * 课程情况查看
	 */
	private void showAllCourse() {
		
		coursedao = CourseDao.getInstance();
		cs = coursedao.getAllEntities();
		Set<String> keySet = cs.keySet();
		System.out.println("个人选课信息：");
		Iterator it = keySet.iterator();
		while(it.hasNext()) {
			Object key = it.next();
			Course value = (Course)cs.get(key);
			System.out.println("课程编号："+value.getCourseNo()+","+"课程名称："+value.getCourseName()+","+"课程学分："+value.getCourseGrade());
		}
		
	}
	/*
	 * 所有已选课程情况查看
	 */
	private void showSeleceCourse() {
		coursedao = CourseDao.getInstance();
		cs = coursedao.getAllEntities();
		scDao = SCDao.getInstance();
		scb = scDao.getAllEntities();
		Set<String> keySet = scb.keySet();
		System.out.println("所有的已选课程信息：");
		Iterator it = keySet.iterator();
		while(it.hasNext()) {
			Object key = it.next();
			SC value = (SC)scb.get(key);
			System.out.println(value.getStudentNo()+","+value.getCourseInformation().get(0));
		}
		judge(student.getStudentNo());
	}
	/*
	 * 个人已选课程情况查看
	 */
	private void selfShowSeleceCourse(String studentNo) {
		coursedao = CourseDao.getInstance();
		cs = coursedao.getAllEntities();
		scDao = SCDao.getInstance();
		scb = scDao.getAllEntities();
		Set<String> keySet = scb.keySet();
		System.out.println("所有的已选课程信息：");
		Iterator it = keySet.iterator();
		while(it.hasNext()) {
			Object key = it.next();
			SC value = (SC)scb.get(key);
			if(studentNo.equals(value.getStudentNo())) {
			System.out.println(value.getStudentNo()+","+value.getCourseInformation().get(0));
		    }
	    }
		judge(student.getStudentNo());
	}
	/*
	 * 判断课程是否存在
	 */
	public boolean judgeCourse(String courseNo) {
		coursedao = CourseDao.getInstance();
		cs = coursedao.getAllEntities();
		 boolean blnExists = cs.containsKey(courseNo);
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
}
