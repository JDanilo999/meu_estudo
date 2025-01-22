nome = str(input('digite alguma coisa')).strip()#strip para tirar os espaços.
a = nome.lower() # deixar tudo menor
#a = nome.upper() Deixa tudo menor
#a = nome.captalize() deixa a primeira letra maiuscula
#a = nome.title() deixa as primeiras letras da palavra maiuscula
b = a.count('a') #quantos numeros tem uma letra especifica
c = a.find('a') #indica a posição de uma letra especificada
# c = a.rfind('a') indica a ultima posição
d = a.split() #divide a frase
# d = a.join() junta a frase
e = 'santos' in a # se a palavra santos existe na frase especificada
f = len(a) - a.find(' ') #conta quantas caracteres tem na frase. use len() ou ==
g = a.replace('Buraco', 'em' ) #substitui uma palavra na outra






