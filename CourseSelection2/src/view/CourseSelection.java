package view;
import java.*;
import java.util.Scanner;
import biz.*;
public class CourseSelection {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		LoginUI.show();
		//show();
	}
	/*
	 * 选课操作
	 */
	public static void show(String studentNo) {
		// TODO Auto-generated method stub
		SCBiz scbiz = new SCBiz();
		scbiz.judge(studentNo);
	}
	/*
	 * 添加课程操作
	 */
	public static void addcourse(String studentNo) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("请输入课程号：");
		String courseNo = scanner.nextLine();
		System.out.println("请输入课程名称：");
		String courseName = scanner.nextLine();
		System.out.println("请输入成绩：");
		int courseGrade = Integer.parseInt(scanner.nextLine());
		CourseBiz cb = new CourseBiz();
		cb.addCourse(studentNo,
				courseNo,
				courseName, 
				courseGrade);
	}

}
