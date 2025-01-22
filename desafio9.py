cidade = input('digite uma cidade')
d = cidade.split()
#v =d[0]
print('Existe Santos em {}? {}'.format(cidade,d[0] in ('Santos')))