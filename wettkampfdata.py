import sqlite3

class Wettkampfdata():

    def __init__(self, id):
        olympic = sqlite3.connect('olympic.db')
        query = "SELECT ID, NAME, DATUM, STARTZEIT, DISZIPLIN FROM WETTKAMPF WHERE ID =" + id
        print query
        cursor = olympic.execute(query).fetchone()
        print cursor
        self.id = str(cursor[0])
        self.name = str(cursor[1])
        self.datum = str(cursor[2])
        self.startzeit = str(cursor[3])
        self.disziplin = str(cursor[4])
        
    def id(self):
        return self.id
        
    def name(self):
        return self.name 
    
    def datum(self):
        return self.datum
        
    def startzeit(self):
        return self.startzeit
        
    def disziplin(self):
        return self.disziplin
