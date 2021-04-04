# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:16:27 2021

@author: Rafhael de Oliveiora Martins
"""

# Importando Bibliotecas
import psycopg2
import pandas as pd
from datetime import datetime


# Conecção com o Banco de Dados PostgreSQL

DB_HOST = "localhost"
DB_USER = "postgres"
DB_PASS = "teste123"
DB_NAME = "postgres"

conn = psycopg2.connect(
    host= DB_HOST, 
    database= DB_NAME,
    user= DB_USER,
    password= DB_PASS)

cur = conn.cursor()

# Consultando a tabela Registro
cur.execute('SELECT * FROM registro;')
# print(cur.fetchall())


# Interação com usuário
def cadastro():
    nome = str(input("Digite seu nome: "))
    peso = float(input("Digite seu peso: "))
    sistolica = int(input("Digite sua pressão Sistólica: "))
    diastolica = int(input("Digite sua pressão Diastólica: "))
    pulsacao = int(input("Digite sua Pulsação: "))
    datahora = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

# Exibição de entradas do usuário
def mostrar():
    print("Data e hora: ", datahora)
    print("Nome: ", nome)
    print("Peso: ", peso, "Kg")
    print("Pressão Sistólica: ", sistolica, "mmHg")
    print("Pressão Diastólica: ", diastolica, "mmHg")
    print("Pulsação: ", pulsacao, "/min")

# Desenvolvimento
print("---------------------------------------")
print("\t \t Medidor de pressão \t \t")
print("---------------------------------------")

while (True):
    print("\n ----- Menu -----")
    print("1 - Cadastrar")
    print("2 - Mostar")
    print("3 - Sair")
    opcao = int(input("Digite sua opção: "))
    
    if (opcao == 1):
        print("Abrindo e criando conexão ocm o Banco!")
        cadastro()
    elif(opcao == 2):
        print("Mostrando registros!")
        mostrar()
    else:
        print("Fechando o programa e fechando conexão com o Banco!")
        break
#Inserção no banco de dados
sql = "insert into registro values (default, %s, %s, %s, %s, %s, %s)"
cur.execute(sql, (datahora, nome, peso, sistolica, diastolica, pulsacao))
conn.commit()

# Fechando conexão com o Banco