val = str(input('Digite sua expressão')).strip()
a = ' '.join(val)
lista = a.split()
d = lista.count('(')
f = lista.count(')')
if d == f:
    print('Sua expressão está certa')
else:
    print('Sua expressão está errada')
