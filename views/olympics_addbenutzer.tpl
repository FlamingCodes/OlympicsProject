%include('header.tpl')
        <div id="content">
        %include('content_head.tpl', head="Registieren")
            <form action="/commitbenutzer" method="post" enctype="multipart/form-data">
                <table>
                    <thead>
                    </thead>
                    <tr>
                        <td><label for="benutzername"> Benutzername: </label></td> 
                        <td><input id="benutzername" type="text" name="benutzername"/> </td>
                    </tr>
                     <tr>
                        <td><label for="passwort"> Passwort: </label></td> 
                        <td><input id="passwort" type="password" name="passwort"/> </td>
                    </tr>
                    <tr>
                        <td><label for="vorname"> Vorname: </label></td>
                        <td><input id="vorname" type="text" name="vorname"/> </td>
                    </tr>
                    <tr>
                        <td><label for="nachname"> Nachname: </label></td>
                        <td><input id="nachname" type="text" name="nachname"/> </td>
                    </tr>
                    <tr>
                        <td><label for="geburtsdatum"> Geburtsdatum: </label></td>
                        <td><input id="geburtsdatum" type="date" name="geburtsdatum"/> </td>
                    </tr>
                    <tr>
                        <td><label for="geschlecht"> Geschlecht: </label></td>
                        <td><input type="radio" name="geschlecht" value="weiblich"> weiblich<br>
                            <input type="radio" name="geschlecht" value="maennlich"> maennlich<br> </td>
                    </tr>
                    <tr>
                        <td><label for="emailadresse"> Email Adresse: </label></td>
                        <td><input id="emailadresse" type="text" name="emailadresse"/> </td>
                    </tr>
                    <tr>
                        <td><label for="ort"> Ort: </label></td>
                        <td><input id="ort" type="text" name="ort"/> </td>
                    </tr>  
                    <tr>
                        <td><label for="land"> Land: </label></td>
                        <td><input id="land" type="text" name="land"/> </td>
                    </tr>    
                    <tr>
                        <td><label for="foto"> Foto: </label></td>
                        <td><input id="foto" type="file" accept="image" name="foto"/> </td>
                    </tr>
                    <tr>
                        <td><label for="journalist"> Jounalist: </label></td>
                        <td><input type="radio" name="journalist" value="ja"> Ja<br>
                            <input type="radio" name="journalist" value="nein"> nein<br> </td>
                    </tr>
                </table>
                <input type="submit" value="submit"/> 

            </form>
        </div>
        <div class="breakfloat"></div>
    </div>
%include('footer.tpl')
