from tkinter import *

janela = Tk()

#quando o botão é clicado
def botao_clicado():
    label.config(text="Botão Clicado!")

label = Label(janela, text="PRIMEIRO LABEL", font=("Arial Bold", 50), bg="green", fg="white")
label.grid(column=0, row=0)

botao = Button(janela, text="CLIQUE", command= botao_clicado)
botao.grid(column=2, row=2)

janela.mainloop()
