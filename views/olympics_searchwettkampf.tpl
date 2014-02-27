%include('header.tpl')
		<div id="content">
			<form action="/searchwettkampf" method="post">
                <table>
                    <thead>
                        <tr>
                            <th><u>Wettkampf:</u></th>
                        </tr>
                    </thead>
                    <tr>
                        <td><label for="id"> ID: </label></td>
                        <td><input id="id" type="text" name="id"/> </td>
                    </tr>
                    <tr>
                        <td><label for="name"> Name: </label></td>
                        <td><input id="name" type="text" name="name"/> </td>
                    </tr>
                    <tr>
                        <td><label for="startzeit"> Startzeit: </label></td>
                        <td><input id="startzeit" type="text" name="startzeit"/> </td>
                    </tr>
                    <tr>
                        <td><label for="datum"> Datum: </label></td>
                        <td><input id="datum" type="text" name="datum"/></td>
                    </tr>
                    <tr>
                        <td><label for="disziplin"> Disziplin: </label></td>
                        <td><input id="disziplin" type="text" name="disziplin"/></td>
                    </tr>
                    <tr>
                        <td><label for="bericht"> Bericht: </label></td>
                        <td><input id="bericht" type="text" name="bericht"/> </td>
                    </tr>
                    <tr>
                        <td><label for="benutzerkommentar"> Benutzerkommentar: </label></td>
                        <td><input id="benutzerkommentar" type="text" name="benutzerkommentar"/> </td>
                    </tr>
                </table>
                <input type="submit" value="submit"/> 

                <table id="datatable1" class="datatable">
                    <thead><th>ID</th><th>Name</th><th>Startzeit</th><th>Datum</th><th>Disziplin</th><th>Bericht</th><th>Benutzerkommentar</th></thead>
                    %x = 0
                    %for col in content:
                    %x+=1
                    %y= x % 2
                    %if y > 0:
                        <tr>
                            <td class="colored">{{col[1]}}</td><td class="colored">{{col[2]}}</td><td class="colored">{{col[3]}}</td><td class="colored">{{col[4]}}</td><td class="colored">{{col[5]}}</td><td class="colored">{{col[6]}}</td><td class="colored">{{col[7]}}</td>
                        </tr>
                    %else:
                         <tr>
                            <td>{{col[1]}}</td><td>{{col[2]}}</td><td>{{col[3]}}</td><td>{{col[4]}}</td><td>{{col[5]}}</td><td>{{col[6]}}</td><td>{{col[7]}}</td>
                        </tr> 
                    %end
                    %end
                </table>
            </form>
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')
