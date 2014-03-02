import sqlite3

class Bericht():

    def __init__(self, id):
        olympic = sqlite3.connect('olympic.db')
        query = "SELECT ID, UEBERSCHRIFT, BERICHT, AUTHOR_ID FROM BERICHT where ID = " + id
        print query
        cursor = olympic.execute(query).fetchone()
        print cursor
        self.id = str(cursor[0])
        self.ueberschrift = str(cursor[1])
        self.bericht = str(cursor[2])
        self.author_id = str(cursor[3])
        cursor = olympic.execute("SELECT VORNAME, NACHNAME FROM BENUTZER WHERE ID = " + self.author_id).fetchone()
        self.author = cursor[0] + " " + cursor[1]
        
    def id(self):
        return self.id
        
    def ueberschrift(self):
        return self.ueberschrift 
    
    def bericht(self):
        return self.bericht
        
    def author_id(self):
        return self.author_id
    
    def author(self):
        return self.author
        

    
