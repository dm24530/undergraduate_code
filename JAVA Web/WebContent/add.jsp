<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<form action="ServletAdd" method="post">

<table>
			<tr>
				<td>用户名</td>
				<td><input type="text" name="username"></td>
			</tr>
			<tr>
				<td>用户密码</td>
				<td><input type="text"  name="password"></td>
			</tr>
				<td>真实姓名</td>
				<td><input type="text" name="name"></td>
			<tr>	
				<td>性别</td>
				<td><input type="text" name="sex"></td>
			</tr>	
				<td>出生日期</td>
				<td><input type="text" name="birthday"></td>
			<tr>	
				<td>角色</td>
				<td>
					<input type="text" name="position">
				</td>			
			</tr>
			<tr>	
				<td>学历</td>
				<td>
					<input type="text" name="qualification">
				</td>			
			</tr>
			<tr>	
				<td>经历</td>
				<td>
					<input type="text" name="experience">
				</td>			
			</tr>
			<tr>	
				<td>职位</td>
				<td>
					<input type="text" name="flag">
				</td>			
			</tr>
			<tr>	
				<td>入职时间</td>
				<td>
					<input type="text" name="hire_date">
				</td>			
			</tr>
</table>
<input type="submit" value="提交">
</form>
</body>
</html>