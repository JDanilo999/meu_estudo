frase = input('Digite uma frase').strip()
h = frase.lower()
f = h.count('a')
p = h.find('a')+1
u = h.rfind('a')+1
print('a frase apresenta {} letras a. e {} caracteres ao todo'.format(f,len(frase) - frase.count(' ')))
print('a posição da primeira letra a é {}'.format(p))
print('a ultima posição da letra a é {}'.format(u))


