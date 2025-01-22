soma = 0
num = 0
for par in range(1,6+1):
    num = int(input('Digite:'))
    par1 = num % 2
    if par1 == 0:
       soma += num
print(soma)
