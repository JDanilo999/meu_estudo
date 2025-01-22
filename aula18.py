f = str(input('Digite a frase:')).strip().lower()
f2 = f[::-1].split()
f3 = ''.join(f2)
f4 = f.replace(' ','')
print(f3)
if f4 == f3:
    print('A Frase é um Polídromo')
else:
    print('A Frase não é um Polídromo')
