%include('header.tpl')
        <div id="content">
            %include('content_head.tpl', head="Anmelden")
            <form action="/do_login" method="post">
                %if user != "Benutzer" and user != "Journalist":
                <table>
                    <tr>
                        <td><label for="benutzername"> Benutzername: </label></td> 
                        <td><input id="benutzername" type="text" name="benutzername"/> </td>
                    </tr>
                    <tr>
                        <td><label for="passwort"> Passwort: </label></td> 
                        <td><input id="passwort" type="password" name="passwort"/> </td>
                    </tr>
                </table>
                <input type="submit" value="submit"/> 
                %end
            </form>
            %if message[0]:
                <p id="login_successful">{{message[1]}}<p>
            %else:
                <p id="login_failed">{{message[1]}}<p>
            %end
        </div>
        <div  class="breakfloat"></div>
    </div>
%include('footer.tpl')