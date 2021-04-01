package view;

import java.util.Scanner;

public class MainUI {
	
	public static void show(String studentNo) {
		System.out.println("1-注册；2-修改密码；3-注册课程；4-选课；5-登录；0-退出");
		System.out.println("请输入你的选择：");
		Scanner scanner = new Scanner(System.in);
		String option = scanner.nextLine();
		if("1".equals(option)||"2".equals(option)||"3".equals(option)||"4".equals(option)||"5".equals(option)) {
		switch (option) {
		case "1":
			RegisterUI.show();
			break;
		case "2":
			ModifyPasswordUI.show(studentNo);
			break;
		case "3":
			CourseSelection.addcourse(studentNo);	
		case "4":
			CourseSelection.show(studentNo);
			break;
		case "5":
			LoginUI.show();
			break;
			}
		}else if("0".equals(option)) {
				System.out.println("退出操作系统");
			}
	}
}
