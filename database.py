import os
import mysql.connector
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

def conectar(database="cadastro"):
    conexao = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=database
    )

    return conexao


def criar_banco():
    conexao = None
    cursor = None

    try:
        conexao = conectar(database=None)
        cursor = conexao.cursor()

        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS cadastro"
        )

        print("Banco verificado/criado com sucesso.")

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()


def criar_tabela():
    conexao = None
    cursor = None

    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS alunos (
            id INT NOT NULL AUTO_INCREMENT,
            nome VARCHAR(100) NOT NULL,
            ano_nascimento SMALLINT NOT NULL,
            nota DECIMAL(4,2) NOT NULL,
            PRIMARY KEY (id)
        )
        """

        cursor.execute(sql)

        print("Tabela alunos verificada/criada com sucesso.")

    finally:
        if cursor is not None:
            cursor.close()

        if conexao is not None and conexao.is_connected():
            conexao.close()

def delete(id:int):
    conexao = None
    cursor = None
        
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
        
        sql = """
        DELETE FROM alunos
        WHERE Id = %s;
        """
        
        cursor.execute(sql, (id,))
        if cursor.rowcount > 0:
            conexao.commit()
            return(f"Aluno(a) deletado com sucesso!")
        else:
            conexao.rollback()
            return(f"Nenhum aluno(a) encontrado com esse ID.")
    
    except mysql.connector.Error as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()
            return(f"Erro ao deletar aluno(a): {erro}")
        
    finally:
        if cursor is not None:
            cursor.close()
        
        if conexao is not None and conexao.is_connected():
            conexao.close()

def insert(nome:str, ano:int, nota:float):
    conexao = None
    cursor = None
    
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
    
        sql = """
        INSERT INTO alunos(nome,ano_nascimento, nota)
        VALUES (%s, %s, %s);
        """
        valores = (nome, ano, nota)
    
        cursor.execute(sql, valores)
        conexao.commit()

    except mysql.connector.Error as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()
            (f"Erro ao cadastrar aluno(a) {nome}: {erro}")
    
    finally:
        if cursor is not None:
            cursor.close()
    
        if conexao is not None and conexao.is_connected():
            conexao.close()


def update_nome(id:int, nome:str):
    conexao = None
    cursor = None
               
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
               
        sql = """
        UPDATE alunos SET nome  = %s
        WHERE id = %s;
        """
        valores = nome , id
        cursor.execute(sql, valores)
        if cursor.rowcount > 0:
            conexao.commit()
            return("Alteração realizada com sucesso!")
        else:
            conexao.rollback()
            return("Nenhum aluno encontrado.")

    except mysql.connector.Error as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()
            return(f"Erro ao atualizar o nome do aluno(a) {nome}: {erro}")
               
    finally:
        if cursor is not None:
            cursor.close()
               
        if conexao is not None and conexao.is_connected():
            conexao.close()

def update_ano(id: int, ano:int):
    conexao = None
    cursor = None
        
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
        
        sql = """
        UPDATE alunos SET ano_nascimento = %s
        WHERE id = %s;
        """
        valores = ano , id
        cursor.execute(sql, valores)
        if cursor.rowcount > 0:
            conexao.commit()
            return("Alteração realizada com sucesso!")
        else:
            conexao.rollback()
            return("Nenhum aluno encontrado.")

    except mysql.connector.Error as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()
            return(f"Erro ao atualizar ano de nascimento do aluno(a): {erro}")
        
    finally:
        if cursor is not None:
            cursor.close()
        
        if conexao is not None and conexao.is_connected():
            conexao.close()

def update_nota(id:int, nota):
    conexao = None
    cursor = None
            
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
            
        sql = """
        UPDATE alunos SET nota  = %s
        WHERE id = %s;
        """
        valores = nota , id
        cursor.execute(sql, valores)
        if cursor.rowcount > 0:
            conexao.commit()
            return("Alteração realizada com sucesso!")
        else:
            conexao.rollback()
            return("Nenhum aluno encontrado.")

    except mysql.connector.Error as erro:
        if conexao is not None and conexao.is_connected():
            conexao.rollback()
            return(f"Erro ao atualizar a nota do aluno(a) : {erro}")
            
    finally:
        if cursor is not None:
            cursor.close()
            
        if conexao is not None and conexao.is_connected():
            conexao.close()

def select_like(nome:str):
    conexao = None
    cursor = None
            
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
            
        sql = """SELECT * FROM alunos
        WHERE nome LIKE %s;
        """
        valores = (f"%{nome}%",)
        cursor.execute(sql, valores)
        resultado = cursor.fetchall()
        if len(resultado) > 0:
            for alunos in resultado:
                print(alunos)
                return True
        else:
            return False
    except mysql.connector.Error as erro:
        print(f"Erro ao buscar alunos: {erro}")        
    finally:
        if cursor is not None:
            cursor.close()
                   
        if conexao is not None and conexao.is_connected():
            conexao.close()

def select_all():
    conexao = None
    cursor = None
            
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
            
        sql = """SELECT * FROM alunos;
        """
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if len(resultado) > 0:
            for alunos in resultado:
                print(alunos)
        else:
            print("Não Há alunos(a) cadastrados!")

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar alunos: {erro}")

    finally:
        if cursor is not None:
            cursor.close()
                   
        if conexao is not None and conexao.is_connected():
            conexao.close()

def max():
    conexao = None
    cursor = None
            
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
            
        sql = """SELECT *
        FROM alunos 
        WHERE nota = (SELECT MAX(nota) FROM alunos);"""
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if len(resultado) > 0:
            for alunos in resultado:
                print(alunos)
        else:
            print("Não Há alunos(a) cadastrados!")

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar alunos: {erro}")

    finally:
        if cursor is not None:
            cursor.close()
                   
        if conexao is not None and conexao.is_connected():
            conexao.close()

def min():
    conexao = None
    cursor = None
            
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
            
        sql = """SELECT *
        FROM alunos 
        WHERE nota = (SELECT MIN(nota) FROM alunos);"""
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if len(resultado) > 0:
            for alunos in resultado:
                print(alunos)
        else:
            print("Não Há alunos(a) cadastrados!")

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar alunos: {erro}")

    finally:
        if cursor is not None:
            cursor.close()
                   
        if conexao is not None and conexao.is_connected():
            conexao.close()

def avg():
    conexao = None
    cursor = None
            
    try:
        conexao = conectar("cadastro")
        cursor = conexao.cursor()
            
        sql = """SELECT AVG(nota) AS media_geral_turma 
        FROM alunos;"""
        cursor.execute(sql)
        resultado = cursor.fetchall()
        if resultado == 0:
            return "Não Há alunos(a) cadastrados!"
        else:
           return resultado

    except mysql.connector.Error as erro:
        print(f"Erro ao buscar alunos: {erro}")

    finally:
        if cursor is not None:
            cursor.close()
                   
        if conexao is not None and conexao.is_connected():
            conexao.close()
