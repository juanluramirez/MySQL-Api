<!DOCTYPE HTML>

<html>
	<head> 
		<link rel="shortcut icon" type="image/x-icon" href="https://upload.wikimedia.org/wikipedia/en/6/62/MySQL.svg" />
		<title>Acceso</title> 
		<link rel="stylesheet" href="/static/css/perfil.css" />
	</head> 
<body>
	<h1>Base de datos: {{db}}.</h1>
	<h2>Tablas :</h2>
	<h3>{{tablas}}</h3>
	<h3>Tiene un total de: {{numero_tablas}} tablas 
	<div id="search-form">
		<form class="form-container" action="/consulta" method="post">
		<p>Datos: <input name="datos" type="text" class="search-field"/>
		<p>Tabla: <input name="tabla" type="text" class="search-field"/>
		<p>Host: <input name="host" type="text" class="search-field"/>
		<p>Usuario: <input name="user" type="text" class="search-field"/>
		<p>Contraseña: <input name="passwd" type="password" class="search-field"/>
		<p>Base de datos: <input name="db" type="text" class="search-field"/>
		<div class="submit-container">
			<input type="submit" value="Acceder" class="submit" />
		</div>
	</div> 
</body>  
</html>