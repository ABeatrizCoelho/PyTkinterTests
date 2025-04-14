import tkinter as tk
from tkinter import messagebox

def submit():
    nome = entry_nome.get()
    email = entry_email.get()

    linguagem_preferida = linguagem_var.get()


    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Linguagem preferida: {linguagem_preferida}")

    messagebox.showinfo("Dados Submetidos:", f"Nome: {nome}\nE-mail: {email}\nLinguagem preferida: {linguagem_preferida}")

# Criação da janela principal
root = tk.Tk()
root.title("Formulário de Cadastro")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Cria um frame para conter os widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Criação dos rótulos e campos de entrada
label_nome = tk.Label(frame, text="Nome:")
label_nome.grid(row=0, column=0, sticky="w", padx=5, pady=5)

#Campo de entrada para o nome
entry_nome = tk.Entry(frame)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

# Criação do rótulo
label_email = tk.Label(frame, text="E-mail:")
label_email.grid(row=1, column=0, sticky="w", padx=5, pady=5)
#Campo de entrada para o e-mail
entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=1, padx=5, pady=5)

# Criação do rótulo para email
email_label = tk.Label(frame, text="E-mail:")
email_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
# Campo de entrada para o e-mail
entry_email = tk.Entry(frame)
entry_email.grid(row=1, column=1, padx=5, pady=5)

# Variavel para armazenar a linguagem preferida
linguagem_var = tk.StringVar(value="Python")

# Criação dos botões de opção (radio buttons)
radio_python = tk.Radiobutton(frame, text="Python", variable=linguagem_var, value="Python")
radio_python.grid(row=2, column=0, sticky="w", padx=5, pady=5)

radio_java = tk.Radiobutton(frame, text="Java", variable=linguagem_var, value="Java")
radio_java.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#Botão de envio
botao_submit = tk.Button(frame, text="Enviar", command=submit) #callback
botao_submit.grid(row=3, columnspan=2, pady=10)

# Inicia o loop principal da aplicação
root.mainloop()


