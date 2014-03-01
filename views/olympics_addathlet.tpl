%include('header.tpl')
<div id="content">
<form action="/commitathlet" method="post" enctype="multipart/form-data">
<table>
<thead>
<tr>
<th><u>Sportler:</u></th>
</tr>
</thead>
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
<tr>
<td><label for="bild"> Bild: </label></td>
<td><input id="bild" type="file" accept="image" name="bild"/> </td>
</tr>

</table>
<input type="submit" value="submit"/>

</form>
</div>
<div class="breakfloat"></div>
</div>
%include('footer.tpl')