class Wettkampfdata():
    
    def __init__(self, cursor):
        self.name = str(cursor[0])
        self.startzeit = str(cursor[1])
        self.datum = str(cursor[2])
        self.disziplin = str(cursor[3])
        self.bericht = str(cursor[4])
        self.benutzerkommentar = str(cursor[5])
        self.id = str(cursor[6])
        
    def name(self):
        return self.name
    
    def startzeit(self):
        return self.startzeit 
    
    def datum(self):
        return self.datum
        
    def disziplin(self):
        return self.disziplin
        
    def bericht(self):
        return self.bericht
        
    def benutzerkommentar(self):
        return self.benutzerkommentar
        
    def id(self):
        return self.id


