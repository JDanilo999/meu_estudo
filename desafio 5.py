from random import choice
a1 = input('diga um nome')
a2 = input('diga outro')
a3 = input('diga mais um')
v = [a1,a2,a3]
#s = choice(v)
print('a pessoa sorteada foi {}'.format(choice(v)))
