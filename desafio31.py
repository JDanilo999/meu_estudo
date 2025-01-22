num = float(input('Digite quantos KM foi rodado.'))
km1 = 0.50*num
km2 = 0.45*num
if num <= 200:
    print('Você irá pagar {}'.format(km1))
else:
    print('Você passou de 200KM, e seu valor deu {:.2f}'.format(km2))