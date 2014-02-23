import sqlite3

olympic = sqlite3.connect('olympic.db')
cursor = olympic.execute("SELECT vorname, nachname, geschlecht, nationalitaet from SPORTLER")
cursor2 = olympic.execute("SELECT name, startzeit, datum, disziplin, bericht, benutzerkommentar from WETTKAMPF")
cursor3 = olympic.execute("SELECT vorname, nachname, geburtsdatum, geschlecht, emailadresse, ort, land, journalist from BENUTZER")

for row in cursor:
    print "VORNAME = ", row[0]
    print "NACHNAME = ", row[1]
    print "GESCHLECHT = ", row[2]
    print "NATIONALITAET = ", row[3], "\n"
    
for row in cursor2:
    print "NAME = ", row[0]
    print "STARTZEIT = ", row[1]
    print "DATUM = ", row[2]
    print "DISZIPLIN = ", row[3]
    print "BERICHT = ", row[4]
    print "BENUTZERKOMMENTAR = ", row[5], "\n"
    
for row in cursor3:
    print "VORNAME = ", row[0]
    print "NACHNAME = ", row[1]
    print "GEBURTSDATUM = ", row[2]
    print "GESCHLECHT = ", row[3]
    print "EMAILADRESSE = ", row[4]
    print "ORT = ", row[5]
    print "LAND = ", row[6]
    print "JOURNALIST = ", row[7], "\n"
