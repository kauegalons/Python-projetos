import tkinter as tk
from tkinter import messagebox

class DraggableWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Janela Movível Teste")
        self.geometry("300x200")

        # Inicializar as coordenadas do mouse
        self.mouse_x = 0
        self.mouse_y = 0

        # Adicionar um rótulo para mostrar instruções
        self.label = tk.Label(self, text="vc quer levar o lucky passear hoje?")
        self.label.pack(pady=20)

        # Adicionar os botões "Sim" e "Não"
        btn_yes = tk.Button(self, text="Sim", width=10, command=self.on_yes)
        btn_yes.pack(side=tk.LEFT, padx=10, pady=10)

        btn_no = tk.Button(self, text="Não", width=10, command=self.on_no)
        btn_no.pack(side=tk.RIGHT, padx=10, pady=10)

        # Configurar eventos de arrastar para a janela
        self.label.bind("<ButtonPress-1>", self.start_drag)
        self.label.bind("<B1-Motion>", self.drag)

    def start_drag(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y

    def drag(self, event):
        # Calcular o deslocamento
        delta_x = event.x - self.mouse_x
        delta_y = event.y - self.mouse_y

        # Mover a janela para a nova posição
        new_x = self.winfo_x() + delta_x
        new_y = self.winfo_y() + delta_y
        self.geometry(f"+{new_x}+{new_y}")

    def on_yes(self):
        messagebox.showinfo("Resposta", "Você escolheu 'Sim'")
        self.destroy()

    def on_no(self):
        messagebox.showinfo("Resposta", "Você escolheu 'Não'")
        self.destroy()

if __name__ == "__main__":
    app = DraggableWindow()
    app.mainloop()
    