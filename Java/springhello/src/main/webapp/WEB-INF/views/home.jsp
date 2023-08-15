<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
 <body>
	<h1>User List</h1>
 
	<c:forEach items="${userList}" var="user">
		<br> ${user.name} <br />
	</c:forEach>
 
 </body>
</html>