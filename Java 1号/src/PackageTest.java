//package student;
class Student1{
	public Student1(){
		System.out.println("this is a student.");
	}
}
//package course;
class Course{
	public Course(){
		System.out.println("this is a course.");
	}
} 
//package teacher;
class Teacher{
	public Teacher(){
		System.out.println("this is a teacher.");
	}
}
//import teacher.*;
//import course.*;
//import student.*;
public class PackageTest{
	public static void main(String[] args){
		Student1 st = new Student1();
		Teacher te = new Teacher();
		Course cs = new Course();
	}
}
