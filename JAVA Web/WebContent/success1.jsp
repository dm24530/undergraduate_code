<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>管理员</title>
    <style type="text/css">
        *{
            margin: 0;
            padding: 0;
        }
        .zhong{
            width: 1000px;
            height: 500;
            margin: 150px auto;
            border: 5px black solid;
        }
        .header h1{
            width: 1000px;
            height: 100px;
            line-height: 100px;
            text-align: center;
        }
        .neirong{
            width: 1000px;
            height: 400px;
        }
        .left{
            float: left;
            height: 400px;
            width: 200px;
        }
        .left ul{
            list-style: none;
            width: 200px;
            height: 400px;
            text-align: center;
            border-top: 5px  black solid;
            border-right: 5px black solid;
        }
        .left li{
            margin-top: 50px;
            height: 50px;
        }
        .right{
            height: 400px;
            width: 800px;
            border-top: 5px black solid;
            float: left;
        }
        .right #show ul{
            list-style: none;
            width:700px;
            height:400px;
            text-align:center;
        }
        .right #show li{
            width:700px;
            height:250px;
            margin-top: 10px;
            float: left;
        }
        #show{
            display: none;
            margin: 0 auto;
        }
        #show ul{
            list-style: none;

            margin: 100px 0 0 200px;
        }
        #show li{
            margin: 20px;
        }
        #add{
            display: none;
            margin: 0 auto;
        }
        #add ul{
            list-style: none;

            margin: 100px 0 0 200px;
        }
        #add li{
            margin: 20px;
        }
        iframe{
        	margin: 0 0 0 5px;
        	width:795px;
        	height:395px;
        	background:#F0FFFF;
        }
    </style>
</head>
<body>
<a href="1.jsp">退出</a>
<div class="zhong">
    <div class="header"><h1>IT科技-----管理员</h1></div>
    <div class="neirong">
        <div class="left">
            <ul id="key">
                <li id="one">查看员工</li>
                <li id="two">添加员工</li>
            </ul>
        </div>
        <div class="right">

            <div id="show">
                <iframe frameborder="0" src="<c:url value='/fingAll.jsp'/>" name="top"></iframe>
                
            </div>
            <div id="add">
            	 
                 <iframe frameborder="0" src="<c:url value='/add.jsp'/>" name="top"></iframe>
            </div>
        </div>
    </div>
</div>
<script>
    function $(id){
        return document.getElementById(id);
    }
    $('one').onclick=function(){
        $('add').style.display="none";
        $('show').style.display="block";
    }
    $('two').onclick=function(){
        $('show').style.display="none";
        $('add').style.display="block";
    }
</script>
</body>
</html>