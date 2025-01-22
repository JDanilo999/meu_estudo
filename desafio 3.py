from math import hypot
c1 = float(input("cateto oposto"))
c2 = float(input('cateto adjecente'))
hipo = hypot(c1, c2)
print('O cateto oposto {}, mais o adjecente {} deu o comprimento de {:.2f}'.format(c1,c2,hipo))