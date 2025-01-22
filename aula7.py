l1 = int(input('digite o primeiro lado do triangulo.'))
l2 = int(input('digite o segundo lado.'))
l3 = int(input('digite o terceiro lado.'))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l2 + l1:
    if l1 == l2 == l3:
        print('O triangulo é um equilatero')
    elif l1 == l2 != l3 or l2 == l3 != l1 or l1 == l3 != l2:
        print('o triangulo é um isosceles')
    elif l1 != l2 != l3 :
        print('o triangulo é um escaleno')
else:
    print('OS SEGMENTOS ACIMA NÃO PODEM FORMAR UM TRIANGULO')