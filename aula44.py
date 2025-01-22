lista = list()
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}:')))
print(lista)
maior = max(lista)
menor = min(lista)
print(f'O maior numero digitado foi {maior} na posição:', end='')
for c, v in enumerate(lista):
    if maior == v:
        print(f'{c}...',end=' ')
print(f'\nO menor numero digitado foi {menor} na posição:', end='')
for c, v in enumerate(lista):
    if menor == v:
        print(f'{c}...',end=' ')
