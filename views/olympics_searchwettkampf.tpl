%include('header.tpl')
		<div id="content">
            %include('content_head.tpl', head=sport)
			<form action="/searchwettkampf/{{sport}}" method="post">
                
                <table class="search_form">
                    <thead>
                    </thead>
                    <tr>
                        <td><label for="id"> ID: </label></td>
                        <td><input id="id" type="text" name="id"/> </td>
                    </tr>
                    <tr>
                        <td><h5>Bitte waehlen Sie ihre Sportart aus!</h5></td>
                        <td>
                            <form action="select.htm">
                                <p>
                                <select name="sportart" size="3">
                                    <option>Alpin</option>
                                    <option>Biathlon</option>
                                    <option>Bob</option>
                                    <option>Curling</option>
                                    <option>Eishockey</option>
                                    <option>Eiskunstlauf</option>
                                    <option>Eisschnelllauf</option>
                                    <option>Freestyle-Skiing</option>
                                    <option>Nordische Kombination</option>
                                    <option>Ronnrodeln</option>
                                    <option>Shorttrack</option>
                                    <option>Skeleton</option>
                                    <option>Skilanglauf</option>
                                    <option>Skispringen</option>
                                    <option>Snowboard</option>
                                </select>
                                </p>
                               </form>
                        </td>
                    </tr>
                    <tr>
                        <td><label for="name"> Name: </label></td>
                        <td><input id="name" type="text" name="name"/> </td>
                    </tr>
                    <tr>
                        <td><label for="startzeit"> Startzeit: </label></td>
                        <td><input id="startzeit" type="text" name="startzeit" value="15:30" size="5" maxlength="5" minlength="5"/> </td>
                    </tr>
                    <tr>
                        <td><label for="datum"> Datum: </label></td>
                        <td><input id="datum" type="text" name="datum" value="01/01/2014" size="10" maxlength="10" minlength="10"/></td>
                    </tr>
                    <tr>
                        <td><label for="disziplin"> Disziplin: </label></td>
                        <td><input id="disziplin" type="text" name="disziplin"/></td>
                    </tr>
                </table>
                <input type="submit" value="submit"/> 
            </form>
            %include('datatable.tpl', path="/wettkampf")
		</div>
		<div class="breakfloat"></div>
	</div>
%include('footer.tpl')
