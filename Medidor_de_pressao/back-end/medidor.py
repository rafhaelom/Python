# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 23:37:21 2021

@author: Rafhael de Oliveira Martins
"""

#%% Importando Bibliotecas
import psycopg2
from datetime import datetime

#%% Desenvolvimento
print("---------------------------------------")
print("\t \t Medidor de pressão \t \t")
print("---------------------------------------\n")

while (True):
    print("----- Menu -----\n")
    print("1 - Cadastrar")
    print("2 - Mostar")
    print("3 - Sair")
    opcao = int(input("Digite sua opção: "))
    
    if (opcao == 1):
        print("\nAbrindo e criando conexão com o Banco!\n")
        # Conecção com o Banco de Dados PostgreSQL
        DB_HOST = "localhost"
        DB_USER = "user_banco"
        DB_PASS = "password_banco"
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
            break
            
        # Interação com usuário
        nome = str(input("Digite seu nome: "))
        peso = float(input("Digite seu peso: "))
        sistolica = int(input("Digite sua pressão Sistólica: "))
        diastolica = int(input("Digite sua pressão Diastólica: "))
        pulsacao = int(input("Digite sua Pulsação: "))
        datahora = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        
        # Inserção no banco de dados
        sql = "insert into registro values (default, %s, %s, %s, %s, %s, %s)"
        cur.execute(sql, (datahora, nome, peso, sistolica, diastolica, pulsacao))
        conn.commit()
    elif(opcao == 2):
        print("Mostrando registros!")
        
        # Exibição de entradas do usuário
        print("Data e hora: ", datahora)
        print("Nome: ", nome)
        print("Peso: ", peso, "Kg")
        print("Pressão Sistólica: ", sistolica, "mmHg")
        print("Pressão Diastólica: ", diastolica, "mmHg")
        print("Pulsação: ", pulsacao, "/min")
        
        # Consultando a tabela Registro
        print("Registros dentro do banco!\n")
        cur.execute('SELECT * FROM registro;')
        print(cur.fetchall())

    else:
        print("---------------------------------------")
        print("Fechando o programa e conexão com o Banco!")
        print("---------------------------------------")
        # Fechando conexão com o Banco
        conn.close()
        break
