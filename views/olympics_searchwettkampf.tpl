%include('header.tpl')
		<div id="content">
            %include('content_head.tpl', head=sport)
			<form action="/searchwettkampf" method="post">
                
                <table class="search_form">
                    <thead>
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
            </form>
            %include('datatable.tpl', path="/wettkampf")
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')
