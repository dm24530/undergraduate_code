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
		<td>开始时间</td>
		<td>结束时间&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>
		<td>任务描述</td>
		<td>任务状态</td>
		<td>员工id</td>
		<td>主管id</td>
	</tr>
		<c:forEach items="${list}" var="row">
			<tr>
				<td>${row.task_name}</td>
				<td>${row.task_begin_time}</td>
				<td>${row.task_end_time}</td>
				<td>${row.task_description}</td>
				<td>${row.task_state}</td>
				<td>${row.staff_id}</td>	
				<td>${row.emp_id}</td>			
				<td>
<%--  					<a href="<c:url value="/ServletUpdate?id=${row.id}"/> " >修改</a> --%>
<%--  					<a href="<c:url value="/ServletController?id=${row.id}"/>" >删除</a> --%>
				</td>
			</tr>
		</c:forEach>
	</table>
</body>
</html>