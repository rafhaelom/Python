# ---------- Bibliotecas ----------
from tkinter import *
from tkinter import messagebox # messagebox é a biblioteca de mensagem do tkinter.
from tkinter import ttk # ttk é a biblioteca gráfica do tkinter.
import psycopg2

# ---------- Objeto da janela principal ----------
janela = Tk()

# ---------- Widgets - componentes da janela ----------
# --- Atributos ---
janela.title("Medidor") # Título da janela.
janela.configure(bg="white") # Cor do backgroud da janela.
janela.resizable(width=False, height=False) # Tira a responsividade da janela.

# --- Frames ---
cima = Frame(janela, width=800, height=397, bg="#64F0DA", relief="raise")
baixo = Frame(janela, width=800, height=100, bg="#50D99E", relief="raise")

# --- botoes ---
sairButton = ttk.Button(baixo, text="Sair", width=20)
cadastrarButton = ttk.Button(cima, text="Cadastrar", width=100)
infoButton = ttk.Button(cima, text="Informações", width=100)

# ---------- Layout - Gereciador de componetes da janela ----------
# --- frames ---
cima.pack(side=TOP)
baixo.pack(side=BOTTOM)
# --- botões ---
sairButton.place(x=330, y=25, height=50)
cadastrarButton.place(x=100, y=70, height=100)
infoButton.place(x=100, y=235, height=100)

# ---------- Tamanho da janela ----------
# --- widgth x heigth + left + topo ---
janela.geometry("800x500+250+110")

janela.mainloop()