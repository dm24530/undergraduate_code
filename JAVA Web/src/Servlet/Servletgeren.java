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

/**
 * Servlet implementation class Servletgeren
 */
@WebServlet(asyncSupported = true, urlPatterns = { "/Servletgeren" })
public class Servletgeren extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String task_state=request.getParameter("task_state");
		String id=request.getParameter("id");
		int count=0;
		try {
			count=aaa.updatestate(task_state, id);
			System.out.println(count);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if(count>0) {
			System.out.println("修改成功");
			RequestDispatcher dispatcher=request.getRequestDispatcher("Servletgenzong");
			dispatcher.forward(request, response);
		}else {
			System.out.println("修改失败");
			RequestDispatcher dispatcher=request.getRequestDispatcher("Servletgenzong");
			dispatcher.forward(request, response);
		}
		
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
