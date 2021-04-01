<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
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
        .right ul{
            list-style: none;
            width:700px;
            height:400px;
            text-align:center;
        }
        .right li{
            width:700px;
            height:250px;
            margin-top: 10px;
            float: left;
        }
        #z{
            display: none;
            margin: 0 auto;
        }
        #z ul{
            list-style: none;

            margin: 100px 0 0 200px;
        }
        #z li{
            margin: 20px;
        }
        #c{
            display: none;
            margin: 0 auto;
        }
        #c ul{
            list-style: none;

            margin: 100px 0 0 200px;
        }
        #c li{
            margin: 20px;
        }
        #g{
            display: none;
            margin: 0 auto;
        }
        #g ul{
            list-style: none;

            margin: 100px 0 0 200px;
        }
        #g li{
            margin: 20px;
        }
        #r{
            display: none;
            margin: 0 auto;
        }
        #r ul{
            list-style: none;

            margin: 100px 0 0 200px;
        }
        #r li{
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
    <div class="header"><h1>IT科技-----员工</h1></div>
    <div class="neirong">
        <div class="left">
            <ul id="key">
                <li id="one">计划管理</li>
                <li id="two">查询计划</li>
            </ul>
        </div>
        <div class="right">
            <div id="z">
                <iframe src="Servletyuangong" frameborder="0"></iframe>
            </div>
            <div id="c">
                 <iframe src="chaxunjihua.jsp" frameborder="0"></iframe>
            </div>
        </div>
    </div>
</div>
<script>
    function $(id){
        return document.getElementById(id);
    }
    $('one').onclick=function(){
    	$('c').style.display="none";
        $('z').style.display="block";
    }
    $('two').onclick=function(){
        $('z').style.display="none";
        $('c').style.display="block";
    }
    
   </script>
</body>
</html>