# ---------- Bibliotecas ----------
from tkinter import *
from tkinter import messagebox # messagebox é a biblioteca de mensagem do tkinter.
from tkinter import ttk # ttk é a biblioteca gráfica do tkinter.
from datetime import datetime
import psycopg2

# ---------- Objeto da janela principal ----------
janela = Tk()

# ---------- Widgets - componentes da janela ----------
# --- Atributos ---
janela.title("Medidor") # Título da janela.
janela.configure(bg="white") # Cor do backgroud da janela.
janela.resizable(width=False, height=False) # Tira a responsividade da janela.

# ------------------------------------------------------------------------------ 
# -------------------------- Funcoes para eventos - events ---------------------
def click_voltar_medidor():
    print("CLICOU VOLTAR MEDIDOR!")

def click_cad_medidor_to_bd():
    print("CLICOU CADASTAR MEDIDOR!")
    data = datetime.now()
    hora = datetime.now().time().strftime("%H:%M:%S")
    peso = pesoEntry.get()
    sistolica = pasEntry.get()
    diastolica = padEntry.get()
    pulsacao = pulsacaoEntry.get()

    if (peso == "" and sistolica == "" and diastolica == "" and pulsacao == "" or peso == "" and sistolica == "" or diastolica == "" and pulsacao == ""or peso == "" or sistolica == "" or diastolica == "" or pulsacao == ""):
        messagebox.showerror(title="Cadastro Erro", message="Campo(s) vazio(s). Preencha todos os campos!")
    else:
        # Inserção no banco de dados
        sql = "INSERT INTO registro VALUES (default, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (data, hora, peso, sistolica, diastolica, pulsacao))
        conn.commit()

        messagebox.showinfo(title="Informação Cadastro", message="Dados cadastrados com Sucesso!")

# --- Frames ---
cima = Frame(janela, width=800, height=397, bg="#64F0DA", relief="raise")
baixo = Frame(janela, width=800, height=100, bg="#50D99E", relief="raise")
# --- peso ---
pesoLabel = Label(cima, text="Peso:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
pesoEntry = ttk.Entry(cima, width=30)
# --- pas ---
pasLabel = Label(cima, text="Pressão Arterial Sistólica:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
pasEntry = ttk.Entry(cima, width=30)
# --- pad ---
padLabel = Label(cima, text="Pressão Arterial Diastólica:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
padEntry = ttk.Entry(cima, width=30)
# --- pulsacao ---
pulsacaoLabel = Label(cima, text="Pulsação:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
pulsacaoEntry = ttk.Entry(cima, width=30)
# --- botoes ---
voltarButton = ttk.Button(baixo, text="Voltar", width=50, command=click_voltar_medidor)
cadastrarButton = ttk.Button(baixo, text="Cadastrar", width=50, command=click_cad_medidor_to_bd)

# ---------- Layout - Gereciador de componetes da janela ----------
# --- frames ---
cima.pack(side=TOP)
baixo.pack(side=BOTTOM)
# --- peso ---
pesoLabel.place(x=55, y=20)
pesoEntry.place(x=150, y=26, height=30)
# --- pas ---
pasLabel.place(x=55, y=89)
pasEntry.place(x=440, y=95, height=30)
# --- pad ---
padLabel.place(x=55, y=158)
padEntry.place(x=460, y=164, height=30)
# --- pulsacao ---
pulsacaoLabel.place(x=55, y=227)
pulsacaoEntry.place(x=210, y=233, height=30)
# --- botões ---
voltarButton.place(x=50, y=25, height=50)
cadastrarButton.place(x=440, y=25, height=50)

# ------------------------------------------------------------------------------ 
# ------------------------------- Banco de dados ------------------------------- 
print("\nAbrindo e criando conexão com o Banco!\n")
# Conecção com o Banco de Dados PostgreSQL
DB_HOST = "localhost"
DB_USER = "user_name"
DB_PASS = "password"
DB_NAME = "postgres"

# Tratamento de exceções(erros)
try:
    # Faz uma conexão, se não puder ser feita haverá uma exceção.
    conn = psycopg2.connect(
        host= DB_HOST, 
        database= DB_NAME,
        user= DB_USER,
        password= DB_PASS)
    
    # conn.cursor() retornará um objeto do tipo cur que é utilizado para fazer consultas
    cur = conn.cursor()
    print("Conectado!\n")

except (psycopg2.Error) as e:
    print("\nFalha de conexão!\n%s" % (e))

try:        
    cur.execute("""
    CREATE TABLE IF NOT EXISTS registro (
        id serial NOT NULL,
        data_reg date not null,
        hora_reg time not null,
        peso float8 not null,
        sistolica int4 not null,
        diastolica int4 not null,
        pulsacao int4 not null,
        PRIMARY KEY (id),
        foreign key (id) references usuarios(id),
        foreign key (nome) references usuarios(nome)
    );
    """)
    print("criado tabela!")
except (psycopg2.Error) as ee:
    print("\nFalha!\n%s" % (ee))

# ------------------------------------------------------------------------------

# ---------- Tamanho da janela ----------
# --- widgth x heigth + left + topo ---
janela.geometry("800x500+250+110")

janela.mainloop()