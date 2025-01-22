cont = soma = 0
while True:
    num = int(input('Digite os numeros'))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'Foram digitados {cont} numeros e a soma entre eles foi de {soma}')