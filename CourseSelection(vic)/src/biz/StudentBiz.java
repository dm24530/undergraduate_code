package biz;

import java.util.Scanner;

import dao.StudentDao;
import entity.IEntity;
import entity.Student;
import view.*;

public class StudentBiz {
	StudentDao studentDao;
	private Student student;
	/*
	 * 用户登录
	 */
	public void login(String studentNo, String studentPassword) {

		studentDao = StudentDao.getInstance();
		student = (Student) studentDao.getEntity(studentNo);
		if (student == null) {
			System.out.println("用户不存在");
			return;
		} else if (student.getStudentPassword().equals(studentPassword)) {
			studentDao = StudentDao.getInstance();
			student = (Student)studentDao.getEntity(studentNo); 
			System.out.println(student.getStudentName()+"同学你好！");
			MainUI.show(studentNo);
		} else {
			System.out.println("密码不正确");
			MainUI.show(studentNo);
		}

	}
	/*
	 * 用户注册，业务逻辑实现
	 */
	public void register(String studentNo,
			            String firstPassword, 
						String secondPassword,
						String studentName, 
						String studentGender, 
						int studentAge, 
						String studentDepartment ) {
		if(firstPassword.equals(secondPassword)) {   //判断第一次与第二次输入的密码是不是一样
			student = new Student();
			student.setStudentNo(studentNo);  //将学生信息存入
			student.setStudentPassword(firstPassword);
			student.setStudentName(studentName);
			student.setStudentGender(studentGender);
			student.setStudentAge(studentAge);
			student.setStudentDepartment(studentDepartment);
			studentDao = StudentDao.getInstance();
			studentDao.insert(student);
			System.out.println(student.getStudentName()+"同学注册成功！");
			save();
			MainUI.show(studentNo);
		}else {
			MainUI.show(studentNo);
		}
	}
	/*
	 * 用户修改密码
	 */
	public void modify(
		String studentNo, 
		String passwd,
		String firstPasswd, 
		String secondPasswd ){
		
		   studentDao = StudentDao.getInstance();
		   student = (Student)studentDao.getEntity(studentNo);      //从学生的账号来获取这个学生的信息
		   //System.out.println(student.getStudentPassword());
		   if(passwd.equals(student.getStudentPassword())) {        //判断输入的密码与这个学生的密码是不是一样
			
				if(firstPasswd.equals(secondPasswd)) {              //判断更新的新密码两次输入是否一样
					student.setStudentPassword(firstPasswd);
					System.out.println("修改成功!");
					save();
					//IEntity ientity = studentDao.getEntity(studentNo);
					
					MainUI.show(studentNo); 
					}else {
						System.out.println("两次密码不一样！请重新输入！");
						ModifyPasswordUI.show(studentNo);
					}
				}else {
					Scanner scanner = new Scanner(System.in);
					System.out.println("原密码输入错误！");
					System.out.println("1-返回主界面；2-修改密码");
					System.out.println("请输入选择：");
					
					String stu = scanner.nextLine();
					if("1".equals(stu)||"2".equals(stu)) {
						if("1".equals(stu)) {
							MainUI.show(studentNo);
						}else {
							ModifyPasswordUI.show(studentNo);
						}
					}else {
						System.out.println("请输入1或2！");
					}
				}
		}
	private void save() {
		StudentDao dbutil = StudentDao.getInstance();
		dbutil.update();
	}
}

