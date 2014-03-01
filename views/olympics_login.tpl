%include('header.tpl')
        <div id="content">
            %include('content_head.tpl', head="Anmelden")
            <form action="/do_login" method="post">
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
            </form>
        </div>
        <div  class="breakfloat"></div>
    </div>
%include('footer.tpl')