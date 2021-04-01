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
<form action="Servletyuangongxiugai" method="post">

<table>
<c:forEach items="${list}" var="row">
			<input type="hidden" value="${row.id}" name="id">
			<tr>
				<td>任务名称</td>
				<td><input type="text" value="${row.task_name}" name="task_name"></td>
			</tr>
			<tr>
				<td>任务开始时间</td>
				<td><input type="text" value="${row.task_begin_time}" name="task_begin_time"></td>
			</tr>
				<td>任务结束时间</td>
				<td><input type="text" value="${row.task_end_time}" name="task_end_time"></td>
			<tr>	
				<td>任务描述</td>
				<td><input type="text" value="${row.task_description}" name="task_description"></td>
			</tr>	
				<td>任务状态</td>
				<td><input type="text" value="${row.task_state}" name="task_state"></td>
			
</c:forEach>
</table>
<input type="submit" value="提交">
</form>
</body>
</html>