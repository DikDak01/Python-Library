#Dateien lesen, schreiben, öffnen


#Datei öffnen

f = open('out.txt', 'w')
print(1, 2, 3, file=f)
f.close()