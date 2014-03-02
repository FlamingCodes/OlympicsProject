%include('header.tpl')
		<div id="content">
            %include('content_head.tpl', head="Wettkampf")
			<form action="/commitwettkampf" method="post" enctype="multipart/form-data">
                <table>
                    <tr>
                        <td><label for="name"> Wettkampf: </label></td> 
                        <td><input id="name" type="text" name="name"/> </td>
                    </tr>
                    <tr>
                        <td><label for="datum"> Datum: </label></td>
                        <td><input id="datum" type="date" name="datum" value="01/01/2014" size="10" maxlength="10" minlength="10"/> </td>
                    </tr>
                    <tr>
                        <td><label for="startzeit"> Startzeit: </label></td>
                        <td><input id="startzeit" type="time" name="startzeit" value="15:30" size="5" maxlength="5" minlength="5"/> </td>
                    </tr>
                    <tr>
                        <td><label for="disziplin"> Disziplin: </label></td>
                        <td><input id="disziplin" type="text" name="disziplin"/> </td>
                    </tr>
					<tr>
                        <td><label for="foto"> Foto: </label></td>
                        <td><input id="foto" type="file" accept="image" name="foto"/> </td>
                    </tr>  
                </table>
                <input type="submit" value="submit"/> 

            </form>
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')
