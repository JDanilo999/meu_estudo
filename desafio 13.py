nome = input('nome completo').strip()
p = nome.split()
u = p[len(p)-1]
print('primeiro nome {} e o ultimo nome {}'.format(p[0],u))