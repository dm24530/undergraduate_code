package Servlet;

import java.io.IOException;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import test.aaa;

/**
 * Servlet implementation class Servletzhidingrenwu
 */
@WebServlet(asyncSupported = true, urlPatterns = { "/Servletzhidingrenwu" })
public class Servletzhidingrenwu extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String task_name=request.getParameter("task_name");
		String task_begin_time=request.getParameter("task_begin_time");
		String task_end_time=request.getParameter("task_end_time");
		String task_description=request.getParameter("task_description");
		String task_state=request.getParameter("task_state");
		String staff_id=request.getParameter("staff_id");
		String emp_id=request.getParameter("emp_id");
		int count=0;
		try {
			count=aaa.addtask(task_name, task_begin_time, task_end_time, task_description, task_state,staff_id,emp_id);
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		System.out.println(count);
		if(count>0) {
			response.getWriter().print("恭喜你添加成功，3秒后自动跳转");
			response.setHeader("refresh", "3;url=zhidingrenwu.jsp");
		}else {
			response.getWriter().print("添加失败，3秒后自动跳转");
			response.setHeader("refresh", "3;url=zhidingrenwu.jsp");
		}
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
