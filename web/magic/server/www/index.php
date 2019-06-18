<?php
	if(isset($_POST['send'])){
		if (md5('QNKCDZO') == md5($_POST['pass'])){
			echo "CTF{E@zy_M@gick_md5}";
		}else{
			echo "Пароль не верный";
		}
	}



?>

<!DOCTYPE html>
<html>
<head>
	<title>Login</title>
</head>
<body>
	<h3> Панель администратора</h3>
	<form action="" method="POST">
		<input type="password" name="pass" placeholder="Введите пароль">
		<input type="submit" name="send" value="Войти">
	</form>
</body>
</html>