soma = 0
tot = 0
for impar in range(1,500+1,2):
    if impar % 3 == 0:
        soma += impar
        tot = tot + 1
print('A soma entre {} valores multiplus de 3 foi de {}'.format(tot,soma))