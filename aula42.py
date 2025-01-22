lista = ('Lápis',1.75,'Borracha',2.00,'Caderno',15.90,'Estojo',25.90)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end= ' ')
    else:
        print(f'{lista[pos]:>4.2f}R$')
