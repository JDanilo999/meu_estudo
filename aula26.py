termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
rep = 0
print('{} - '.format(termo), end = '')
while rep <= 9:
    termo = termo + razao
    rep += 1
    print('{} - '.format(termo), end = '')
print('FIM')
