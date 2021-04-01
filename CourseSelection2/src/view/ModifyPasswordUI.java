package view;
import biz.*;
import dao.SCDao;
import dao.StudentDao;
import entity.SC;
import entity.Student;

import java.*;
import java.util.HashMap;
import java.util.Scanner;
public class ModifyPasswordUI {
	public static void show(String studentNo) {
		 
		StudentDao studentDao;
		HashMap<String, Student> students;
	    Student student;
		
		Scanner scanner = new Scanner(System.in);
		System.out.println("请输入原密码：");
		String password = scanner.nextLine();
		System.out.println("请输入改正后的密码：");
		String firstPasswd = scanner.nextLine();
		System.out.println("请再次输入密码：");
		String secondPasswd = scanner.nextLine();
		StudentBiz sc = new StudentBiz();
		sc.modify(
			studentNo,
			password,
			firstPasswd,
			secondPasswd);
		    
	}    
}
