alt = float(input('digite sua altura'))
peso = float(input('digite seu peso'))
#calculo imc ==> indice de massa corporea
imc = peso/alt**2
print('massa corporea de {:.1f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 25:
    print ('Peso ideal')
elif imc <= 30:
    print('sobrepeso')
elif imc <= 40 :
    print('obesidade')
else:
    print('obesidade morbida')

#José Danilo Gouveia Santos