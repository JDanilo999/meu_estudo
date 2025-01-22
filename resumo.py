from time import sleep
a = str(input("digite qualquer palavra")).strip().lower()
b = a.split()
c = '_'.join(b)
d = a.find('i')+1
print('carregando..')
sleep(1)
e = 'furico' in a
f = a.replace('carai','boba')
g = f.replace('porra','boba')
h = g.count('a')
print('na frase: {} existe {} letras a'.format(g,h))