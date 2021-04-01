<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	<form action="Servlettianjiarenwu" method="post">

<table>
			<tr>
				<td>任务名称</td>
				<td><input type="text" name="task_name"></td>
			</tr>
			<tr>
				<td>开始时间</td>
				<td><input type="text"  name="task_begin_time"></td>
			</tr>
				<td>截至时间</td>
				<td><input type="text" name="task_end_time"></td>
			<tr>	
				<td>任务描述</td>
				<td><input type="text" name="task_description"></td>
			</tr>	
				<td>任务状态</td>
				<td><input type="text" name="task_state"></td>
</table>
<input type="submit" value="提交">
</form>
</body>
</html>