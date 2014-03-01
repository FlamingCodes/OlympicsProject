class Userdata():
    ###def__init__(self, benutzername, vorname, nachname, geburtsdatum, geschlecht, emailadresse, ort, land, foto, user_name):
    def __init__(self, cursor):
        self.benutzername = str(cursor[0])
        self.vorname = str(cursor[1])
        self.nachname = str(cursor[2])
        self.geburtsdatum = str(cursor[3])
        self.geschlecht = str(cursor[4])
        self.emailadresse = str(cursor[5])
        self.ort = str(cursor[6])
        self.land = str(cursor[7])
        self.user_name = str(cursor[8])
        
    def benutzername(self):
        return self.benutzername
    
    def vorname(self):
        return self.vorname 
    
    def nachname(self):
        return self.nachname
        
    def geburtsdatum(self):
        return self.geburtdatum
        
    def geschlecht(self):
        return self.geschlecht
        
    def emailadresse(self):
        return self.emailadresse
        
    def ort(self):
        return self.ort
        
    def land(self):
        return self.land
        
    def user_name(self):
        return self.user_name


