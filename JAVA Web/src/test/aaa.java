package test;   //操作方法

import java.sql.SQLException;
import java.util.List;

import javax.sql.DataSource;

import org.apache.commons.dbutils.QueryRunner;
import org.apache.commons.dbutils.handlers.BeanHandler;
import org.apache.commons.dbutils.handlers.BeanListHandler;

import com.mchange.v2.c3p0.ComboPooledDataSource;

import aaa.User;
import aaa.Usertask;
import testbbb.C3p0Utils;

public class aaa {
	private static DataSource sc=null;
	static {
		ComboPooledDataSource date= new ComboPooledDataSource("abc");
		sc=date;
	}
	private static QueryRunner ru=new QueryRunner(C3p0Utils.getDataSource());
	
	
	public static List listAll() throws SQLException {  //查找全部
		String sql = "select * from t_emp";
		// 调用方法
		List list = (List) ru.query(sql, new BeanListHandler(User.class));
		System.out.println(list);
		return list;
	}
	
	public static int deleteAll(String id) throws SQLException {  //根据id删除
		
		String sql = "delete  from t_emp where Id=?";
		int count=ru.update(sql,id);
		return count;
	}
	
	public static List selectByusername(String staff_id) throws SQLException {   //根据username查找
		
		String sql = "select * from t_task where staff_id=?";
		List list = (List) ru.query(sql, new BeanListHandler(Usertask.class),staff_id);
		return list;
	}
	public static List selectById(String id) throws SQLException {   //根据id查找
	
		String sql = "select * from t_emp where id=?";
		List list = (List) ru.query(sql, new BeanListHandler(User.class),id);
		return list;
	}
	
	public static int updateAll(String username,String password,String name,String sex,String birthday,String position,String id) throws SQLException {
		String sql = "update t_emp set username=?,password=?,name=?,sex=?,birthday=?,position=? where id=?";
		int count=ru.update(sql,username,password,name,sex,birthday,position,id);  //修改
		return count;
	}
	
	public static User login(String username,String password,String flag) {   //登录验证
		String sql="select * from t_emp where username =? and password = ? and flag =?";
		try {
			User user = ru.query(sql,new BeanHandler<User>(User.class),username,password,flag);
			return user;
		} catch (SQLException e) {
			throw new RuntimeException(e);
		}
	}
	public static int add(String username,String password,String name,String sex,String birthday,String position,String flag,String qualification,String experience, String hire_date) throws SQLException {
		String sql="insert into t_emp(username,password,name,sex,birthday,position,flag,qualification,experience,hire_date) values(?,?,?,?,?,?,?,?,?,?)";
			int count=ru.update(sql,username,password,name,sex,birthday,position,flag,qualification,experience,hire_date);
			return count; //插入
	}
	public static List showtesk() throws SQLException {  //查找task表全部
		String sql = "select * from t_task";
		// 调用方法
		List list = (List) ru.query(sql, new BeanListHandler(Usertask.class));
		System.out.println(list);
		return list;
	}
	public static int addtask(String task_name,String task_begin_time,String task_end_time,String task_description,String task_state,String staff_id,String emp_id) throws SQLException {
		String sql="insert into t_task(task_name,task_begin_time,task_end_time,task_description,task_state,staff_id,emp_id) values(?,?,?,?,?,?,?)";
			int count=ru.update(sql,task_name,task_begin_time,task_end_time,task_description,task_state,staff_id,emp_id);
			return count;
	}
	public static List showwei(String s) throws SQLException {  //查找全部未完成
		String sql = "select * from t_task where task_state=?";
		// 调用方法
		List list = (List) ru.query(sql, new BeanListHandler(Usertask.class),s);
		System.out.println(list);
		return list;
	}
	public static List selectBytaskId(String id) throws SQLException {   //根据id查找
		
		String sql = "select * from t_task where id=?";
		List list = (List) ru.query(sql, new BeanListHandler(Usertask.class),id);
		return list;
	}
	public static int updatestate(String task_state,String id) throws SQLException {
		String sql = "update t_task set task_state=? where id=?";
		int count=ru.update(sql,task_state,id);  //修改
		return count;
	}
	public static int updatetask(String task_name,String task_begin_time,String task_end_time,String task_description,String task_state,String id) throws SQLException {
		String sql = "update t_task set task_name=?,task_begin_time=?,task_end_time=?,task_description=?,task_state=? where id=?";
		int count=ru.update(sql,task_name,task_begin_time,task_end_time,task_description,task_state,id);  //修改
		return count;
	}
	public static List selectBytasktime(String task_begin_time,String task_end_time) throws SQLException {   //根据时间查找
		
		String sql = "select * from t_task where task_begin-time>? task_begin_time<?";
		List list = (List) ru.query(sql, new BeanListHandler(Usertask.class),task_begin_time,task_end_time);
		return list;
	}
}
