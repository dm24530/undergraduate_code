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

//删除 操作

@WebServlet("/ServletController")
public class ServletController extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
   
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// TODO Auto-generated method stub
		String id=req.getParameter("id");
		System.out.println(id);
		aaa a=new aaa();
		int count=0;
		try {
			count=a.deleteAll(id);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		if(count>0) {
			System.out.println("删除成功");
			RequestDispatcher dispatcher=req.getRequestDispatcher("ControllerServlet");
			dispatcher.forward(req, resp);
		}else {
			System.out.println("删除失败");
			RequestDispatcher dispatcher=req.getRequestDispatcher("ControllerServlet");
			dispatcher.forward(req, resp);
		}
		
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
