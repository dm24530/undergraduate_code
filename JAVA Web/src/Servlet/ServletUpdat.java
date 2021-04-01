package Servlet;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import test.aaa;

// 修改


@WebServlet("/ServletUpdat")
public class ServletUpdat extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		aaa a=new aaa();
		String id=req.getParameter("id");
		String username=req.getParameter("username");
		String password=req.getParameter("password");
		String name=req.getParameter("name");
		String sex=req.getParameter("sex");
		String birthday=req.getParameter("birthday");
		String position=req.getParameter("position");
		System.out.println("进入了修改");
		System.out.println(id);
		int count=0;
		try {
			count=a.updateAll(username, password, name, sex, birthday, position, id);
			System.out.println(count);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if(count>0) {
			System.out.println("修改成功");
			RequestDispatcher dispatcher=req.getRequestDispatcher("ControllerServlet");
			dispatcher.forward(req, resp);
		}else {
			System.out.println("修改失败");
			RequestDispatcher dispatcher=req.getRequestDispatcher("ControllerServlet");
			dispatcher.forward(req, resp);
		}	
	}
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
