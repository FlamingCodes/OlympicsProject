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
				<li><a href="/search_athlet" target="menu1">Athleten</a></li>
				<li><a href="/add_athlet" target="menu2">Athleten hinzufügen</a></li>
				<li><a href="menu3" target="menu3">Menu Point 3</a></li>
				<li><a href="menu4" target="menu4">Menu Point 4</a></li>
			</ul>
		</div>
		<div id="content">
			<form action="/search_athlet" method="post">
                <table>
                    <thead>
                        <tr>
                            <th><u>Sportler:</u></th>
                        </tr>
                    </thead>
                    <tr>
                        <td><label for="id"> Vorname: </label></td>
                        <td><input id="id" type="text" name="id"/> </td>
                    </tr>
                    <tr>
                        <td><label for="vorname"> Vorname: </label></td>
                        <td><input id="vorname" type="text" name="vorname"/> </td>
                    </tr>
                    <tr>
                        <td><label for="nachname"> Nachname: </label></td>
                        <td><input id="nachname" type="text" name="nachname"/> </td>
                    </tr>
                    <tr>
                        <td><label for="geschlecht"> Geschlecht: </label></td>
                        <td><input type="radio" name="geschlecht" value="weiblich"> weiblich<br>
                            <input type="radio" name="geschlecht" value="maennlich"> maennlich<br> </td>
                    </tr>
                    <tr>
                        <td><label for="nationalitaet"> Nationalitaet: </label></td>
                        <td><input id="nationalitaet" type="text" name="nationalitaet"/> </td>
                    </tr>
                </table>
                <input type="submit" value="submit"/> 

                <table id="datatable1" class="datatable">
                    <thead><th>ID</th><th>Vorname</th><th>Nachname</th><th>Geschlecht</th><th>Nationaität</th></thead>
                    %x = 0
                    %for col in content:
                    %x+=1
                    %y= x % 2
                    %if y > 0:
                        <tr>
                            <td class="colored">{{col[0]}}</td><td class="colored">{{col[1]}}</td><td class="colored">{{col[2]}}</td><td class="colored">{{col[3]}}</td><td class="colored">{{col[4]}}</td>
                        </tr>
                    %else:
                         <tr>
                            <td>{{col[0]}}</td><td>{{col[1]}}</td><td>{{col[2]}}</td><td>{{col[3]}}</td><td>{{col[4]}}</td>
                        </tr> 
                    %end
                    %end
                </table>
            </form>
		</div>
		<div class="breakfloat"></div>
	</div>
	<div id="footer">
		<a href="impressum" target="impressum">Impressum</a>
	</div>
	</body>
</html>
