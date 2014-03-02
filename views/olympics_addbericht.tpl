%include('header.tpl')
		<div id="content">
            %include('content_head.tpl', head="Wettkampfbericht anlegen")
            <br/>
            <form action="/addreport/{{bericht_id}}" method="post">
                %include('small_head.tpl', head="Überschrift")
                <input type="text" name="ueberschrift"/>
                %include('small_head.tpl', head="Bericht")
                <textarea cols="70" rows="5" name="bericht"></textarea><br/>
                <input type="submit" value="Speichern"></input>
            </form>
		</div>
		<div class="breakfloat"></div>
        </div>
%include('footer.tpl')