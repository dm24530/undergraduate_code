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
		<td>编号</td>
		<td>密码</td>
		<td>姓名</td>
		<td>性别</td>
		<td>学历</td>
		<td>入职时间</td>
		<td>职位</td>
		<td>角色</td>
	</tr>
		<c:forEach items="${list}" var="row">
			<tr>
			<td>${row.id}</td>
			<td>${row.password}</td>
			<td>${row.name}</td>
			<td>${row.sex}</td>
				<td>${row.qualification}</td>
				<td>${row.hire_date}</td>
				<td>${row.position}</td>
				<td>${row.flag}</td>			
				
			</tr>
		</c:forEach>
	</table>
</body>
</html>