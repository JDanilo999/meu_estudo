termo = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
rep = 0
parar = 0
contagem = 1
cont = 0
print(termo)
while rep <= 9:
    termo = termo + razao
    rep += 1
    print(termo)
contagem = int(input('Quer continuar? digite (1) para sim ou (0) para nao)'))
if contagem == 1:
    while contagem > 0:
        contagem = int(input('Quer mostrar mais quantos termos(digite 0 para parar)?'))
        rep = 0
        while rep <= contagem - 1:
            termo = termo + razao
            rep += 1
            print(termo)
if contagem != 0 or 1:
    print('Opção invalida Tente Novamente')
