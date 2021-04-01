<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>修改界面</title>
</head>
<body>
<form action="ServletUpdat" method="post">

<table>
<c:forEach items="${list}" var="row">
<input type="hidden" value="${row.id}" name="id">
			<tr>
				<td>用户名</td>
				<td><input type="text" value="${row.username}" name="username"></td>
			</tr>
			<tr>
				<td>用户密码</td>
				<td><input type="text" value="${row.password}" name="password"></td>
			</tr>
				<td>真实姓名</td>
				<td><input type="text" value="${row.name}" name="name"></td>
			<tr>	
				<td>性别</td>
				<td><input type="text" value="${row.sex}" name="sex"></td>
			</tr>	
				<td>出生日期</td>
				<td><input type="text" value="${row.birthday}" name="birthday"></td>
			<tr>	
				<td>角色</td>
				<td>
					<input type="text" value="${row.position}" name="position">
				</td>			
			</tr>
</c:forEach>
</table>
<input type="submit" value="提交">
</form>
</body>
</html>