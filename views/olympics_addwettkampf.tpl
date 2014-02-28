%include('header.tpl')
		<div id="content">
			<form action="/commitwettkampf" method="post" enctype="multipart/form-data">
                <table>
                    <thead>
                        <tr>
                            <th><u>Wettkampf:</u></th>
                        </tr>
                    </thead>
                    <tr>
                        <td><label for="name"> Wettkampf: </label></td> 
                        <td><input id="name" type="text" name="name"/> </td>
                    </tr>
                    <tr>
                        <td><label for="datum"> Datum: </label></td>
                        <td><input id="datum" type="date" name="datum"/> </td>
                    </tr>
                    <tr>
                        <td><label for="startzeit"> Startzeit: </label></td>
                        <td><input id="startzeit" type="time" name="startzeit"/> </td>
                    </tr>
                    <tr>
                        <td><label for="disziplin"> Disziplin: </label></td>
                        <td><input id="disziplin" type="text" name="disziplin"/> </td>
                    </tr>
					<tr>
                        <td><label for="foto"> Foto: </label></td>
                        <td><input id="foto" type="file" accept="image" name="foto"/> </td>
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

            </form>
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')
