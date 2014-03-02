%include('header.tpl')
<div id="content">
<form action="/search_athlet" method="post">
<table>
<thead>
<tr>
<th><u>Sportler:</u></th>
</tr>
</thead>
<tr>
<td><label for="id"> ID: </label></td>
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
%include('datatable.tpl', path="sportlerprofil")
</form>
</div>
<div class="breakfloat"></div>
</div>
%include('footer.tpl')