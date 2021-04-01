<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>IT科技任务管理系统</title>

</head>
<body>

	<table>
	<tr>
		<td>姓名</td>
		<td>性别</td>
		<td>入职时间</td>
		<td>职位</td>
		<td>操作</td>
	</tr>
		<c:forEach items="${list}" var="row">
			<tr>
				<td>${row.name}</td>
				<td>${row.sex}</td>
				<td>${row.hire_date}</td>
				<td>${row.position}</td>			
				<td>
 					<a href="<c:url value="/ServletUpdate?id=${row.id}"/> " >修改</a>
 					<a href="<c:url value="/ServletController?id=${row.id}"/>" >删除</a>
				</td>
			</tr>
		</c:forEach>
	</table>
	
</body>
</html>