dados = list()
lista = list()
peso = list()
nome = list()
maior = list()
menor = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('peso: ')))
    lista.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? sim/não')).strip().lower()[0]
    if resp == 'n':
        break
cont = 0
for p in lista:
    peso += [p[1]]
    nome += [p[0]]
    if p[1] >= 100:
        maior.append(p[0])
    elif p[1] <= 70:
        menor.append(p[0])
print(f'Foram digitadas: {len(nome)} Pessoas')
print(f'O maior peso foi de {max(peso)} de. {maior}')
print(f'O menor peso foi de {min(peso)} de. {menor}')
