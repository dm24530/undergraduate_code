<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="Servletzhidingrenwu" method="post">

<table>
			<tr>
				<td>任务名称</td>
				<td><input type="text" name="task_name"></td>
			</tr>
			<tr>
				<td>任务开始时间</td>
				<td><input type="text" name="task_begin_time"></td>
			</tr>
				<td>任务结束时间</td>
				<td><input type="text" name="task_end_time"></td>
			<tr>	
				<td>任务描述</td>
				<td><input type="text"  name="task_description"></td>
			</tr>	
				<td>任务状态</td>
				<td><input type="text" name="task_state"></td>
			<tr>	
				<td>员工id</td>
				<td><input type="text"  name="staff_id"></td>
			</tr>
			<tr>	
				<td>主管id</td>
				<td><input type="text"  name="emp_id"></td>
			</tr>
			
</table>
<input type="submit" value="提交">
</form>
</body>
</html>