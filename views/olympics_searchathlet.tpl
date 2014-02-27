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

                <table id="datatable1" class="datatable">
                    <thead><th>ID</th><th>Vorname</th><th>Nachname</th><th>Geschlecht</th><th>Nationaität</th></thead>
                    %x = 0
                    %for col in content:
                    %x+=1
                    %y= x % 2
                    %if y > 0:
                        <tr>
                            <td class="colored">{{col[1]}}</td><td class="colored">{{col[2]}}</td><td class="colored">{{col[3]}}</td><td class="colored">{{col[4]}}</td><td class="colored">{{col[5]}}</td>
                        </tr>
                    %else:
                         <tr>
                            <td>{{col[1]}}</td><td>{{col[2]}}</td><td>{{col[3]}}</td><td>{{col[4]}}</td><td>{{col[5]}}</td>
                        </tr> 
                    %end
                    %end
                </table>
            </form>
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')
