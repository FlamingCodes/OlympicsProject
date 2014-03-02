			<ul id="login_state_list">
                %if user != "Journalist" and user != "Benutzer": 
                    <li class="lh">Nicht angemeldet</li>
                    <li><a href="/login">Anmelden</a></li>
                    <li><a href="/add_benutzer">Registrieren</a></li>
                %else:
                    <li class="lh">{{user_name}}</li>
                    <li><a href="/logout">Abmelden</a></li>
                    <li><a href="benutzerprofil">Benutzerprofil</a></li>
                    <li><a href="changeprofil">Profil bearbeiten</a></li>
                %end
            </ul>
            <ul>
				<li class="lh">Sportler</li>
					<li><a href="/search_athlet">Athleten</a></li>
                    %if user == "Journalist":
                        <li><a href="add_athlet">Athleten hinzufügen</a></li>
                    %end
				<li class="lh">Wettkampf</li>
					<li><a href="/select_sport">Wettkampf</a></li>
                    %if user == "Journalist":
                        <li><a href="menu4">Wettkampfbericht hinzufügen</a></li>
                        <li><a href="/add_wettkampf">Wettkampf hinzufügen</a></li>
                    %end
                    %if (user == "Journalist" ) or (user == "Benutzer"):
                        <li><a href="menu5">Benutzerkommentar hinzufügen</a></li>
                    %end
				<li class="lh">Medaillen</li>
					<li><a href="menu11">Medaillenspiegel</a></li>
			</ul>
