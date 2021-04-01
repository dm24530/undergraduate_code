package entity;

import java.util.ArrayList;

public class SC implements IEntity {
	private String studentNo;
	private StringBuffer courseNo;
	private int grade;
	private ArrayList<Course> courseInformation;
	
	public String getStudentNo() {
		return studentNo;
	}
	public void setStudentNo(String studentNo) {
		this.studentNo = studentNo;
	}
	public StringBuffer getCourseNo() {
		return courseNo;
	}
	public void setCourseNo(StringBuffer stringBuffer) {
		this.courseNo = stringBuffer;
	}
	public int getGrade() {
		return grade;
	}
	public void setGrade(int grade) {
		this.grade = grade;
	}
	public void setCourseInformation(ArrayList courseInformation) {
		// TODO Auto-generated method stub
		this.courseInformation=courseInformation;
	}
	public ArrayList<Course> getCourseInformation() {
		// TODO Auto-generated method stub
		return courseInformation;
	}
	
}
