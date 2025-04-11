from tkinter import *

janela = Tk()
janela.title("Exemplo de Place")

# Criando um rótulo
rotulo = Label(janela, text="Posicionamento Absoluto")
rotulo.place(x=50, y=50)

# Criando um botão com posicionamento relativo
botao = Button(janela, text="Clique-me!")
botao.place(relx=0.5, rely=0.5, anchor=CENTER)

janela.mainloop()

