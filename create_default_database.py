import sqlite3

olympic = sqlite3.connect('olympic.db')
olympic.execute('''CREATE TABLE SPORTLER(VORNAME TEXT NOT NULL, NACHNAME TEXT NOT NULL, GESCHLECHT BOOLEAN NOT NULL, NATIONALITAET TEXT NOT NULL)''')

olympic.execute("INSERT INTO SPORTLER (VORNAME, NACHNAME, GESCHLECHT, NATIONALITAET) VALUES ('Giulia', 'Kirstein', 'TRUE', 'deutsch')")
olympic.commit()
cursor = olympic.execute("SELECT vorname, nachname, geschlecht, nationalitaet from SPORTLER")

for row in cursor:
    print "VORNAME = ", row[0]
    print "NACHNAME = ", row[1]
    print "GESCHLECHT = ", row[2]
    print "NATIONALITAET = ", row[3], "\n"
   
olympic.close()
