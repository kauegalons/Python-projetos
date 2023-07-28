import tkinter as tk
from tkinter import messagebox

def on_yes():
    messagebox.showinfo("Resposta", "Você escolheu 'Sim'")
    root.destroy()

def on_no():
    messagebox.showinfo("Resposta", "Você escolheu 'Não'")
    root.destroy()

# Criar a janela principal
root = tk.Tk()
root.title("Janela com Botões")

# Criar os botões "Sim" e "Não"
btn_yes = tk.Button(root, text="Sim", width=10, command=on_yes)
btn_yes.pack(pady=10)

btn_no = tk.Button(root, text="Não", width=10, command=on_no)
btn_no.pack(pady=10)

# Iniciar o loop principal da aplicação
root.mainloop()
