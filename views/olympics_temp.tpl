<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">

<html>
	<head>
		<title>Olympics</title>
		<link rel="stylesheet" media="screen" href="{{ get_url('static', path='olympics.css') }}">
	</head>
	<body>
	<div id="header">
		<h1>Olympic Games - Sochi 2014</h1>
	</div>
	<div id="content_wrapper">
		<div id="menu">
			<ul>
				<li><a href="menu1" target="menu1">Menu Point 1</a></li>
				<li><a href="menu2" target="menu2">Menu Point 2</a></li>
				<li><a href="menu3" target="menu3">Menu Point 3</a></li>
				<li><a href="menu4" target="menu4">Menu Point 4</a></li>
			</ul>
		</div>
		<div id="content">
			{{content}}
		</div>
		<div class="breakfloat"></div>
	</div>
	<div id="footer">
		<a href="impressum" target="impressum">Impressum</a>
	</div>
	</body>
</html>