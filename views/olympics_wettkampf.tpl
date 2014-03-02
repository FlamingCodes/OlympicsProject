%include('header.tpl')
		<div id="content">
        %include('content_head.tpl', head="Wettkampf")
            Name des Wettkampfs: {{userdata.benutzername}} <br/>
            Datum: {{userdata.vorname}} <br/>
            Startzeit: {{userdata.nachname}} <br/>
            Disziplin: {{userdata.geburtsdatum}} <br/>
            Bericht: {{userdata.geschlecht}} <br/>
            Benutzerkommentar: {{userdata.emailadresse}} <br/>
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')