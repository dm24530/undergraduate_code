package biz;

import dao.*;
import entity.*;
import view.MainUI;

public class CourseBiz {	
	CourseDao courseDao;
	private Course course;
	
	public void addCourse(String studentNo,
			              String courseNo,
			              String courseName,  
			              int courseGrade) {
		course = new Course();
		course.setCourseNo(courseNo);     //将课程信息存入
		course.setCourseName(courseName);
		course.setCourseGrade(courseGrade);
		courseDao = CourseDao.getInstance();
		courseDao.insert(course);
		System.out.println(course.getCourseName()+"课程注册成功！");
		save();
		MainUI.show(studentNo);
	}
	private void save() {
		CourseDao dbutil = CourseDao.getInstance();
		dbutil.update();
	}
}
