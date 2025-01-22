ficha = list()
conti2 = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome ,[nota1, nota2], media]) #aqui eu posso organizar os [] dentro da lista da forma que eu quiser
    conti = str(input('Quer continuar? sim/não')).lower()[0]
    if conti == 'n':
        break
print(f'{"No.":<4} {"Nome":<10} {"Media":>8}')#posso usar uma formataçao para organizar melhor os valores que possuem o numero de letras diferentes
for p, v in enumerate(ficha):
    print(f'{p:<4} {v[0]:<10} {v[2]:>8}')
while conti2 != 999:
    conti2 = int(input('Quer mostrar a nota de qual aluno?(digite 999 para parar)'))
    if conti2 <= len(ficha) - 1:# aqui foi ultilizado uma condiçao de escolha, onde o if so aparece se o conti2 for menor que o numeros de elementos presente na lista
        print(f'Notas de {ficha[conti2][0]} foram {ficha[conti2][1]}')#aqui coloquei o conti2 dentro dos colchetes para escolher qual informaçao vai aparecer na print da posiçao[0] que eu escolhi(ela representa os nomes)

