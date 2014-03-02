%include('header.tpl')
		<div id="content">
        %include('content_head.tpl', head="Wettkampf")
            Name des Wettkampfs: {{wettkampfdata.name}} <br/>
            Datum: {{wettkampfdata.datum}} <br/>
            Startzeit: {{wettkampfdata.startzeit}} <br/>
            Disziplin: {{wettkampfdata.disziplin}} <br/>
            Bericht: {{wettkampfdata.bericht}} <br/>
            Benutzerkommentar: {{wettkampfdata.benutzerkommentar}} <br/>
            %include('datatable.tpl', path="/sportlerprofil")
		</div>
        <div class="breakfloat"></div>
	</div>
%include('footer.tpl')