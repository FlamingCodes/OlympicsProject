%include('header.tpl')
<div id="content">
%include('content_head.tpl', head="Sportler hinzufuegen")
    <form action="/commitathlet" method="post" enctype="multipart/form-data">
        <table>
            <tr>
            <td><label for="vorname"> Vorname: </label></td>
            <td><input id="vorname" type="text" name="vorname"/> </td>
            </tr>
            <tr>
            <td><label for="nachname"> Nachname: </label></td>
            <td><input id="nachname" type="text" name="nachname"/> </td>
            </tr>
            <tr>
            <td><label for="geschlecht"> Geschlecht: </label></td>
            <td><input type="radio" name="geschlecht" value="weiblich"> weiblich<br>
            <input type="radio" name="geschlecht" value="maennlich"> maennlich<br> </td>
            </tr>
            <tr>
            <td><h5>Bitte waehlen Sie ihre Nation aus!</h5></td>
            <td>
            <form action="select.htm">
                <p>
                <select name="nations" size="3">
                %for n in nations:   
                    <option>{{n}}</option>
                %end
                </select>
                </p>
            </form>
            </td>
            </tr>
            <tr>
            <td><label for="bild"> Bild: </label></td>
            <td><input id="bild" type="file" accept="image" name="bild"/> </td>
            </tr>

        </table>
        <input type="submit" value="submit"/>

    </form>
    </div>
    <div class="breakfloat"></div>
</div>
%include('footer.tpl')