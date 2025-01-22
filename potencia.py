base = int(input("Digite a base: "))
expoente = int(input("digite o expoente"))
potencia = 1
for cont in range(1,expoente + 1):
    potencia *= base
    print(potencia)