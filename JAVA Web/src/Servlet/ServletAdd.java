package Servlet;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import aaa.User;
import test.aaa;

/**
 * Servlet implementation class ServletAdd
 */
@WebServlet(asyncSupported = true, urlPatterns = { "/ServletAdd" })
public class ServletAdd extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		aaa a=new aaa();
		User user=new User();
		
		String flag=request.getParameter("flag");
		String username=request.getParameter("username");
		String password=request.getParameter("password");
		String sex=request.getParameter("sex");
		String name=request.getParameter("name");
		String birthday=request.getParameter("birthday");
		String position=request.getParameter("position");
		String qualification=request.getParameter("qualification");
		String experience=request.getParameter("experience");
		String hire_date=request.getParameter("hire_date");
		int count=0;
		try {
			count=a.add(username, password, name, sex, birthday, position, flag, qualification, experience,hire_date);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if(count>0) {
			response.getWriter().print("恭喜你添加成功，3秒后自动跳转");
			response.setHeader("refresh", "3;url=add.jsp");
		}else {
			response.getWriter().print("添加失败，3秒后自动跳转");
			response.setHeader("refresh", "3;url=add.jsp");
		}
	}


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
