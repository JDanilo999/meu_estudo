from tkinter import *
def dell ():
    visor.delete(0,END)

def soma():
    pnum = visor.get()
    global prinum
    global matematica
    matematica = 'soma'
    prinum = int(pnum)
    visor.delete(0, END)

def mult():
    pnum = visor.get()
    global prinum
    global matematica
    matematica = 'mult'
    prinum = int(pnum)
    visor.delete(0,END)

def div():
    pnum = visor.get()
    global prinum
    global matematica
    matematica = 'div'
    prinum = int(pnum)
    visor.delete(0,END)

def menos():
    pnum = visor.get()
    global prinum
    global matematica
    matematica = 'menos'
    prinum = int(pnum)
    visor.delete(0,END)

def numero(numero):
    atual = visor.get()
    visor.delete(0,END)
    visor.insert(END,str(atual) + str(numero))

def igual():
    segnum = visor.get()
    visor.delete(0,END)
    if matematica == 'soma':
        visor.insert(0,prinum + int(segnum))
    elif matematica == 'mult' :
        visor.insert(0, prinum * int(segnum))
    elif matematica == 'menos':
        visor.insert(0, prinum - int(segnum))
    elif matematica == 'div':
        visor.insert(0, prinum / int(segnum))
    else:
        visor.insert('Error')

janela = Tk()
janela.title('Calculadora')
janela.resizable(False,False)
janela.geometry('280x380')
janela.config(bg='black')
visor = Entry(janela,bg='darkgray',width=20)
visor.config(bg='white',width=20,font='arial')
visor.grid(column= 0, row=0,columnspa=4,padx=25,pady=25)

num7 = Button(janela,text='7',bg='gray',padx=25,pady=25,command= lambda:numero(7))
num7.grid(column= 0, row=1)

num8 = Button(janela,text='8', bg='gray',padx=30,pady=25,command= lambda:numero(8))
num8.grid(column= 1, row=1 )

num9 = Button(janela,text='9', bg='gray',padx=25,pady=25,command= lambda:numero(9))
num9.grid(column= 2, row=1)

num4 = Button(janela,text='4', bg='gray',padx=25,pady=33,command= lambda:numero(4))
num4.grid(column= 0, row=2)

num5 = Button(janela,text='5', bg='gray',padx=30,pady=33,command= lambda:numero(5))
num5.grid(column= 1, row=2)

num6 = Button(janela,text='6', bg='gray',padx=25,pady=33,command= lambda:numero(6))
num6.grid(column= 2, row=2)

num3 = Button(janela,text='3', bg='gray',padx=25,pady=25,command= lambda:numero(3))
num3.grid(column= 2, row=3)

num2 = Button(janela,text='2', bg='gray',padx=30,pady=25,command= lambda:numero(2))
num2.grid(column= 1, row=3)

num1 = Button(janela,text='1', bg='gray',padx=25,pady=25,command= lambda:numero(1))
num1.grid(column= 0, row=3)

num0 = Button(janela,text='0', bg='gray',padx=30,pady=25,command= lambda:numero(0))
num0.grid(column= 1, row=4 )

div = Button(janela,text='/', bg='darkorange',padx=28,pady=25,command=div)
div.grid(column= 3, row=1)

mult = Button(janela,text='x', bg='darkorange',padx=28,pady=33,command=mult)
mult.grid(column= 3, row=2)

menos = Button(janela,text='-', bg='darkorange',padx=29,pady=25,command=menos)
menos.grid(column= 3, row=3 )

soma = Button(janela,text='+', bg='darkorange',padx=27,pady=25,command=soma)
soma.grid(column= 3, row=4 )

igual = Button(janela,text='=', bg='darkorange',padx=25,pady=25,command=igual)
igual.grid(column= 2, row=4)

delet = Button(janela,text='CE', bg='darkorange',padx=22,pady=25,command=dell)
delet.grid(column= 0, row=4)

janela.mainloop()
