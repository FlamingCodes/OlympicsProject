%include('header.tpl')
		<div id="content">
        %include('content_head.tpl', head=bericht.ueberschrift)
            von {{bericht.author}}<br/>
            <br/><p>
            {{bericht.bericht}}</p>
            <br/>
        %include('content_head', head="Kommentare")
        %if user == "Benutzer" or user == "Journalist":
        <form action="/bericht/{{bericht.id}}" method="post">
            <textarea name="kommentar"></textarea>
            <input type="submit"/>
        </form>
        %end
        %include('datatable.tpl', path="")
		</div>
        <div class="breakfloat"></div>
	</div>
%include('footer.tpl')