import sqlite3

class Sportlerdata():
    ###def__init__(self, benutzername, vorname, nachname, geburtsdatum, geschlecht, emailadresse, ort, land, foto, user_name):
    def __init__(self, id):
        olympic = sqlite3.connect('olympic.db')
        query = "SELECT ID, VORNAME, NACHNAME, GEBURTSDATUM, GESCHLECHT, NATIONALITAET FROM SPORTLER WHERE ID =" + id
        print query
        cursor = olympic.execute(query).fetchone()
        print cursor
        self.id = str(cursor[0])
        self.vorname = str(cursor[1])
        self.nachname = str(cursor[2])
        self.geburtsdatum = str(cursor[3])
        
        if str(cursor[4]).upper() == "TRUE":
            self.geschlecht = "Weiblich"
        else: 
            self.geschlecht = "Maennlich"

        self.nationalitaet = str(cursor[5])
        
    def id(self):
        return self.id
    def vorname(self):
        return self.vorname 
    
    def nachname(self):
        return self.nachname
        
    def geburtsdatum(self):
        return self.geburtsdatum
        
    def geschlecht(self):
        return self.geschlecht
        
    def nationalitaet(self):
        return self.nationalitaet
