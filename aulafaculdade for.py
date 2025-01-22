filmes = ['Velozes e Furiosos','Chihiro','Django','Vingadores','Homem Aranha']
print('Classifique os filmes de um a 5 estrelas. caso queira parar aperte 0')
for f in filmes:
    c = int(input('Nota para {}'.format(f)))
    if c == 0:
        print('que pena que você quer parar')
        break
    print('Você deu nota {} para {}'.format(c, f))
    if c > 5:
        print('e a classificou com nota invalida, tente novamente.')
        break
print('Obrigado por sua Atenção')