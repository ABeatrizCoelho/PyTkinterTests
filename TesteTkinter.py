from tkinter import *

# Criação da janela principal
janela = Tk()

# Define o título da janela
janela.title("OLÁ MUNDO!")

#criacao de um rótulo
rotulo = Label(janela, text= "Teste")
rotulo_personalizado = Label(janela, text="Olá, Tkinter!", font=("Arial", 16), fg="blue")

label = Label(janela, text="PRIMEIRO LABEL", font=("Arial Bold", 50), bg="green", fg="white")


#adicionar rotulo a janela
rotulo.pack(side=LEFT, padx=10)
rotulo_personalizado.pack()
label.pack()

# Define as dimensões da janela (largura x altura)
janela.geometry("700x700")

# Inicia o loop principal da aplicação
janela.mainloop()