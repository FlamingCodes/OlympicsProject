%include('header.tpl')
		<div id="content">
            %include('content_head.tpl', head=athlet.vorname + " " + athlet.nachname)
            ID: {{athlet.id}} <br/>
            Vorname: {{athlet.vorname}} <br/>
            Nachname: {{athlet.nachname}} <br/>
            Geschlecht: {{athlet.geschlecht}} <br/>
            Nationalitaet: {{athlet.nationalitaet}} <br/>
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')