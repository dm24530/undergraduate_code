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


@WebServlet(asyncSupported = true, urlPatterns = { "/Servletyuangongxiugai" })
public class Servletyuangongxiugai extends HttpServlet {
	private static final long serialVersionUID = 1L;

	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String id=request.getParameter("id");
		String task_name=request.getParameter("task_name");
		String task_begin_time=request.getParameter("task_begin_time");
		String task_end_time=request.getParameter("task_end_time");
		String task_description=request.getParameter("task_description");
		String task_state=request.getParameter("task_state");
		int count=0;
		try {
			count=aaa.updatetask(task_name,task_begin_time,task_end_time, task_description,task_state,id);
			System.out.println(count);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		if(count>0) {
			System.out.println("修改成功");
			RequestDispatcher dispatcher=request.getRequestDispatcher("Servletyuangong");
			dispatcher.forward(request, response);
		}else {
			System.out.println("修改失败");
			RequestDispatcher dispatcher=request.getRequestDispatcher("Servletyuangong");
			dispatcher.forward(request, response);
		}
		
	}

	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
