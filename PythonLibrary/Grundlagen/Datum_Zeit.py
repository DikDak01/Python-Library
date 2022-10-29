#Datum und Uhrzeit mit Python

#native: Native Objekte geben einen Zeitpunkt an, ihnen fehlt aber
#die Kontextinformation, in welcher Zeitzone die Zeit gilt, ob
#Sommer- oder Winterzeit gilt

#aware: Zeitobjekte, die diese Zeitobjekte haben, werden
#aware genannt. Bei solchen Objekten ist eine Feststellung möglich,
#welcher Zeitpunkt absolut gesehen früher oder später ist.

#Die meisten Zeitobjekte sind unverändliche Typen (immutable).

#-----------------------------------------------------------------------------------------------------#

#Zeit ermitteln und darstellen

#Das Modul datetime hat wie jedes andere Modul verschiedene Klassen
#eines davon ist datetime. Nur import datetime würde den Tippaufwand
#erhöhen (date.datetime.now())
from datetime import datetime

#-----------------------------------------------------------------------------------------------------#

#Hier wird von dem Modul datetime nur die Klasse date importiert
from datetime import date

#-----------------------------------------------------------------------------------------------------#

now = datetime.now()
print(now)

#einzelne Zeitkomponenten ausgeben lassen

print(now.year)

print(now.month)

#Datum und Uhrzeit formatiert ausgeben

print(now.isoformat())

print(now.strftime('%d.%m.%Y, %H:%M'))

#Datum aus Zeichenkette einlesen (parsen)

t = '01.10.2022 20:01'
dt = datetime.strptime(t, '%d.%m.%Y %H:%M')

#-----------------------------------------------------------------------------------------------------#

#Nur das aktuelle Datum ausgeben
today = date.today()
print(today)

#Mit dem datetime Objekt diese Aufgabe lösen
today2 = datetime.now()
print(now.date())

#Zeit ohne Datum
print(datetime.now().time())

today = datetime.today()
time = datetime.now().time()
#together = datetime.combine(date, time) #nochmals anschauen

#-----------------------------------------------------------------------------------------------------#

#Objekte für einen beliebigen Zeitpunkt
somedate = datetime(2022, 12, 31, 12, 0, 0)
print(somedate.isoformat())



