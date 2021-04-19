# ---------- Bibliotecas ----------
from tkinter import *
from tkinter import messagebox # messagebox é a biblioteca de mensagem do tkinter.
from tkinter import ttk # ttk é a biblioteca gráfica do tkinter.
import psycopg2

# ---------- Objeto da janela principal ----------
janela = Tk()

# ---------- Widgets - componentes da janela ----------
# --- Atributos ---
janela.title("Medição e monitoramento") # Título da janela.
janela.configure(bg="white") # Cor do backgroud da janela.
janela.resizable(width=False, height=False) # Tira a responsividade da janela.
janela.attributes("-alpha", 0.97) # Transparencia da janela.
janela.iconbitmap(default="icon/logo.ico")

# --- Carregando imagens ---
logo = PhotoImage(file="icon/logo.png")

# ------------------------------------------------------------------------------ 
# -------------------------- Funcoes para eventos - events ---------------------
def click_cadastrar():
    print("CLICOU CADASTRAR!")

    # ----- Remove Componentes -----
    # --- cadastrar ---
    cadastrarButton.place(x=5000)
    # --- entrar ---
    entrarButton.place(x=5000)
    # --- opcao Cadastrar ---
    opcaoCadLabel.place(x=5000)
    # ----- Inseri Componetes -----
    # --- nome ---
    nomeLabel.place(x=55, y=20)
    nomeEntry.place(x=200, y=26, height=30)
    # --- email ---
    emailLabel.place(x=55, y=61)
    emailEntry.place(x=200, y=69, height=30)
    # --- botoes ---
    confirmarButton.place(x=260, y=265, height=30)
    voltarButton.place(x=80, y=265, height=30)

def click_voltar():
    print("CLICOU VOLTAR!")
    # ----- Remove Componentes -----
    # --- nome ---
    nomeLabel.place(x=5000)
    nomeEntry.place(x=5000)
    # --- email ---
    emailLabel.place(x=5000)
    emailEntry.place(x=5000)
    # --- cadastrar ---
    confirmarButton.place(x=5000)
    # --- entrar ---
    voltarButton.place(x=5000)

    # ----- Inseri Componetes -----
    # --- opção de cadastro ---
    opcaoCadLabel.place(x=85, y=355)
    # --- botões ---
    entrarButton.place(x=170, y=265, height=30)
    cadastrarButton.place(x=300, y=355, height=30)
    

def click_confirmar():
    print("CLICOU CONFIRMAR!")
    # ----- Remove Componentes -----
    # --- nome ---
    nomeLabel.place(x=5000)
    nomeEntry.place(x=5000)
    # --- email ---
    emailLabel.place(x=5000)
    emailEntry.place(x=5000)
    # --- cadastrar ---
    confirmarButton.place(x=5000)
    # --- entrar ---
    voltarButton.place(x=5000)
    # ----- Inseri Componetes -----
    # --- opção de cadastro ---
    opcaoCadLabel.place(x=85, y=355)
    # --- botões ---
    entrarButton.place(x=170, y=265, height=30)
    cadastrarButton.place(x=300, y=355, height=30)

def cadastro_to_bd():
    #click_confirmar()
    nome = nomeEntry.get()
    email = emailEntry.get()
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    if (nome == "" and email == "" and usuario == "" and senha == "" or nome == "" and email == "" or usuario == "" and senha == ""or nome == "" or email == "" or usuario == "" or senha == ""):
        messagebox.showerror(title="Cadastro Erro", message="Campo(s) vazio(s). Preencha todos os campos!")
    else:
        # Inserção no banco de dados
        sql = "INSERT INTO usuarios VALUES (default, %s, %s, %s, %s)"
        cur.execute(sql, (nome, email, usuario, senha))
        conn.commit()

        messagebox.showinfo(title="Informação Cadastro", message="Conta criada com Sucesso!")

def logando():
    usuario = usuarioEntry.get()
    senha = senhaEntry.get()

    cur.execute("""
    SELECT * FROM usuarios
    WHERE usuario = '{}' and senha = '{}';
    """.format(usuario, senha))
    conn.commit()
    print("Selecionou!")
    verifLogin = cur.fetchone()
    print(verifLogin)
    try:
        if (usuario in verifLogin and senha in verifLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado, Bem Vindo!")
    except:
        messagebox.showinfo(title="Login Info", message="Acesso Negado. Verifique se está cadastrado no sistema!")
# ------------------------------------------------------------------------------ 

# --- Frames ---
ladoEsquerdo = Frame(janela, width=300, height=400, bg="#50D99E", relief="raise")
ladoDireito = Frame(janela, width=497, height=400, bg="#64F0DA", relief="raise")
# --- Imagem Logo ---
logoLabel = Label(ladoEsquerdo, image=logo, bg="#50D99E")
# --- usuario ---
usuarioLabel = Label(ladoDireito, text="Usuário:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
usuarioEntry = ttk.Entry(ladoDireito, width=30)
# --- senha ---
senhaLabel = Label(ladoDireito, text="Senha:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
senhaEntry = ttk.Entry(ladoDireito, width=30, show="*")
# --- opção de cadastro ---
opcaoCadLabel = Label(ladoDireito, text="Não é cadastrado?", font=("Indie Flower", 15), bg="#64F0DA", fg="white") 
# --- botoes ---
entrarButton = ttk.Button(ladoDireito, text="Entrar", width=20, command=logando)
cadastrarButton = ttk.Button(ladoDireito, text="Cadastrar", width=20, command=click_cadastrar)

# ----- Inseri Componentes -----
# --- nome ---
nomeLabel = Label(ladoDireito, text="Nome:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
nomeEntry = ttk.Entry(ladoDireito, width=30)
# --- email ---
emailLabel = Label(ladoDireito, text="E-mail:", font=("Indie Flower", 25), bg="#64F0DA", fg="white")
emailEntry = ttk.Entry(ladoDireito, width=30)
# --- botoes ---
confirmarButton = ttk.Button(ladoDireito, text="Confirmar", width=20, command=cadastro_to_bd)
voltarButton = ttk.Button(ladoDireito, text="Voltar", width=20, command=click_voltar)

# ---------- Layout - Gereciador de componetes da janela ----------
# --- frames ---
ladoEsquerdo.pack(side=LEFT)
ladoDireito.pack(side=RIGHT)
# --- imagem logo ---
logoLabel.place(x=18, y=30)
# --- usuario ---
usuarioLabel.place(x=55, y=102)
usuarioEntry.place(x=200, y=112, height=30)
# --- senha ---
senhaLabel.place(x=55, y=160)
senhaEntry.place(x=200, y=168, height=30)
# --- opção de cadastro ---
opcaoCadLabel.place(x=85, y=355)
# --- botões ---
entrarButton.place(x=170, y=265, height=30)
cadastrarButton.place(x=300, y=355, height=30)

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
    CREATE TABLE IF NOT EXISTS usuarios (
        id serial NOT NULL,
        nome varchar(30) NOT NULL UNIQUE,
        email varchar(50) NOT NULL,
        usuario varchar(20) NOT NULL UNIQUE,
        senha varchar(8) NOT NULL,
        PRIMARY KEY(id)
    );
    """)
    print("criado tabela!")
except (psycopg2.Error) as ee:
    print("\nFalha!\n%s" % (ee))

# ------------------------------------------------------------------------------ 

# ---------- Tamanho da janela ----------
# --- widgth x heigth + left + topo ---
janela.geometry("800x400+250+180")

janela.mainloop()