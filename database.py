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
        conexao = conectar(database=None)
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

def update():
    pass

def delete():
    pass

def insert():
    pass

def select():
    pass

if __name__ == "__main__":
    criar_banco()
    criar_tabela()