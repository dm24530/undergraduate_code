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
	<table>
	<tr>
		<td>任务名称</td>
		<td>任务开始时间</td>
		<td>任务截至时间</td>
		<td>任务状态</td>
		<td>操作</td>
	</tr>
		<c:forEach items="${list}" var="row">
			<tr>
				<td>${row.task_name}</td>
				<td>${row.task_begin_time}</td>
				<td>${row.task_end_time}</td>
				<td>${row.task_state}</td>			
				<td>
 					<a href="<c:url value="/Servletyuangongrenwu?id=${row.id}"/> " >修改任务</a>
				</td>
			</tr>
		</c:forEach>
	</table>
</body>
</html>