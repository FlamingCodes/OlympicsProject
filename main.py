from bottle import get, post, route, run, request, view, static_file, template, response
import bottle
import sqlite3

### index ###
@route('/')
@view('olympics_index')
def index():
    return {"content" : "Willkommen auf meiner SupiDupi Sochi Seite! Olympia ist vorbei du Spasti!!!", "get_url" : bottle.url}
### simple pages ####
@route('/select_sport')
@view('select_sport')
def select_sport():
    return  {"get_url" : bottle.url}
    
### ????? pages #######

@route('/select_sport/<sport>')
@view('olympics_searchwettkampf')
def select_sport(sport):
    allowed_sports = ["biathlon", "bob", "curling", "eishockey", "eiskunstlauf", "eisschnelllauf", "freestyleski", "nordkomb", "rodeln", "shorttrack", "alpin", "langlauf", "skispringen", "snowboard"]
    datatable = {}
    header = []
    if sport in allowed_sports:
        #olympic = sqlite3.connect('olympic.db')
        #query = "SELECT ID, NAME  from WETTKAMPF where SPORTART='" + sport.upper() + "'"
        #print "query: " + query
        #datatable = olympic.execute(query)
        datatable = create_datatable("WETTKAMPF", "WHERE SPORTART='ALPIN'", "ID", "NAME", "DISZIPLIN")
        sport = sport[:1].upper() + sport[1:].lower()
        return {"datatable": datatable ,"sport" : sport, "get_url" : bottle.url} 
    else:
        return {"datatable": datatable ,"sport" : "Sportart existiert nicht!", "get_url" : bottle.url} 

        
def create_datatable(table, condition, *spalten):
    header = spalten
    query = "SELECT "
    for i in spalten:
        query += i.upper() + ", "
    query = query[:len(query)-2] + " "
    query += "FROM " + table.upper() + " " + condition.upper()
    olympic = sqlite3.connect('olympic.db')
    print query
    data = olympic.execute(query)
    
    datatable = [header, data]
    return datatable
    
    
### formular pages ####
@route('/add_athlet')
@view('olympics_addathlet')
def add_athlet():
    return {"get_url" : bottle.url}
    
@route('/search_athlet')
@view('olympics_searchathlet')
def search_athlet():
    datatable = create_datatable("SPORTLER", "", "VORNAME", "NACHNAME", "GESCHLECHT", "NATIONALITAET")
    return {"datatable" : datatable ,"get_url" : bottle.url}

#@route('/search_athlet')
#@view('olympics_searchathlet')
#def teilnahme_an():
#    olympic = sqlite3.connect('olympic.db')
#    content = select sportler.ID as wettkampf.sportler_id from SPORTLER, wettkampf where sportler.id = wettkampf.sportler_id;
#    return {"content" : content ,"get_url" : bottle.url}

@route('/add_wettkampf')
@view('olympics_addwettkampf')
def add_wettkampf():
    return {"get_url" : bottle.url}

@route('/searchwettkampf')
@view('olympics_searchwettkampf')
def search_wettkampf():
    olympic = sqlite3.connect('olympic.db')
    content = olympic.execute("select * from wettkampf");
    return {"content" : content ,"get_url" : bottle.url}

@route('/add_benutzer')
@view('olympics_addbenutzer')
def add_benutzer():
    return {"get_url" : bottle.url}
    
### database pages ####
### Sportler ####
@route('/commitathlet', method='POST')
@view('olympics_athlet_added')
def commit_athlet():
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
    #query = "INSERT INTO SPORTLER (VORNAME, NACHNAME, GESCHLECHT, NATIONALITAET) VALUES ('" + request.forms.get("vorname") + "', '" + request.forms.get("nachname") + "', " + woman + ", '" + request.forms.get("nationalitaet") +",)"
    query = "INSERT INTO SPORTLER (VORNAME, NACHNAME, GESCHLECHT, NATIONALITAET, FOTO) VALUES ('" + request.forms.get("vorname") + "', '" + request.forms.get("nachname") + "', " + woman + ", '" + request.forms.get("nationalitaet") + "', ?)"
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
    
    return {"ID" : x, "vorname": request.forms.get("vorname"), "nachname": request.forms.get("nachname"), "geschlecht": request.forms.get("geschlecht"), "nationalitaet": request.forms.get("nationalitaet") , "get_url" : bottle.url}

### Wettkampf ###

@route('/commitwettkampf', method='POST')
@view('olympics_wettkampf_added')
def commit_wettkampf():
    olympic = sqlite3.connect('olympic.db')
    
    query = "SELECT ID from WETTKAMPF where Vorname='" + request.forms.get("vorname") + "' AND Nachname='" + request.forms.get("nachname") + "'"
    cursor = olympic.execute(query)
    l = []
    for i in cursor:
        l.append(i[0])

    #query = "INSERT INTO SPORTLER (VORNAME, NACHNAME, GESCHLECHT, NATIONALITAET) VALUES ('" + request.forms.get("vorname") + "', '" + request.forms.get("nachname") + "', " + woman + ", '" + request.forms.get("nationalitaet") +",)"
    query = "INSERT INTO WETTKAMPF(NAME, DATUM, STARTZEIT, DISZIPLIN, FOTO, BERICHT, BENUTZERKOMMENTAR) VALUES ('" + request.forms.get("name") + "', '" + request.forms.get("datum") + "', '" + request.forms.get("startzeit") + "', '" + request.forms.get("disziplin") + "', '" + request.forms.get("foto") + "', '" + request.forms.get("bericht") + "', '" + request.forms.get("benutzerkommentar") + "' ?)"
    c = olympic.cursor()
    file = request.files.bild
    raw = file.file.read()
    print file.filename
    bin = [sqlite3.Binary(file.file.read())]
    c.execute(query, bin)
    olympic.commit()
    
    #olympic.execute(query) #Auskommentieren
    query = "SELECT ID from WETTKAMPF where Name='" + request.forms.get("name") + "'"
    for i in l:
        query += " AND ID IS NOT " + str(i)
    print query
    cursor = olympic.execute(query)
    x = ""
    for i in cursor:
        x = i[0]
        break
    
    return {"ID" : x, "name": request.forms.get("name"), "datum": request.forms.get("datum"), "startzeit": request.forms.get("startzeit"), "disziplin": request.forms.get("disziplin") , "foto": request.forms.get("foto") , "bericht": request.forms.get("bericht") , "benutzerkommentar": request.forms.get("benutzerkommentar") , "get_url" : bottle.url}

### Benutzer registrieren ###

@route('/commitbenutzer', method='POST')
@view('olympics_benutzer_added')
def commit_benutzer():
    olympic = sqlite3.connect('olympic.db')
    
    query = "SELECT ID from BENUTZER where Benutzername='" + request.forms.get("benutzername") + "' "
    cursor = olympic.execute(query)
    l = []
    for i in cursor:
        l.append(i[0])

    #query = "INSERT INTO SPORTLER (VORNAME, NACHNAME, GESCHLECHT, NATIONALITAET) VALUES ('" + request.forms.get("vorname") + "', '" + request.forms.get("nachname") + "', " + woman + ", '" + request.forms.get("nationalitaet") +",)"
    query = "INSERT INTO BENUTZER(BENUTZERNAME, VORNAME, NACHNAME, GEBURTSDATUM, GESCHLECHT, EMAILADRESSE, ORT, LAND, FOTO, JOURNALIST) VALUES ('" + request.forms.get("benutzername") + "', '" + request.forms.get("vorname") + "', '" + request.forms.get("nachname") + "', '" + request.forms.get("geburtsdatum") + "', '" + request.forms.get("geschlecht") + "', '" + request.forms.get("emailadresse") + "', '" + request.forms.get("ort") + "', '" + request.forms.get("land") + "', '" + request.forms.get("foto") + "', '" + request.forms.get("journalist") + "' ?)"
    c = olympic.cursor()
    file = request.files.bild
    raw = file.file.read()
    print file.filename
    bin = [sqlite3.Binary(file.file.read())]
    c.execute(query, bin)
    olympic.commit()
    
    #olympic.execute(query) #Auskommentieren
    query = "SELECT ID from BENUTZER where Benutzername='" + request.forms.get("benutzername") + "'"
    for i in l:
        query += " AND ID IS NOT " + str(i)
    print query
    cursor = olympic.execute(query)
    x = ""
    for i in cursor:
        x = i[0]
        break
    
    return {"ID" : x, "benutzername": request.forms.get("benutzernamename"), "vorname": request.forms.get("vorname"), "nachname": request.forms.get("nachname"), "geburtsdatum": request.forms.get("geburtsdatum") , "geschlecht": request.forms.get("geschlecht") , "emailadresse": request.forms.get("emailadresse") , "ort": request.forms.get("ort") , "land": request.forms.get("land") ,  "foto": request.forms.get("foto") , "journalist": request.forms.get("journalist") , "get_url" : bottle.url}

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')
    

run(host='localhost', port=8080, debug=True)
