lista2 = list()
val = str(input('Digite sua expressão')).strip()
a = ' '.join(val)
lista = a.split()
d = lista.count('(')
f = lista.count(')')
for simb in lista:
    if '(' == simb:
        lista2.append('(')
    if ')' == simb:
        lista2.append(')')
if '(' == lista2[0] and ')' == lista2[-1]:
    if d == f:
        print('Sua expressão está certa')
    else:
        print('Sua expressão está errada')
else:
    print('Sua expressão está errada')
