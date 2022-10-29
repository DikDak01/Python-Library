#Python Basics 

#& TODO: Ausgabe optimieren, jede Ausgabe mit kurzer erklärung und Farbe

#!Codierung ändern, Python nimmt normal UTF-8 
#! -*- coding: <encoding name> -*-
#~ TODO: Codierung anschauen

#--------------------------------------------------------------------------------------------#

#!einfache Ausgabe
print("einfache Ausgabe: Hello World")

#!mehrere Ausgaben
print("mehrere Ausgaben:", 1, 2, 3/4, 'abc', 2==3)

#!Ausgabe als String"1/4 ist"
print("Ausgabe als String:", "1/4 ist", 1/4)

#!sep stellt die Zeichenkette zwischen den Parametern ein
print("sep fügt zwischen den Zahlen --- ein:", 1, 2, 3, sep = '---')

#!end definiert die Zeichenkette, die nach dem letzten Parameter ausgegeben wird
print("end definiert das Ende der Zeichenkette:", 1, 2, 3, sep = '&', end = '\nEOF\n') 

#--------------------------------------------------------------------------------------------#

#!Strings zusammenfügen
name = 'Nik Nak'
programming_language = 'Python'
print("Strings zusammenfügen:", name, 'loves', programming_language)

#--------------------------------------------------------------------------------------------#

#!Hochzahlen 10^3
number = 10**3
print(number)

#!Division mit Fliesskommazahlen
print(2/3, 6/3)

#!ganzzahlige Division
print(2//3, 6//3)

#--------------------------------------------------------------------------------------------#

#!Länge einer Zeichenkette ermitteln
s = 'Hello'
print(len(s))

#--------------------------------------------------------------------------------------------#

#!Listen
lst = [0, 1, 2, 3, 4] #~Liste
lst.extend([32]) #~ein Element zu einer Liste hinzufügen

print(lst)

#--------------------------------------------------------------------------------------------#

#!For-Schleife
for i in range(4):
    print(i)

#--------------------------------------------------------------------------------------------#

#!Variabelnzuweisung
print('abc',
      'xyz')

a = 1 + 2 + \
3 + 4

print(a)

#!mehrere Variablenzuweisung 
a = 1; b = 2; c = 3

print(a, b, c)

x, y, z = 7, 8, 9

print(x, y, z)

#--------------------------------------------------------------------------------------------#

#!If Abfragen 
l = 12
n = 13 #^ TODO: 2 If Abfragen in einander verschachteln

if l > 12:
    print("l ist grösser als 12")
    
else:
    print("l ist nicht grösser als 12")
    
#!2 Bedingungen gleichzeitig prüfen

zo = 12

if zo > 10 and zo%2 == 0:
    print('grösser als 10 und gerade')
    
#!Variabeln und Daten vergleichen

za = 'abc'
xa = 'abc'

if za == xa:
    print('Der Inhalt der Variabeln za und xa stimmen überrein')
    
na = 'xyz'
ma = na

if na is ma:
    print('na und ma verweisen auf dasselbe Objekt')

oa = ['a', 'b', 'c']
ca = ['b']

ca.append('a')
ca.append('c')

print(a, b)

if oa == ca:
    print('Die Listen, auf die oa und ca zeigen stimmen überein')

if oa is ca:
    print('oa und ca verweisen auf dasselbe Objekt')

#--------------------------------------------------------------------------------------------#

#!Liste, Tumpel (einfache Liste, kann nicht geändert werden), Set
i, k, l = ['eine', 'Liste'], ('ein', 'Tupel'), {'ein', 'Set'}

print(i, k, l)

#--------------------------------------------------------------------------------------------#

#!Input verarbeitet Texteingaben
#hobby = input("Was ist dein Hobby:   ")
#print("Niklas Hobby lautet:", hobby)

#!Input mit einer Zahl statt Texteingabe
#z = int(input("Gibst du bitte eine Zahl ein:   "))
#print("Die Zahl lautet:", z)

#--------------------------------------------------------------------------------------------#

#!Datentyp erkennen mit type
xy = 3; 
print(type(xy))

#!Datentyp erkennen mit isistance (zu verwenden)
s = 'abc'
print(isinstance(s, str))
print(isinstance(s, int))

#--------------------------------------------------------------------------------------------#

#!Angabe des vorgesehenen Datentyps (Type Annotations)
msg: str = 'Wichtige Nachricht!'
s: str = 'Kadse'
i: int = 123

#!Die Variabeln können einfach überschrieben werden, da es für Python keine bindende Wirkung 
#!von den oben geschriebenen Variabeln gibt (die Informationen werden als Kommentare betrachtet)

i = 'wow'
s = 123

print(msg, i, s)


#--------------------------------------------------------------------------------------------#

#!Typumwandlung
ab = 3
cd = 2.4
ef = ab * cd

print(ef)


#!Integer und String zusammenführen
xd = 123
dx = 'abc'
dxd = dx + str(xd)

print(xd, dx, dxd)

#--------------------------------------------------------------------------------------------#

#!Gültikeitsbereich von Variabeln

#!Das if Statement ist erfüllt, daher wird die Variable x ausgegeben
if 1:
    x = 1
    print(x)

#!Das if Statement ist nicht erfüllt, da i nicht definiert wurde
if 0:
    i = 1
    print(i)


#!Die if Statements sind beide nicht erfüllt, da wie oben q nicht definiert wurde
#xi = None

#if 0:
#    q = 1
#    
#if x != None:
#    print(q)

#!Del löscht die benannte Variable 
#test = 34
#del test
#print(test)

#--------------------------------------------------------------------------------------------#

#!In Operator (nur in der Python Shell möglich)
lst2 = [1, 4, 5, 6, 7,8 ]

15 in lst2
9 in lst2

#--------------------------------------------------------------------------------------------#

#!Boolesche Werte
xc = True
xd = 7==8

print(xc)
print(not xd)
 
print(type(xc))

#--------------------------------------------------------------------------------------------#















