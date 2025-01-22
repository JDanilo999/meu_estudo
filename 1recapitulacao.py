l = input('Está preparado para a recapitulação?')
print('Bom, aprendi os seguintes comandos')
print('print(''.format())')
print('tipos primitivos')
print('str==string, floot==numeros flutuantes tipo 2.5, boat==espaco vazio ou cheio e int==numeros inteiros')
print('comandos como type() verifica o tipo primitivo e .is, mostra na tela com  comando print')
print('comandos basicos')
print('(,)==junta e (=) == recebe (==) == igual (#) == comentario')
print('Expressões Aritmetica')
print('é necessario sempre respeitar a ordem da aritmetica')
print('resolvendo primeiro na ordem a seguir')
print('()(conchetes 1 )')
print('**(potencia 2 )')
print('*, / , // , % (multiplicação, divisão, divisão inteiro e a sobra da divisão 3)')
print('+ , _ (soma e diminuir 4)')
print('Vou fazer uma simples calculadora da tabuada do 9 com potencias e sobras na ordem')
n = int(input('digite qualquer numero para a tabuada do nove'))
a = n**9
b = 9*n
c = 9/n
d = 9//n
f = 9%n
g = 9+n
h = n-9
print('a potencia de 9 elevado a {} deu {}'.format(n,a))
print ('a multiplicação de 9 vezes {} deu {}'.format(n,b))
print('A divisão de 9 por {} deu {}'.format(n,c))
print('A divisão inteira de 9 por {} deu {} e sobrou {}'.format(n,d,f))
print('A soma de 9 e {} deu {}'.format(n,g))
print('A diminuição de 9 por {} deu {}'.format(n,h))