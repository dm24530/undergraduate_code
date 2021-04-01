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

import dao.CourseDao;
import dao.SCDao;
import dao.StudentDao;
import entity.Course;
import entity.SC;
import entity.Student;
import view.MainUI;

public class SCBiz {
	static StudentDao studentDao;
	static CourseDao coursedao;
	static SCDao scDao;
	private SC sc;
	private static Student student;
	private ArrayList<String> al;
	
	static Scanner scanner = new Scanner(System.in);
	
	public static void judge(String studentNo){
		studentDao = StudentDao.getInstance();
		student = (Student) studentDao.getEntity(studentNo);

			System.out.println("1-选课；2-退选；3-已选课程情况查看；0-返回主界面");
			System.out.println("请输入你的选择：");
			Scanner in = new Scanner(System.in);
			String s = in.nextLine();
			if("1".equals(s) || "2".equals(s)) {
			switch (s) {
			case "1": //选课操作
			   CourseBiz.selection(studentNo);
			   break;
			case "2": //退选操作
				CourseBiz.exitRace(studentNo);
			}
		  }else if("3".equals(s)) {   //3-已选课程情况查看
			  File file = new File("sc1.txt"); 
			  CourseBiz.getTxt(file,studentNo);
		  }else if("0".equals(s)) {
			  MainUI.show(studentNo); 
		  }
	}
}
