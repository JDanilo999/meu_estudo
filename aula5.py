nota = float(input('Digite sua nota'))
nota2 = float(input('digite a outra nota'))
media = (nota + nota2)/2
if media <= 5.0:
    print('VOCÊ ESTÁ REPROVADO HAHAHAHA!!!!!!!. SUA MÉDIA FOI DE {:.1f}'.format(media))
elif media <= 6.9:
    print('VOCÊ ESTÁ EM RECUPERAÇÃOOOOOOOOOO!!!!!! ESTUDE MAIS. SUA MÉDIA FOI DE {:.1f}'.format(media))
elif media > 7.0 or media == 10.0:
    print('você passou, sua média é de {:.1f}'.format(media))
