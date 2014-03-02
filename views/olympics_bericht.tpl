%include('header.tpl')
		<div id="content">
        %include('content_head.tpl', head=bericht.ueberschrift)
            von {{bericht.author}}<br/>
            <br/><p>
            {{bericht.bericht}}</p>
            <br/>
        %include('content_head', head="Kommentare")
        %if user == "Benutzer" or user == "Journalist":
        <form>
            <textarea></textarea>
        </form>
        %end
        %include('datatable.tpl', path="")
		</div>
        <div class="breakfloat"></div>
	</div>
%include('footer.tpl')