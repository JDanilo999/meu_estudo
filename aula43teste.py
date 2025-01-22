palavras = ('Carro', 'Bike', 'Faca', 'Biscoito', 'Panela', 'Carne', 'Moto', 'Paralelepipado')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as vogais:',end=' ')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(vogais,end=' ')
