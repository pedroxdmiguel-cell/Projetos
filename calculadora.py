

import tkinter as tk

# Janela principal
root = tk.Tk()
root.title("Calculadora Glass")
root.geometry("300x350")
root.configure(bg="#0f172a")
root.resizable(False, False)

# Frame principal (efeito glass)
glass = tk.Frame(
    root,
    bg="#1e293b",
    bd=0
)
glass.place(relx=0.5, rely=0.5, anchor="center", width=320, height=500)

# Display
display = tk.Entry(
    glass,
    font=("SF Pro Display", 28),
    justify="right",
    bd=0,
    bg="#334155",
    fg="white",
    insertbackground="white"
)
display.place(x=20, y=30, width=280, height=70)

# Estilo dos botões
btn_bg = "#475569"
btn_fg = "white"

botoes = [
    ['C', '±', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

y = 130

for linha in botoes:
    x = 20

    for texto in linha:
        largura = 60

        if texto == '0':
            largura = 130

        botao = tk.Button(
            glass,
            text=texto,
            font=("SF Pro Display", 18, "bold"),
            bg=btn_bg,
            fg=btn_fg,
            activebackground="#64748b",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        botao.place(x=x, y=y, width=largura, height=60)

        x += largura + 10

    y += 75

root.mainloop()