%include('header.tpl')
		<div id="content">
        %include('content_head.tpl', head=bericht.ueberschrift)
            von {{bericht.author}}<br/>
            <br/>
            {{bericht.bericht}}
		</div>
        <div class="breakfloat"></div>
	</div>
%include('footer.tpl')