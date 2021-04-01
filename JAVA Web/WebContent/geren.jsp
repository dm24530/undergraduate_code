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
<form action="Servletgeren" method="post">

<table>
<c:forEach items="${list}" var="row">
			<input type="hidden" value="${row.id}" name="id">
			<tr>
				<td>任务名称</td>
				<td>${row.task_name}</td>
			</tr>
			<tr>
				<td>任务开始时间</td>
				<td>${row.task_begin_time}</td>
			</tr>
				<td>任务结束时间</td>
				<td>${row.task_end_time}</td>
			<tr>	
				<td>任务描述</td>
				<td>${row.task_description}</td>
			</tr>	
				<td>任务状态</td>
				<td><input type="text" value="${row.task_state}" name="task_state"></td>
			<tr>	
				<td>员工id</td>
				<td>
					${row.staff_id}
				</td>			
			</tr>
</c:forEach>
</table>
<input type="submit" value="提交">
</form>
</body>
</html>