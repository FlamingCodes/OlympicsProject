%include('header.tpl')
		<div id="content">
            Benutzer hinzugefuegt: <br/>
            ID: {{userdata.id}} <br/>
            Benutzername: {{userdata.benutzername}} <br/>
            Vorname: {{userdata.vorname}} <br/>
            Nachname: {{userdata.nachname}} <br/>
            Geschlecht: {{userdata.geschlecht}} <br/>
            Emailadresse: {{userdata.emailadresse}} <br/>
            Ort: {{userdata.ort}} <br/>
            Land: {{userdata.land}} <br/>
            Journalist: {{userdata.user_name}} <br/>
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')