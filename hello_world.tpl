<!DOCTYPE html>
<html>
<head>
<title>
Hello World!
</title>
<head>

<body>
<p>Welcome {{username}}</p>
<ul>
%for thing in things:
<li>{{thing}}</li>
%end
</ul>
<form action="/favourite_fruit" method="POST">
What is your favourite fruite?
<input type="text" name="fruit" size=40, value="pshoo"><br>
<input type="submit" name="Submit">
</form>
</body>
</html>
