			<ul>
				<li class="lh">Sportler</li>
					<li><a href="/search_athlet">Athleten</a></li>
                    %if user == "Journalist":
                        <li><a href="add_athlet">Athleten hinzufügen</a></li>
                    %end
				<li class="lh">Wettkampf</li>
					<li><a href="/searchwettkampf">Wettkampf</a></li>
                    %if user == "Journalist":
                        <li><a href="menu4">Wettkampfbericht hinzufügen</a></li>
                        <li><a href="/add_wettkampf">Wettkampf hinzufügen</a></li>
                    %end
                    %if (user == "Journalist" ) or (user == "Benutzer"):
                        <li><a href="menu5">Benutzerkommentar hinzufügen</a></li>
                    %end
				<li class="lh">Benutzerprofil</li>
                    %if user == "Journalist":
                        <li><a href="menu7">Benutzerprofil</a></li>
                        <li><a href="menu9">Profil bearbeiten</a></li>
                    %end
                    %if (user != "Journalist" ) and (user != "Benutzer"):
                        <li><a href="menu8">Anmelden</a></li>
                        <li><a href="/add_benutzer">Registrieren</a></li>
                    %end
				<li class="lh">Medaillen</li>
					<li><a href="menu11">Medaillenspiegel</a></li>
			</ul>
