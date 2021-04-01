package Servlet;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import aaa.User;
import test.aaa;

/**
 * Servlet implementation class ServletLogin
 */
@WebServlet(asyncSupported = true, urlPatterns = { "/ServletLogin" })
public class ServletLogin extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		aaa a=new aaa();
		User user=new User();
		
		String flag=request.getParameter("flag");
		String username=request.getParameter("username");
		String password=request.getParameter("password");
		System.out.println(flag);
		System.out.println(username);
		System.out.println(password);
		int a1 = Integer.parseInt(flag);
		user=aaa.login(username,password,flag);
		
		HttpSession session = request.getSession();
		if(user!=null){
			session.setAttribute("username",username);
			if(a1==1) {
				response.sendRedirect("success1.jsp");
			}
			if(a1==2) {
				response.sendRedirect("success2.jsp");
			}
			if(a1==3) {
				response.sendRedirect("success3.jsp");
			}
			
		}else {
			request.setAttribute("msg","您输入的账号或密码或职位错误！");
			response.sendRedirect("1.jsp");
		}
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
