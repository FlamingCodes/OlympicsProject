from bottle import get, post, route, run, request, view, static_file, template, response
import bottle, random, sqlite3
from userdata import Userdata
from sportlerdata import Sportlerdata
from wettkampfdata import Wettkampfdata
from bericht import Bericht

### index ###
@route('/')
@view('olympics_index')
def index():
    user_type = controllAuthification()
    welcome_message = "Willkommen!"
    return {"message" : welcome_message , "get_url" : bottle.url , "user" : user_type, "user_name" : str(request.get_cookie("user"))}

@route('/logout')
@view('olympics_index')
def pushed_logout():
    logout()
    message = "Erfolgreich ausgeloggt!"
    return  {"message" : message, "get_url" : bottle.url , "user" : "None", "user_name" : "None" }
    
    
@route('/login', method='GET')
@view('olympics_login')
def login():
    user_type = controllAuthification();
    return {"get_url" : bottle.url , "user" : user_type, "user_name" : str(request.get_cookie("user")), "message" : [False, ""]}
    
### simple pages ####
@route('/select_sport')
@view('select_sport')
def select_sport():
    user_type = controllAuthification()
    return  {"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
    
### ????? pages #######

@route('/do_login', method="POST")
#@view('olympics_login')
def do_login():
    user_found = False
    message = [False, "LogIn fehlgeschalgen!"]
    olympics = sqlite3.connect('olympic.db')
    #user_type = controllAuthification()
    user = request.forms.get("benutzername")
    password = request.forms.get("passwort")
    
    if password_check(user, password):
        response.set_cookie("user", user,path='/')
        key = str(int(random.random()*1000000000))
        response.set_cookie("key", str(key),path='/' )
        query = "UPDATE BENUTZER SET SECURITY_KEY = '" + key + "' WHERE BENUTZERNAME = '" + user + "'"
        print query
        olympics.execute(query)
        olympics.commit()
        user_type = str(olympics.execute("SELECT USER_TYPE FROM BENUTZER WHERE BENUTZERNAME = '" + user + "'").fetchone()[0])
        message = [True, "LogIn erfolgreich. Willkommen, " + user + " :)"]
        return template('olympics_index.tpl',{"get_url" : bottle.url , "user" : user_type, "user_name" : user, "message" : message[1]})

    else:
        print "passwords dont match"
        response.set_cookie("user_type", "None", path='/')
        response.set_cookie("user", "None", path='/')
        response.set_cookie("key", "None" , path='/')
        user_type = "None"
        user = "None"
    return template('olympics_login.tpl',{"get_url" : bottle.url , "user" : user_type, "user_name" : user, "message" : message})

@route('/select_sport/<sport>')
@view('olympics_searchwettkampf')
def select_sport(sport):
    user_type = controllAuthification()
    allowed_sports = ["biathlon", "bob", "curling", "eishockey", "eiskunstlauf", "eisschnelllauf", "freestyleski", "nordkomb", "rodeln", "shorttrack", "alpin", "langlauf", "skispringen", "snowboard"]
    datatable = {}
    if sport in allowed_sports:
        datatable = create_datatable("WETTKAMPF", "WHERE SPORTART='"+ sport.upper() +"'", "ID", "NAME", "DATUM", "STARTZEIT", "DISZIPLIN")
        sport = sport[:1].upper() + sport[1:].lower()
        return {"datatable": datatable ,"sport" : sport, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))} 
    else:
        return {"datatable": datatable ,"sport" : "Sportart existiert nicht!", "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))} 
@route('/addreport/<id>')
@view('olympics_addbericht')
def add_report(id):
    user_type = controllAuthification()
    return {"bericht_id" : id,"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
    
@route('/addreport/<id>', method="post")
@view('olympics_wettkampf')
def commit_report(id):
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    user_name = request.get_cookie('user') 
    author_id = str(olympic.execute("SELECT ID FROM BENUTZER WHERE BENUTZERNAME = '" + user_name + "'").fetchone()[0])
    head = request.forms.get('ueberschrift')
    report = request.forms.get('bericht')
    query = "INSERT INTO BERICHT (AUTHOR_ID, BERICHT, UEBERSCHRIFT) VALUES(" + author_id + ", '" + report +"', '" + head + "')" 
    print query
    c = olympic.execute(query)
    report_id = str(c.lastrowid)
    query = "INSERT INTO WETTKAMPF_BERICHT (BERICHT_ID, WETTKAMPF_ID) VALUES(" + report_id + ", " + id +")" 
    print query
    c = olympic.execute(query)
    olympic.commit()
   
    wettkampf = Wettkampfdata(id)
    conditions = '''SPORTLER_WETTKAMPF  AS SW JOIN SPORTLER AS S JOIN WETTKAMPF as w WHERE 
    s.id = sw.sportler_id and sw.wettkampf_id = w.id and w.id = "''' + id + '''" ORDER BY PLATZIERUNG'''
    datatable = create_datatable("",conditions , "s.vorname", "s.nachname", "sw.platzierung", "s.id as ID" )
    berichte = get_berichte(id)
    return {"wettkampfdata": wettkampf, "datatable" : datatable, "berichte" : berichte, "bericht_id" : id,"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
    
def create_datatable(table, conditions, *spalten):
    x = spalten
    query = "SELECT "
    for i in spalten:
        query += i.upper() + ", "
    query = query[:len(query)-2] + " "
    query += "FROM " + table.upper() + " " + conditions
    olympic = sqlite3.connect('olympic.db')
    print query
    data = olympic.execute(query)
    
    datatable = [list(map(lambda x: x[0], data.description)), data]
    return datatable
    
    
### formular pages ####
@route('/add_athlet')
@view('olympics_addathlet')
def add_athlet():
    user_type = controllAuthification()
    return {"nations" : get_nations(), "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
    
@route('/search_athlet')
@view('olympics_searchathlet')
def search_athlet():
    user_type = controllAuthification()
    datatable = create_datatable("SPORTLER", "", "VORNAME", "NACHNAME", "GESCHLECHT", "NATIONALITAET", "ID")
    return {"nations" : get_nations(), "datatable" : datatable ,"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user") )}


@route('/search_athlet', method="post")
@view('olympics_searchathlet')
def search_athlet():
    user_type = controllAuthification()
    vorname = request.forms.get("vorname")
    nachname = request.forms.get("nachname")
    geschlecht = request.forms.get("geschlecht")
    nationalitaet = request.forms.get("nationalitaet")
    id = request.forms.get("id")
    if vorname == None:
        vorname = ""
    if nachname == None:
        nachname = ""
    if geschlecht == None:
        geschlecht = ""
    if geschlecht == "weiblich":
        geschlecht = "True"
    if geschlecht == "maennlich":
        geschlecht = "False"
    if nationalitaet == None:
        nationalitaet = ""
    conditions = "WHERE VORNAME LIKE '%" + vorname  +"%' " + "AND NACHNAME LIKE '%" + nachname  +"%' " + "AND GESCHLECHT LIKE '%" + geschlecht  +"%' " + "AND NATIONALITAET LIKE '%" + nationalitaet  +"%' " 
    if id != None and id != "":
       conditions += "AND ID = " + id  +" " 
    print conditions
    datatable = create_datatable("SPORTLER", conditions, "VORNAME", "NACHNAME", "GESCHLECHT", "NATIONALITAET", "ID")
    return {"nations" : get_nations(), "datatable" : datatable ,"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user") )}
    
@route('/add_wettkampf')
@view('olympics_addwettkampf')
def add_wettkampf():
    user_type = controllAuthification()
    return {"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

@route('/searchwettkampf')
@view('olympics_searchwettkampf')
def search_wettkampf():
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    content = olympic.execute("select * from wettkampf");
    return {"content" : content ,"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user") )}

@route('/searchwettkampf/<sport>', method="post")
@view('olympics_searchwettkampf')
def search_wettkampf(sport):
    user_type = controllAuthification()
    sportart = request.forms.get("sportart")
    print sportart
    name = request.forms.get("name")
    startzeit = str(request.forms.get("startzeit"))
    datum = str(request.forms.get("datum"))
    disziplin = request.forms.get("disziplin")
    id = request.forms.get("id")
    if sportart == None:
        sportart = ""    
    if name == None:
        name = ""
    if startzeit == None:
        startzeit = ""
    if datum == None:
        datum = ""
    if disziplin == None:
        disziplin = ""
    conditions = "WHERE SPORTART LIKE '%" + sportart  +"%' " + "AND NAME LIKE '%" + name  +"%' " + "AND STARTZEIT LIKE '%" + startzeit +"%' " + "AND DATUM LIKE '%" + datum  +"%' " + "AND DISZIPLIN LIKE '%" + disziplin  +"%' " 
    if id != None and id != "":
       conditions += "AND ID = " + id  +" " 
    print conditions
    datatable = create_datatable("WETTKAMPF", conditions, "SPORTART","NAME", "STARTZEIT", "DATUM", "DISZIPLIN", "ID")
    #print "datatable" + str(datatable[1].fetchone())
    return {"datatable" : datatable , "sport" : sport, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user") )}

@route('/wettkampf/<id>')
@view('olympics_wettkampf')
def wettkampf(id):
    user_type = controllAuthification()
    wettkampf = Wettkampfdata(id)
    conditions = '''SPORTLER_WETTKAMPF  AS SW JOIN SPORTLER AS S JOIN WETTKAMPF as w WHERE 
    s.id = sw.sportler_id and sw.wettkampf_id = w.id and w.id = "''' + id + '''" ORDER BY PLATZIERUNG'''
    datatable = create_datatable("",conditions , "s.vorname", "s.nachname", "sw.platzierung", "s.id as ID" )
    berichte = get_berichte(id)
    return {"berichte" : berichte, "datatable" : datatable, "wettkampfdata" : wettkampf, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

@route('/bericht/<id>', method='POST')
@view('olympics_bericht/')
def commit_commentary(id):
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    user_name = request.get_cookie('user') 
    author_id = str(olympic.execute("SELECT ID FROM BENUTZER WHERE BENUTZERNAME = '" + user_name + "'").fetchone()[0])
    commentary = request.forms.get('kommentar')
    query = "INSERT INTO KOMMENTARE (AUTHOR_ID, KOMMENTAR) VALUES(" + author_id + ", '" + commentary +"')" 
    c = olympic.execute(query)
    commentary_id = str(c.lastrowid)
    query = "INSERT INTO BERICHTE_KOMMENTARE (KOMMENTAR_ID, BERICHT_ID) VALUES(" + commentary_id + ", " + id +")" 
    print query
    c = olympic.execute(query)
    olympic.commit()
    
    conditions = '''KOMMENTARE AS K JOIN BERICHTE_KOMMENTARE 
    AS bk JOIN BERICHT AS b where b.id = bk.bericht_id and k.id = bk.kommentar_id and b.id = ''' + id
    datatable = create_datatable("", conditions , "k.KOMMENTAR")
    bericht = Bericht(id)
    return {"bericht" : bericht, "datatable" : datatable,  "wettkampfdata" : wettkampf, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

@route('/bericht/<id>')
@view('olympics_bericht')
def bericht(id):
    user_type = controllAuthification()
    conditions = '''KOMMENTARE AS K JOIN BERICHTE_KOMMENTARE 
    AS bk JOIN BERICHT AS b where b.id = bk.bericht_id and k.id = bk.kommentar_id and b.id = ''' + id
    datatable = create_datatable("", conditions , "k.KOMMENTAR")
    bericht = Bericht(id)
    return {"bericht" : bericht, "datatable" : datatable,  "wettkampfdata" : wettkampf, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

@route('/remove_athlet_from_contest/<contest_id>')
@view('remove_athlet_from_contest')    
def remove_athlet_from_contest(contest_id): 
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    query = "SELECT SPORTLER_ID FROM SPORTLER_WETTKAMPF AS SW  WHERE SW.WETTKAMPF_ID =" + contest_id
    cursor = olympic.execute(query)
    starter_list = []
    for c in cursor:
        starter_list.append(c[0])
    print "Starterlist: " + str(starter_list)
    conditions = "WHERE ID IN (" + str(starter_list)[1:len(str(starter_list))-1] +")"
    message =""
    datatable = create_datatable("SPORTLER", conditions, "VORNAME", "NACHNAME", "NATIONALITAET", "ID")
    contest_name = str(olympic.execute("SELECT NAME FROM WETTKAMPF WHERE ID = " + contest_id).fetchone()[0])
    print "contest_name: " + contest_name
    return {"wettkampf_id": contest_id, "wettkampfname" : contest_name, "message" : "", "datatable" : datatable, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

@route('/remove_athlet_from_contest/<contest_id>/<sportler_id>')
@view('remove_athlet_from_contest')    
def remove_athlet_from_contest(contest_id, sportler_id): 
    user_type = controllAuthification()

    olympic = sqlite3.connect('olympic.db')
    query = "DELETE FROM SPORTLER_WETTKAMPF WHERE WETTKAMPF_ID=" + contest_id + " and SPORTLER_ID=" +sportler_id
    print query
    cursor = olympic.execute(query)
    olympic.commit()

    query = "SELECT SPORTLER_ID FROM SPORTLER_WETTKAMPF AS SW  WHERE SW.WETTKAMPF_ID =" + contest_id
    cursor = olympic.execute(query)
    starter_list = []
    for c in cursor:
        starter_list.append(c[0])
    print "Starterlist: " + str(starter_list)
    conditions = "WHERE ID IN (" + str(starter_list)[1:len(str(starter_list))-1] +")"
    
    datatable = create_datatable("SPORTLER", conditions, "VORNAME", "NACHNAME", "NATIONALITAET", "ID")
    contest_name = str(olympic.execute("SELECT NAME FROM WETTKAMPF WHERE ID = " + contest_id).fetchone()[0])
    print "contest_name: " + contest_name
    return {"wettkampf_id": contest_id, "wettkampfname" : contest_name, "message" : "", "datatable" : datatable, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
    
    
@route('/add_athlet_to_contest/<contest_id>')
@view('add_athlet_to_contest')    
def add_athlet_to_contest(contest_id): 
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    query = "SELECT SPORTLER_ID FROM SPORTLER_WETTKAMPF AS SW  WHERE SW.WETTKAMPF_ID =" + contest_id
    cursor = olympic.execute(query)
    starter_list = []
    for c in cursor:
        starter_list.append(c[0])
    print "Starterlist: " + str(starter_list)
    conditions = "WHERE ID NOT IN (" + str(starter_list)[1:len(str(starter_list))-1] +")"
    message =""
    datatable = create_datatable("SPORTLER", conditions, "VORNAME", "NACHNAME", "NATIONALITAET", "ID")
    contest_name = str(olympic.execute("SELECT NAME FROM WETTKAMPF WHERE ID = " + contest_id).fetchone()[0])
    print "contest_name: " + contest_name
    return {"wettkampf_id": contest_id, "wettkampfname" : contest_name, "message" : "", "datatable" : datatable, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

@route('/add_athlet_to_contest/<contest_id>/<sportler_id>')
@view('add_athlet_to_contest')    
def add_athlet_to_contest(contest_id, sportler_id): 
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    query = "SELECT SPORTLER_ID, WETTKAMPF_ID FROM SPORTLER_WETTKAMPF";
    contest_sportler_list = olympic.execute(query).fetchall()
    print contest_sportler_list
    print (sportler_id, contest_id)
    if (int(sportler_id), int(contest_id)) not in contest_sportler_list:
        query = "INSERT INTO SPORTLER_WETTKAMPF(SPORTLER_ID, WETTKAMPF_ID) VALUES(" + sportler_id + ", " + contest_id +")" 
        print query
        c = olympic.execute(query)
        olympic.commit()

    olympic = sqlite3.connect('olympic.db')
    query = "SELECT SPORTLER_ID FROM SPORTLER_WETTKAMPF AS SW  WHERE SW.WETTKAMPF_ID =" + contest_id
    cursor = olympic.execute(query)
    starter_list = []
    for c in cursor:
        starter_list.append(c[0])
    print "Starterlist: " + str(starter_list)
    conditions = "WHERE ID NOT IN (" + str(starter_list)[1:len(str(starter_list))-1] +")"
    message =""
    datatable = create_datatable("SPORTLER", conditions, "VORNAME", "NACHNAME", "NATIONALITAET", "ID")
    contest_name = str(olympic.execute("SELECT NAME FROM WETTKAMPF WHERE ID = " + contest_id).fetchone()[0])
    print "contest_name: " + contest_name
    return {"wettkampf_id": contest_id, "wettkampfname" : contest_name, "message" : "", "datatable" : datatable, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
    
  
@route('/add_benutzer')
@view('olympics_addbenutzer')
def add_benutzer():
    user_type = controllAuthification()
    return {"message" : "", "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

    
@route('/benutzerprofil')
@view('olympics_benutzerprofil')
def benutzerprofil():
    user_type = controllAuthification()
    user = str(request.get_cookie("user") )
    userdata = get_userdata(user)
    return {"get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user")), "userdata" : userdata}

@route('/changeprofil')
@view('olympics_changeprofil')
def change_benutzerprofil():
    user_type = controllAuthification()
    user = str(request.get_cookie("user") )
    userdata = get_userdata(user)
    return {"message" : "", "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user")), "userdata" : userdata}
    
@route('/sportlerprofil/<id>')
@view('olympics_athlet')
def sportlerprofil(id):
    print "ID: " + id
    user_type = controllAuthification()
    athlet = Sportlerdata(id)
    conditions ='''SPORTLER_WETTKAMPF AS SW JOIN SPORTLER AS S JOIN WETTKAMPF as w WHERE s.id = sw.sportler_id and sw.wettkampf_id = w.id and s.id = ''' + id
    datatable = create_datatable("", conditions, "w.name", "w.disziplin", "w.datum", "sw.platzierung", "w.id")
    return {"datatable" : datatable, "athlet" : athlet, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
            
### database pages #### 
### Sportler ####
@route('/commitathlet', method='POST')
@view('olympics_athlet_added')
def commit_athlet():
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    
    query = "SELECT ID from SPORTLER where Vorname='" + request.forms.get("vorname") + "' AND Nachname='" + request.forms.get("nachname") + "'"
    cursor = olympic.execute(query)
    l = []
    for i in cursor:
        l.append(i[0])
    
    geschlecht = request.forms.get("geschlecht")
    if geschlecht == "weiblich":
        woman = "'TRUE'"
    elif geschlecht == "maennlich":
        woman = "'FALSE'"
    query = "INSERT INTO SPORTLER (VORNAME, NACHNAME, GESCHLECHT, NATIONALITAET, FOTO) VALUES ('" + request.forms.get("vorname") + "', '" + request.forms.get("nachname") + "', " + woman + ", '" + request.forms.get("nations") + "', ?)"
    c = olympic.cursor()
    file = request.files.bild
    raw = file.file.read()
    print file.filename
    bin = [sqlite3.Binary(file.file.read())]
    c.execute(query, bin)
    olympic.commit()
    
    #olympic.execute(query) #Auskommentieren
    query = "SELECT ID from SPORTLER where Vorname='" + request.forms.get("vorname") + "' AND Nachname='" + request.forms.get("nachname") + "'"
    for i in l:
        query += " AND ID IS NOT " + str(i)
    print query
    cursor = olympic.execute(query)
    x = ""
    for i in cursor:
        x = i[0]
        break
    
    return {"ID" : x, "vorname": request.forms.get("vorname"), "nachname": request.forms.get("nachname"), "geschlecht": request.forms.get("geschlecht"), "nationalitaet": request.forms.get("nationalitaet") , "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

### Wettkampf ###

@route('/commitwettkampf', method='POST')
@view('olympics_wettkampf_added')
def commit_wettkampf():
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    
    query = "SELECT ID from WETTKAMPF where name='" + request.forms.get("name") + "' "
    cursor = olympic.execute(query)
    l = []
    for i in cursor:
        l.append(i[0])

    query = "INSERT INTO WETTKAMPF(SPORTART, NAME, DATUM, STARTZEIT, DISZIPLIN, FOTO) VALUES ('" + request.forms.get("sportart") + "', '" + request.forms.get("name") + "', '" + str(request.forms.get("datum")) + "', '" + str(request.forms.get("startzeit")) + "', '" + request.forms.get("disziplin") + "', ?)"
    print query
    c = olympic.cursor()
    file = request.files.foto
    raw = file.file.read()
    print file.filename
    bin = [sqlite3.Binary(file.file.read())]
    c.execute(query, bin)
    olympic.commit()
    
    query = "SELECT ID from WETTKAMPF where Name='" + request.forms.get("name") + "'"
    for i in l:
        query += " AND ID IS NOT " + str(i)
    print query
    cursor = olympic.execute(query)
    x = ""
    for i in cursor:
        x = i[0]
        break
    
    return {"ID" : x, "sportart": request.forms.get("sportart"), "name": request.forms.get("name"), "datum": str(request.forms.get("datum")), "startzeit": str(request.forms.get("startzeit")), "disziplin": request.forms.get("disziplin"), "foto": request.forms.get("foto"), "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user") )}

@route('/medallien_spiegel')
@view('olympics_medallien_spiegel')
def medallien_spiegel(): 
    user_type = controllAuthification()

    olympic = sqlite3.connect('olympic.db')

    nations = get_nations()
    f = []
    for key in nations:
        query = "SELECT s.NATIONALITAET FROM SPORTLER AS S JOIN SPORTLER_WETTKAMPF AS SW WHERE S.ID = SW.SPORTLER_ID and sw.PLATZIERUNG = 1 and NATIONALITAET = '" + key + "'"
        gold =   len(olympic.execute(query).fetchall())
        query = "SELECT s.NATIONALITAET FROM SPORTLER AS S JOIN SPORTLER_WETTKAMPF AS SW WHERE S.ID = SW.SPORTLER_ID and sw.PLATZIERUNG = 2 and NATIONALITAET = '" + key + "'"
        silver = len(olympic.execute(query).fetchall())
        query = "SELECT s.NATIONALITAET FROM SPORTLER AS S JOIN SPORTLER_WETTKAMPF AS SW WHERE S.ID = SW.SPORTLER_ID and sw.PLATZIERUNG = 3 and NATIONALITAET = '" + key + "'"
        bronce = len(olympic.execute(query).fetchall())
        f.append((key, gold,silver, bronce))
    
    f = sorted(f, key=lambda tup: tup[1], reverse=True)

        
    print f
    datatable = [("Nation","Gold", "Silber", "Bronze"), f]
    return {"datatable" : datatable, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user") )}

    
### Benutzer registrieren ###

@route('/commitbenutzer', method='POST')
@view('olympics_benutzer_added')
def commit_benutzer():
    message = ""
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    
    query = "SELECT Benutzername from BENUTZER where Benutzername='" + request.forms.get("benutzername") + "' "
    cursor = olympic.execute(query).fetchone()
    if cursor != None:
        message = "Benutzername existiert bereits"
        return template('olympics_addbenutzer.tpl',{"message" : message, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))})
    else:
        geschlecht = request.forms.get("geschlecht")
        if geschlecht == "weiblich":
            woman = "'TRUE'"
        elif geschlecht == "maennlich":
            woman = "'FALSE'"
            
        query = "INSERT INTO BENUTZER(BENUTZERNAME, PASSWORT, VORNAME, NACHNAME, GEBURTSDATUM, GESCHLECHT, EMAILADRESSE, ORT, LAND, USER_TYPE) VALUES ('" + str(request.forms.get("benutzername")) + "', '" + str(request.forms.get("passwort")) + "', '" + str(request.forms.get("vorname")) + "', '" + str(request.forms.get("nachname")) + "', '" + str(request.forms.get("geburtsdatum")) + "', " + woman + ", '" + str(request.forms.get("emailadresse")) + "', '" + str(request.forms.get("ort")) + "', '" + str(request.forms.get("land")) + "', '" + str(request.forms.get("user_type")) + "')"
        #c = olympic.cursor()
        #file = request.files.bild
        #raw = file.file.read()
        #print file.filename
        #bin = [sqlite3.Binary(file.file.read())]
        #c.execute(query, bin)
        print query
        olympic.execute(query)
        olympic.commit()
        user = request.forms.get("benutzername")
        query = "SELECT ID from BENUTZER where Benutzername='" + request.forms.get("benutzername") + "'"
        return {"userdata" : get_userdata(user), "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

        
@route('/changebenutzer', method='POST')
@view('olympics_changeprofil') 
def changebenutzer():
    message = ""
    user_type = controllAuthification()
    olympic = sqlite3.connect('olympic.db')
    
    user = str(request.get_cookie("user"))
    password = str(request.forms.get("passwort"))
    new_username = request.forms.get("Benutzername")
    if password_check(user, password):
        if user != new_username:
            query = "SELECT BENUTZERNAME FROM BENUTZER WHERE BENUTZERNAME ='" + new_username +"'"
            cursor = olympic.execute(query).fetchone()
            if cursor != None:
                message = "Benutzername existiert bereits"
                print "1"
                return {"userdata" : get_userdata(user), "message" : message, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}
        geschlecht = request.forms.get("geschlecht")
        if geschlecht == "weiblich":
            woman = "'TRUE'"
        elif geschlecht == "maennlich":
            woman = "'FALSE'"
            
        query = "UPDATE BENUTZER SET BENUTZERNAME='" + str(request.forms.get("Benutzername")) + "', passwort='" + str(request.forms.get("passwort")) + "', VORNAME='" + str(request.forms.get("vorname")) + "', NACHNAME='" + str(request.forms.get("nachname")) + "', GEBURTSDATUM='" + str(request.forms.get("geburtsdatum")) + "', GESCHLECHT='" + str(request.forms.get("geschlecht")) + "', EMAILADRESSE='" + str(request.forms.get("emailadresse")) + "', ORT='" + str(request.forms.get("ort")) + "', LAND='" + str(request.forms.get("land")) + "', FOTO='" + str(request.forms.get("foto")) + "', USER_TYPE='" + str(request.forms.get("user_type")) + "' "
        print query
        olympic.execute(query)
        olympic.commit()
    else:
        message = "Falsches password!"
        return {"userdata" : get_userdata(user),"message" : message, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}

    message = "Aenderung erfolgreich!"
    return {"userdata" : get_userdata(new_username), "message" : message, "get_url" : bottle.url, "user" : user_type, "user_name" : str(request.get_cookie("user"))}    
        
@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')
    
def controllAuthification(): 
    user_type = "None"
    checkOk = False
    olympics = sqlite3.connect('olympic.db')
    user = str(request.get_cookie("user"))
    key = str(request.get_cookie("key"))
    print "user: " + user + ", key: " + key
    query = "SELECT SECURITY_KEY FROM BENUTZER WHERE BENUTZERNAME = '" + user + "'"
    controll_key = olympics.execute(query).fetchone()
    print controll_key
    if controll_key == None or controll_key == "":
        logout()
    else:
        controll_key = str(controll_key[0])
        if key == controll_key:
            checkOk = True
            key = str(int(random.random()*1000000000))
            query = "UPDATE BENUTZER SET SECURITY_KEY = " + key + " WHERE BENUTZERNAME = '" + user + "'"
            olympics.execute(query)
            olympics.commit()
            result = olympics.execute("SELECT USER_TYPE FROM BENUTZER WHERE BENUTZERNAME = '" + user + "'").fetchone()
            response.set_cookie("key", key,path='/')
            if result != None:
                user_type = str(result[0])
            else:
                user_type = "None"
            print "user: " + user + ", key: " + key + ", user_type: " + user_type
        else:
            logout()
            print "user: " + "None" + ", key: " + "None"
    olympics.close()
    return user_type
    
def logout():
    response.set_cookie("user", "",path='/')
    response.set_cookie("user_type", "",path='/')
    response.set_cookie("key", "",path='/')

###############################################
    
def get_userdata(user):
    print "Catch data from User: " + user
    olympic = sqlite3.connect('olympic.db')
    query = "SELECT BENUTZERNAME, VORNAME, NACHNAME, GEBURTSDATUM, GESCHLECHT, EMAILADRESSE, ORT, LAND, USER_TYPE, ID FROM BENUTZER WHERE BENUTZERNAME = '" + user + "'"
    cursor = olympic.execute(query).fetchone()
    return Userdata(cursor)

def password_check(user, password):
    olympic = sqlite3.connect('olympic.db')
    query = "SELECT PASSWORT FROM BENUTZER WHERE BENUTZERNAME = '" + user + "'"
    db_password = olympic.execute(query).fetchone()
    print db_password
    print password
    if db_password != None:
        user_found = True
        db_password = str(db_password[0])
    else:
        db_password = ""
        return False
        
    if db_password == password and user_found:
        return True
    else:
        return False

def get_berichte(id):
    olympic = sqlite3.connect('olympic.db')
    query = "SELECT b.id FROM WETTKAMPF_BERICHT as wb JOIn BERICHT AS b where b.id = wb.bericht_id and wb.wettkampf_id =" + id
    print query
    cursor =olympic.execute(query)
    berichte = []
    for c in cursor:
        print "fetch report from id: " + str(c[0])
        berichte.append(Bericht(str(c[0])))
    for b in berichte:
        print b.ueberschrift
    return berichte
    
def get_nations():
    liste = ["Russland", "Norwegen", "Kanada", "USA", "Niederlande", "Deutschland", "Schweiz", "Weissrussland", "Oesterreich", "Frankreich", "Polen", "China", "Suedkorea", "Schweden", "Tschechien", "Slowenien", "Japan", "Finnland", "VereinigtesKoenigreichGrossbritannien", "Ukraine", "Slowakei", "Italien", "Lettland", "Australien", "Kroatien", "Kasachstan"]
    return liste

    
run(host='localhost', port=8080, debug=True)
