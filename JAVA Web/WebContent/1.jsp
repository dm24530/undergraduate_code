<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>用户登录</title>
<style type="text/css">
 		body{ 
 			background:url("img/timg.jpg"); 
 		} 
 		h3{ 
			margin-top:300px; 
 			margin-left:300px;        
 		} 
 		#outer{ 
			margin-left:200px; 
 			width:750px; 
 		} 
 		span{ 
 			color:#ff0000; 
 		} 
 		div{ 
			height:20px; 
 			margin-bottom:10px; 
 		} 
 		.ch{ 
 			width:80px; 
 			text-align:right; 
 			float:left; 
 		} 
 		.ip{ 
 			width:500px;
 			float:left; 
 		} 
 		.ip>input{ 
 			margin-right:20px;		 
 		}
 		#bt{ 
 			margin-left:100px; 
 		} 
 		#bt>input{ 
 			margin-right:30px; 
 		} 
 		#cd{ 
 			margin-left: 125px; 
 		}
	</style>
</head>
<body>

	<form action="ServletLogin" method="post">
		<font size="90" color="red">IT科技</font>
		<h3>任务管理系统</h3>
		<div id="outer">
		<div>
			<div class="ch">用户名：</div>
			<div class="ip">
				<input type="text" name="username" "/>
			</div>
		</div>
		<div>
			<div class="ch">密码：</div>
			<div class="ip">
				<input type="text" name="password">
			</div>
		</div>
		<div>
			<select id="cd" name="flag">
    			<option value="2">主管</option>
    			<option value="3">员工</option>
    			<option value="1">管理员</option>
			</select>
			
		</div>
		<div id="bt">
			<input type="reset" value="重置"/>
			<input type="submit" value="登录"/>
		</div>
		
		</div>
	</form>
</body>
</html>