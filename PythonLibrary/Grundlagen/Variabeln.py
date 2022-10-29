
#!mutable und immutable Datentypen (veränderlich und unveränderliche Datentypen)

#!Beispiel mit Zahlen

#!Variable b hat immer noch die Zahl 3 deklariert, da a erst nach der Übergabe von b = a auf 4
#!deklariert wurde (a und b sind unabhängig voneinander)

a = 3
b = a
a = 4

print(a, b)

#!Beispiel mit Listen

#!siehe obere Tabellen, diese 2 Listen (k, m) sind veränderlich
#!da m durch k erzeugt wurde, wird bei jeder Änderung von k auch m verändert

k = [1, 2, 3, 4]
m = k
k[0] = 4

print(k, m)