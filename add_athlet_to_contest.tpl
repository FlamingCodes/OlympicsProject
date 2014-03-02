%include('header.tpl')
		<div id="content">
            %include('content_head.tpl', head="Sportler zu '" + wettkampfname + "' hinzufuegen")
            <span class="action">"Zum hinzufügen eines Sportlers den Link in der Spalte ID betätigen."</span>
            <br/>
            %include('datatable.tpl', path ="/add_athlet_to_contest/" + wettkampf_id)
		</div>
		<div class="breakfloat"></div>
        </div>
%include('footer.tpl')