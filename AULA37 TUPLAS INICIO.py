#lanche = ('bife','batata','banana','arroz') ---> tupla
#print(lanche)

'''lanche = ('bife','batata','banana','arroz')
print('Eu comi', end=' ')
for comida in lanche:
    print(comida, end=', ')

print('estou satisfeito!')'''

lanche = ('bife','batata','banana','arroz')
for cont in range(0,len(lanche)):
    print(f'Eu comi {lanche[cont]}')
print('estou satisfeito!')
