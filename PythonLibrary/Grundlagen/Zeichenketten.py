
#!Zeichenketten
#!Zeichenketten kann man mit '' oder "", spielt aber keine Rolle 
s = 'abc'
print(type(s))

#!Lange Zeichenketten werden immer mit 3 '''' oder """ geschrieben
s = '''eine lange
    Zeichenkette'''

#--------------------------------------------------------------------------------------------#
print('--------------------------------------------------------------------------------------------')

#!Zeichenketten aneinanderfügen und vervielfältigen
sg = 'abc'
sb = 'xyc'

sx = sg + sb
sy = sg * 3 + sb * 4

print(sg, "\n", sb, "\n", sx, "\n", sy)

#--------------------------------------------------------------------------------------------#
print('--------------------------------------------------------------------------------------------')

#!Raw Zeichenketten
#!Python interpretiert \ als Sequenzen um das zu verhindern muss r vor jedem \ stehen
latexcode = r'\section{Überschrift}'

print(latexcode)

#--------------------------------------------------------------------------------------------#
print('--------------------------------------------------------------------------------------------')

#!chr und ord Funktion
#!Die chr Funktion liefert aus Zahlen einen ASCI Code
print(chr(65))

print(chr(1666))

#!Die ord Funktion liefert den umgekehrten Wert (von ASCI zu Dezimal Schreibweise)
print(ord('A'))

print(ord('$'))

#--------------------------------------------------------------------------------------------#
print('--------------------------------------------------------------------------------------------')

#!Zugriff auf Teilzeichenketten
tzk = 'oawbrikgjbsdalkjbflkajbdlkjbsdkljblakjdsb'

print(tzk[4]) #~Das 4 Element aus der Zeichenkette (Achtung: Python startet bei 0)

print(tzk[3:6]) #~gibt die Zeichenkette von der 3 bis zu 6 Stelle an

print(tzk[:4]) #~alles bis und mit der 4 Stelle

print(tzk[4:]) #~alles ab der 4 Stelle (exklusive)

print(tzk[-4]) #~Das viertletzte Zeichen

print(tzk[-4:]) #~alles ab dem viertletzten Zeichen

print('--------------------------------------------------------------------------------------------')

#!Zeichenkette mit Schrittweiten Parameter (Stride)
print(tzk[::2]) #~jedes zweite Zeichen

print(tzk[:10:2]) #~von den ersten 10 Zeichen jedes zweite

print(tzk[10::2]) #~ab dem 10. Zeichen jedes zweite

print(tzk[::-1]) #~Mit einer negativen Schrittweite kehrt man die Reihenfolge um

print(tzk[::-2]) #~jedes 2. Zeichen in umgekehrter Reihenfolge

print(tzk[0:10:-1]) #~leeres Ergebnis

print(tzk[10:0:-1]) #~vom 11. zum zweiten Zeichnis

print(tzk[:10][::-1]) #~die ersten 10 Zeichen in inverser Reihenfolge

#--------------------------------------------------------------------------------------------#
print('--------------------------------------------------------------------------------------------')

#!Funktionen uund Methoden für Zeichenketten
s = 'aöoiwehnpgoaiwenöriojndsgfkajnd'

print(len(s))

print(str(s))

print('sub' in s)

print(s.endswith('wehn'))

print(s.count('aöoi'))

print(s.expandtabs())


#--------------------------------------------------------------------------------------------#
print('--------------------------------------------------------------------------------------------')

#!Eigenschaften Zeichenketten ermitteln
print(str.isalpha('a'))

print(str.isalpha('avrelräöö'))

print(str.isalpha('abc123'))



print(str.isdigit('8'))

print(str.isdigit('a'))

print(str.isdigit('alwkenfs45'))



print(str.isalnum('sdaksjld'))

print(str.isalnum('43544'))

print(str.isalnum('adbkajd2323sdfgs'))



print(str.isascii('abv'))

print(str.isascii('3535964305'))

print(str.isascii('abdsdj34534sddfj'))



print(str.islower('ankew'))

print(str.islower('ASDKLSJDF'))



print(str.upper('SKLHADFLKD'))

print(str.isupper('alsdjfaljs'))

#--------------------------------------------------------------------------------------------#

#!Suchen und ersetzen
st = 'oghsjdfhslgkdfhgkljsdhfkjsdfhk'

print(st.find('ogh')) #~Wird an der Position 0 (Anfang) gefunden

print(st.find('ogh', 4)) #~Wird hnicht gefunden, da es ab Position 4 beginnt 

print(st.find('ogh', 7)) #~wird auch nicht gefunden, da es ab Position 7 beginnt

print(st.replace('o', 'X')) #~ TODO: st.replace nochmals anschauen

#--------------------------------------------------------------------------------------------#

