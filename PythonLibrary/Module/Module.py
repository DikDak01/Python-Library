#verschiedene Import-Anweisungen
#!Das Modul time kann zb das jeweilige Datum in der Zeitzone anzeigen
import time, locale

#!Alle Funktionen in diesem Modul können genutzt werden, mit name.funktionsname()
import os 

#!Mehrere Module importieren
import sys, _osx_support, sysconfig

#!Importiert das Modul OS aber die Funktionen werden verkürzt geschrieben o.funktionsname()
import os as o

#!Bei dieser Variante kann man Funktionen & Klassen ohne Voranstellen des Modulnamens einsetzen
#from mailbox import n1, n2 

#!Diese Variante importiert alle Symbole deren Name nicht mit __ beginnt
#from mock import *

#!VORSICHT: Bei dieser Variante das es unbeabsichtig gleichnamige Variabeln überschreiben!!!

#!Das Operator Modul enthält zu allen Python-Operatoren entsprechende Funktion
import operator

#!veränderliche Daten kopieren 
#!Copy-Modul für eine unabhängige Kopie von veränderlichen Daten zu erstellen
import copy

#!Ganzzahlige Zufallszahlen mit dem Random Modul
#import random

#!nur die Funktion randint von dem Random Modul
from random import randint

#!von dem Random Module nur die Funktionen: random und uniform importieren
from random import random, uniform

#!Math Modul für Funktionen wie Sinus, Cosinus, Tangens und Quadratwurzel
import math

#!Das Math Modul kommt mit komplexen Zahlen nicht zurecht deshalb ist es besser das Modul C-Math zu nutzen
import cmath

#!Das Modul Fractions stellt Funktionen zur Verfügung die es ermöglicht ohne Rundungsfehler 
#!mit rationalen Zahlen bzw. Brüchen zu arbeiten (rationale Zahlen)
from fractions import Fraction

#!Solange nicht 28 Stellen überschritten werden kann das Dezimal Modul exakt und ohne Rundungsfehler
#!das Ergebnis anzeigenA
from decimal import *

#!Das locale Modul berücksichtigt landesspezifische Einstellungen (statt Komma einen Dezimalpunkt)
import locale
from unicodedata import name

#-----------------------------------------------------------------------------------------------------#

#!Input String
name = input("Write your Name:")

#!Zeigt das Datum in der jeweiligen Zeitzone an
locale.setlocale(locale.LC_ALL, '') #~Nutzt die Sprache des Betriebssystems
time = time.strftime('Heute ist %A, der %d. %B.') #~time.strftime (Methode) formatiert Datum und Uhrzeit in der jeweiligen Landessprache 

print(time)

#-----------------------------------------------------------------------------------------------------#

#!Gibt den Pfad von Python an mithilfe des Moduls sys
print(sys.path)

#-----------------------------------------------------------------------------------------------------#

#!Operator Modul
operator.mul(operator.add(2, 3), 7) #~(2+3) * 7

#-----------------------------------------------------------------------------------------------------#

#!Beispiel mit copy
p = [1,2,3,4]

#!q verweist hier auf eine unabhängige Kopie von p 
q = copy.copy(p)

#!ändert das Listenelement von p, q bleibt unverändert
p[1] = 23

print(p, q)

#-----------------------------------------------------------------------------------------------------#

#!Beispiel mit deepcopy
o = [1,2,[5,6]]
i = copy.deepcopy(o)

o[0] = 4

print(o, i)

#-----------------------------------------------------------------------------------------------------#

#!Zufallszahlen mit Random Modul
print(randint(0, 7)) #~Zufallszahl zwischen 0 - 7

#!Zahlen zwischen 0 und 1
print(random())

#!Zahlen zwischen 2.0 und 7.5
print(uniform(2.0, 7.5))

#-----------------------------------------------------------------------------------------------------#

#!Kreisteilungszahl berechnen
print(math.sqrt(2))

#!Sinus berechnen
print(math.sin(4))

#-----------------------------------------------------------------------------------------------------#
#!Kreisteilungszahl mit cmath berechnen
cmath.sqrt(-1)

#-----------------------------------------------------------------------------------------------------#

#!Bruch ohne Rundungsfehler berechnen mit Fraction (Rationale Zahlen)
x = Fraction(1 / 3)
z = Fraction(1 / 5)

print(x + z)

#!Zeichenketten formatieren und konvertieren

#!Der Bruch als Fraction Objekt
x2 = Fraction('1/3') 
print(x2) 

#!maschinenlesbare Form
xl = repr(x2)
print(xl)

#!Rückwandlung in ein Objekt
xe = eval(xl)
print(xe)
#-----------------------------------------------------------------------------------------------------#

#!Dezimalzahlen
a = Decimal(0.7)
b = Decimal(0.9)
c = a + Decimal(0.2)
d = b * Decimal(0.4)

print(a, b, c, d)

print(c == d)

print(a - b)

#!Frei einstellbare Stellenanzahl mit getcontext().prec = n
getcontext().prec = 45
print(Decimal(1) / Decimal(7))

#-----------------------------------------------------------------------------------------------------#

#!Daten formatieren

print('%language) hat %(number) im Wort.' %{'language': "Python", "number": 2}) #? TODO: siehe Ausgabe & erweitern

#-----------------------------------------------------------------------------------------------------#


