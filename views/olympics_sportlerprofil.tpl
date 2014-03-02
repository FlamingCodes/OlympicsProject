%include('header.tpl')
		<div id="content">
        %include('content_head.tpl', head="Sportlerprofil")
            Benutzername: {{userdata.benutzername}} <br/>
            Vorname: {{userdata.vorname}} <br/>
            Nachname: {{userdata.nachname}} <br/>
            Geburtsdatum: {{userdata.geburtsdatum}} <br/>
            Geschlecht: {{userdata.geschlecht}} <br/>
            Emailadresse: {{userdata.emailadresse}} <br/>
            Ort: {{userdata.ort}} <br/>
            Land: {{userdata.land}} <br/>
            Benutzertyp: {{userdata.user_name}} <br/>
		</div>
        %include('datatable.tpl', path="/wettkampf")
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')
