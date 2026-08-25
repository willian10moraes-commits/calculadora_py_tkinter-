#fazendo a importação do tkinter
from tkinter import *


#cores
cor_preta="#080808"
cor_branca="#f7fafa"
cor_amarelo="#faf370"
cor_vermelha="#470e0e"
cor_cinza="#6b6b6b"

#criando a janela inicial
janela=Tk()#metodo
janela.title("calculadora")#titulo
janela.geometry("240x316")#dimenções lxa
janela.config(background=cor_preta)

#criando frames
frame_visor=Frame(janela,width=240,height=50,bg=cor_preta)
frame_visor.grid(row=0,column=0)

frame_teclado=Frame(janela,width=240,height=270,bg=cor_preta)
frame_teclado.grid(row=1,column=0)

todos_valores=""

#criando função

def entrar_valor(a):
    global todos_valores
    todos_valores=todos_valores+str(a)


    #passando valor para tela
    app_label.config(text=todos_valores)

#função para calcular

def calcular():
    global todos_valores
    if todos_valores=="":
        return
    resultado=eval(todos_valores)
    todos_valores=str(resultado)

    app_label.config(text=todos_valores)

#função apagar 1
def apagar():
    global todos_valores

    todos_valores = todos_valores[:-1]

    app_label.config(text=todos_valores)

#função limpar tela

def limpar_tela():
    global todos_valores
    todos_valores=""
    app_label.config(text=todos_valores)

#criando label

app_label=Label(frame_visor,text="",width=16,height=2,padx=7,relief=FLAT,anchor="e",justify="right",font=('Ivi 18'),bg=cor_preta,fg=cor_branca)
app_label.place(x=0,y=0)

#criando botoes

b1=Button(frame_teclado,command=limpar_tela,text="C   ",width=11,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b1.place(x=0,y=0)
b2=Button(frame_teclado,command=lambda:apagar(),text="⌫",width=5,height=2,fg=cor_vermelha,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b2.place(x=120,y=0)
b3=Button(frame_teclado,command=lambda: entrar_valor("/"),text="/",width=5,height=2,fg=cor_branca,bg=cor_vermelha,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b3.place(x=180,y=0)

b4=Button(frame_teclado,command=lambda: entrar_valor("7"),text="7",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b4.place(x=0,y=53)
b5=Button(frame_teclado,command=lambda: entrar_valor("8"),text="8",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b5.place(x=60,y=53)
b6=Button(frame_teclado,command=lambda: entrar_valor("9"),text="9",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b6.place(x=120,y=53)
b7=Button(frame_teclado,command=lambda: entrar_valor("*"),text="*",width=5,height=2,fg=cor_branca,bg=cor_vermelha,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b7.place(x=180,y=53)

b8=Button(frame_teclado,command=lambda: entrar_valor("4"),text="4",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b8.place(x=0,y=106)
b9=Button(frame_teclado,command=lambda: entrar_valor("5"),text="5",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b9.place(x=60,y=106)
b10=Button(frame_teclado,command=lambda: entrar_valor("6"),text="6",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b10.place(x=120,y=106)
b11=Button(frame_teclado,command=lambda: entrar_valor("-"),text="-",width=5,height=2,fg=cor_branca,bg=cor_vermelha,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b11.place(x=180,y=106)

b12=Button(frame_teclado,command=lambda: entrar_valor("1"),text="1",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b12.place(x=0,y=159)
b13=Button(frame_teclado,command=lambda: entrar_valor("2"),text="2",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b13.place(x=60,y=159)
b14=Button(frame_teclado,command=lambda: entrar_valor("3"),text="3",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b14.place(x=120,y=159)
b15=Button(frame_teclado,command=lambda: entrar_valor("+"),text="+",width=5,height=2,fg=cor_branca,bg=cor_vermelha,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b15.place(x=180,y=159)

b16=Button(frame_teclado,command=lambda: entrar_valor("0"),text="0   ",width=11,height=2,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b16.place(x=0,y=212)
b17=Button(frame_teclado,command=lambda: entrar_valor("."),text=".",width=5,height=2,fg=cor_preta,bg=cor_cinza,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b17.place(x=120,y=212)
b18=Button(frame_teclado,command=calcular,text="=",width=5,height=2,fg=cor_branca,bg=cor_vermelha,font=('Ivi 13 bold'),relief=RAISED,overrelief=RIDGE)
b18.place(x=180,y=212)



janela.mainloop()
