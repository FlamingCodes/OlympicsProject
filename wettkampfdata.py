import sqlite3

class Wettkampfdata():

    def __init__(self, id):
        olympic = sqlite3.connect('olympic.db')
        query = "SELECT ID, SPORTART, NAME, DATUM, STARTZEIT, DISZIPLIN FROM WETTKAMPF WHERE ID =" + id
        print query
        cursor = olympic.execute(query).fetchone()
        print cursor
        self.id = str(cursor[0])
        self.sportart = str(cursor[1])
        self.name = str(cursor[2])
        self.datum = str(cursor[3])
        self.startzeit = str(cursor[4])
        self.disziplin = str(cursor[5])
        
    def id(self):
        return self.id
        
    def sportart(self):
        return self.sportart
        
    def name(self):
        return self.name 
    
    def datum(self):
        return self.datum
        
    def startzeit(self):
        return self.startzeit
        
    def disziplin(self):
        return self.disziplin
