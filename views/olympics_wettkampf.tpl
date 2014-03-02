%include('header.tpl')
		<div id="content">
        %include('content_head.tpl', head="Wettkampf")
            Name des Wettkampfs: {{wettkampfdata.name}} <br/>
            Datum: {{wettkampfdata.datum}} <br/>
            Startzeit: {{wettkampfdata.startzeit}} <br/>
            Disziplin: {{wettkampfdata.disziplin}} <br/>
            <br/>
            %include('content_head.tpl', head="Berichte")
            %if user == "Journalist":
                <span class="action"><a href="/addreport/{{wettkampfdata.id}}">>>neuen Bericht erstellen</a></span>
                <br/>
            %end
            %for b in berichte:
                <a href="/bericht/{{b.id}}">{{b.ueberschrift}}</a><br/>
            %end
            <br/>
            %include('content_head.tpl', head="Teilnehmer")
            %if user == "Journalist":
                <span class="action"><a href="/add_athlet_to_contest/{{wettkampfdata.id}}">>>Teilnehmer hinzufügen</a></span>
                <span class="action"><a href="/remove_athlet_from_contest/{{wettkampfdata.id}}">>>Teilnehmer entfernen</a></span>
                <br/>
            %end
            %include('datatable.tpl', path="/sportlerprofil")
		</div>
        <div class="breakfloat"></div>
	</div>
%include('footer.tpl')