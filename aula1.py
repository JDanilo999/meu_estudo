vc = float(input('Qual é o valor da casa?'))
s = float(input('Qual é o valor do seu salario?'))
anos = int(input('Quantos anos você irá pagar a casa?'))
m = anos * 12
p = vc / m
if p > 3 * s / 10 :
    print('Valor negado')
else:
    print('valor aprovado. suas parcelas seram de {:.2f} Reais! por {:.2f} meses'.format(p,m))
