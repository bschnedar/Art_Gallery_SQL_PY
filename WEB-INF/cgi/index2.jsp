<%-- 
    Document   : index
    Created on : Oct 3, 2018, 12:26:37 PM
    Author     : Bschnedar
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ page import="java.util.*"%>
<%@ page import="java.io.*" %>
<%@ page import="java.sql.*"%

<!DOCTYPE html>
<html>
  <head>
    <title>Bank Application</title>   
  </head>
 

<body>
  <b>2. Add new art:</b>
	<form method="post" >
    		<input name="funcID" type="hidden" value="2">
		Title: <input name="title" type="text">
		</br>
		Year:  <input name="year" type="text">
		</br>
		Artist: <input name="art" type="text">
		</br>
		Caption: <input name="cap" type="text">
		</br>
		image:  <input name="image" type="text">  
		
		</br>
    	<input type="submit" value="Add">
	</form>
  </br>  
  
  

  
  

</body>
</html>




<% 
	String j_title = request.getParameter("title");
	String j_year = request.getParameter("year");
	String j_art = request.getParameter("art");
	String j_cap = request.getParameter("cap");
	String j_img = request.getParameter("image");
%>
	</br>
	
	<p> Title: <%out.println(j_title);  %>
	</br>
	YEAR: <%out.println(j_year);  %>
	</br>
	ARTIST:<%out.println(j_art);  %>
	</br>
	DESCRIPTION:<%out.println(j_cap);  %>
	</p>
 </br>
   <img  src="<%=j_img%>" border="3">

<p> HTML: <%out.println(j_img);%> </p>


<% 
try {  Class.forName("com.mysql.jdbc.Driver").newInstance(); } catch(Exception e) { out.println("can't load mysql driver"); out.println(e.toString()); } 
  %>

  <%
String url="jdbc:mysql://127.0.0.1:3306/gallery";     String id="gallery";     String pwd="eecs118";     Connection con= DriverManager.getConnection(url,id,pwd); 
 
  %>




