%include('header.tpl')
        <div id="content">
        %include('content_head.tpl', head="Profil bearbeiten")
            <form action="/changebenutzer" method="post" enctype="multipart/form-data">
                <p id="login_failed>">{{message}}</p>
                <table>
                    <thead>
                    </thead>
                    <tr>
                        <td><label for="Benutzername"> Benutzername: </label></td> 
                        <td><input id="Benutzername" type="text" name="Benutzername" value="{{userdata.benutzername}}"/> </td>
                    </tr>
                    <tr>
                        <td><label for="passwort"> Passwort: </label></td> 
                        <td><input id="passwort" type="password" name="passwort" value=""/> </td>
                    </tr>
                    <tr>
                        <td><label for="vorname"> Vorname: </label></td>
                        <td><input id="vorname" type="text" name="vorname" value="{{userdata.vorname}}"/> </td>
                    </tr>
                    <tr>
                        <td><label for="nachname"> Nachname: </label></td>
                        <td><input id="nachname" type="text" name="nachname" value="{{userdata.nachname}}"/> </td>
                    </tr>
                    <tr>
                        <td><label for="geburtsdatum"> Geburtsdatum: </label></td>
                        <td><input id="geburtsdatum" type="date" name="geburtsdatum" value="{{userdata.geburtsdatum}}"/> </td>
                    </tr>
                    <tr>
                        <td><label for="geschlecht"> Geschlecht: </label></td>
                        <td><input type="radio" name="geschlecht" value="weiblich" checked="checked"> weiblich<br>
                            <input type="radio" name="geschlecht" value="maennlich"> maennlich<br> </td>
                    </tr>
                    <tr>
                        <td><label for="emailadresse"> Email Adresse: </label></td>
                        <td><input id="emailadresse" type="text" name="emailadresse" value="{{userdata.emailadresse}}"/> </td>
                    </tr>
                    <tr>
                        <td><label for="ort"> Ort: </label></td>
                        <td><input id="ort" type="text" name="ort" value="{{userdata.ort}}"/> </td>
                    </tr>  
                    <tr>
                        <td><label for="land"> Land: </label></td>
                        <td><input id="land" type="text" name="land" value="{{userdata.land}}"/> </td>
                    </tr>    
                    <tr>
                        <td><label for="foto"> Foto: </label></td>
                        <td><input id="foto" type="file" accept="image" name="foto"/> </td>
                    </tr>
                    <tr>
                        <td><label for="user_type"> Jounalist: </label></td>
                        <td><input type="radio" name="user_type" value="Journalist"> Ja<br>
                            <input type="radio" name="user_type" value="Benutzer" checked="checked"> nein<br> </td>
                    </tr>
                </table>
                <input type="submit" value="submit"/> <br><br>
                

            </form>
            <form action="/loescheprofil" method="post" enctype="multipart/form-data">
                <table>
                    <tr>
                        <td><label for="passwort">Passwort: </label></td> 
                        <td><input id="passwort" type="password" name="passwort" value=""/> </td>
                    </tr>    
                </table>
                <input type="submit" value="Profil loeschen"/>
            </form>
        </div>
        <div class="breakfloat"></div>
    </div>
%include('footer.tpl')
