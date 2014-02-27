from bottle import get, post, route, run, request, view, static_file, template, response
import bottle
import sqlite3

### index ###
@route('/')
@view('olympics_index')
def index():
    return {"content" : "Willkommen auf meiner SupiDupi Sochi Seite! Olympia ist vorbei du Spasti!!!", "get_url" : bottle.url}
### formular pages ####
@route('/add_athlet')
@view('olympics_addathlet')
def add_athlet():
    return {"get_url" : bottle.url}
    
@route('/search_athlet')
@view('olympics_searchathlet')
def search_athlet():
    olympic = sqlite3.connect('olympic.db')
    content = olympic.execute("select * from sportler");
    return {"content" : content ,"get_url" : bottle.url}
    
@route('/searchwettkampf')
@view('olympics_searchwettkampf')
def search_wettkampf():
    olympic = sqlite3.connect('olympic.db')
    content = olympic.execute("select * from wettkampf");
    return {"content" : content ,"get_url" : bottle.url}


### database pages ####
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




@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')
    

run(host='localhost', port=8080, debug=True)
