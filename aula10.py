
v = float(input('Valor do produto'))
print(15 * '===~===')
print('PIX A VISTA, 10% DE DESCONTO. CARTAO A VISTA, 5% DE DESCONTO.')
print('CARTAO PARCELADO EM 2X, VALOR DO PRODUTO SEM JUROS.')
print('CARTAO PARCELADO EM 3X, 20% DE JUROS.')
print(15 * '===~===')
print('Escolha a forma de pagamento')
forma = str(input('(PIX),(CARTAO),(CARTAO2X) OU (CARTAO3X)')).upper()
pix = v - (v * 10 / 100)
ca = v - (v * 5 / 100)
ca2x = v
ca3x = v * 20 / 100 + v
if forma == 'PIX':
    print('O valor a 10% de desconto deu {} reais'.format(pix))
elif forma == 'CARTAO':
    print('O valor a 5% de desconto deu {} reais'.format(ca))
elif forma == 'CARTAO2X':
    print('O valor deu {} reais, em parcelas de {} '.format(ca2x, ca2x / 2))
elif forma == 'CARTAO3X':
    parcelas = int(input('QUANTAS PARCELAS?'))
    print('O valor a 20% de juros deu {} reais, em parcelas de {}x de {}'.format(ca3x,parcelas,ca3x / parcelas))
else:
    print('OPÇÃO INVALIDA')