
inicio = int(input('Inicio:'))
final = int(input('Final:'))
passos = int(input('Pular:'))
somar = 0
for t in range(inicio,final+1,passos):
    print(t)
    somar += t
print('A soma entre todos esses numeros foi de {}'.format(somar))
