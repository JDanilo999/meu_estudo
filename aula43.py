palavras = ('Carro', 'Bike', 'Faca', 'Biscoito', 'Panela', 'Carne', 'Moto', 'Paralelepipado')
def vogal(a):
    if 'a' in a :
        for p in range(0,a.count('a')):
            print('a',end=' ')
    if 'e' in a :
        for p in range(0,a.count('e')):
            print('e',end=' ')
    if 'i' in a:
        for p in range(0,a.count('i')):
            print('i',end=' ')
    if 'o' in a:
        for p in range(0,a.count('o')):
            print('o',end=' ')
    if 'u' in a:
        for p in range(0,a.count('u')):
            print('u',end=' ')
            return
for p in palavras:
    print(f'\nNa palavra {p}, temos as vogais:',end=' '),vogal(p)
